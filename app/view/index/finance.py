from flask import render_template, Blueprint, request, redirect
from app.common.utils.stocks import get_income, get_fina_audit
from app.models.finance import Fina_audit, Cashflow, Income, Balance
from app.common.utils.check_stocks_data import get_all_by_endDate
from app.extensions.init_sqlalchemy import db
import numpy as np

finance_bp = Blueprint('finance', __name__, url_prefix='/')


@finance_bp.route('/finance')
def finance_index():
    return render_template('index/finance/index.html')


@finance_bp.route('/finance_result', methods=['POST'])
def finance_result():
    if request.method == 'POST':
        data = request.form
        stocks_data = get_fina_audit(data.get('stocks_code'), limit=10)
        check_res = get_all_by_endDate(Fina_audit, data.get('stocks_code'))
        if check_res:
            print("数据已存在")
            stocks_data_clear = stocks_data.drop(stocks_data[
                stocks_data['end_date'] <= check_res[0].end_date].index)
        else:
            stocks_data_clear = stocks_data
            print("数据不存在，应增加")
        check_res.append(np.ndarray(stocks_data_clear))
        stocks_data_clear.to_sql('fina_audit',
                                 db.get_engine(),
                                 index=None,
                                 if_exists='append')
        return render_template('index/finance/result.html',
                               fina_audits=check_res)

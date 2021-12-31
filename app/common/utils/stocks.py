import os
import tushare as ts

secret = os.getenv('TUSHARE_API_SECRET')

pro = ts.pro_api(secret)


def get_fina_audit(ts_code,
                   ann_date='',
                   start_date='',
                   end_date='',
                   period='',
                   limit='',
                   offset=''):
    """获取财务审计意见

    Keyword arguments:
    ts_code -- 股票代码
    ann_date -- 公告日期 20201231
    start_date -- 公告开始日期 20201201
    end_date -- 公告结束日期 20201231
    period -- 报告期 
    limit -- 单次返回数据长度
    offset -- 请求数据的开始位移量
    Return: return_description
    """
    # 拉取数据
    df = pro.fina_audit(**{
        "ts_code": ts_code,
        "ann_date": ann_date,
        "start_date": start_date,
        "end_date": end_date,
        "period": period,
        "limit": limit,
        "offset": offset
    },
                        fields=[
                            "ts_code", "ann_date", "end_date", "audit_result",
                            "audit_fees", "audit_agency", "audit_sign"
                        ])
    df.drop_duplicates(subset=['end_date'], keep='first', inplace=True)
    return df


def get_income(ts_code,
               ann_date='',
               f_ann_date='',
               start_date='',
               end_date='',
               period='',
               report_type='',
               comp_type='',
               end_type='',
               is_calc='',
               limit='',
               offset=''):
    # 拉取数据
    df = pro.income(
        **{
            "ts_code": ts_code,
            "ann_date": ann_date,
            "f_ann_date": f_ann_date,
            "start_date": start_date,
            "end_date": end_date,
            "period": period,
            "report_type": report_type,
            "comp_type": comp_type,
            "end_type": end_type,
            "is_calc": is_calc,
            "limit": limit,
            "offset": offset
        },
        fields=[
            "ts_code", "ann_date", "f_ann_date", "end_date", "report_type",
            "comp_type", "end_type", "basic_eps", "diluted_eps",
            "total_revenue", "revenue", "int_income", "prem_earned",
            "comm_income", "n_commis_income", "n_oth_income", "n_oth_b_income",
            "prem_income", "out_prem", "une_prem_reser", "reins_income",
            "n_sec_tb_income", "n_sec_uw_income", "n_asset_mg_income",
            "oth_b_income", "fv_value_chg_gain", "invest_income",
            "ass_invest_income", "forex_gain", "total_cogs", "oper_cost",
            "int_exp", "comm_exp", "biz_tax_surchg", "sell_exp", "admin_exp",
            "fin_exp", "assets_impair_loss", "prem_refund", "compens_payout",
            "reser_insur_liab", "div_payt", "reins_exp", "oper_exp",
            "compens_payout_refu", "insur_reser_refu", "reins_cost_refund",
            "other_bus_cost", "operate_profit", "non_oper_income",
            "non_oper_exp", "nca_disploss", "total_profit",
            "income_tax", "n_income", "n_income_attr_p", "minority_gain",
            "oth_compr_income", "t_compr_income", "compr_inc_attr_p",
            "compr_inc_attr_m_s", "ebit", "ebitda", "insurance_exp",
            "undist_profit", "distable_profit", "rd_exp", "fin_exp_int_exp",
            "fin_exp_int_inc", "transfer_surplus_rese",
            "transfer_housing_imprest", "transfer_oth", "adj_lossgain",
            "withdra_legal_surplus", "withdra_legal_pubfund",
            "withdra_biz_devfund", "withdra_rese_fund", "withdra_oth_ersu",
            "workers_welfare", "distr_profit_shrhder", "prfshare_payable_dvd",
            "comshare_payable_dvd", "capit_comstock_div",
            "continued_net_profit", "update_flag"
        ])
    df.drop_duplicates(subset=['end_date'], keep='first', inplace=True)
    return df

from app.extensions.init_sqlalchemy import db


def get_first_by_endDate(model: db.Model, ts_code):
    """
    :param model: 模型类
    :param value: value
    :return: 返回单个查询结果
    """
    return model.query.filter_by(ts_code=ts_code).order_by(
        model.end_date.desc()).first()


def get_all_by_endDate(model: db.Model, value):
    """
    :param model: 模型类
    :param value: value
    :return: 返回单个查询结果
    """
    return model.query.filter_by(ts_code=value).order_by(
        model.end_date.desc()).all()

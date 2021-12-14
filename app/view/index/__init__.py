from app.view.index.index import index_bp
from app.view.index.user import user_bp
from . import index


def register_index_views(app):
    """
    初始化蓝图
    """
    app.register_blueprint(index_bp)
    app.register_blueprint(user_bp)
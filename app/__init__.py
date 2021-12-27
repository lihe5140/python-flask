import os
from flask import Flask
from app.common.script import init_script
from app.config import config
from app.extensions import init_plugs
from app.view import init_view


def create_app(config_name=None):
    #创建Flask实例
    app = Flask(__name__,
                instance_relative_config=True,
                template_folder='./templates',
                static_folder='./static')
    if not config_name:
        #尝试从本地环境中读取
        config_name = os.getenv('FLASK_ENV', 'development')
    app.config.from_object(config[config_name])
    # 注册插件
    init_plugs(app)

    # 注册路由
    init_view(app)

    # 注册命令
    init_script(app)

    return app
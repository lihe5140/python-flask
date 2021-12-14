import os
from flask import Flask
from app.config import config

def create_app(config_name=None):
    #创建Flask实例
    app = Flask(__name__, instance_relative_config=True)
    if not config_name:
        #尝试从本地环境中读取
        config_name = os.getenv('FLASK_ENV', 'development')

    app.config.from_object(config[config_name])
    
    # 注册蓝图
    
    # 注册路由
    
    return app
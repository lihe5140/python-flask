import os


class BaseConfig:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev key')

    # mysql 配置
    MYSQL_USERNAME = os.getenv('MYSQL_USERNAME') or "root"
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD') or "root"
    MYSQL_HOST = os.getenv('MYSQL_HOST') or "127.0.0.1"
    MYSQL_PORT = int(os.getenv('MYSQL_PORT') or 3306)
    MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')
    # mysql 数据库的配置信息
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(BaseConfig):
    """ 测试配置 """


class DevelopmentConfig(BaseConfig):
    """ 开发配置 """


class ProductionConfig(BaseConfig):
    """生产环境配置"""


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
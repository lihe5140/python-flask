import os 


class BaseConfig:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev key')
    
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
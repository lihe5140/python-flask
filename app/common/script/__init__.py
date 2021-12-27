from app.common.script.initdb import init_db


def init_script(app):
    @app.cli.command()
    # print('初始化数据库')
    def init():
        init_db()

    # 测试命令
    @app.cli.command()
    def test():
        print('检查数据库更新')

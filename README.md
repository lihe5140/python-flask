# python-flask-andinfo

### 1、配置开发、测试、生产环境（完成）

```bash
# 安装虚拟环境
# windows
py -3 -m venv venv

# Macos
python3 -m venv venv

# 激活/关闭虚拟环境
# windows
venv\Script\activate    deactivate
#Macos
. venv/bin/activate  	deactivate


# 安装扩展
pip install -r requirements.txt
```



### 2、安装数据库扩展(完成)

```bash
# 安装pymysql（提供驱动，也就是路径）
# 安装flask-sqlaclchemy  （基于SQLAlchemy的优化和提升，实现ORM映射）
# 会自动安装 SQLalchemy（ORM 映射关系） 
# 安装flask-migrate （提供命令工具，操作ORM） 数据库迁移工具
# 安装 flask_marshmallow

# 初始化数据库
flask init

# 数据库模型修改后需重复命令
flask db migrate
flask db upgrade
```



### 3、蓝图注册（进行中）


from flask import render_template, Blueprint, request

user_bp = Blueprint('user', __name__, url_prefix='/')


@user_bp.route('/user')
def index():
    return render_template('index/user/index.html')


@user_bp.route('/login')
def login():
    return render_template('index/user/login.html')


@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    r = request.method
    if r == 'GET':
        return render_template('index/user/register.html')
    else:
        return "这是提交注册"
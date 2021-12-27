from flask import render_template, Blueprint, request,redirect

from app.models.user import User

user_bp = Blueprint('user', __name__, url_prefix='/')
users = []

@user_bp.route('/user')
def user_list():
    return render_template('index/user/list.html',users=users)


@user_bp.route('/login')
def login():
    return render_template('index/user/login.html')


@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form
        username= data.get('username')
        psw= data.get('psw')
        repsw= data.get('repsw')
        if psw == repsw:
            # 用户名唯一
            for user in users:
                if user.username == username:
                    return render_template('index/user/register.html',msg='用户名已存在')
            # 创建user对象
            user = User(username,psw)
            users.append(user)
            return redirect('/user')
    
    return render_template('index/user/register.html')
        
import logging
import time
from functools import wraps
from flask import Flask, render_template, request, url_for, redirect, session, flash, jsonify, abort, \
    get_flashed_messages
from flask_bootstrap import Bootstrap5
from itsdangerous import URLSafeSerializer

# 导入注册验证类
from function.forms import RegistrationForm
# 导入注册用户方法
from function.registration import register_user

from modes.func import *

app = Flask(__name__)
# 加载配置文件
app.config.from_pyfile('conf.py')
# 初始化数据库
db.init_app(app)

bootstrap = Bootstrap5(app)  # 使用Bootstrap5

# 用于生成和验证令牌的密钥
token_serializer = URLSafeSerializer(app.secret_key)


# 自定义装饰器
@app.template_filter('md')
def markdown_to_html(txt):
    from markdown import markdown
    return markdown(txt)


@app.route('/')
def index():
    next_url = request.args.get('next')
    # 在登录页面中，将 next_url 传递给模板，用于生成登录表单中的 action 属性
    user, _ = user_is_have(session.get('user', None))
    # 调用文章db
    articles = get_all_article_object()
    return render_template('index.html', next=next_url, user=user, articles=articles)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    username = request.form['username']
    password = request.form['password']

    message, res = login_validation(username, password)
    if res:
        # 登录成功，创建会话并生成令牌
        session['user'] = username
        # token = token_serializer.dumps(username)
        # return redirect(url_for('index', token=token))
        return redirect(url_for('index'))
    else:
        # 登录失败，重新显示登录页面并显示错误消息
        return render_template('login.html', message=message)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        # verification_code = form.verification_code.data
        result, message = register_user(username, email, password)
        flash(message, 'success' if result else 'danger')
        if result:
            time.sleep(1)
            return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/logout')
def logout():
    # 登出，删除会话
    session.clear()
    return redirect(url_for('index'))


# @app.route('/check_user/<username>', methods=['GET'])
# def check_user(username):
#     user = User.query.filter_by(username=username).first()
#     if user:
#         return jsonify({'exists': True})
#     else:
#         return jsonify({'exists': False})

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == "GET":
        return render_template('./main/adduser.html')
    # 从请求中获取用户信息

    data = request.form
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    # 检查用户名是否已经存在

    new_user = User(
        username=username,
        password=password,
        email=email
    )
    # 添加到数据库
    db.session.add(new_user)
    db.session.commit()

    flash("注册成功", 'success')


# 404错误处理
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.route('/about', methods=['GET'])
def about():
    user, _ = user_is_have(session.get("user"))
    return render_template('./main/aboutme.html', user=user)


# 文章加载页面
@app.route('/article/<article_id>')
def article_id_show(article_id):
    user, _ = user_is_have(session.get('user', None))
    article = get_article(article_id)
    logging.debug(article.id)
    comments = get_all_comments()
    messages = get_flashed_messages()
    return render_template('article.html', article=article, comments=comments,messages=messages,user=user)


# 新增文章页面
@app.route('/add_article')
def add_article():
    return render_template('./main/add_article.html')


@app.route('/add_comment/<article_id>', methods=['POST'])
def add_comment(article_id):
    commentTest: str | None = request.form.get('comment_out')
    logging.debug(commentTest)
    username = session.get('user')
    type = "article"
    source = 0
    user, _ = user_is_have(username)
    msg, res, = add_comment_func(source, type, user.id, commentTest)
    flash(msg, 'success')
    article_url = url_for('article_id_show',article_id=article_id)

    flash(msg,'success')

    return redirect(article_url)


if __name__ == '__main__':
    app.run(debug=True)

import random
import smtplib
from email.mime.text import MIMEText
import re
from functools import wraps

from flask import session, redirect, url_for, request


# TODO 时间紧张，后续开发
# 随机验证码生成
def generate_verification_code():
    return ''.join(random.choices('0123456789', k=6))


# TODO 时间紧张，后续开发
# 验证码邮箱发送功能
def send_verification_code(email, verification_code):
    # 在此处添加发送邮件的代码，这里使用SMTP来发送邮件
    # 你需要填写你的邮箱账号和密码，以及邮件服务器的地址和端口
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    sender_email = 'your_email@example.com'
    sender_password = 'your_email_password'

    msg = MIMEText(f'这里是natsume-Blog网站，您的验证码是：{verification_code}', 'plain', 'utf-8')
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = '邮箱验证码'

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, [email], msg.as_string())


# 用户登录检验（装饰器）
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            # 如果用户未登录，将其重定向到登录页面，并在登录后返回原始请求的页面
            return redirect(url_for('index', next=request.url))
        return f(*args, **kwargs)

    return decorated_function

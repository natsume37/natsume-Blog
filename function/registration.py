# registration.py

# 模拟已注册用户的字典
registered_users = {
    'user1': {'email': 'user1@example.com', 'password': 'password1'}
}

# 模拟后台发送的验证码的字典
# verification_code = {}


def register_user(username, email, password,):
    if username in registered_users:  # 检查用户名是否已存在
        return False, '该用户名已被注册，请选择另一个用户名'

    # 暂时不开发
    # if email not in verification_code:
    #     # 检查邮箱验证码是否正确
    #     return False, '邮箱验证码不正确，请重新输入'

    # 注册用户并返回成功消息
    registered_users[username] = {'email': email, 'password': password}
    return True, '注册成功！'

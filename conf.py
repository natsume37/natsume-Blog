# config.py
CSRF_ENABLED = True  # 用于开启CSRF保护，但默认状态下都是开启的
SECRET_KEY = 'X1X2X3X4X5'  # 用于生成动态令牌的秘钥

# config.py
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123@localhost/blog'
SQLALCHEMY_TRACK_MODIFICATIONS = False

class Config(object):
    """配置参数"""
    # sqlalchemy的配置参数
    SQLALCHEMY_DATABASE_URI = "mysql://root:123@127.0.0.1:3306/blog"
    # 设置sqlalchemy自动更跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 设置每次请求结束后会自动提交数据库中的改动
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # 查询时会显示原始SQL语句
    SQLALCHEMY_ECHO = True

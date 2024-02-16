import time

from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from conf.settings import *
# 添加缓存
from flask_caching import Cache

app = Flask(__name__)
# 加载配置文件
app.config.from_pyfile('conf/settings.py')
bootstrap = Bootstrap5(app)
# 初始化缓存
cache = Cache(app=app, config=redis_config)  # 创建Cache对象


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


# 添加缓存、照片流量大、设置超时时间
@app.route('/album')
# @cache.cached(timeout=5)
def album_func():
    # time.sleep(5)
    return render_template('album.html')


@app.route('/msg-board')
def msg_board():  # put application's code here
    return render_template('msg-board.html')


@app.route('/test')
def test():  # put application's code here
    return render_template('test.html')


if __name__ == '__main__':
    app.run(debug=True)

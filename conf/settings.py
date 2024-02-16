# coding:utf-8
# USER: 冷不丁
# @FILE_NAME: settings
# @TIME: 2024/1/16 16:26

DEBUG = True
SECRET_KEY = '123456'

# 配置RedisCache缓存类型参数值，我们使用本地的redis，没有密码
redis_config = {
    'CACHE_TYPE': 'redis',  # 使用redis作为缓存
    'CACHE_REDIS_HOST': '127.0.0.1',  # redis地址
    'CACHE_REDIS_PORT': 6379  # redis端口号
}

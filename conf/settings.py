# coding:utf-8
# USER: 冷不丁
# @FILE_NAME: settings
# @TIME: 2024/1/16 16:26
import logging
import logging.config
DEBUG = True
SECRET_KEY = '123456'

# 配置RedisCache缓存类型参数值，我们使用本地的redis，没有密码
redis_config = {
    'CACHE_TYPE': 'redis',  # 使用redis作为缓存
    'CACHE_REDIS_HOST': '127.0.0.1',  # redis地址
    'CACHE_REDIS_PORT': 6379  # redis端口号
}

# 日志配置字典
import os.path

# 路径配置
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # 项目根目录
INFO_LOG_DIR = os.path.join(BASE_DIR, "log", 'info.log')
ERROR_LOG_DIR = os.path.join(BASE_DIR, "log", 'error.log')

LOGGING_DIC = {
    'version': 1.0,
    'disable_existing_loggers': False,
    # 日志格式
    'formatters': {
        'standard': {
            'format': '%(asctime)s %(threadName)s:%(thread)d [%(name)s] %(levelname)s [%(pathname)s:%(lineno)d] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'simple': {
            'format': '%(asctime)s [%(name)s] %(levelname)s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'test': {
            'format': '%(asctime)s %(message)s',
        },
    },
    'filters': {},
    # 日志处理器
    'handlers': {
        'console_debug_handler': {
            'level': 'DEBUG',  # 日志处理的级别限制
            'class': 'logging.StreamHandler',  # 输出到终端
            'formatter': 'simple'  # 日志格式
        },
        'file_info_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件,日志轮转
            'filename': f'{INFO_LOG_DIR}',
            'maxBytes': 1024 * 1024 * 10,  # 日志大小 10M
            'backupCount': 10,  # 日志文件保存数量限制
            'encoding': 'utf-8',
            'formatter': 'standard',
        },
        'file_debug_handler': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',  # 保存到文件
            'filename': f'{ERROR_LOG_DIR}',  # 日志存放的路径
            'encoding': 'utf-8',  # 日志文件的编码
            'formatter': 'test',
        },
    },
    # 日志记录器
    'loggers': {
        'logger1': {  # 导入时logging.getLogger时使用的app_name
            'handlers': ['console_debug_handler'],  # 日志分配到哪个handlers中
            'level': 'DEBUG',  # 日志记录的级别限制
            'propagate': False,  # 默认为True，向上（更高级别的logger）传递，设置为False即可，否则会一份日志向上层层传递
        },
        'logger2': {
            'handlers': ['console_debug_handler', 'file_debug_handler'],
            'level': 'INFO',
            'propagate': False,
        },
        # 万能日志记录器
        '': {
            'handlers': ['console_debug_handler', 'file_debug_handler'],  # 及答应到终端、也保存到文件
            'level': 'INFO',
            'propagate': False,
        },
    }
}

# 使用
logging.config.dictConfig(LOGGING_DIC)
logging1 = logging.getLogger("logger1")
logging1.debug("这是一条测试数据")


# 注：进行日志轮转的日志文件，不能和其他handler共用，不然会导致文件被占用无法更名而报错！

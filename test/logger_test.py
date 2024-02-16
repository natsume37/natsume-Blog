import logging
import logging.config
import os.path

# 路径配置
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # 项目根目录
INFO_LOG_DIR = os.path.join(BASE_DIR, "log", 'info.log')
ERROR_LOG_DIR = os.path.join(BASE_DIR, "log", 'error.log')
DEBUG_LOG_DIR = os.path.join(BASE_DIR, "log", 'debug.log')

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
            'filename': f'{DEBUG_LOG_DIR}',  # 日志存放的路径
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
            'handlers': ['console_debug_handler', 'file_info_handler'],  # 及答应到终端、也保存到文件
            'level': 'INFO',
            'propagate': False,
        },
        '': {
            'handlers': ['console_debug_handler', 'file_info_handler'],  # 及答应到终端、也保存到文件
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}
# 注：进行日志轮转的日志文件，不能和其他handler共用，不然会导致文件被占用无法更名而报错！
print(BASE_DIR)
print(INFO_LOG_DIR)
print(ERROR_LOG_DIR)

for i in range(10):
    logging.config.dictConfig(LOGGING_DIC)
    logging1 = logging.getLogger("logger1")
    logging1.debug("这是一条测试数据")
    logging2 = logging.getLogger("logger2")
    logging2.warning("这是一条测试数据")
    logging3 = logging.getLogger("这是自定义名称的记录器")
    logging3.debug("只要找不到、就用记录器名称为空的记录器")
    logging4 = logging.getLogger("记录器二号")
    logging4.debug("这是另一个记录器")

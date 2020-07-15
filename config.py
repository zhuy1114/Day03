import logging.handlers
import os
import time

PUB_ARTICLE_TITLE = "testCase_{}".format(time.strftime("%d%H%M%S"))

BASE_PATH = os.path.dirname(os.path.abspath("__file__"))


# 日志的基础配置方法
def base_log_config():
    # 1.创建日志器
    logger = logging.getLogger()
    # 2.设置日志器级别
    logger.setLevel(level=logging.INFO)
    # 3.创建处理器
    ls = logging.StreamHandler()
    lht = logging.handlers.TimedRotatingFileHandler(filename=BASE_PATH + '/log/test.log', when='h', interval=1,
                                                    backupCount=2)
    # 4.创建格式化器
    formatter = logging.Formatter(fmt="%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")
    # 5.将格式化器绑定到处理器
    ls.setFormatter(formatter)
    lht.setFormatter(formatter)
    # 6.将处理器添加到日志器
    logger.addHandler(ls)
    logger.addHandler(lht)

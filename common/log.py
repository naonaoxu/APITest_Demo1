import requests

from common.get_token import GetToken
from config.public_data import format_time
encoding='utf-8'

"""
封装log方法
package logging
"""
import logging
import os

#LEVELS = {
#    'debug':logging.DEBUG,
#    'info':logging.INFO,
#    'warning':logging.WARNING,
 #   'error':logging.ERROR,
 #   'cirtical':logging.CRITICAL
#}
#日志存放路径
log_file = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'\\log\\123.log'
logger = logging.getLogger()

class MyLog:
    logger.setLevel(logging.DEBUG)
    date="%Y-%m-%d %H:%M:%S"
    handler = logging.FileHandler(log_file, encoding='utf-8')


    def debug(self,log_meg):
        logger.addHandler(self.handler)
        logger.debug("[DEBUG]" + format_time+ log_meg)
        logger.removeHandler(self.handler)

    def info(self,log_meg):
        logger.addHandler(self.handler)
        logger.debug("[INFO]" + format_time+ log_meg)
        logger.removeHandler(self.handler)

    def warning(self,log_meg):
        logger.addHandler(self.handler)
        logger.debug("[WARNING]" + format_time+ log_meg)
        logger.removeHandler(self.handler)

    def error(self,log_meg):
        logger.addHandler(self.handler)
        logger.debug("[ERROR]" + format_time+ log_meg)
        logger.removeHandler(self.handler)

    def critical(self,log_meg):
        logger.addHandler(self.handler)
        logger.debug("[CRITICAL]" + format_time+ log_meg)
        logger.removeHandler(self.handler)







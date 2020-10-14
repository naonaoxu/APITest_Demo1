import logging.config
import logging
from config.public_data import logger_conf

logging.config.fileConfig(logger_conf)   #相对路径和绝对路径都可以
logger = logging.getLogger("example01")

#日志配置文件：多个logger,每个logger，指定不同的handler
#handler:设定了日志输出行的格式
#handler:设定写日志到文件（是否回滚）？还是到屏幕
#handler：设定了打印日志的级别

def debug(message):
    # 打印debug级别的日志方法
    logger.debug(message)

def warning(message):
    # 打印warning级别的日志方法
    logger.warning(message)

def info(message):
    #打印info级别的日志方法
    logging.info(message)

def error(message):
    #打印error级别的日志方法
    logger.error(message)

if __name__=="__main__":
    debug("hi")
    info("gloryroad")
    warning("hello")
    error("error")
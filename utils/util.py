import time
import os

class Util:
    def udid(self):
        return "test"+str(time.time()).replace(".", "")[0:11]

#创建日志存放路径和日志
    def create_file(filename):
        log_path = ('\\').join(filename.split('\\')[0:-1])
        if not os.path.isdir(log_path):
            os.makedirs(log_path)
        if not os.path.isfile(filename):
            fd=open(filename,mode='w',encoding='utf-8')
            fd.close()
        else:
            pass



#coding=utf-8
import sys
import yaml
import os
import logging
from config.public_data import *
#from common.log1 import logger


class PraseYaml:
    #读取yaml文件
    @classmethod
    def load_yaml(self,file_path):
        try:
            print(file_path)
            with open(file_path,encoding='utf-8') as f:
                data=yaml.load(f.read(),Loader=yaml.FullLoader)
            print(data)
            return data
        except Exception as e:
            print(e,"未找到yaml具体字段")
#            logger.exception('获取用例基本信息失败，{}'.format())
            return {}


    #写入yaml文件
    def write_yaml(self,file_name,date):
        file_path = os.path.abspath('..') + file_name
        with open(file_path,encoding="utf-8") as f:
            update_date=yaml.dump(date,stream=f,allow_unicode=True)

    #读取yaml文件里的具体字段值
    @classmethod
    def get_yaml_data(self,file_name,*krgs):
        data = self.load_yaml(file_name)
        try:
            for i in krgs:
                data=data.get(i)
            return data
        except Exception as e:
            print(e,"Not find: ",file_name,"Krgs:",krgs)
            return {}


if __name__=="__main__":
    A=PraseYaml
    print(A.load_yaml(corp_data_path))







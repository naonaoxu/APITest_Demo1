import yaml
import requests
from utils.prase_yaml import PraseYaml
from config.public_data import *


class GetToken():
    _token=""

    @classmethod
    def get_token(cls):
        if len(cls._token)==0:
            cls._token=cls.get_token_new()
        return cls._token

    @classmethod
    def get_token_new(cls):
        conf=PraseYaml.load_yaml(corp_data_path)
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                         params={"corpid": conf['env']["corpid"],
                                 "corpsecret": conf['env']["corpsecret"]}
                         ).json()
        return r["access_token"]

from common.get_token import GetToken
from config.public_data import base_url_pth
from utils.prase_yaml import PraseYaml

#set server to base_url
server_url=PraseYaml.load_yaml(base_url_pth)['base_url']
#server_url=PraseYaml.load_yaml(base_url_pth)['qa_url']
#server_url=PraseYaml.load_yaml(base_url_pth)['beta_url']
#server_url=PraseYaml.load_yaml(base_url_pth)['beta_url']

class PrepareTestData:

    #set test url
    @classmethod
    def set_url(cls,api_address):
        print(api_address)
        api_url = PraseYaml.get_yaml_data(api_address,"config","url")
        test_url = server_url + api_url
        return test_url

   #set token
    @classmethod
    def set_token(cls,token=None):
        if token == None:
            params = {"access_token": GetToken.get_token()}
        else:
            if token['token'] != 'default':
                params={"access_token": token['token']}
            else:
                params={"access_token": GetToken.get_token()}
        return params

    @classmethod
    def set_data(cls):
        pass


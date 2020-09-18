import allure
import pytest
from common.assert_result import AssertResult
from common.base_api import BaseAPI
from common.get_token import GetToken
from config.public_data import *
from utils.prase_yaml import PraseYaml
from utils.util import Util
from common.log import MyLog


base_url=PraseYaml.load_yaml(base_url_pth)['base_url']
param={"access_token": GetToken.get_token()}

list_test_case = PraseYaml.load_yaml(list_dept_data_path)
list_url=base_url+list_test_case['config']['url']

create_test_case=PraseYaml.load_yaml(create_dept_data_path)
create_url=base_url+create_test_case['config']['url']

delete_test_case=PraseYaml.load_yaml(delete_dept_data_path)
delete_url=base_url+delete_test_case['config']['url']

id_list=[]
log=MyLog()

@allure.feature("Test Create New Department API")
class TestDepartmentAPI:
    @allure.testcase('Delete Departments')
    def test_delete_all_department(self):
        r = self.test_list_department()
        all_department = r.json()['department']
        for department in all_department[2:]:
            id_list.append(department['id'])
        try:
            for id in id_list:
                param["id"] = id
                r = BaseAPI.delete_api(self, delete_url, param)
            log.debug("success delete depart")
            log.info(str(r.json()))
        except:
            log.error("fail delete depart")

    @allure.title("Test Title")
    @allure.testcase('Create New Department')
    @pytest.mark.parametrize('data',create_test_case['case'])
    def test_create_department(self,data):
        create_data=data['data']
        #prepare name_data
        if create_data["name"]=="forDuplicateTest":
            pass
        else:
            create_data["name"]=Util.udid(self)
        #prepare token_data
        if 'token' in data:
            param={"access_token": data['token']}
        else:
            param={"access_token": GetToken.get_token()}

        with allure.step("requestAPI：%s,requestAddress：%s,requestMehod：%s,requestCookie：%s"
                         % (create_test_case['config']['name'], create_test_case['config']['url'], create_test_case['config']['method'], param)):
            allure.attach("Request Senario：", "{0}".format(data["name"]))
            allure.attach("Request Data", "{0}".format(data['data']))

        try:
            r = BaseAPI.post_api(self, create_url, create_data, param)
            log.debug("success create depart")
            log.info(str(r.json()))
        except:
            log.error("fail create depart")

        create_exp_status_code = data['validate']['exp_status_code']
        create_exp_errcode = data['validate']['exp_errcode']
        create_exp_errmsg = data['validate']['errmsg']
        AssertResult.assert_code(r.status_code, create_exp_status_code)
        AssertResult.assert_code(r.json()['errcode'], create_exp_errcode)
        AssertResult.assert_msg_in_text(self, r.json()['errmsg'], create_exp_errmsg)

    @allure.testcase('List All Department')
    def test_list_department(self):
        try:
            r=BaseAPI.get_api(self,list_url,param)
            log.debug(" success list department ")
            log.info(str(r.json()))
            return r
        except:
            log.error(" fail list department")







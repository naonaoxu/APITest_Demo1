import allure
import pytest
from common.assert_result import AssertResult
from common.base_api import BaseAPI
from common.prepare_testdata import PrepareTestData
from config.public_data import *
from utils.prase_yaml import PraseYaml
from utils.util import Util
from common.log import MyLog

param=PrepareTestData.set_token()
log=MyLog()

@allure.feature("Test Create New Department API")
class TestDepartmentAPI:
    @allure.story('Delete Departments')
    def test_delete_all_department(self):
        delete_url = PrepareTestData.set_url(delete_dept_data_path)
        r = self.test_list_department()
        all_department = r.json()['department']
        id_list = []
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

    @allure.story("Story:Create department")
    @allure.description('The description of test create New Department API,it contains 5 senarios')
    @allure.title('{senario}')
    @allure.testcase('This is the link of testcases')
    @pytest.mark.parametrize('senario,data,token,validate', PraseYaml.get_yaml_data(create_dept_data_path, 'case'))
    def test_create_department(self, senario, data, token, validate):
        create_url = PrepareTestData.set_url(create_dept_data_path)
        # prepare name_data
        create_data = data['data']
        if create_data['name'] == "forDuplicateTest":
            pass
        else:
            create_data['name'] = Util.udid(self)
        print("prapare_data :", create_data)

        # prepare token_data
        param = PrepareTestData.set_token(token)
        print('prepare token:', param)

        with allure.step("requestAPI：%s,\
            requestAddress：%s,requestMehod：%s,requestCookie：%s"
                         % (PraseYaml.get_yaml_data(create_dept_data_path, 'config', 'name'),
                            PraseYaml.get_yaml_data(create_dept_data_path, 'config', 'url'),
                            PraseYaml.get_yaml_data(create_dept_data_path, 'config', 'method'), param)):
            #                         % (create_test_case['config']['name'], create_test_case['config']['url'], create_test_case['config']['method'], param))
            allure.attach("Request Senario：", "{0}".format(senario["senario"]))
            allure.attach("Request Data", "{0}".format(data['data']))

        try:
            r = BaseAPI.post_api(self, create_url, create_data, param)
            print(r.json())
            log.debug("success create depart")
            log.info(str(r.json()))
        except:
            log.error("fail create depart")

        create_exp_status_code = validate['validate']['exp_status_code']
        create_exp_errcode = validate['validate']['exp_errcode']
        create_exp_errmsg = validate['validate']['errmsg']
        AssertResult.assert_code(r.status_code, create_exp_status_code)
        AssertResult.assert_code(r.json()['errcode'], create_exp_errcode)
        AssertResult.assert_msg_in_text(self, r.json()['errmsg'], create_exp_errmsg)

    @allure.story('List All Department')
    def test_list_department(self):
        list_url = PrepareTestData.set_url(list_dept_data_path)
        try:
            r=BaseAPI.get_api(self,list_url,param)
            log.debug(" success list department ")
            log.info(str(r.json()))
            return r
        except:
            log.error(" fail list department")







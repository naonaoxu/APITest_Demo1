import os
import time

#整个项目的路径
project_path=os.path.dirname(os.path.dirname(__file__))

#config的路径
config_path=project_path+"\\config\\config.yaml"

#corp数据的路径：
corp_data_path=project_path+"\\config\\corp.yaml"

#BaseUrl数据的路径：
base_url_pth=project_path+"\\config\\config.yaml"

#createdepartment测试数据的路径
create_dept_data_path=project_path+"\\config\\dept_create.yaml"

#listdepartment测试数据的路径
list_dept_data_path=project_path+"\\config\\dept_list.yaml"

#Data Path of delete department
delete_dept_data_path=project_path+"\\config\\dept_delete.yaml"

#log data path
log_path=project_path+'\\log'

#xml report path
xml_report_path=project_path+"\\reports\\xml"

#html report path
html_report_path=project_path+"\\reports\html"

#test_department_path
test_department_path=project_path+"\\testcases\\testdepartment_api.py"

#format time
format_time = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))


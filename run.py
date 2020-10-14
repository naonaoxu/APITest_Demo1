import pytest
from common.log import *
from config.public_data import *

if __name__ == '__main__':
    # perform test
    args = ['-s', '-q', '--alluredir', xml_report_path,test_department_path]
    try:
        pytest.main(args)
        info("success perform test")
    except:
        error("fail perform test")


    #Create allure test report
    cmd = 'allure generate --clean %s -o %s' % (xml_report_path, html_report_path)
    try:
        os.system(cmd)
        info("success create auller report,please goto 'projectpath\reports\html\index.html' to review report")
    except:
        error("fail create alluer report")



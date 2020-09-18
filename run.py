import pytest
from common.log import MyLog
from config.public_data import *

if __name__ == '__main__':

    log = MyLog()

    # perform test
    args = ['-s', '-q', '--alluredir', xml_report_path,test_department_path]
    try:
        pytest.main(args)
        log.info("success perform test")
    except:
        log.error("fail perform test")


    #Create allure test report
    cmd = 'allure generate --clean %s -o %s' % (xml_report_path, html_report_path)
    try:
        os.system(cmd)
        log.info("success create auller report,please goto 'projectpath\reports\html\index.html' to review report")
    except:
        log.error("fail create alluer report")



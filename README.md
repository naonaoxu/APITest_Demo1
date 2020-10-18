**说明**  

**申明:这个演示使用的测试接口是腾讯公开的企业微信的接口；所有测试(框架)代码均为自己撰写，和在职公司的测试(框架)代码无关。**

**测试 API说明:**  
这是企业微信里面创建部门的接口
请求方式：POST（HTTPS）  
请求地址：https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token=ACCESS_TOKEN  
请求body：  
{   
   "name": "name",  
   "name_en": "name_en",   
   "parentid": 1,  
}  

**计划的测试用例为:**  
1.创建成功:status code =200,err_code=0  
2.名字重复:statuscode =200,err_code=60008  
3.parentid不是int32:statuscode =200,err_code=60004  
4.access_token错误:statuscode =200,err_code=40014  
5.access_token为空:statuscode =200,err_code=41001  
6.待续(因为仅仅为一个接口自动化的演示，所以并没有列全).

**如何完成测试并且获得测试报告:**  
1.pip install -r [path of requirements.txt]  
2.run run.py  
3.report address:projectpath\reports\html\index.html  

**代码介绍:**  
这个测试工具，使用python语言编写。
测试用例存储在yaml文件中，通过解析yaml文件，来构建接口数据，再使用python的requests库来向服务器发送接口请求。
将返回的response存储起来，并且断言响应状态码，errorcode等。


**English version ReadMe**  
**Test API:**  
Request Method：POST（HTTPS）  
Request Address：https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token=ACCESS_TOKEN  
Request body：  
{   
   "name": "name",  
   "name_en": "name_en",   
   "parentid": 1,  
}  

**The test case which I plan to test are:**  
1.Success:status code =200,err_code=0  
2.Name duplicate:statuscode =200,err_code=60008  
3.parentid not int32:statuscode =200,err_code=60004  
4.wrong access_token:statuscode =200,err_code=40014  
5.null access_token:statuscode =200,err_code=41001  
6.TBD.

**How to complete the test and get report:**  
1.pip install -r [path of requirements.txt]  
2.run run.py  
3.report address:projectpath\reports\html\index.html  


**Code Introduce:**  
This test tool write by python language.
Test cases store in yaml file,parse yaml file,get interface data,then use requests send interface request to serve.
Store the back response,and assert response code,errorcode,etc.

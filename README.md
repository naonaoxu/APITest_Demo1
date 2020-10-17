**ReadMe**  

**申明:这个demo使用的测试接口是腾讯公开的企业微信的接口；所有测试(框架)代码均为自己撰写，和目前在职公司的测试(框架)代码无关**

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

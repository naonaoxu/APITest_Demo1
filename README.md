**ReadMe**

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

**How to complete the test and get report:**  
1.pip install -r [path of requirements.txt]  
2.run run.py  
3.report address:projectpath\reports\html\index.html  

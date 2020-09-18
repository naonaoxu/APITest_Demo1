import requests
class BaseAPI:
    def get_api(self,url,param):
        """send get request"""
        r =requests.get(url=url,
                        params=param,
                        )
        return r

    def post_api(self,url,data,param):
        """send post request"""
        r=requests.post(url=url,
                        params=param,
                        json=data,
                        )
        return r

    def delete_api(self,url,param):
        """send delete request"""
        r=requests.delete(url=url,
                          params=param)
        return r

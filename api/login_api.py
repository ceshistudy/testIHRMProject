# 导包
import requests

# 创建封装的接口类
class LoginApi:
    def __init__(self):
        self.login_url = "http://ihrm-test.itheima.net" + "/api/sys/login"

    def login(self,jsonDate,headers):
        # 发送登录的请求，并返回response对象
        return requests.post(url=self.login_url,json=jsonDate,headers=headers)
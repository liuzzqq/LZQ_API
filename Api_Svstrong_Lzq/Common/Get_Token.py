import requests

from Conf import Read_Config


#获取登录成功后的token

class Token():
    def __init__(self,env):
        self.env = env # 选择环境
    def get_token(self):
        test_url = Read_Config.Read_Config(self.env, 'host').readconfig()
        test_path = Read_Config.Read_Config(self.env, 'path').readconfig()
        login_url = 'https://' + test_url + test_path
        login_params = Read_Config.Read_Config(self.env, 'loginInfo').readconfig()
        #忽略https证书认证
        #urllib3.disable_warnings()
        #添加请求头信息
        form_header = {"content-type": "application/json"}
        res = requests.post(login_url, login_params,headers=form_header)
        get_token = {'token': ((res.json())['data'])['t']}
        return get_token








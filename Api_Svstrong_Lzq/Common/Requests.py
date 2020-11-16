
from Common import Get_Token
from Common import Consts
import requests
import json



class Request:
    def __init__(self,env):
        self.env = env
    def get_request(self,url,params):
        #获取登录成功后token信息
        get_token = Get_Token.Token('Svs').get_token()
        #判断Get请求中是否包含参数,有参数带参数请求,无参数直接headers访问
        #请求异常抛出
        try:
            if params is None :
                res = requests.get(url=url,headers=get_token)

                return res

            else:
                res = requests.get(url=url,params=params,headers=get_token)

                return res


        except requests.RequestException as e :
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()
        except Exception as e :
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()
            # 计算响应时间并添加全局变量中
            time_consuming = res.elapsed.microseconds / 1000
            time_total = res.elapsed.total_seconds()

            Consts.STRESS_LIST.append(time_consuming)

            # 将返回数据整合放在list中
            res_dict = dict()
            res_dict['code'] = res.status_code
            try:
                res_dict['body'] = res.json()
            except Exception as e:
                print(e)
                res_dict['body'] = ''
            res_dict['text'] = res.text
            res_dict['time_consuming'] = time_consuming
            res_dict['time_total'] = time_total

            return res_dict

    def post_requests(self,url,data):
        #获取登录后token信息
        get_token = Get_Token.Token('Svs').get_token()
        #定义post header信息
        header = get_token

        header.update({"content-type": "application/json"})
        try:
            res = requests.post(url=url,data=json.dumps(data),headers=header)
            return res
        except requests.RequestException as e :
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()
            # 计算响应时间并添加全局变量中
            time_consuming = res.elapsed.microseconds / 1000
            time_total = res.elapsed.total_seconds()


            Consts.STRESS_LIST.append(time_consuming)

            # 将返回数据整合放在list中
            res_dict = dict()
            res_dict['code'] = res.status_code
            try:
                res_dict['body'] = res.json()
            except Exception as e:
                print(e)
                res_dict['body'] = ''
            res_dict['text'] = res.text
            res_dict['time_consuming'] = time_consuming
            res_dict['time_total'] = time_total


            return res_dict

























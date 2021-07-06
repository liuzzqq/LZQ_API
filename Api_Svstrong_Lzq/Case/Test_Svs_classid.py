from time import sleep

from Common import Requests
import unittest
from Conf  import Read_Config

class Test_svs_class(unittest.TestCase):

   def test_class_001(self):
         #创建课程接口
       data = {"class_id":8395,"title":"test","courseware_id":1340,"ai_state":0,"room_id":""}
       path = '/api/v1/tang/create'
       # 获取域名[host]
       test_host = Read_Config.Read_Config('Svs', 'host').readconfig()
       # 拼接接口地址
       url = 'https://' + test_host + path
       res = Requests.Request('Svs').post_requests(url, data)
       print(res.json())
       class_id={"tid" : res.json()['data']['id']}




          #发送截图答题
       data = { "img_url": "https://qn.svstrong.com/2020-12-30-fd7eddeb6f1c4460bcf87543d2357a55.jpeg",
               "question_type": 2, "option_count": 3}
       data.update(class_id)
       path = '/api/v1/question/createScreenQuestion'
       # 拼接接口地址
       url = 'https://' + test_host + path
       res = Requests.Request('Svs').post_requests(url, data)
       print(res.json())
       q_id = res.json()['data']['id']
       question_id = {"question_id":q_id}



           #设置答案
       data = {"answer":["1"],"score":10}
       data.update(question_id)
       path = '/api/v1/question/screenAnswerSet'
         # 拼接接口地址
       url = 'https://' + test_host + path
       res = Requests.Request('Svs').post_requests(url, data)
       print(res.json())





            #开始互动答题
       data ={"interact_id":10614}
       data.update(class_id)
       path = '/api/v1/question/coursewareQuestionPuslish'
       url = 'https://' + test_host + path
       res = Requests.Request('Svs').post_requests(url, data)
       print(res.json())





            #结束互动答题
       data = {"biz_id":1069,"question_state":0}
       data.update(class_id)
       path = '/api/v1/question/coursewareQuestionCommand'
       url = 'https://' + test_host + path
       res = Requests.Request('Svs').post_requests(url, data)
       print(res.json())


            #发送批注
       data = { "img_url":"https://qn.svstrong.com/2020-12-30-831224f7d6ea43d0ba5f2a122feb382d.png"}
       data.update(class_id)
       path = '/api/v1/tang/postil/add'
       url = 'https://' + test_host + path
       res = Requests.Request('Svs').post_requests(url, data)
       print(res.json())

           #结束授课
       data=class_id
       data['id'] = data.pop('tid')
       path = '/api/v1/tang/end'
       url = 'https://' + test_host + path
       res = Requests.Request('Svs').post_requests(url, data)
       print(res.json())



if __name__ == '__main__':
    unittest.main()




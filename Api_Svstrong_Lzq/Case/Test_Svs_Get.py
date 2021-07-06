from Params.Read_TestData import DataTest
import unittest
from ddt import ddt,data

from Conf.Read_Config import Read_Config
from Common.Requests import Request
from Common.Assert import Assert
from Common.Log import Log
from Common import Email

@ddt
class Test_Svs_Get(unittest.TestCase):
    test_data = DataTest('/svs_get.yaml').test_read()
    print(test_data)
    @data(*test_data)
    def test_get_01(self,test_item):
        #获取域名[host]
        test_host = Read_Config('Svs','host').readconfig()
        #拼接接口地址
        url = 'https://' + test_host + test_item['path']
        log = Log()
        #判断接口状态是否开启
        if test_item['status'] == 0:
            res = Request('Svs').get_request(url, test_item['params'])
            log.debug('正在执行第{0}条case:"标题为{1}"'.format(test_item['id'], test_item['dec']))
            code =res.status_code

            #对比接口状态码实际结果与预期结果
            test_code = self.assertEqual(code,200)
            if test_code == None:
                pass
            else:

                log.error('【状态码错误!!】执行第{0}条case:标题为"{1}"'.format(test_item['id'],
                          test_item['dec']))
                print("当前错误码为" + str(code))
            res = res.json()

            #提取接口响应内容进行比较
            test_result = self.assertEqual(res['code'],test_item['expectd_body']['code'])



            if test_result == None:
                log.info('【测试通过!!】执行第{0}条case:标题为"{1}"'.format(test_item['id'], test_item['dec']) + '结束。')
            else:
                log.error('【测试失败!!】执行第{0}条case:标题为"{1}"'.format(test_item['id'], test_item['dec']) + '失败。')
                print("当前接口返回的信息为：" + str(res))

          

        else:
            # Log打印接口状态未开启
            log.warning('未执行第{0}条case:"标题为{1}"'.format(test_item['id'], test_item['dec']) + '未开启状态')












if __name__ == '__main__':
    unittest.main()








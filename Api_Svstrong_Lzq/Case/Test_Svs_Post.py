from Params.Read_TestData import DataTest
import unittest
from ddt import ddt,data
from Conf.Read_Config import Read_Config
from Common.Requests import Request
from Common.Assert import Assert
from Common.Log import Log
from BeautifulReport import BeautifulReport

bf =BeautifulReport
@ddt
class Test_Svs(unittest.TestCase):
    test_data = DataTest('/TestPostData.yaml').test_read()
    @data(*test_data)
    def test_svs_02(self, test_item):
        log = Log()
        # 获取域名[host]
        test_host = Read_Config('Svs', 'host').readconfig()
        # 拼接接口地址
        url = 'https://' + test_host + test_item['path']

        if test_item['status'] == 0:
            res = Request('Svs').post_requests(url, test_item['data'])
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


            res = res.json()['code']

            #提取接口响应内容进行比较
            test_result = self.assertEqual(res,test_item['expectd_body']['code'])


            if test_result == None:
                log.info('【测试通过!!】执行第{0}条case:标题为"{1}"'.format(test_item['id'],
                        test_item['dec']))

            else:
                log.error('【测试失败!!】执行第{0}条case:标题为"{1}"'.format(test_item['id'],
                          test_item['dec']) + '失败。')
                print("当前接口返回的信息为："+str(res))


        else:
            # Log打印接口状态未开启

            log.warning('未执行第{0}条case:"标题为{1}"'.format(test_item['id'],
                        test_item['dec']) + '未开启状态')
            pass






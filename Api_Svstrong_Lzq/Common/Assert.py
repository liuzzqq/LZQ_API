from Common.Log import Log
import unittest



class Assert():

    # def __init__(self,code,expectd_code,body,expectd_body):
    #     self.code = code
    #     self.expected = expectd_code
    #     self.body = body
    #     self.expectd_body = expectd_body


    def assert_code(code,expected):

        try:

            assert code == expected
            return True
        except:
            return False
    def assert_body(body,expectd_body):

        try:
            assert body == expectd_body

            return True

        except:

            return False




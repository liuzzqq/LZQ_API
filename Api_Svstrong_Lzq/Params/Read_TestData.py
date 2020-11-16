

import yaml
import os

class DataTest:
    def __init__(self, yaml_name):
        self.yaml_name = yaml_name

    def test_read(self):

        #当前文件路径
        file_path = '/Users/vita/Desktop/Api_Svstrong_Lzq/Params/Param'
        #拼接yaml文件路径
        yaml_path = file_path+self.yaml_name

        #打开文件
        open_yaml = open(yaml_path,encoding='utf-8')
        #读取yaml文件
        read_yaml = open_yaml.read()
        #加载文件 FullLoader 加载yaml所有文件
        test_data = yaml.load(read_yaml,Loader = yaml.FullLoader)


        return test_data




if __name__ == '__main__':
    test = DataTest('/TestData.yaml').test_read()
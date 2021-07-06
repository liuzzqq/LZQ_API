
"""
通过section和options进行config.ini读取
"""



import configparser


class Read_Config:
    def __init__(self,section,options):
        self.section=section
        self.options=options

    def readconfig(self):
        #文件路径
        config_path = '/Users/vita/Desktop/svs/Api_Svstrong_Lzq/Conf/config.ini'

        config = configparser.ConfigParser()
        config.read(config_path,encoding="utf-8-sig")

        cookie_data=config.get(self.section,self.options)
        print(cookie_data)
        return cookie_data


if __name__ == '__main__':
    test = Read_Config('Svs','host').readconfig()

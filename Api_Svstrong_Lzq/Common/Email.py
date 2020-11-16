
"""
邮件发送直接调用即可

"""


import smtplib
import time
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from Conf import Read_Config
from Common import Log
from Common import Consts

class Email:
    def send_Email(self):
        msg = MIMEMultipart()
        # body = """
        # <h3>Hi，all</h3>
        # <p>本次接口自动化测试报告如下。</p>
        # """
        # mail_body = MIMEText(body, _subtype='html', _charset='utf-8')
        stress_body = Consts.STRESS_LIST
        result_body = Consts.RESULT_LIST
        body2 = 'Hi，all\n本次接口自动化测试报告如下：\n   接口响应时间集：%s\n   接口运行结果集：%s' % (stress_body, result_body)
        mail_body2 = MIMEText(body2, _subtype='plain', _charset='utf-8')
        tm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        msg['Subject'] = Header("接口自动化测试报告" + "_" + tm+"From lzq", 'utf-8')
        msg['From'] = Read_Config.Read_Config('mail', 'sender').readconfig()
        receivers = Read_Config.Read_Config('mail', 'receiver').readconfig()
        toclause = receivers.split(',')
        msg['To'] = ",".join(toclause)
        # msg.attach(mail_body)

        msg.attach(mail_body2)

        try:
            smtp = smtplib.SMTP()
            smtp.connect(Read_Config.Read_Config('mail', 'smtpserver').readconfig())
            smtp.login(Read_Config.Read_Config('mail', 'username').readconfig(), Read_Config.Read_Config('mail', 'password').readconfig())
            smtp.sendmail(Read_Config.Read_Config('mail', 'sender').readconfig(), toclause, msg.as_string())
        except Exception as e:
            print(e)
            print("发送失败")
            Log.Log.info('邮件发送失败，请检查邮件配置')

        else:
            print("发送成功")
            Log.Log.info('邮件发送成功!!!')
        finally:
            smtp.quit()

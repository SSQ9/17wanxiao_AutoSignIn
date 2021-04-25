# coding=utf-8
import smtplib
from email.mime.text import MIMEText
import time

import requests


#import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
  
global contents
contents = ''


yburl = 'https://free-api.heweather.com/s6/weather/forecast'
cyurl = 'https://free-api.heweather.com/s6/weather/lifestyle'

value = {
    'location': '咸阳',
    'key': '1fb7bd7b7a224138b85e1d2f570b86a1',
    'lang': 'zh'
}

ybreq = requests.get(yburl, params=value)
cyreq = requests.get(cyurl, params=value)

ybjs = ybreq.json()
cyjs = cyreq.json()

d3 = ''
for i in range(2):
    yb = ybjs['HeWeather6'][0]['daily_forecast']
    cy = cyjs['HeWeather6'][0]['lifestyle'][1]
    gj = cyjs['HeWeather6'][0]['lifestyle'][0]
    d1 = ''
    if i == 0:
      d1 = '今天'
    elif i == 1:
      d1 = '\r\n\r\n' + '明天'
    else:
      d1 = ''
    d1 += u'\r\n\r\n咸阳' + '\t' + yb[i]['cond_txt_d'] + '\t' + yb[i]['tmp_min'] + '~' + yb[i]['tmp_max'] + '℃'  + '\r\n'
    d1 += yb[i]['wind_dir']  + '\t' + yb[i]['wind_sc'] + '级' + '\r\n'
    d3 += d1
#    d2 = gj['txt'] + ' \r\n' + cy['txt']
#    d3 += d1 + ' \n' + d2

def sendEmail(mail, key):
    subject = " 小黑天气预报 "
    msg_from = '2722436469@qq.com'  # 发送方邮箱，
    passwd = ''.join(key)  # 填入发送方邮箱的授权码
    msg_to = ''.join(mail)   # 收件人邮箱
    content = timer()
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    
    qqtalk = 'https://qmsg.zendee.cn/send/8a5f6ff4bc4be27de56ff8de66e85bb2?msg=' + content + '&qq=2722436469'
    requests.get(qqtalk)
    qqtalk = 'https://qmsg.zendee.cn/send/8a5f6ff4bc4be27de56ff8de66e85bb2?msg=' + content + '&qq=2722436469'
    requests.get(qqtalk)


    try:
        send = smtplib.SMTP_SSL("smtp.qq.com", 465)   # 邮件服务器及端口号
        send.login(msg_from, passwd)
        send.sendmail(msg_from, msg_to, msg.as_string())
        return "邮箱推送成功"
    except Exception:
        return "邮箱推送失败"


def timer():
#    now_time = int(time.time())
#    now_time += 28800
#    t = time.strftime("%Y-%m-%d   %H:%M ", time.localtime(now_time))
    t = ''
    t += d3
    return t 

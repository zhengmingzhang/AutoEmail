#!/home/zhangzhengming/anaconda3/envs/torch/bin/python3.7
# -*- coding: utf-8 -*-
import time
import traceback
from twilio.rest import Client
from get_email import auto_get_email
username = "ecust_zhang@126.com"
authorization_code = "NMMJUJVNCPXKPEYQ"
server_name = "pop.126.com"
auth_token = 'adeba142c44fbcb2c41ab77449307145'  # 去twilio.com注册账户获取token
account_sid = 'ACe1db177682321d67e1738d44be6126e2'
leader_email = "2413226942@qq.com"
text = auto_get_email.run_ing(username, authorization_code, server_name, leader_email)
client = Client(account_sid, auth_token)
print(text)
def sent_message(phone_number):
    mes = client.messages.create(
        from_='+12058435854',  # 填写在active number处获得的号码
        body=text,
        to=phone_number
    )
    print("OK")


sent_message("+86 181 0181 9127")


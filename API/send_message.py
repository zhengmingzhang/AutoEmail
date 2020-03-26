#!/home/zhangzhengming/anaconda3/envs/torch/bin/python3.7
# -*- coding: utf-8 -*-
import time
import traceback
import argparse
from twilio.rest import Client
from get_email import auto_get_email
def sent_message(phone_number, text):
    mes = client.messages.create(
        from_='+12058435854',  # 填写在active number处获得的号码
        body=text,
        to=phone_number
    )
    print("OK")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--username', type=str, help='your email')
    parser.add_argument('--authorization_code', type=str, help='授权码')
    parser.add_argument('--server_name', type=str, help='your pop server email')
    parser.add_argument('--leader_email', type=str, help='the email you want to get from')
    parser.add_argument('--your_number', type=str, help='your phone number')
    # username = "ecust_zhang@126.com"
    # authorization_code = "NMMJUJVNCPXKPEYQ"
    # server_name = "pop.126.com"
    # leader_email = "2413226942@qq.com"
    set = parser.parse_args()
    text = auto_get_email.run_ing(set.username, set.authorization_code, set.server_name, set.leader_email)
    auth_token = 'adeba142c44fbcb2c41ab77449307145'  # 去twilio.com注册账户获取token
    account_sid = 'ACe1db177682321d67e1738d44be6126e2'
    client = Client(account_sid, auth_token)
    print(text)
    sent_message("+86 181 0181 9127", text)


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
    set_args = parser.parse_args()
    text = auto_get_email.run_ing(set_args.username, set_args.authorization_code, set_args.server_name, set_args.leader_email)
    auth_token = '00d93b6c1b581d15c75f26b18b1561f7'
    account_sid = 'ACe1db177682321d67e1738d44be6126e2'
    client = Client(account_sid, auth_token)
    print(set_args.your_number)
    sent_message(set_args.your_number, text)


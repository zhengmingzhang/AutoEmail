#!/home/zhangzhengming/anaconda3/envs/torch/bin/python3.7
# -*- coding: utf-8 -*-
import poplib
import email
import datetime
import locale
import time
from email.parser import Parser
from email.header import decode_header
import traceback
import sys
import telnetlib

# from email.utils import parseaddr
from numpy import unicode


class auto_get_email:
    # 字符编码转换
    @staticmethod
    def mbs_to_utf8(s):
        # 确定运行环境的encoding
        __g_codeset = sys.getdefaultencoding()
        if "ascii" == __g_codeset:
            __g_codeset = locale.getdefaultlocale()[1]
        return s.decode(__g_codeset).encode("utf-8")

    @staticmethod
    def guess_charset(msg):
        charset = msg.get_charset()
        if charset is None:
            content_type = msg.get('Content-Type', '').lower()
            pos = content_type.find('charset=')
            if pos >= 0:
                charset = content_type[pos + 8:].strip()
        return charset

    @staticmethod
    def get_info(msg, str_day):
        # f = open('%s.log' % (str_day), 'w')
        text = ""
        for msg in msg:
            subject = msg.get('subject')
            dh = decode_header(subject)
            subject = dh[0][0].decode(dh[0][1])
            # print("Date: %s"%(msg["Date"]), file=f)
            # print("From: %s"%(email.utils.parseaddr(msg.get('from'))[1]), file = f)
            # print("To: %s"%(email.utils.parseaddr(msg.get('to'))[1]), file = f)
            # print("Subject: %s"%subject, file = f)
            # print("Data:", file = f)
            text += '\n' + "From: %s" % (email.utils.parseaddr(msg.get('from'))[1]) + '\n'
            text += "Subject: %s" % subject
            # text += 'Data: ' + '\n'
            # j = 0
            # for part in msg.walk():
            #     j = j + 1
            #     fileName = part.get_filename()
            #     contentType = part.get_content_type()
            #     mycode = part.get_content_charset()
            #     # 保存附件
            #     if fileName:
            #         data = part.get_payload(decode=True)
            #         h = email.Header.Header(fileName)
            #         dh = email.Header.decode_header(h)
            #         fname = dh[0][0]
            #         encodeStr = dh[0][1]
            #         if encodeStr != None:
            #             fname = fname.decode(encodeStr, mycode)
            #         # end if
            #         fEx = open("%s" % (fname), 'wb')
            #         fEx.write(data)
            #         fEx.close()
            #     elif contentType == 'text/plain':
            #         if mycode == None:
            #             content = part.get_payload(decode=True)
            #         else:
            #             content = part.get_payload(decode=True).decode(mycode)
            #         # print(content, file=f)
            #         text += content + '\n'

        return text

    @staticmethod
    def change_date(date1):
        date1 = " ".join(date1[:-2])
        try:
            date1 = time.strptime(date1, '%a, %d %b %Y')
        except ValueError:
            date1 = time.strptime(date1, '%d %b %Y')
        # 邮件时间格式转换
        date2 = time.strftime("%Y%m%d", date1)
        return date2

    def run_ing(username, authorization_code, server_name, leader_email):
        # 输入邮件地址, 口令和POP3服务器地址:
        email_user = username
        # 此处密码是授权码,用于登录第三方邮件客户端
        password = authorization_code
        pop3_server = server_name
        # 日期赋值
        day = datetime.date.today()
        str_day = str(day).replace('-', '')
        print(str_day)
        text = ""
        # 连接到POP3服务器,有些邮箱服务器需要ssl加密，可以使用poplib.POP3_SSL
        try:
            telnetlib.Telnet(pop3_server, 995)
            server = poplib.POP3_SSL(pop3_server, 995, timeout=10)
        except:
            time.sleep(5)
            server = poplib.POP3(pop3_server, 110, timeout=10)
        # server = poplib.POP3(pop3_server, 110, timeout=120)
        # 可以打开或关闭调试信息
        # server.set_debuglevel(1)
        # 打印POP3服务器的欢迎文字:
        # 身份认证:
        server.user(email_user)
        server.pass_(password)
        # list()返回所有邮件的编号:
        resp, mails, octets = server.list()
        # 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
        index = len(mails)
        date_email = {}
        for i in range(index, 0, -1):
            resp, lines, octets = server.retr(i)
            # lines存储了邮件的原始文本的每一行,
            # 邮件的原始文本:
            msg_content = b'\r\n'.join(lines).decode('utf-8')
            # 解析邮件:
            msg = Parser().parsestr(msg_content)
            # 获取邮件时间,格式化收件时间
            Date = msg.get("Date").split(" ")
            if '' in Date:
                Date.remove('')
            Date = Date[:6]
            date = auto_get_email.change_date(Date)
            email_from = email.utils.parseaddr(msg.get('from'))[1]
            if date == str_day and email_from == leader_email:
                date_email.setdefault(date, set()).add(msg)
            else:
                continue
        if date_email:
            text = auto_get_email.get_info(date_email[str_day], str_day)
        server.quit()
        return text


if __name__ == '__main__':
    username = "ecust_zhang@126.com"
    authorization_code = "NMMJUJVNCPXKPEYQ"
    server_name = "pop.126.com"
    leader_email = "2413226942@qq.com"
    try:
        text = auto_get_email.run_ing(username, authorization_code, server_name, leader_email)
        print(text)
    except Exception as e:
        s = traceback.format_exc()
        print(e)
        tra = traceback.print_exc()

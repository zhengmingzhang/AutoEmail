#!/home/zhangzhengming/anaconda3/envs/torch/bin/python3.7
# -*- coding: utf-8 -*-
import os
import traceback
from crontab import CronTab
from PyQt5 import  QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from API.AutoEmail import Ui_Dialog
class mywindow(QtWidgets.QWidget, Ui_Dialog):
    def __init__(self):
        super(mywindow, self).__init__()
        self.local_place = os.getcwd()
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.readfile)
        self.pushButton.clicked.connect(self.confirm)
    def process(self):
        username = self.textEdit.toPlainText()
        print(username)
        authorization_code = self.textEdit_3.toPlainText()
        print(authorization_code)
        server_name = self.textEdit_4.toPlainText()
        print(server_name)
        auth_token = 'adeba142c44fbcb2c41ab77449307145'  # 去twilio.com注册账户获取token
        account_sid = 'ACe1db177682321d67e1738d44be6126e2'
        leader_email = self.textEdit_2.toPlainText()
        print(leader_email)
        your_number = self.textEdit_5.toPlainText()
        print(your_number)
        python_path = self.lineEdit.text()
        print(python_path)
        time_set = self.timeEdit.text()
        time_set = self.time_process(time_set)
        my_user_cron = CronTab(user=True)
        crontab = my_user_cron.new(command='%s %s/API/send_message.py --username %s --authorization_code '
                                           '%s --server_name %s --leader_email %s '
                                           '--your_number %s> ./art.log 2>&1 &'%(python_path, self.local_place, username,
                                                                                            authorization_code, server_name,
                                                                                            leader_email, your_number),comment='dateinfo')
        crontab.setall(time_set)
        my_user_cron.write()
        print(time_set)

    def readfile(self):
        file_name, file_type = QFileDialog.getOpenFileName(self, "choose", "/", "All Files(*)")
        self.lineEdit.setText(file_name)

    def confirm(self):
        reply = QMessageBox.question(self, "confirm your information","your email is: " + self.textEdit.toPlainText() + " "+'your leader email is: ' +
                             self.textEdit_2.toPlainText() +" "+'your phone number is: ' + self.textEdit_5.toPlainText()
                             + ' '+"the time you set is: " + self.timeEdit.text() + ' ', QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.process()


    def time_process(self, time_set):
        time_set = time_set.split(":")
        hour = time_set[0]
        min = time_set[1]
        second = time_set[2]
        return min+' '+hour+' '+'*'+' '+"*" + ' *'

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = mywindow()
    ui.show()
    sys.exit(app.exec_())

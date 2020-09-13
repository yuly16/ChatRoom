# 新窗体类的定义以及信号的定义

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget
import login
import dialog
import chatroom
import connect
import os


# 定义信号：该信号可以在某个函数中发射，发送到窗体中
class Str_Signal(QtCore.QObject):
    signal = pyqtSignal(str)


warning = Str_Signal()


# 定义新窗体类，该窗体类重写closeEvent方法
class Widget(QWidget):
    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        QCoreApplication.instance().quit()
        os._exit(5)


# 登录界面Ui设计及信号与槽定义
class Ui_Form_login(login.Ui_Form):
    pass


# 聊天界面Ui设计及信号与槽定义
class Ui_Form_chatroom(chatroom.Ui_Form):
    # 初始化窗口定义新的信号
    def setupUi(self, Form):
        chatroom.Ui_Form.setupUi(self, Form)
        # 定义信号
        self.showtestbrowser = Str_Signal()
        self.showtestbrowser.signal.connect(self.textBrowser.append)
        self.pushButton.clicked.connect(self.onclick)
    # 定义按钮的功能
    def onclick(self):
        msg = self.textEdit.toPlainText()
        self.textEdit.setText('')
        connect.sender(msg, warning.signal)


# 提示框的Ui设计及信号与槽的定义
class Ui_Dialog_warning(dialog.Ui_Dialog):
    # 初始化窗口定义新的信号
    def setupUi(self, Dialog):
        dialog.Ui_Dialog.setupUi(self, Dialog)
        # 定义信号

        warning.signal.connect(self.label.setText)
        warning.signal.connect(Dialog.show)


        self.pushButton.clicked.connect(Dialog.close)
        self.pushButton.clicked.connect(self.exit_app)
    def exit_app(self):
        os._exit(5)


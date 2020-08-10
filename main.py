import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog
import login, chatroom
import connect
import threading
from window import *

# 处理登录事项
def main_login():
    # 登录
    name = ui1.textEdit.toPlainText()
    if name != '':
        # 和服务器建立第一次连接
        status = connect.first_connect(name, warning.signal)
        if status == 0:
            # 窗口转换
            Chatroom.show()
            MainWindow.close()
            ui2.title.setText(name)
            t = threading.Thread(target=connect.receiver, args=(ui2.showtestbrowser.signal, warning.signal, name))
            t.start()


# def config():
#     f = open('config', 'r')
#     f_lines = f.readlines()
#     f.close()
#     global host
#     global port
#     host = f_lines[0].split('=')[-1].strip()
#     port = int(f_lines[1].split('=')[-1].strip())

def main():
    app = QApplication(sys.argv)

    # print(host, type(host))
    # print(port, type(port))
    # # 初始化网络配置
    # config()
    # print(host, type(host))
    # print(port, type(port))
    # 定义窗口
    global MainWindow
    global ui1
    MainWindow = QWidget()
    ui1 = Ui_Form_login()
    ui1.setupUi(MainWindow)

    global Chatroom
    global ui2
    Chatroom = Widget()
    ui2 = Ui_Form_chatroom()
    ui2.setupUi(Chatroom)

    global Warning
    global ui3
    Warning = QDialog()
    ui3 = Ui_Dialog_warning()
    ui3.setupUi(Warning)
    # 定义信号和槽
    ui1.pushButton.clicked.connect(main_login)



    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
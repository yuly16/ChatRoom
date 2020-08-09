import sys
from PyQt5.QtWidgets import QApplication, QWidget
import login, chatroom
import connect
import threading
from chatroom import Widget

# 处理登录事项
def main_login():
    # 登录
    name = ui1.textEdit.toPlainText()
    if name != '':
        # 和服务器建立第一次连接
        connect.first_connect(name)
        # 窗口转换
        Chatroom.show()
        MainWindow.close()
        ui2.title.setText(name)
        t = threading.Thread(target=connect.receiver, args=(ui2.showtestbrowser.signal,))
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
    ui1 = login.Ui_Form()
    ui1.setupUi(MainWindow)

    global Chatroom
    global ui2
    Chatroom = Widget()
    ui2 = chatroom.Ui_Form()
    ui2.setupUi(Chatroom)

    # 定义信号和槽
    ui1.pushButton.clicked.connect(main_login)
    ui2.pushButton.clicked.connect(ui2.onclick)


    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
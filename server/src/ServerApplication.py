# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/13
# ide：PyCharm
# describe：服务器启动类
# editDate：
# editBy：
# version：1.0.0

import sys
from gui import MainWindow
from PyQt5 import QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow.MainWindow()
    window.show()

    if app.exec_() == 0:
        print("窗口关闭了，保存聊天记录")

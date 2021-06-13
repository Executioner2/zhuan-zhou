# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/3
# ide：PyCharm
# describe：客户端启动类
# editDate：
# editBy：
# version：1.0.0

import sys
from gui import MainWindow, LoginWindow
from PyQt5 import QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    loginWindows = LoginWindow.LoginWindow()
    mainWindow = MainWindow.MainWindow()

    loginWindows.show()
    loginWindows.skipSignal.connect(mainWindow.recevieSkipSignal)

    sys.exit(app.exec_())



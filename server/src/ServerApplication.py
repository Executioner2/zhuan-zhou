# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/13
# ide：PyCharm
# describe：服务器启动类
# editDate：
# editBy：
# version：1.0.0

import sys
from server.src.gui import MainWindow
from PyQt5 import QtWidgets
from server.src.signal import ServerSignal
from server.src.service import SocketService

if __name__ == '__main__':
    # 自定义信号类
    serverSignal = ServerSignal.ServerSignal()

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow.MainWindow(serverSignal)
    window.show()

    # 开启socket服务
    # socketService = SocketService.SocketService()
    # socketService.start(serverSignal)

    sys.exit(app.exec_())

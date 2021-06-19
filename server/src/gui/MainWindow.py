# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/13
# ide：PyCharm
# describe：
# editDate：
# editBy：
# version：1.0.0

import re

from PyQt5 import QtWidgets, QtGui

from server.src.thread_ import ServerSocketThread
from server.src.ui import MainWindow_ui


class MainWindow(QtWidgets.QMainWindow, MainWindow_ui.Ui_MainWindow):

    """重写关闭确认"""
    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        result = QtWidgets.QMessageBox.question(
            self, "退出服务端", "确认要退出服务端？",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            # TODO 保存聊天记录
            a0.accept()
            QtWidgets.QWidget.closeEvent(self, a0)
        else:
            a0.ignore()

    def __init__(self, serverSignal):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.serverSignal = serverSignal
        self.startServerBtn.clicked.connect(self.on_startServer_cliecked)
        # 启动socket服务线程
        self.socketService = ServerSocketThread.SocketService(serverSignal)


    """服务器开关"""
    def on_startServer_cliecked(self):
        if self.startServerBtn.text() == "启动服务器":
            pattern = re.compile(
                r'^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]{1,2})(\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]{1,2})){3}$')
            result = pattern.match(self.serverIpLE.text())
            if not result:
                msgHint = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "警告", "请输入正确的ip地址格式")
                msgHint.exec_()
                return
            pattern = re.compile(r'^\d+$')
            port = self.serverPortLE.text()
            result = pattern.match(port)
            if result:
                # 是数字
                if int(port) < 0 or int(port) > 65535:
                    msgHint = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "警告", "端口号必须是0-65535")
                    msgHint.exec_()
                    return
            else:
                # 不是数字
                msgHint = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "警告", "端口号必须是整数")
                msgHint.exec_()
                return
            # 执行到这儿表示上面没问题才开启服务器
            self.serverSignal.startupSignal.emit((self.serverIpLE.text(), int(self.serverPortLE.text())))
            self.serverIpLE.setEnabled(False)
            self.serverPortLE.setEnabled(False)
            self.startServerBtn.setText("关闭服务器")
        else:
            self.serverSignal.shutdownSignal.emit()
            self.serverIpLE.setEnabled(True)
            self.serverPortLE.setEnabled(True)
            self.startServerBtn.setText("启动服务器")
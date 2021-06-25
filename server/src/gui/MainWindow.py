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

from model.dto import ServerDataRecordDto
from model.enum_.GroupNameEnum import GroupNameEnum


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
        self.setWindowTitle("小又丑服务端")
        self.dataRecord = self.readDataRecordFile()
        self.serverSignal = serverSignal
        self.startServerBtn.clicked.connect(self.on_startServer_cliecked)
        # 启动socket服务线程
        self.socketService = ServerSocketThread.SocketService(serverSignal, self.dataRecord)
        # 更新数据记录
        self.serverSignal.updateDataRecordSignal.connect(self.updateDataRecord)
        # 添加条件记录预览
        self.serverSignal.insertMsgRecordSignal.connect(self.insertMsgRecord)
        # 移除指定项
        # self.clientListWidget.removeItemWidget(self.clientListWidget.takeItem(i))

    """可视化消息记录"""
    def insertMsgRecord(self, msgDto):
        content = msgDto["content"]
        nickname = msgDto["nickname"]
        datetime_ = msgDto["datetime_"]
        # 显示去除毫秒微秒
        index = datetime_.find(".")
        if index != -1: datetime_ = datetime_[:index]

        objName = GroupNameEnum.getObjNameByNo(msgDto["group"])
        listWidget = self.findChild(QtWidgets.QListWidget, objName)
        # 空白行
        spaceItem = QtWidgets.QListWidgetItem(listWidget)
        spaceItem.setText("")
        # 日期时间 用户行
        titleItem = QtWidgets.QListWidgetItem(listWidget)
        title = "{}  {}".format(datetime_, nickname)
        titleItem.setForeground(QtGui.QBrush(QtGui.QColor(0, 0, 255))) # 设置前景色
        titleItem.setText(title)
        # 内容行
        contentItem = QtWidgets.QListWidgetItem(listWidget)
        contentItem.setText(content)


    """读取数据记录文件"""
    def readDataRecordFile(self):
        dataRecord = ServerDataRecordDto.ServerDataRecordDto()
        # TODO 读取记录文件，并把读取的数据给dataRecord对象
        return dataRecord

    """更新数据记录到ui上"""
    def updateDataRecord(self):
        self.nowPeoples.setText(str(self.dataRecord.nowPeoples) + "人")
        self.maxPeoples.setText(str(self.dataRecord.maxPeoples) + "人")
        self.nowFlows.setText(str(self.dataRecord.nowFlows) + "条")
        self.maxFlows.setText(str(self.dataRecord.maxFlows) + "条")

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
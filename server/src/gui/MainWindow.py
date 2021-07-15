# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/13
# ide：PyCharm
# describe：
# editDate：
# editBy：
# version：1.0.0
import datetime
import os
import pickle
import re
import sys

from PyQt5 import QtWidgets, QtGui

from server.src.thread_ import ServerSocketThread
from server.src.ui import MainWindow_ui

from model.dto import ServerDataRecordDto
from model.enum_.GroupNameEnum import GroupNameEnum
from common.util import ConfigFileUtil

FILENAME = "records.data"
SERVICE_DATA_FILE = "/resource/data_record/serverRecord.data"

class MainWindow(QtWidgets.QMainWindow, MainWindow_ui.Ui_MainWindow):
    msgList = [] # 消息记录集合
    clientAddressList = [] # 客户端地址集合

    """重写关闭确认"""
    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        result = QtWidgets.QMessageBox.question(
            self, "退出服务端", "确认要退出服务端？",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            # 保存历史数据记录
            folder = os.path.dirname(os.path.dirname(sys.argv[0])) + "/resource/data_record/"
            if not os.path.exists(folder): os.makedirs(folder)
            path = folder + "serverRecord.data"
            with open(path, "wb") as f:
                pickle.dump(self.dataRecord, f)

            # 保存聊天记录
            today = str(datetime.date.today())
            folder = os.path.dirname(os.path.dirname(sys.argv[0])) + "/resource/records/" + today + "/"
            if not os.path.exists(folder): os.makedirs(folder)
            path = folder + FILENAME
            for item in self.msgList:
                with open(path, "ab") as f:
                        pickle.dump(item, f)

            # 保存ip和端口到配置文件
            folder = os.path.dirname(os.path.dirname(sys.argv[0])) + "/resource/config/"
            if not os.path.exists(folder): os.makedirs(folder)
            path = folder + "connect_config.ini"
            params = {"ip": self.serverIpLE.text(), "port": int(self.serverPortLE.text())}
            ConfigFileUtil.wirteConfig(path, params)

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
        # 服务器开关
        self.startServerBtn.clicked.connect(self.on_startServer_cliecked)
        # 启动socket服务线程
        self.socketService = ServerSocketThread.SocketService(serverSignal, self.dataRecord, self.msgList, self.clientAddressList)
        # 更新数据记录
        self.serverSignal.updateDataRecordSignal.connect(self.updateDataRecord)
        # 添加条件记录预览
        self.serverSignal.insertMsgRecordSignal.connect(self.insertMsgRecord)
        # 加载聊天记录
        self.checkRecordFile.clicked.connect(self.on_checkRecordFile_click)
        # 添加客户端信息到列表
        self.serverSignal.insertClientInfoSignal.connect(self.inserClientInfo)
        # 移除指定项
        self.serverSignal.removeClientInfoSignal.connect(self.removeClientInfo)
        # 读取数据记录
        self.readDataRecordFile()
        # 读取配置文件
        self.readConfig()

    """读取配置文件设置ip和端口"""
    def readConfig(self):
        path = os.path.dirname(os.path.dirname(sys.argv[0])) + "/resource/config/connect_config.ini"
        if os.path.exists(path):
            result = ConfigFileUtil.readConfig(path)
            self.serverIpLE.setText(result[0][1])
            self.serverPortLE.setText(result[1][1])

    """移除列表中的客户端信息"""
    def removeClientInfo(self, address):
        index = self.clientAddressList.index(address) + 1
        self.clientAddressList.remove(address)
        self.clientListWidget.removeItemWidget(self.clientListWidget.takeItem(index))

    """添加客户端信息到列表"""
    def inserClientInfo(self, address):
        item = QtWidgets.QListWidgetItem(self.clientListWidget)
        text = "客户端IP：{}     客户端端口：{}".format(address[0], str(address[1]))
        item.setText(text)

    """加载聊天记录"""
    def on_checkRecordFile_click(self):
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(self, "选取聊天记录文件", "../resource/records", "Data File(*.data);")
        tempList = []
        try:
            if not os.path.exists(fileName): return
            with open(fileName, "rb") as f:
                while True:
                    tempList.append(pickle.load(f))
        except EOFError:
            pass
        for item in tempList:
            self.insertMsgRecord(item)


    """可视化消息记录"""
    def insertMsgRecord(self, msgDto):
        content = msgDto.content
        nickname = msgDto.nickname
        datetime_ = msgDto.datetime_
        # 显示去除毫秒微秒
        index = datetime_.find(".")
        if index != -1: datetime_ = datetime_[:index]

        objName = GroupNameEnum.getObjNameByNo(msgDto.group)
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
        filename = os.path.dirname(os.path.dirname(sys.argv[0])) + SERVICE_DATA_FILE
        # 读取记录文件，并把读取的数据给dataRecord对象
        if os.path.exists(filename):
            with open(filename, "rb") as f:
                temp = pickle.load(f)
            dataRecord.maxFlows = temp.maxFlows
            dataRecord.maxPeoples = temp.maxPeoples
        self.updateDataRecord(dataRecord)
        return dataRecord

    """更新数据记录到ui上"""
    def updateDataRecord(self, data):
        self.nowPeoples.setText(str(data.nowPeoples) + "人")
        self.maxPeoples.setText(str(data.maxPeoples) + "人")
        self.nowFlows.setText(str(data.nowFlows) + "条")
        self.maxFlows.setText(str(data.maxFlows) + "条")

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
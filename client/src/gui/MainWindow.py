# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/9
# ide：PyCharm
# describe：主窗口
# editDate：
# editBy：
# version：1.0.0
import copy
import os
import sys
import time

from PyQt5 import QtWidgets, QtGui, QtCore

from client.src.signal import ClientSignal
from client.src.thread_ import ClientReceiveThread
from client.src.ui import MainWindow_ui
from common.util import MsgWidgetUtil
from model.enum_.MsgTypeEnum import MsgTypeEnum
from common.util import TransmitUtil
from common.result.Result import Result
from common.result.IndexTableEnum import IndexTableEnum
from model.dto import MsgDto
import datetime
import pickle

SELECT_STYLE = "background-color: rgb(186, 186, 186)" # 选中时的样式
COUNT = 20 # 历史消息每次加载数量为20

class MainWindow(QtWidgets.QMainWindow, MainWindow_ui.Ui_MainWindow, QtCore.QObject):
    username = None # 用户名，用来登录的那个，唯一的
    headStyle = None # 头像颜色
    nickname = None # 昵称
    clientSocket = None  # socket
    checkedGroupIndex = 0  # 选中的群组的下标，默认第一个分组
    inputBoxList = []  # 输入框的内容
    groupVLList = []  # 群组对象集合
    groupMsgWidgetList = [] # 群组消息widget集合，用于存放msgWidget集合
    groupMsgList = [] # 消息集合，方便存聊天记录
    groupMsgHistoryList = []  # 历史消息集合
    groupMsgHistoryWidgetList = [] # 历史消息widget集合
    msgSectionList = [] # 消息切片

    """重写窗口缩放事件"""
    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        # 重新设置sendWidget的坐标
        if len(self.groupMsgWidgetList) > 0:
            msgWidgetList = self.groupMsgWidgetList[self.checkedGroupIndex]
            MsgWidgetUtil.refresh(self.scrollArea, self.scrollWidget, self.msgHistoryLabel, msgWidgetList)

    """重写关闭确认"""
    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        result = QtWidgets.QMessageBox.question(
            self, "退出客户端", "确认要退出客户端？",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            try:
                # 保存聊天记录
                folder = os.path.dirname(os.path.dirname(sys.argv[0])) + "/resource/user_file/" + self.username + "/records/"
                if not os.path.exists(folder): os.makedirs(folder)
                for index in range(len(self.groupMsgList)):
                    path = folder + str(index) + ".data"
                    with open(path, "ab") as f:
                        for item in self.groupMsgList[index]: # 保存list中的元素，方便读取
                            pickle.dump(item, f)
                a0.accept()
                QtWidgets.QWidget.closeEvent(self, a0)
            finally:
                # 关闭客户端socket
                self.clientSocket.close()
        else:
            a0.ignore()

    """初始化"""
    def __init__(self, clientSignal:ClientSignal):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.clientSignal = clientSignal
        # 绑定发送按钮（当发送按钮发送消息时追加消息）
        self.pushBtn.clicked.connect(self.sendMsg)
        self.textEdit.sendSignal.connect(self.sendMsg)
        self.clientSignal.skipSignal.connect(self.recevieSkipSignal)
        self.clientSignal.msgReceiveSignal.connect(self.addMsgWidgets)
        # 鼠标点击事件
        self.msgHistoryLabel.mouseReleaseSignal.connect(self.checkMsgHistory)
        self.group1.mouseReleaseSignal.connect(self.on_mouseClick_clicked)
        self.group2.mouseReleaseSignal.connect(self.on_mouseClick_clicked)
        self.group3.mouseReleaseSignal.connect(self.on_mouseClick_clicked)
        # 设置鼠标跟踪
        self.group1.isSelected = True  # 设置组1默认选中

    """查看历史消息"""
    def checkMsgHistory(self):
        length = self.msgSectionList[self.checkedGroupIndex]
        tempWidgetList = self.groupMsgHistoryWidgetList[self.checkedGroupIndex][0:length]
        if len(tempWidgetList) > length:
            MsgWidgetUtil.addMsgHistory(self.verticalLayout, self.scrollWidget, self.scrollArea, tempWidgetList,
                                        self.groupMsgWidgetList[self.checkedGroupIndex], True)
            self.msgSectionList[self.checkedGroupIndex] = length + COUNT
            return

        tempList = self.groupMsgHistoryList[self.checkedGroupIndex][-length:None]
        if length - COUNT < len(self.groupMsgHistoryList[self.checkedGroupIndex]):
            resultList = MsgWidgetUtil.addMsgHistory(self.verticalLayout, self.scrollWidget, self.scrollArea, tempList,
                                                     self.groupMsgWidgetList[self.checkedGroupIndex])
            resultList.extend(self.groupMsgHistoryWidgetList[self.checkedGroupIndex])
            self.groupMsgHistoryWidgetList[self.checkedGroupIndex] = resultList
            self.msgSectionList[self.checkedGroupIndex] = length + COUNT
        else:
            msgBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, "提示", "没有更多的历史消息记录了")
            msgBox.exec_()


    """读取聊天记录"""
    def readRecordFile(self):
        folder = os.path.dirname(os.path.dirname(sys.argv[0])) + "/resource/user_file/" + self.username + "/records/"
        begin = int(round(time.time() * 1000))
        for index in range(len(self.groupMsgList)):
            path = folder + str(index) + ".data"
            # 如果不存则下一个
            if not os.path.exists(path): continue
            try:
                with open(path, "rb") as f:
                    while True:
                        self.groupMsgHistoryList[index].append(pickle.load(f))
            except EOFError: # 抛出此异常表示文件没有数据可读了，所以pass过去
                pass
        end = int(round(time.time() * 1000))
        print("读取文件耗时：", end - begin)

    """点击了某个群组"""
    def on_mouseClick_clicked(self, widget:QtWidgets.QWidget):
        groupIndex = int(widget.objectName()[-1]) - 1 # 取得组号
        if widget.isSelected:
            # 当前点击了已经选中的群组就直接返回
            return
        else:
            # 不是当前选中的分组，把当前的分组中的输入消息记录存入inputBoxList中
            self.inputBoxList[self.checkedGroupIndex] = self.textEdit.toPlainText()
            # 初始化上一群组的部分值
            self.msgSectionList[self.checkedGroupIndex] = COUNT
            self.groupVLList[self.checkedGroupIndex].setStyleSheet("") # 设置无背景色
            self.groupVLList[self.checkedGroupIndex].isSelected = False
            # 当前群组
            widget.isSelected = True
            widget.setStyleSheet(SELECT_STYLE)
            self.checkedGroupIndex = groupIndex # 设置当前选中的群组的下标
            # 重绘聊天区域
            MsgWidgetUtil.redraw(self.verticalLayout, self.scrollWidget,
                                 self.groupMsgWidgetList[self.checkedGroupIndex],
                                 self.scrollArea, self.textEdit, self.inputBoxList[self.checkedGroupIndex])

    """接收到登录页跳转信号"""
    def recevieSkipSignal(self, params):
        loginDto = params[0]
        self.clientSocket = params[1]
        self.show()
        self.headStyle = loginDto.headStyle
        self.nickname = loginDto.nickname
        self.username = loginDto.username
        self.setWindowTitle("CHAT  user:{}  serverIp:{}  serverPort:{}".format(self.nickname, loginDto.serverIp, loginDto.serverPort))
        # 获得groupVL中所有的widget（所有分组）
        for index in range(self.groupVL.count()):
            child = self.groupVL.itemAt(index).widget()
            self.groupVLList.append(child) # 把群组存入群组集合
            self.groupMsgWidgetList.append([]) # 不要用下面的*来创建，创建的是同一个list
            self.groupMsgList.append([])
            self.groupMsgHistoryWidgetList.append([])
            self.msgSectionList.append(COUNT)
            self.groupMsgHistoryList.append([])
        # 初始化数据框list的大小
        self.inputBoxList = [""] * self.groupVL.count()
        # 读取聊天文件
        self.readRecordFile()
        self.msgHistoryLabel.setFixedSize(self.scrollArea.width() - 5, 14) # 设置历史消息label的大小，要在ui.show()后设置才有效
        # 启动消息接收线程
        self.clientReceiveThread = ClientReceiveThread.ClientReceiveThread(self.clientSocket, self.clientSignal)
        self.clientReceiveThread.start()

    """通过socket发送消息"""
    def sendMsg(self):
        msg = self.textEdit.toPlainText()
        msgDto = MsgDto.MsgDto(self.checkedGroupIndex, msg, MsgTypeEnum.SEND.value, datetime.datetime.now())
        # 先发送过去，发过去了再显示到聊天框中
        TransmitUtil.send(self.clientSocket, Result.ok(IndexTableEnum.NOTIFY.value, msgDto))
        # 封装参数
        msgDto.nickname = self.nickname
        msgDto.headStyle = self.headStyle
        msgDto.content = msg
        msgDto.group = self.checkedGroupIndex
        # 可视化
        self.addMsgWidgets(msgDto)

    """添加widget"""
    def addMsgWidgets(self, msgDto, isHistory=None):
        # 超简单设置文本效果
        msgObj = MsgWidgetUtil.simpleSetStyle(self.scrollWidget, self.verticalLayout, self.scrollArea, msgDto, self.checkedGroupIndex)

        # 添加到集合中
        self.groupMsgWidgetList[msgDto.group].append(msgObj)
        if isHistory != True:
            self.groupMsgList[msgDto.group].append(msgDto)
            if msgDto.type == MsgTypeEnum.SEND.value:
                # 如果是发送则清空textEdit的内容
                self.textEdit.clear()
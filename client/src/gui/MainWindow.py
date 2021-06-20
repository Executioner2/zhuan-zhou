# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/9
# ide：PyCharm
# describe：主窗口
# editDate：
# editBy：
# version：1.0.0

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


class MainWindow(QtWidgets.QMainWindow, MainWindow_ui.Ui_MainWindow, QtCore.QObject):
    mouseClick = QtCore.pyqtSignal(object)
    headStyle = None # 头像颜色
    username = None # 用户名
    groupMsgWidgetList = [] # 群组消息widget集合，用于存放msgWidget集合
    groupPositionList = [] # 群组坐标集合
    groupVLList = [] # 群组对象集合
    checkedGroupIndex = 0 # 选中的群组的下标，默认第一个分组
    inputBoxList = [] # 输入框的内容
    clientSocket = None # socket

    """重写鼠标点击信号"""
    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent) -> None:
        self.mouseClick.emit(a0)

    """重写窗口缩放事件"""
    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        # 重新设置sendWidget的坐标
        if len(self.groupMsgWidgetList) > 0:
            msgWidgetList = self.groupMsgWidgetList[self.checkedGroupIndex]
            MsgWidgetUtil.refresh(self.scrollArea, self.scrollWidget, msgWidgetList)

    """重写关闭确认"""
    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        result = QtWidgets.QMessageBox.question(
            self, "退出客户端", "确认要退出客户端？",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            try:
                # TODO 保存聊天记录
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
        # 鼠标点击事件
        self.mouseClick.connect(self.on_mouseClick_clicked)
        # 绑定发送按钮（当发送按钮发送消息时追加消息）
        self.pushBtn.clicked.connect(self.sendMsg)
        self.textEdit.sendSignal.connect(self.sendMsg)
        self.clientSignal.skipSignal.connect(self.recevieSkipSignal)
        self.clientSignal.msgReceiveSignal.connect(self.addReceiveMsgWidgets)

    """检测是否点击到了群组列表"""
    def on_mouseClick_clicked(self, a0: QtGui.QMouseEvent):
        flag = False
        for index, item in enumerate(self.groupPositionList):
            if a0.x() >= item[0] and a0.x() <= item[1] and a0.y() >= item[2] and a0.y() <= item[3]:
                if self.checkedGroupIndex == index:
                    # 如果当前点击了已经选中的群组就直接返回
                    return
                else:
                    # 如果不是当前选中的分组，那么把当前的分组中的输入消息记录存入inputBoxList中
                    self.inputBoxList[self.checkedGroupIndex] = self.textEdit.toPlainText()
                    flag = True
                    # 遍历设置所有群组无背景色
                    for temp in self.groupVLList:
                        temp.setStyleSheet("")
                    # 设置当前选中的群组的背景色
                    self.groupVLList[index].setStyleSheet("background-color: rgb(186, 186, 186)")
                    self.checkedGroupIndex = index # 设置当前选中的群组的下标
                    break
        # 选中的是群组才重绘
        if flag:
            # 重绘聊天区域
            MsgWidgetUtil.redraw(self.verticalLayout, self.scrollWidget, self.groupMsgWidgetList[self.checkedGroupIndex],
                             self.scrollArea, self.textEdit, self.inputBoxList[self.checkedGroupIndex])

    """接收到登录页跳转信号"""
    def recevieSkipSignal(self, params):
        loginDto = params[0]
        self.clientSocket = params[1]
        self.show()
        self.headStyle = loginDto.headStyle
        self.username = loginDto.nickname
        self.setWindowTitle("CHAT  user:{}  serverIp:{}  serverPort:{}".format(self.username, loginDto.serverIp, loginDto.serverPort))
        # 获得groupVL中所有的widget（所有分组）
        for index in range(self.groupVL.count()):
            child = self.groupVL.itemAt(index).widget()
            self.groupVLList.append(child) # 把群组存入群组集合
            tempTuple = (child.x(), child.width() + child.x(), child.y(),
                         child.height() + child.y())  # (left_x, right_x, top_y, bottom_y)
            self.groupPositionList.append(tempTuple)
            self.groupMsgWidgetList.append([]) # 不要用下面的*来创建，创建的是同一个list
        # 初始化数据框list的大小
        self.inputBoxList = [""] * self.groupVL.count()
        # 启动消息接收线程
        self.clientReceiveThread = ClientReceiveThread.ClientReceiveThread(self.clientSocket, self.clientSignal)
        self.clientReceiveThread.start()


    """通过socket发送消息"""
    def sendMsg(self):
        msg = self.textEdit.toPlainText()
        msgDto = MsgDto.MsgDto(self.checkedGroupIndex, msg)
        # 先发送过去，发过去了再显示到聊天框中
        TransmitUtil.send(self.clientSocket, Result.ok(IndexTableEnum.NOTIFY.value, msgDto))
        self.addSendMsgWidgets(msg)

    """添加接收消息到聊天界面"""
    def addReceiveMsgWidgets(self, params):
        msg = params.content
        group = params.group
        nickname = params.nickname
        headStyle = params.headStyle

        # 超简单设置文本效果
        widget = MsgWidgetUtil.simpleSetStyle(self.scrollWidget, self.verticalLayout, self.scrollArea,
                                              MsgTypeEnum.RECEIVE, nickname, headStyle, msg, group)
        # 添加到集合中
        msgObj = {"widget":widget, "type":MsgTypeEnum.RECEIVE}
        self.groupMsgWidgetList[self.checkedGroupIndex].append(msgObj)


    """添加发送到聊天界面"""
    def addSendMsgWidgets(self, msg):
        # 超简单设置文本效果
        widget = MsgWidgetUtil.simpleSetStyle(self.scrollWidget, self.verticalLayout, self.scrollArea,
                                              MsgTypeEnum.SEND, self.username, self.headStyle, msg, self.checkedGroupIndex)
        # 添加到集合中
        msgObj = {"widget": widget, "type": MsgTypeEnum.SEND}
        self.groupMsgWidgetList[self.checkedGroupIndex].append(msgObj)
        # 清空textEdit的内容
        self.textEdit.clear()
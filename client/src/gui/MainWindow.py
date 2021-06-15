# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/9
# ide：PyCharm
# describe：主窗口
# editDate：
# editBy：
# version：1.0.0

from client.src.ui import MainWindow_ui
from enum_.MsgTypeEnum import MsgTypeEnum
from client.src.util.MsgWidgetUtil import MsgWidgetUtil
from PyQt5 import QtWidgets, QtGui, QtCore
from dto import LoginDto


class MainWindow(QtWidgets.QMainWindow, MainWindow_ui.Ui_MainWindow, QtCore.QObject):
    mouseClick = QtCore.pyqtSignal(object)
    headColor = None # 头像颜色
    username = None # 用户名
    msgWidgetList = [] # 消息widget集合
    groupMsgWidgetList = [] # 群组消息widget集合，用于存放上面的widget集合
    groupPositionList = [] # 群组坐标集合
    groupVLList = [] # 群组对象集合
    checkedGroupIndex = 0 # 选中的群组的下标，默认第一个分组
    inputBoxList = [] # 输入框的内容

    """重写鼠标点击信号"""
    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent) -> None:
        self.mouseClick.emit(a0)

    """重写窗口缩放事件"""
    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        # 重新设置sendWidget的坐标
        MsgWidgetUtil.refresh(self.scrollArea, self.scrollWidget, self.msgWidgetList)

    """重写关闭确认"""
    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        result = QtWidgets.QMessageBox.question(
            self, "退出客户端", "确认要退出客户端？",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            # TODO 保存聊天记录
            a0.accept()
            QtWidgets.QWidget.closeEvent(self, a0)
        else:
            a0.ignore()

    """初始化"""
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        # 绑定发送按钮（当发送按钮发送消息时追加消息）
        # self.pushBtn.clicked.connect(self.addReceiveMsgWidgets)
        self.pushBtn.clicked.connect(self.sendMsg)
        self.mouseClick.connect(self.checkClickGroup)


    """检测是否点击到了群组列表"""
    def checkClickGroup(self, a0: QtGui.QMouseEvent):
        for index, item in enumerate(self.groupPositionList):
            if a0.x() >= item[0] and a0.x() <= item[1] and a0.y() >= item[2] and a0.y() <= item[3]:
                if self.checkedGroupIndex == index:
                    # 如果当前点击了已经选中的群组就直接返回
                    return
                else:
                    # 如果不是当前选中的分组，那么把当前的分组中的输入消息记录存入inputBoxList中
                    self.inputBoxList[self.checkedGroupIndex] = self.textEdit.toPlainText()
                # 遍历设置所有群组无背景色
                for temp in self.groupVLList:
                    temp.setStyleSheet("")
                # 设置当前选中的群组的背景色
                self.groupVLList[index].setStyleSheet("background-color: rgb(186, 186, 186)")
                self.checkedGroupIndex = index # 设置当前选中的群组的下标
                break
        # TODO 重绘聊天区域
        # 重设输入框文本
        self.textEdit.setPlainText(self.inputBoxList[self.checkedGroupIndex])
        # 光标移动至最后
        self.textEdit.moveCursor(QtGui.QTextCursor.End)


    """接收到登录页跳转信号"""
    def recevieSkipSignal(self, loginDto:LoginDto):
        self.show()
        self.headColor = loginDto.headStyle
        self.username = loginDto.cryp if loginDto.cryp else loginDto.token
        # 获得groupVL中所有的widget（所有分组）
        for index in range(self.groupVL.count()):
            child = self.groupVL.itemAt(index).widget()
            self.groupVLList.append(child) # 把群组存入群组集合
            tempTuple = (child.x(), child.width() + child.x(), child.y(),
                         child.height() + child.y())  # (left_x, right_x, top_y, bottom_y)
            self.groupPositionList.append(tempTuple)
        # 初始化数据框list的大小
        self.inputBoxList = [""] * self.groupVL.count()
        self.groupMsgWidgetList = [[]] * self.groupVL.count()


    """通过socket发送消息"""
    def sendMsg(self):
        msg = self.textEdit.toPlainText()
        # 先发送过去，发过去了再显示到聊天框中
        self.addSendMsgWidgets(msg)


    """添加接收消息到聊天界面"""
    def addReceiveMsgWidgets(self, msg, checkedGroupIndex = None):
        # 超简单设置文本效果
        widget = MsgWidgetUtil.simpleSetStyle(self.scrollWidget, self.verticalLayout, self.scrollArea,
                                              MsgTypeEnum.RECEIVE, self.username, self.headColor, msg, checkedGroupIndex)
        # 添加到集合中
        msgObj = {"widget":widget, "type":MsgTypeEnum.RECEIVE}
        self.groupMsgWidgetList[self.checkedGroupIndex].append(msgObj)
        self.msgWidgetList.append(msgObj)


    """添加发送到聊天界面"""
    def addSendMsgWidgets(self, msg):
        # 超简单设置文本效果
        widget = MsgWidgetUtil.simpleSetStyle(self.scrollWidget, self.verticalLayout, self.scrollArea,
                                              MsgTypeEnum.SEND, self.username, self.headColor, msg, self.checkedGroupIndex)
        # 添加到集合中
        msgObj = {"widget": widget, "type": MsgTypeEnum.SEND}
        self.msgWidgetList.append(msgObj)
        # 清空textEdit的内容
        self.textEdit.clear()
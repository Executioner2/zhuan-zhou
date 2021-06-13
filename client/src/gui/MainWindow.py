# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/9
# ide：PyCharm
# describe：主窗口
# editDate：
# editBy：
# version：1.0.0

from ui import MainWindow_ui
from enum_.MsgTypeEnum import MsgTypeEnum
from util.MsgWidgetUtil import MsgWidgetUtil
from PyQt5 import QtWidgets, QtGui, QtCore
from dto import LoginDto


class MainWindow(QtWidgets.QMainWindow, MainWindow_ui.Ui_MainWindow, QtCore.QObject):
    mouseClick = QtCore.pyqtSignal(object)
    headColor = None # 头像颜色
    username = None # 用户名
    msgWidgetList = [] # 消息widget集合
    groupPositionList = [] # 群组坐标集合

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
        self.pushBtn.clicked.connect(self.addSendMsgWidgets)
        self.mouseClick.connect(self.checkClickGroup)

    """检测是否点击到了群组列表"""
    def checkClickGroup(self, a0: QtGui.QMouseEvent):
        for index, item in enumerate(self.groupPositionList):
            if a0.x() >= item[0] and a0.x() <= item[1] and a0.y() >= item[2] and a0.y() <= item[3]:
                print("第{}组被点击了".format(index+1))
                break

    """接收到登录页跳转信号"""
    def recevieSkipSignal(self, loginDto:LoginDto):
        self.show()
        self.headColor = loginDto.headStyle
        self.username = loginDto.cryp if loginDto.cryp else loginDto.token
        # 获得groupVL中所有的widget（所有分组）
        for index in range(self.groupVL.count()):
            child = self.groupVL.itemAt(index).widget()
            tempTuple = (child.x(), child.width() + child.x(), child.y(),
                         child.height() + child.y())  # (left_x, right_x, top_y, bottom_y)
            self.groupPositionList.append(tempTuple)

    """添加接收消息到聊天界面"""
    """
        注意：下列widget子组件的存储方式必须按title userHead content
        的顺序存储，不然会导致组件样式出现意想不到的问题
    """
    def addReceiveMsgWidgets(self):
        msg = self.textEdit.toPlainText()

        # 创建widget 父组件为scrollWidget (滚动窗口)
        widget = QtWidgets.QWidget(self.scrollWidget)
        # 创建用户名，发送日期时间的label 父组件为widget
        title = QtWidgets.QLabel(widget)
        # 创建头像，父组件为widget
        userHead = QtWidgets.QLabel(widget)
        # 创建装消息内容的label 父组件为widget
        content = QtWidgets.QLabel(widget)

        # 设置title样式
        MsgWidgetUtil.setTitleStyle(title, self.username, MsgTypeEnum.RECEIVE)
        # 设置坐标
        title.move(5, 10)
        # 设置头像样式
        MsgWidgetUtil.setHeadStyle(userHead, self.headColor)
        # 设置坐标
        userHead.move(5, 35)
        # 设置消息内容样式
        MsgWidgetUtil.setTextStyle(content, msg)
        # 设置坐标
        content.move(userHead.width() + 10, 35)
        # 设置聊天框显示效果
        MsgWidgetUtil.setShowStyle(widget, self.scrollWidget, self.verticalLayout, self.scrollArea)
        # 添加到集合中
        msgObj = {"widget": widget, "type":MsgTypeEnum.RECEIVE}
        self.msgWidgetList.append(msgObj)


    """添加发送到聊天界面"""
    """
        注意：下列widget子组件的存储方式必须按title userHead content
        的顺序存储，不然会导致组件样式出现意想不到的问题
    """
    def addSendMsgWidgets(self):
        msg = self.textEdit.toPlainText()
        # 取得scrollWidget原始宽度-5
        scrollWidth = self.scrollArea.width() - 5

        # 创建widget 父组件为scrollWidget (滚动窗口)
        widget = QtWidgets.QWidget(self.scrollWidget)
        # 创建用户名，发送日期时间的label 父组件为widget
        title = QtWidgets.QLabel(widget)
        # 创建头像，父组件为widget
        userHead = QtWidgets.QLabel(widget)
        # 创建装消息内容的label 父组件为widget
        content = QtWidgets.QLabel(widget)

        # 设置title样式
        MsgWidgetUtil.setTitleStyle(title, self.username, MsgTypeEnum.SEND)
        # 设置坐标
        title.move(scrollWidth - title.width() - 25, 10)
        # 设置头像样式
        MsgWidgetUtil.setHeadStyle(userHead, self.headColor)
        # 设置坐标
        userHead.move(scrollWidth - userHead.width() - 25, 35)
        # 设置消息内容样式
        MsgWidgetUtil.setTextStyle(content, msg)
        # 设置坐标
        content.move(scrollWidth - content.width() - userHead.width() - 30, 35)
        # 设置聊天框显示效果
        MsgWidgetUtil.setShowStyle(widget, self.scrollWidget, self.verticalLayout, self.scrollArea)
        # 添加到集合中
        msgObj = {"widget": widget, "type": MsgTypeEnum.SEND}
        self.msgWidgetList.append(msgObj)
        # 清空textEdit的内容
        self.textEdit.clear()
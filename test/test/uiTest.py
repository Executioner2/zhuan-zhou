# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/3
# ide：PyCharm
# describe：导入ui测试
# editDate：
# editBy：
# version：1.0.0

import sys
import demoSimple
import datetime
from PyQt5 import QtWidgets

# 该用户的颜色
ONESELF_COLOR = "rgb(0, 170, 0)"
# 用户名
USER_NAME = "2Executioner"

class MyWindow(QtWidgets.QMainWindow, demoSimple.Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        # 绑定发送按钮（当发送按钮发送消息时追加消息）
        self.pushBtn.clicked.connect(self.addSendMsgWidgets)


    """添加发送到界面"""
    def addSendMsgWidgets(self):
        msg = self.textEdit.toPlainText()

        # 取得scrollWidget原始宽度-5
        scrollWidth = self.scrollArea.width() - 5

        # 创建widget 父组件为scrollWidget (滚动窗口)
        sendWidget = QtWidgets.QWidget(self.scrollWidget)

        # 创建头像，父组件为sendWidget
        sendUserHead = QtWidgets.QLabel(sendWidget)
        # 创建装消息内容的label 父组件为sendWidget
        sendContent = QtWidgets.QLabel(sendWidget)
        # 创建用户名，发送日期时间的label 父组件为sendWidget
        sendTitle = QtWidgets.QLabel(sendWidget)

        # 设置sendTitle的 坐标 内容 大小 样式
        sendTitle.setText("{} {}".format(datetime.datetime.now().replace(microsecond=0), USER_NAME))
        sendTitle.adjustSize()
        sendTitle.move(scrollWidth - sendTitle.width() - 25, 10)

        # 设置头像 坐标 大小 样式
        sendUserHead.setFixedSize(41, 41)
        print(scrollWidth)
        sendUserHead.move(scrollWidth - sendUserHead.width() - 25, 35)
        sendUserHead.setStyleSheet("background-color: {}; border-radius: 20px".format(ONESELF_COLOR))

        # 设置发送消息内容 坐标 内容 大小 样式
        sendContent.setText(msg) # 内容
        # 动态大小
        sendContent.setMinimumSize(0, 40) # 设置最小大小
        sendContent.adjustSize()  # 动态大小 这个一定要在超出大小自动换行后面才会生效
        if sendContent.width() > 200:
            # 如果width大于200则固定宽度为200，高度为动态增加后的高度加上25
            sendContent.setFixedWidth(200)  # 固定宽度
            sendContent.setWordWrap(True)  # 超出大小自动换行
            sendContent.adjustSize()  # 动态大小 这个一定要在超出大小自动换行后面才会生效
            sendContent.setFixedHeight(sendContent.height() + 40) # 在动态大小的基础上加40设置固定高度
        else:
            # 否者设置宽度为动态设定的宽度上加30，高度为最小值40不变
            sendContent.setFixedWidth(sendContent.width() + 30)
        # 坐标
        sendContent.move(scrollWidth - sendContent.width() - sendUserHead.width() - 30, 35)
        # 设置样式表
        sendContent.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 10px; padding: 10px; border: 2px solid gainsboro;")


        # 设置sendWidget的 坐标 大小
        sendWidget.move(0, self.scrollWidget.minimumHeight())
        # 计算出widgetHeight
        widgetHeight = sendUserHead.height() + sendContent.height() + 5
        sendWidget.setFixedSize(scrollWidth, widgetHeight)

        # 添加到layout中
        self.verticalLayout.addWidget(sendWidget)

        # 设置scrollWidget的最小高度
        self.scrollWidget.setMinimumSize(scrollWidth - 19, self.scrollWidget.minimumHeight() + widgetHeight + 5)

        # 滚动条自动滚动到最下方
        scrollBar = self.scrollArea.verticalScrollBar()
        scrollBar.setValue(self.scrollWidget.minimumHeight())

        # 清空textEdit的内容
        self.textEdit.clear()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    windows = MyWindow()
    windows.show()

    sys.exit(app.exec_())



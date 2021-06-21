# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/9
# ide：PyCharm
# describe：消息组件工具类
# editDate：
# editBy：
# version：1.0.0

import datetime
from PyQt5 import QtWidgets, QtGui
from model.enum_.MsgTypeEnum import MsgTypeEnum

"""完全重绘"""
def redraw(layout, scrollWidget, msgWidgetList, scrollArea, textEdit, inputText):
    # 隐藏layout中所有widget
    for index in range(layout.count()):
        layout.itemAt(index).widget().hide()
    # 重置scrollWidget的最小尺寸
    scrollWidget.setMinimumSize(0, 0)
    # 取得滚动窗口的宽度
    scrollWidth = scrollArea.width() - 5
    # 循环显示layout中指定的widget
    widgetHeight = 0
    for item in msgWidgetList:
        heightList = []
        widget = item['widget']
        widget.show()
        for kids in widget.children():
            heightList.append(kids.height())
        maxHeight = max(heightList)
        minHeight = min(heightList)
        widgetHeight += maxHeight + minHeight + 25 + 6
    # 修改scrollWidget尺寸
    scrollWidget.setMinimumSize(scrollWidth - 19, scrollWidget.minimumHeight() + widgetHeight + 6)
    # 刷新
    refresh(scrollArea, scrollWidget, msgWidgetList)
    # 重设输入框文本
    textEdit.setPlainText(inputText)
    # 光标移动至最后
    textEdit.moveCursor(QtGui.QTextCursor.End)

"""刷新（重新设置坐标）"""
def refresh(scrollArea, scrollWidget, msgWidgetList):
    # 取得scrollWidget原始宽度-5
    scrollWidth = scrollArea.width() - 5
    for item in msgWidgetList:
        if item["type"] == MsgTypeEnum.SEND:
            widget = item["widget"]
            kinds = widget.children()
            # 按照title userHead content的顺序取子项
            if isinstance(kinds[0], QtWidgets.QLabel):
                # 设置title坐标
                kinds[0].move(scrollWidth - kinds[0].width() - 25, 10)
            if isinstance(kinds[1], QtWidgets.QLabel):
                # 设置头像坐标
                kinds[1].move(scrollWidth - kinds[1].width() - 25, 35)
            if isinstance(kinds[2], QtWidgets.QLabel):
                # 设置content坐标
                kinds[2].move(scrollWidth - kinds[2].width() - kinds[1].width() - 30, 35)
            # 更新widget长度
            widget.setFixedWidth(scrollWidth)
    # 更新滚动widget最小宽度
    scrollWidget.setMinimumWidth(scrollWidth - 19)
    # 滚动条自动滚动到最下方
    scrollBar = scrollArea.verticalScrollBar()
    scrollBar.setValue(scrollWidget.minimumHeight())

"""设置显示效果（widget大小位置以及scroll大小）"""
def setShowStyle(widget, scrollWidget, layout, scrollArea, checkedGroupIndex = None):
    itemList = widget.children()
    heightList = []
    for item in itemList:
        heightList.append(item.height())
    maxHeight = max(heightList)
    minHeight = min(heightList)
    scrollWidth = scrollArea.width() - 5
    widgetHeight = maxHeight + minHeight + 25
    widget.setFixedSize(scrollWidth, widgetHeight)
    # 添加到layout中
    layout.addWidget(widget)
    # 如果不是当前显示组则不显示
    if checkedGroupIndex == None:
        widget.hide()
        return
    # 设置scrollWidget的最小尺寸
    scrollWidget.setMinimumSize(scrollWidth - 19, scrollWidget.minimumHeight() + widgetHeight + 6)
    # 滚动条自动滚动到最下方
    scrollBar = scrollArea.verticalScrollBar()
    scrollBar.setValue(scrollWidget.minimumHeight())

"""设置头像样式"""
def setHeadStyle(head, color:str):
    head.setFixedSize(41, 41)
    head.setStyleSheet("background-color: {}; border-radius: 20px".format(color))

"""设置title样式"""
def setTitleStyle(title, name:str, msgType:MsgTypeEnum, datetime_:str):
    # 显示去除毫秒微秒
    index = datetime_.find(".")
    if index != -1: datetime_ = datetime_[:index]
    if msgType == MsgTypeEnum.SEND.value:
        title.setText("{} {}".format(datetime_, name))
    else:
        title.setText("{} {}".format(name, datetime_))
    title.adjustSize()

"""设置文本样式"""
def setTextStyle(content, msg:str):
    content.setText(msg)  # 内容
    # 动态大小
    content.setMinimumSize(0, 0)  # 设置最小大小
    content.adjustSize()  # 动态大小
    if content.width() > 200:
        # 如果width大于200则固定宽度为200，高度为动态增加后的高度加上25
        content.setFixedWidth(200)  # 固定宽度
        content.setWordWrap(True)  # 超出大小自动换行
        content.adjustSize()  # 动态大小 这个一定要在超出大小自动换行后面才会生效
        content.setFixedHeight(content.height() + 40)  # 在动态大小的基础上加40设置固定高度
    else:
        # 否者设置宽度为动态设定的宽度上加30
        content.setFixedWidth(content.width() + 30)
        if content.height() > 16:
            # 动态高度如果大于16px(一个字符的大小), 则动态设置高度
            content.setFixedHeight(content.height() + 24)  # 在动态大小的基础上加40设置固定高度
        else:
            # 否则未产生换行
            content.setFixedHeight(40)  # 固定高度40

    # 设置样式表
    content.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 10px; padding: 10px; border: 2px solid gainsboro;")

"""简单设置样式"""
"""
    注意：下列widget子组件的存储方式必须按title userHead content
    的顺序存储，不然会导致组件样式出现意想不到的问题
"""
def simpleSetStyle(scrollWidget, verticalLayout, scrollArea, checkedGroupIndex, msgDto):
    # 取得scrollWidget原始宽度-5
    scrollWidth = scrollArea.width() - 5
    # 创建widget 父组件为scrollWidget (滚动窗口)
    widget = QtWidgets.QWidget(scrollWidget)
    # 创建用户名，发送日期时间的label 父组件为widget
    title = QtWidgets.QLabel(widget)
    # 创建头像，父组件为widget
    userHead = QtWidgets.QLabel(widget)
    # 创建装消息内容的label 父组件为widget
    content = QtWidgets.QLabel(widget)
    group = msgDto.group if msgDto.group == checkedGroupIndex else None
    # 设置title样式
    setTitleStyle(title, msgDto.nickname, msgDto.type, msgDto.datetime_)
    # 设置头像样式
    setHeadStyle(userHead, msgDto.headStyle)
    # 设置消息内容样式
    setTextStyle(content, msgDto.content)
    # 设置坐标
    if msgDto.type == MsgTypeEnum.SEND.value:
        title.move(scrollWidth - title.width() - 25, 10)
        userHead.move(scrollWidth - userHead.width() - 25, 35)
        content.move(scrollWidth - content.width() - userHead.width() - 30, 35)
    elif msgDto.type == MsgTypeEnum.RECEIVE.value:
        title.move(5, 10)
        userHead.move(5, 35)
        content.move(userHead.width() + 10, 35)

    # 设置聊天框显示效果
    setShowStyle(widget, scrollWidget, verticalLayout, scrollArea, group)
    return widget
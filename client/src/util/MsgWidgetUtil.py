# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/9
# ide：PyCharm
# describe：消息组件工具类
# editDate：
# editBy：
# version：1.0.0

import datetime
from PyQt5 import QtWidgets
from enum_.MsgTypeEnum import MsgTypeEnum

class MsgWidgetUtil:
    def __init__(self):
        pass

    """刷新（重新设置坐标）"""
    @staticmethod
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

    """设置显示效果（widget大小位置以及scroll大小）"""
    @staticmethod
    def setShowStyle(widget, scrollWidget, layout, scrollArea):
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
        # 设置scrollWidget的最小高度
        scrollWidget.setMinimumSize(scrollWidth - 19, scrollWidget.minimumHeight() + widgetHeight + 6)
        # 滚动条自动滚动到最下方
        scrollBar = scrollArea.verticalScrollBar()
        scrollBar.setValue(scrollWidget.minimumHeight())

    """设置头像样式"""
    @staticmethod
    def setHeadStyle(head, color:str):
        head.setFixedSize(41, 41)
        head.setStyleSheet("background-color: {}; border-radius: 20px".format(color))

    """设置title样式"""
    @staticmethod
    def setTitleStyle(title, name:str, msgType:MsgTypeEnum):
        if msgType.value == MsgTypeEnum.SEND.value:
            title.setText("{} {}".format(datetime.datetime.now().replace(microsecond=0), name))
        else:
            title.setText("{} {}".format(name, datetime.datetime.now().replace(microsecond=0)))
        title.adjustSize()

    """设置文本样式"""
    @staticmethod
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
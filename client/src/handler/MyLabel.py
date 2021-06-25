# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/23
# ide：PyCharm
# describe：
# editDate：
# editBy：
# version：1.0.0

from PyQt5 import QtWidgets, QtGui, QtCore

class MyLabel(QtWidgets.QLabel):
    mouseReleaseSignal = QtCore.pyqtSignal()  # 鼠标点击信号

    def __init__(self, parent=None):
        super(MyLabel, self).__init__(parent)

    """重写鼠标点击事件"""
    def mouseReleaseEvent(self, ev: QtGui.QMouseEvent) -> None:
        self.mouseReleaseSignal.emit()

    """鼠标进入"""
    def enterEvent(self, a0: QtCore.QEvent) -> None:
        self.setStyleSheet("color: rgb(49, 188, 255)")

    """鼠标离开"""
    def leaveEvent(self, a0: QtCore.QEvent) -> None:
        self.setStyleSheet("")
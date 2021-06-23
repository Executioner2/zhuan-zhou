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
        print("点击了")
        self.mouseReleaseSignal.emit()
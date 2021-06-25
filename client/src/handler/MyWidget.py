# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/23
# ide：PyCharm
# describe：
# editDate：
# editBy：
# version：1.0.0

from PyQt5 import QtWidgets, QtGui, QtCore

class MyWidget(QtWidgets.QWidget, QtCore.QObject):
    mouseReleaseSignal = QtCore.pyqtSignal(object)
    isSelected = False

    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)

    def enterEvent(self, a0: QtCore.QEvent) -> None:
        if not self.isSelected:
            self.setStyleSheet("background-color: rgb(219, 219, 219)")

    def leaveEvent(self, a0: QtCore.QEvent) -> None:
        if not self.isSelected:
            self.setStyleSheet("")

    """重写鼠标点击"""
    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent) -> None:
        self.mouseReleaseSignal.emit(self)


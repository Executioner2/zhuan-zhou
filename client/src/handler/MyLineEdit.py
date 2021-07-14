# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/17
# ide：PyCharm
# describe：
# editDate：
# editBy：
# version：1.0.0

from PyQt5 import QtWidgets, QtGui, QtCore

class MyLineEdit(QtWidgets.QLineEdit):
    focusSignal = QtCore.pyqtSignal(str) # 获得焦点信号
    blurSignal = QtCore.pyqtSignal(str) # 失去焦点信号
    keyPressSignal = QtCore.pyqtSignal(str) # 按键按下

    def __init__(self, parent):
        QtWidgets.QLineEdit.__init__(self)
        self.parent = parent

    """重写获得焦点"""
    def focusInEvent(self, a0: QtGui.QFocusEvent) -> None:
        # print("获得焦点", self.objectName())
        QtWidgets.QLineEdit.focusInEvent(self, a0)

    """重写失去焦点"""
    def focusOutEvent(self, a0: QtGui.QFocusEvent) -> None:
        # print("失去焦点", self.objectName())
        self.blurSignal.emit(self.objectName())
        QtWidgets.QLineEdit.focusOutEvent(self, a0)

    """按键按下"""
    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        self.keyPressSignal.emit(self.objectName())
        QtWidgets.QLineEdit.keyPressEvent(self, a0)

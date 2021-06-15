# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/15
# ide：PyCharm
# describe：
# editDate：
# editBy：
# version：1.0.0

from PyQt5 import QtWidgets, QtCore, QtGui

class MyTextEdit(QtWidgets.QTextEdit):
    sendSignal = QtCore.pyqtSignal()

    def __init__(self, parent):
        QtWidgets.QTextEdit.__init__(self)
        self.parent = parent

    """重写按键按下事件"""
    def keyPressEvent(self, e: QtGui.QKeyEvent) -> None:
        if e.key() == QtCore.Qt.Key_Return:
            if QtWidgets.QApplication.keyboardModifiers() != QtCore.Qt.ShiftModifier:
                self.sendSignal.emit()  # 发送一个发送文本信号
                return
        # 这条是父类的按键按下事件（如果是组合键(shift+return)则响应回车）
        QtWidgets.QTextEdit.keyPressEvent(self, e)

# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/17
# ide：PyCharm
# describe：
# editDate：
# editBy：
# version：1.0.0

from PyQt5 import QtWidgets, QtGui, QtCore
from model.enum_.RegisterLeNameEnum import RegisterLeNameEnum

class MyLineEdit(QtWidgets.QLineEdit):
    focusSignal = QtCore.pyqtSignal(str) # 获得焦点信号
    blurSignal = QtCore.pyqtSignal(str) # 失去焦点信号

    def __init__(self, parent, hint:QtWidgets.QLabel):
        QtWidgets.QLineEdit.__init__(self)
        self.parent = parent
        self.hint = hint

    """重写获得焦点"""
    def focusInEvent(self, a0: QtGui.QFocusEvent) -> None:
        print("获得焦点", self.objectName())
        QtWidgets.QLineEdit.focusInEvent(self, a0)

    """重写失去焦点"""
    def focusOutEvent(self, a0: QtGui.QFocusEvent) -> None:
        print("失去焦点", self.objectName())
        if self.objectName() == RegisterLeNameEnum.USERNAME.value:
            if self.text().strip() == "":
                self.hint.setText("用户名不能为空")
                self.hint.show()
        elif self.objectName() == RegisterLeNameEnum.PASSWORD.value:
            if self.text().strip() == "":
                self.hint.setText("密码不能为空")
                self.hint.show()
        elif self.objectName() == RegisterLeNameEnum.CONFIRM_PASSWORD.value:
            if self.text().strip() == "":
                self.hint.setText("用户名不能为空")
                self.hint.show()
        QtWidgets.QLineEdit.focusOutEvent(self, a0)

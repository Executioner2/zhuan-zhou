# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/13
# ide：PyCharm
# describe：
# editDate：
# editBy：
# version：1.0.0

from ui import MainWindow_ui
from PyQt5 import QtWidgets, QtGui

class MainWindow(QtWidgets.QMainWindow, MainWindow_ui.Ui_MainWindow):

    """重写关闭确认"""
    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        result = QtWidgets.QMessageBox.question(
            self, "退出服务端", "确认要退出服务端？",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            a0.accept()
            QtWidgets.QWidget.closeEvent(self, a0)
        else:
            a0.ignore()

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setDockNestingEnabled(True)
        self.setupUi(self)

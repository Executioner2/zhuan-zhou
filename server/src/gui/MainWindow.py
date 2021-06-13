# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/13
# ide：PyCharm
# describe：
# editDate：
# editBy：
# version：1.0.0

from ui import MainWindow_ui
from PyQt5 import QtWidgets

class MainWindow(QtWidgets.QMainWindow, MainWindow_ui.Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setDockNestingEnabled(True)
        self.setupUi(self)

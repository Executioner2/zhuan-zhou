# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/17
# ide：PyCharm
# describe：
# editDate：
# editBy：
# version：1.0.0

from PyQt5.QtCore import pyqtSignal, QObject

class ClientSignal(QObject):
    loginSignal = pyqtSignal(object)
    loginResultSignal = pyqtSignal(bool)
    skipSignal = pyqtSignal(object) # 跳转信号
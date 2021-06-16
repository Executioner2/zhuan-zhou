# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/16
# ide：PyCharm
# describe：
# editDate：
# editBy：
# version：1.0.0

from PyQt5 import QtCore


class ClientSocketThread(QtCore.QThread):
    
    def __init__(self, loginDto):
        super(ClientSocketThread, self).__init__()
        self.loginDto = loginDto

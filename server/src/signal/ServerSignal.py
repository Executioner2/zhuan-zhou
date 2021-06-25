# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/16
# ide：PyCharm
# describe： 服务器自定义信号
# editDate：
# editBy：
# version：1.0.0

from PyQt5.QtCore import pyqtSignal, QObject

class ServerSignal(QObject):
    startupSignal = pyqtSignal(object) # 服务器启动信号
    shutdownSignal = pyqtSignal() # 服务器关闭信号
    updateDataRecordSignal = pyqtSignal() # 更新数据记录信号
    insertMsgRecordSignal = pyqtSignal(object) # 插入聊天记录到listWidget中


# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/16
# ide：PyCharm
# describe：
# editDate：
# editBy：
# version：1.0.0

from PyQt5.QtCore import pyqtSignal, QObject
class MySignal(QObject):
    sendmsg = pyqtSignal(str)

class Send(QObject):
    def __init__(self, signal:MySignal):
        self.signal = signal

    def sendMsg(self, msg):
        self.signal.sendmsg.emit(msg)

class Slot:
    def __init__(self, signal:MySignal):
        self.signal = signal
        self.signal.sendmsg.connect(self.get)

    def bind(self, signal):
        signal.sendmsg.connect(self.get)

    def get(self, msg):
        print("收到了自定义信号发来的信息：" + msg)

if __name__ == '__main__':
    signal = MySignal()
    send = Send(signal)
    slot = Slot(signal)

    send.sendMsg("你好你好")


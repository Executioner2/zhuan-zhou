# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/3
# ide：PyCharm
# describe：自定义信号测试
# editDate：
# editBy：
# version：1.0.0

from PyQt5.QtCore import pyqtSignal,QObject
class Signal(QObject):
    sendmsg = pyqtSignal(str)
    def run(this, msg):
        this.sendmsg.emit(msg)

class Slot(QObject):
    def get(this, msg):
        print("收到了自定义信号1发来的信息：" + msg)

if __name__ == '__main__':
    msg = Signal()
    slot = Slot()
    msg.sendmsg.connect(slot.get)
    msg.run("干饭干饭！")



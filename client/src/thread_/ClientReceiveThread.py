# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/16
# ide：PyCharm
# describe：
# editDate：
# editBy：
# version：1.0.0

from PyQt5 import QtCore
from client.src.signal import ClientSignal
from common.util import TransmitUtil
from common.util import ToObjectUtil
from model.enum_.MsgTypeEnum import MsgTypeEnum

class ClientReceiveThread(QtCore.QThread):

    def __init__(self, clientSocket, clientSignal:ClientSignal):
        super(ClientReceiveThread, self).__init__()
        self.clientSocket = clientSocket
        self.clientSignal = clientSignal

    """重写run"""
    def run(self) -> None:
        # 消息接收线程
        print("进入到消息接收线程")
        try:
            while True:
                print("开始接收消息")
                result = TransmitUtil.receive(self.clientSocket)
                data = ToObjectUtil.dictToObject(result["data"])
                # 发送信号渲染到ui上
                self.clientSignal.msgReceiveSignal.emit(data)
        except Exception:
            print("客户端断开了")

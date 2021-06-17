# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/16
# ide：PyCharm
# describe：
# editDate：
# editBy：
# version：1.0.0

from PyQt5 import QtCore
from common.util import TransmitUtil, Json2ObjectUtil
from server.src.api.ClientSocketApi import ClientSocketApi

class ClientSocketThread(QtCore.QThread):

    """重写run方法"""
    def run(self) -> None:
        try:
            while True:
                try:
                    result = TransmitUtil.receive(self.clientSocket)
                    data = Json2ObjectUtil.jsonToObject(result["data"])
                    print(result["url"])
                    fun = getattr(ClientSocketApi(), result["url"])
                    # print(self.fun)
                    fun(data) # 调用有参数的方法
                except AttributeError:
                    continue
                except TypeError: # 出现此错误说明该方法没有参数，注：url的方法只能有一个参数
                    fun() # 调用没参数的方法
        except ConnectionError:
            pass
        finally:
            print("断开连接")
            self.clientSocketList.remove(self.clientSocket)
            # TODO 发送退出群聊通知


    """初始化"""
    def __init__(self, clientSocketList, clientSocket, clientAddress):
        super(ClientSocketThread, self).__init__()
        self.clientSocketList = clientSocketList
        self.clientSocket = clientSocket
        self.clientAddress = clientAddress


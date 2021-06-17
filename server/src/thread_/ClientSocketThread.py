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

class ClientSocketThread(QtCore.QThread):

    """重写run方法"""
    def run(self) -> None:
        try:
            while True:
                try:
                    result = TransmitUtil.receive(self.clientSocket)
                    data = Json2ObjectUtil.jsonToObject(result["data"])
                    url = result["url"]
                    url(data) # 调用有参数的方法
                except AttributeError:
                    continue
                except TypeError: # 出现此错误说明该方法没有参数，注：url的方法只能有一个参数
                    url() # 调用没参数的方法
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

    """消息群发"""
    def notify(self):
        pass

    """用户登录"""
    def login(self, token):
        print("开始执行用户登录")
        pass

    """用户注册"""
    def register(self):
        pass


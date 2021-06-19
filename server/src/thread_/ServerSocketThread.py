# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/16
# ide：PyCharm
# describe：
# editDate：
# editBy：
# version：1.0.0

import socket

from PyQt5 import QtCore

from server.src.thread_ import ClientSocketThread
from server.src.handler import DataSourceFactory

MAX_CONTENT = 100 # 排队个数

class SocketService(QtCore.QThread):
    clientList = []
    peopers = 0
    server = None
    address = None
    dsf = None

    """重写run"""
    def run(self) -> None:
        try:
            # 创建一个tcp ipv4的socket对象
            print(self.address)
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.bind(self.address)
            self.server.listen(MAX_CONTENT)  # 最大排队数
            print("服务器启动成功....")
            # 创建数据库连接池
            self.dsf = DataSourceFactory.DataSourceFactory("E:\\PythonProject\\study\\pythonProject\\agc\server\\resource\\config\\datasource.conf")
            while True:
                print("正在监听")
                clientSocket, clientAddress = self.server.accept()
                # 把客户端socket添加到列表中
                self.clientList.append(clientSocket)
                # 为这个客户端开启一个消息读取和发送的线程
                clientThread = ClientSocketThread.ClientSocketThread(self.clientList, clientSocket, clientAddress, self.dsf)
                clientThread.start()
        except OSError:
            pass
        finally:
            self.server.close()
            self.server = None
            self.dsf.closeAll() # 关闭数据库
            print("服务器已经关闭")

    """初始化"""
    def __init__(self, serverSignal):
        super(SocketService, self).__init__()
        self.serverSignal = serverSignal
        self.serverSignal.startupSignal.connect(self.startup)
        self.serverSignal.shutdownSignal.connect(self.shutdown)

    """启动服务器"""
    def startup(self, address):
        self.address = address
        self.start()

    """关闭服务器"""
    def shutdown(self):
        # 关闭所有客户端socket线程
        for item in self.clientList:
            item.close() # 关闭socket线程就会自动运行完毕并退出
        # 然后关闭服务socket
        if self.server:
            self.server.close()
            print("成功关闭服务器！")



# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/16
# ide：PyCharm
# describe：
# editDate：
# editBy：
# version：1.0.0
import os
import socket
import sys

import pymysql
from PyQt5 import QtCore
from dbutils.pooled_db import PooledDB

import threading

from common.util import ConfigFileUtil
from server.src.thread_ import ClientSocketThread

MAX_CONTENT = 25 # 最大监听数

class SocketService(QtCore.QThread):
    clientList = [] # 客户端socket集合
    msgHistoryList = [] # 历史消息集合
    server = None
    address = None
    rootPath = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))
    datasource = ConfigFileUtil.readDataSourceConfig(rootPath + "\\resource\\config\\datasource.ini")
    # 数据库连接池
    sqlConnPool = PooledDB(
        creator=pymysql,  # 使用链接数据库的模块
        maxconnections=50,  # 连接池允许的最大连接数，0和None表示不限制连接数
        mincached=10,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
        maxcached=20,  # 链接池中最多闲置的链接，0和None不限制
        blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
        maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
        # 连接mysql
        host=datasource[0],
        port=int(datasource[1]),
        database=datasource[2],
        user=datasource[3],
        password=datasource[4],
        charset='utf8'
    )

    """重写run"""
    def run(self) -> None:
        try:
            # 创建一个tcp ipv4的socket对象
            print(self.address)
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.bind(self.address)
            self.server.listen(MAX_CONTENT)  # 最大排队数
            lock = threading.Lock() # 互斥锁对象
            print("服务器启动成功....")
            while True:
                print("正在监听")
                clientSocket, clientAddress = self.server.accept()
                # 把客户端socket添加到列表中
                self.clientList.append(clientSocket)
                self.clientAddressList.append(clientAddress)
                # 为这个客户端开启一个消息读取和发送的线程
                clientThread = ClientSocketThread.ClientSocketThread(self.clientList, clientSocket, self.sqlConnPool,
                                                                     self.msgList, self.dataRecord, lock,
                                                                     self.serverSignal, clientAddress)
                clientThread.start()
                self.serverSignal.insertClientInfoSignal.emit(clientAddress)
                try:
                    lock.acquire() # 加锁占有资源
                    self.dataRecord.nowPeoples += 1
                    if self.dataRecord.nowPeoples > self.dataRecord.maxPeoples:
                        self.dataRecord.maxPeoples = self.dataRecord.nowPeoples
                    # 发送更新数据记录的信号
                    self.serverSignal.updateDataRecordSignal.emit(self.dataRecord)
                except Exception as e:
                    print(e)
                finally:
                    lock.release()  # 释放锁
        except OSError:
            pass
        finally:
            self.server.close()
            self.server = None
            print("服务器已经关闭")

    """初始化"""
    def __init__(self, serverSignal, dataRecord, msgList, clientAddressList:list):
        super(SocketService, self).__init__()
        self.serverSignal = serverSignal
        self.dataRecord = dataRecord # 记录数据
        self.serverSignal.startupSignal.connect(self.startup)
        self.serverSignal.shutdownSignal.connect(self.shutdown)
        self.msgList = msgList
        self.clientAddressList = clientAddressList

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



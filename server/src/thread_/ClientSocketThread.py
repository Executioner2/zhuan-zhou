# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/16
# ide：PyCharm
# describe：
# editDate：
# editBy：
# version：1.0.0
import datetime
import os
import pickle
import sys

import pymysql
from PyQt5 import QtCore

from common.util import TransmitUtil, ToObjectUtil
from common.util import UUIDUtil
from server.src.api.ClientSocketApi import ClientSocketApi
from model.dto import MsgDto
import threading
from server.src.signal import ServerSignal

FILENAME = "records.data"
USERNAME = ""

class ClientSocketThread(QtCore.QThread):

    """重写run方法"""
    def run(self) -> None:
        try:
            while True:
                try:
                    result = TransmitUtil.receive(self.clientSocket)
                    if result == None: break
                    data = result["data"]
                    data = ToObjectUtil.dictToObject(data)
                    fun = getattr(self.clientSocketApi, result["url"])
                    fun(data) # 调用有参数的方法
                except AttributeError:
                    continue
                except TypeError as e: # 出现此错误说明该方法没有参数，注：url的方法只能有一个参数
                    print(e)
                    fun() # 调用没参数的方法
                # 流量自增
                try:
                    self.lock.acquire()
                    self.dataRecord.nowFlows += 1
                    if self.dataRecord.maxFlows < self.dataRecord.nowFlows:
                        self.dataRecord.maxFlows = self.dataRecord.nowFlows
                    # 发送更新数据记录的信号
                    self.serverSignal.updateDataRecordSignal.emit()
                except Exception as e:
                    print(e)
                finally:
                    self.lock.release()
        except ConnectionError:
            pass
        finally:
            try:
                self.lock.acquire()
                self.dataRecord.nowPeoples -= 1
                # 发送更新数据记录的信号
                self.serverSignal.updateDataRecordSignal.emit()
            except Exception as e:
                print(e)
            finally:
                self.lock.release()
            self.saveChatRecords()
            self.clientSocket.close()
            self.clientSocketList.remove(self.clientSocket)
            print("客户端断开了连接")

    """初始化"""
    def __init__(self, clientSocketList, clientSocket, clientAddress, sqlConnPool, msgList, dataRecord, lock:threading.Lock, serverSignal:ServerSignal.ServerSignal):
        super(ClientSocketThread, self).__init__()
        self.clientSocketList = clientSocketList
        self.clientSocket = clientSocket
        self.clientAddress = clientAddress
        self.sqlConnPool = sqlConnPool # 数据库连接池
        self.clientSocketApi = ClientSocketApi(self.clientSocketList, self.clientSocket, self.sqlConnPool, msgList, serverSignal)
        self.msgList = msgList # 服务器端接收到的消息集合
        self.dataRecord = dataRecord # 数据记录
        self.lock = lock # dataRecord对象的锁
        self.serverSignal = serverSignal
        self.connectTime = str(datetime.datetime.now()) # 客户端连接开始时间

    """保存聊天记录"""
    def saveChatRecords(self):
        conn = None
        cursor = None
        try:
            # 客户端断开连接时间
            disconnectTime = str(datetime.datetime.now())
            folder = os.path.dirname(os.path.dirname(sys.argv[0])) + "/resource/user_file/" + USERNAME + "/"
            if not os.path.exists(folder): os.makedirs(folder)
            path = folder + FILENAME
            # 只保存客户端连接期间的聊天记录
            with open(path, "ab") as f:
                for msgDto in self.msgList:
                    if self.connectTime <= msgDto.datetime_ and msgDto.datetime_ <= disconnectTime:
                        pickle.dump(msgDto, f)
            # 保存到数据库聊天文件
            conn = self.sqlConnPool.connection()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("select id from tbl_user where username=%s and is_deleted=0", (USERNAME))
            userId = cursor.fetchall()[0]["id"]
            cursor.execute("select id from tbl_chatting_records where user_id=%s", (userId))
            result = cursor.fetchall()
            if len(result) == 0:  # 创建
                id = UUIDUtil.getUUID()
                cursor.execute("insert into tbl_chatting_records(id, user_id, file_path) values(%s, %s, %s)",
                               (id, userId, path))
                conn.commit()
            else:  # 更新
                id = result[0]["id"]
                cursor.execute("update tbl_chatting_records set file_path=%s where id=%s", (path, id))
                conn.commit()
        except Exception as e:
            print(e)
        finally:
            # 把连接断开（实际上是还回连接池了）
            if cursor != None:
                cursor.close()
            if conn != None:
                conn.close()
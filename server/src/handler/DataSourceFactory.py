# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/19
# ide：PyCharm
# describe：
# editDate：
# editBy：
# version：1.0.0

import threading
import time
import warnings

import pymysql

from common.util import ConfigFileUtil

warnings.warn("该类写错了不建议使用，有更好的替代品", DeprecationWarning)
class DataSourceFactory:
    cursorList = [] # 数据库游标集合

    def __init__(self, path=None, datasource=None):
        self.datasource = ConfigFileUtil.readDataSourceConfig(path, datasource)  # 连接源
        self.conn = pymysql.connect(host=self.datasource[0], db=self.datasource[1], user=self.datasource[2],
                                    password=self.datasource[3])
        self.lock = threading.RLock()
        self.initCursor()
        # 启动守护线程
        thread = threading.Thread(target=self.run)
        thread.setDaemon(True)
        thread.start()

    """初始化游标"""
    def initCursor(self):
        # 创建20个游标
        for index in range(20):
            cursor = self.conn.cursor(pymysql.cursors.DictCursor) # 返回结果为 [{}, {}]
            temp = {"flag":True, "cursor":cursor, "ttl":-1} # flag为是否空闲，ttl为游标生存时间，-1为永久
            self.cursorList.append(temp)

    """获取游标"""
    def getCursor(self):
        try:
            self.lock.acquire() # 加锁
            for item in self.cursorList:
                if item["flag"]: # 是空闲的
                    if item["ttl"] != -1: # 如果不是永久存在的则更新ttl，默认为10分钟
                        item["ttl"] = self.getCurrentTimestamp()+(1000*60*10)
                    # 设置游标被使用，置为不可用
                    item["flag"] = False
                    return item["cursor"] # 返回游标
            # 执行到这里表示没有空闲的游标，那么就新建五个游标
            for index in range(5):
                cursor = self.conn.cursor(pymysql.cursors.DictCursor)  # 返回结果为 [{}, {}]
                temp = {"flag": True, "cursor": cursor, "ttl": self.getCurrentTimestamp()+(1000*60*10)}  # flag为是否空闲，ttl为游标生存时间，设ttl为10分钟
                if index == 4:
                    temp["flag"] = False
                self.cursorList.append(temp)
            # 返回最后一个
            return temp["cursor"]
        finally:
            self.lock.release() # 释放锁

    """归还cursor"""
    def giveBack(self, cursor):
        try:
            self.lock.acquire() # 加锁
            for item in self.cursorList:
                if item["cursor"] == cursor:
                    item["flag"] = True # 空闲
                    if item["ttl"] != -1:
                        item["ttl"] = self.getCurrentTimestamp()+(1000*60*10) # 再更新一手ttl
                    break
        finally:
            self.lock.release() # 释放锁

    """辅助检测到有未使用且ttl超时的cursor就关闭并删除它"""
    def run(self):
        while True:
            try:
                time.sleep(0.5)  # 每隔0.5秒执行一次
                self.lock.acquire()  # 加锁
                for item in self.cursorList:
                    if item["flag"] and item["ttl"] != -1 and item["ttl"] <= self.getCurrentTimestamp():
                        item["cursor"].close()
                        self.cursorList.remove(item)
                        print("空闲的cursor被清除掉了：", item)
            finally:
                self.lock.release() # 释放锁


    """关闭所有"""
    def closeAll(self):
        for item in self.cursorList:
            cursor = item["cursor"]
            cursor.close()
        # 断开连接
        self.conn.close()

    """获取当前毫秒级别的时间戳"""
    def __getCurrentTimestamp(self):
        return int(round(time.time() * 1000))
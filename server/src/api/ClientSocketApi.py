# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/17
# ide：PyCharm
# describe：
# editDate：
# editBy：
# version：1.0.0

import pymysql
from dbutils.pooled_db import PooledDB

from common.result.Result import Result
from common.result.ResultCodeEnum import ResultCodeEnum
from common.util import TransmitUtil
from common.util import UUIDUtil
from common.util.TokenUtil import TokenUtil
from model.dto import MsgDto


class ClientSocketApi:
    nickname = None
    headStyle = None
    def __init__(self, clientSocketList, socket, sqlConnPool:PooledDB):
        self.clientSocketList = clientSocketList
        self.socket = socket
        self.sqlConnPool = sqlConnPool

    """消息群发"""
    def notify(self, params):
        print("开始转发消息")
        msgDto = MsgDto.MsgDto(group=params.group, content=params.content, nickname=self.nickname, headStyle=self.headStyle)
        for item in self.clientSocketList:
            if item != self.socket: # 不给自己发
                TransmitUtil.send(item, Result.ok(data=msgDto))


    """用户登录"""
    def login(self, loginDto):
        token = loginDto.token
        try:
            print("开始执行用户登录")
            userinfo = TokenUtil.getUserInfo(token)
            # 获取连接
            conn = self.sqlConnPool.connection()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("select id, username from tbl_user where username=%s and password=%s and is_deleted=0", (userinfo[0], userinfo[1]))
            result = cursor.fetchall()
            if len(result) != 0:
                self.headStyle = loginDto.headStyle
                self.nickname = loginDto.cryp if loginDto.cryp else result[0]["username"]
                TransmitUtil.send(self.socket, Result.ok(data=self.nickname))
            else:
                TransmitUtil.send(self.socket, Result.build(ResultCodeEnum.LOGIN_USER_FAIL.value[0]))
        finally:
            if cursor != None:
                cursor.close()
            if conn != None:
                conn.close()

    """用户注册"""
    def register(self, token):
        try:
            print("开始注册用户")
            userinfo = TokenUtil.getUserInfo(token)
            # 获取连接
            conn = self.sqlConnPool.connection()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("select count(*) from tbl_user where username=%s and is_deleted=0", (userinfo[0]))
            result = cursor.fetchall()[0]["count(*)"]
            if result != 0:
                TransmitUtil.send(self.socket, Result.build(ResultCodeEnum.REGISTER_USERNAME_ERROR.value[0])) # 用户名已存在
            else:
                id = UUIDUtil.getUUID()
                count = cursor.execute("insert into tbl_user(id, username, password) values(%s, %s, %s)", (id, userinfo[0], userinfo[1]))
                conn.commit() # 提交数据
                if count == 1:
                    TransmitUtil.send(self.socket, Result.ok())
                else:
                    TransmitUtil.send(self.socket, Result.fail())
        finally:
            # 把连接断开（实际上是还回连接池了）
            if cursor != None:
                cursor.close()
            if conn != None:
                conn.close()
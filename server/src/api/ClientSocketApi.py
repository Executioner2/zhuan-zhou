# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/17
# ide：PyCharm
# describe：
# editDate：
# editBy：
# version：1.0.0

from common.util import TransmitUtil
from common.result.Result import Result


class ClientSocketApi:

    """消息群发"""
    def notify(self):
        pass

    """用户登录"""
    def login(self, params):
        socket = params[0]
        token = params[1]
        print("开始执行用户登录")
        print(token)
        TransmitUtil.send(socket, Result.ok())

    """用户注册"""
    def register(self, params):
        socket = params[0]
        token = params[1]
        print(params)
        print("开始注册用户")
        TransmitUtil.send(socket, Result.ok())

    """用户名重复性检测"""
    def usernameCheck(self):
        pass
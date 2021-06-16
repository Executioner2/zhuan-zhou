# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/10
# ide：PyCharm
# describe：用户登录界面到聊天界面的数据传递类
# editDate：
# editBy：
# version：1.0.0

class LoginDto:
    def __init__(self, token=None, serverIp=None, serverPort=None, headStyle=None, cryp=None):
        self._token = token
        self._serverIp = serverIp
        self._serverPort = serverPort
        self._headStyle = headStyle
        self._cryp = cryp

    def __str__(self):
        return "token:{} serverIp:{} serverPort:{} headStyle:{} cryp:{}".format(self._token, self._serverIp, self._serverPort, self._headStyle, self._cryp)

    @property
    def cryp(self):
        return self._cryp
    @cryp.setter
    def cryp(self, cryp):
        self._cryp = cryp

    @property
    def token(self):
        return self._token
    @token.setter
    def token(self, token):
        self._token = token

    @property
    def serverIp(self):
        return self._serverIp
    @serverIp.setter
    def serverIp(self, serverIp):
        self._serverIp = serverIp

    @property
    def serverPort(self):
        return self._serverPort
    @serverPort.setter
    def serverPort(self, serverPort):
        self._serverPort = serverPort

    @property
    def headStyle(self):
        return self._headStyle
    @headStyle.setter
    def headStyle(self, headStyle):
        self._headStyle = headStyle
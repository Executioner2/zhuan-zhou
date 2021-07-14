# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/10
# ide：PyCharm
# describe：用户登录界面到聊天界面的数据传递类
# editDate：
# editBy：
# version：1.0.0

class LoginDto:
    nickname = None
    username = None
    def __init__(self, token=None, serverIp=None, serverPort=None, headStyle=None, cryp=None):
        self.token = token
        self.serverIp = serverIp
        self.serverPort = serverPort
        self.headStyle = headStyle
        self.cryp = cryp

    def __str__(self):
        return str(self.__dict__)
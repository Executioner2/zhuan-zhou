# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/20
# ide：PyCharm
# describe：
# editDate：
# editBy：
# version：1.0.0

"""消息传输类"""
class MsgDto:

    def __init__(self, group, content, nickname=None, headStyle=None):
        self.group = group
        self.content = content
        self.nickname = nickname
        self.headStyle = headStyle

    def __str__(self):
        return str(self.__dict__)

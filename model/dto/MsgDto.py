# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/20
# ide：PyCharm
# describe：
# editDate：
# editBy：
# version：1.0.0

"""消息传输类"""
class MsgDto(dict):

    def __init__(self, group, content, type, datetime_, nickname=None, headStyle=None):
        self.group = group
        self.content = content
        self.type = type
        self.nickname = nickname
        self.headStyle = headStyle
        self.datetime_ = str(datetime_)

    def __str__(self):
        return str(self.__dict__)
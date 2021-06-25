# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/25
# ide：PyCharm
# describe：服务端数据记录DTO
# editDate：
# editBy：
# version：1.0.0

class ServerDataRecordDto:
    def __init__(self, maxPeoples=0, nowPeoples=0, maxFlows=0, nowFlows=0):
        self.maxPeoples = maxPeoples
        self.nowPeoples = nowPeoples
        self.maxFlows = maxFlows
        self.nowFlows = nowFlows

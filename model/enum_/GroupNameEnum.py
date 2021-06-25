# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/25
# ide：PyCharm
# describe：
# editDate：
# editBy：
# version：1.0.0

from enum import Enum

class GroupNameEnum(Enum):
    GROUP_1 = {"no":0, "objName":"chatRecordWidget_1"}
    GROUP_2 = {"no":1, "objName":"chatRecordWidget_2"}
    GROUP_3 = {"no":2, "objName":"chatRecordWidget_3"}

    """根据组号（no）取得objName"""
    @staticmethod
    def getObjNameByNo(no:int):
        for item in GroupNameEnum:
            if item.value["no"] == no:
                return item.value["objName"]
# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/19
# ide：PyCharm
# describe：
# editDate：
# editBy：
# version：1.0.0

import uuid

def getUUID():
    uid = str(uuid.uuid4())
    return ''.join(uid.split('-'))
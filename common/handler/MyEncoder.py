# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/17
# ide：PyCharm
# describe： 字节数组转json
# editDate：
# editBy：
# version：1.0.0

import json

class MyEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, bytes):
            return str(o, encoding="utf-8")
        return json.JSONEncoder.default(self, o)

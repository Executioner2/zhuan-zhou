# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/17
# ide：PyCharm
# describe：json转复杂object
# editDate：
# editBy：
# version：1.0.0

import json

class UpdateParams:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __getattr__(self, item):
        print(f"没有该属性:{item}")
        return None

    def __str__(self):
        return str(self.__dict__)

"""json转对象"""
def jsonToObject(jsonData):
    try:
        params = UpdateParams.__new__(UpdateParams)
        params.__dict__.update(jsonData)
        return params
    except TypeError: # 如果TypeError那么就不转直接返回
        return jsonData
    except ValueError: # 如果ValueError那么就不转直接返回
        return jsonData
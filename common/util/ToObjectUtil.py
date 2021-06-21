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

class Dict(dict):
    __setattr__ = dict.__setitem__
    __getattr__ = dict.__getitem__

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

"""dict转对象"""
def dictToObject(d):
    # 如果不是字典类型则返回
    if isinstance(d, dict): return d
    try:
        val = Dict(d)
        return val
    except Exception as e:
        print("字典转对象错误：", e)
        return d

from model.dto import MsgDto
if __name__ == '__main__':
    msg = MsgDto.MsgDto(1, 2, 3, 4)
    print(msg)
    print(type(msg))
    d = msg.__dict__
    print(d)
    print(type(d))
    obj = Dict(d)
    print(obj.group)

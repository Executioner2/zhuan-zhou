# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/17
# ide：PyCharm
# describe：json转复杂object
# editDate：
# editBy：
# version：1.0.0
import inspect

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
    __bases__ = dict.__bases__

    """返回序列化状态值"""
    def __getstate__(self):
        # 序列化时以字典类型返回该动态对象的属性和值
        # 动态取得属性和值
        propertiesDict = inspect.getmembers(self)[2][1]
        return propertiesDict

    """反序列化时调用"""
    def __setstate__(self, state):
        print(state)

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
    if not isinstance(d, dict): return d
    try:
        val = Dict(d)
        return val
    except Exception as e:
        print("字典转对象错误：", e)
        return d
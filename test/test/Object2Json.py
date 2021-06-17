# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/17
# ide：PyCharm
# describe：
# editDate：
# editBy：
# version：1.0.0

import json
from common.handler.MyEncoder import MyEncoder

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Result:
    result = {"code":None, "url":None, "data":None}

    def __init__(self, code, url, data = None):
        self.result["code"] = code
        self.result["url"] = url
        if hasattr(data, "__dict__"):
            self.result["data"] = data.__dict__
        else:
            self.result["data"] = data

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
    except TypeError:
        return jsonData
    except ValueError:
        return jsonData

if __name__ == '__main__':
    zs = Student("张三", 22)
    result = Result(200, "login",  b'1233')
    jsonStr = json.dumps(result.result, cls=MyEncoder)
    print(jsonStr)
    objectStr = json.loads(jsonStr)

    obj = jsonToObject(objectStr["data"])
    print(obj)


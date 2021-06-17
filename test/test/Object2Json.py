# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/17
# ide：PyCharm
# describe：
# editDate：
# editBy：
# version：1.0.0

import json

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

if __name__ == '__main__':
    zs = Student("张三", 22)
    result = Result(200, "/login", True)
    jsonStr = json.dumps(result.result)
    print(jsonStr)
    objectStr = json.loads(jsonStr)
    print(objectStr)


# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/17
# ide：PyCharm
# describe：服务器与客户端交换数据的类
# editDate：
# editBy：
# version：1.0.0

class Result:
    result = {"code":None, "url":None, "data":None}

    def __init__(self, code, url, data=None):
        self.result["code"] = code
        self.result["url"] = url
        if hasattr(data, "__dict__"): # 先判断对象是否包含__dict__属性，如果有则转为字典
            self.result["data"] = data.__dict__
        else: # 如果不包含__dict__属性则直接赋值
            self.result["data"] = data
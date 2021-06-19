# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/17
# ide：PyCharm
# describe：服务器与客户端交换数据的类
# editDate：
# editBy：
# version：1.0.0

from common.result.ResultCodeEnum import ResultCodeEnum

class Result:
    result = {"code":None, "url":None, "data":None}

    def __init__(self, url, code, data=None):
        self.result["url"] = url
        self.result["code"] = code
        # self.__setCode(code)
        self.__setData(data)


    def __setCode(self, code):
        if code == None:
            self.result["code"] = ResultCodeEnum.SUCCESS.value[0]
        else:
            self.result["code"] = code

    def __setData(self, data):
        if hasattr(data, "__dict__"): # 先判断对象是否包含__dict__属性，如果有则转为字典
            self.result["data"] = data.__dict__
        else: # 如果不包含__dict__属性则直接赋值
            self.result["data"] = data

    """自定义状态"""
    @staticmethod
    def build(code, url="", data=None):
        return Result(url, code, data)

    """成功"""
    @staticmethod
    def ok(url="", data=None):
        return Result(url, ResultCodeEnum.SUCCESS.value[0], data)

    """失败"""
    @staticmethod
    def fail(url=""):
        return Result(url, ResultCodeEnum.FAIL.value[0])

    def __str__(self):
        return str(self.result)

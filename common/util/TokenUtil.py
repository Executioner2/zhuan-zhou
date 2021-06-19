# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/11
# ide：PyCharm
# describe：
# editDate：
# editBy：
# version：1.0.0

import base64
import json
from common.util import MD5Util

number = (48, 57)  # 数字字符ascii码范围
upper = (65, 90)  # 大写字符ascii码范围
lower = (97, 122)  # 小写字符ascii码范围

class TokenUtil:
    # 加盐
    _salt = b"LK@NK#*&N!@"

    def __init__(self):
        pass

    @staticmethod
    def createToken(username:str, password:str):
        password = MD5Util.saltMD5(password) # 对密码进行MD5加盐加密
        mapStr = '{"username":"'+username+'", "password":"'+password+'"}'
        token = base64.b64encode(mapStr.encode(encoding='utf-8'))
        # 加密后
        token = TokenUtil.__encrypt(token)
        return token

    """对base64进行加密"""
    @staticmethod
    def __encrypt(token):
        tokenList = list(token)
        bSalt = TokenUtil._salt
        saltIndex = -1
        for index, item in enumerate(tokenList):
            saltIndex += 1
            saltIndex = saltIndex % len(bSalt)
            if item >= number[0] and item <= number[1]:
                # 数字
                temp = bSalt[saltIndex] % (number[1] - number[0] + 1) + item
                if number[1] < temp:
                    tokenList[index] = number[0] - 1 + temp % number[1]
                else:
                    tokenList[index] = temp
            elif item >= upper[0] and item <= upper[1]:
                # 大写
                temp = bSalt[saltIndex] % (upper[1] - upper[0] + 1) + item
                if upper[1] < temp:
                    tokenList[index] = upper[0] - 1 + temp % upper[1]
                else:
                    tokenList[index] = temp
            elif item >= lower[0] and item <= lower[1]:
                # 小写
                temp = bSalt[saltIndex] % (lower[1] - lower[0] + 1) + item
                if lower[1] < temp:
                    tokenList[index] = lower[0] - 1 + temp % lower[1]
                else:
                    tokenList[index] = temp
        # 对加密后的base64编码再编码
        base = bytearray(base64.b64encode(bytes(tokenList)))
        # 去掉后面补充的==，让它看起来不像是base64编码
        while True:
            if base[-1] == 61:
                base.remove(base[-1])
            else:
                break
        return base

    """对加密后的base64编码进行解密"""
    @staticmethod
    def __decode(token):
        # 如果是str则进行转型
        if isinstance(token, str):
            token = str.encode(token)
            token = bytearray(token)
        # 补充去掉的==
        i = len(token) % 4
        for index in range(i):
            token.append(61)
        # 然后对base64进行一次解码
        token = base64.b64decode(token)
        tokenList = list(token)
        bSalt = TokenUtil._salt
        saltIndex = -1
        for index, item in enumerate(tokenList):
            saltIndex += 1
            saltIndex = saltIndex % len(bSalt)
            if item >= number[0] and item <= number[1]:
                # 数字
                temp = item - bSalt[saltIndex] % (number[1] - number[0] + 1)
                if temp < number[0]:
                    tokenList[index] = number[1] + 1 - number[0] % temp
                else:
                    tokenList[index] = temp
            elif item >= upper[0] and item <= upper[1]:
                # 大写
                temp = item - bSalt[saltIndex] % (upper[1] - upper[0] + 1)
                if temp < upper[0]:
                    tokenList[index] = upper[1] + 1 - upper[0] % temp
                else:
                    tokenList[index] = temp
            elif item >= lower[0] and item <= lower[1]:
                # 小写
                temp = item - bSalt[saltIndex] % (lower[1] - lower[0] + 1)
                if temp < lower[0]:
                    tokenList[index] = lower[1] + 1 - lower[0] % temp
                else:
                    tokenList[index] = temp
        # 解密后的
        return bytes(tokenList)

    @staticmethod
    def getUserInfo(token):
        # 先对token进行解密
        token = TokenUtil.__decode(token)
        # 对解密后的token进行base64解码
        mapStr = base64.b64decode(token)
        map = json.loads(mapStr)
        return map["username"], map["password"]

"""测试"""
if __name__ == '__main__':
    token = TokenUtil.createToken("zhangsan", "12332bbbbaa1svabaag2121211")
    print(token)
    value = TokenUtil.getUserInfo(token)
    print(value)

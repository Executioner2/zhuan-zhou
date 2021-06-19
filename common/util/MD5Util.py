# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/19
# ide：PyCharm
# describe：md5加盐加密
# editDate：
# editBy：
# version：1.0.0

import hashlib

"""md5加盐加密"""
def saltMD5(val:str):
    md5 = hashlib.md5(b"$J2&*GN0%@B") # 盐
    md5.update(val.encode("utf-8"))
    return md5.hexdigest() # 返回密文

# 测试
if __name__ == '__main__':
    result = saltMD5("123456")
    print(result)
# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/17
# ide：PyCharm
# describe：数据传输，封装工具类
# editDate：
# editBy：
# version：1.0.0

import json
from socket import socket

from common.handler.MyEncoder import MyEncoder
from common.result import Result
from common.util.Base64Util import Base64Util

"""发送数据"""
def send(socket:socket, result:Result):
    data = json.dumps(result.result, cls=MyEncoder)
    ciphertext = Base64Util.encipher(data) # 加密数据
    socket.send(ciphertext)


"""接收数据"""
def receive(socket:socket):
    try:
        # 字节数组
        ciphertext = bytearray()
        while True:
            ciphertext.extend(socket.recv(1024*1024)) # 默认1MB 缓冲区大小单位为字节
            # 末尾为\0则读取完毕，则跳出循环
            if ciphertext[-1] == 0: break

        data = Base64Util.decipher(ciphertext)  # 解密密文
        return data
    except IndexError as e:
        print(e)
    except Exception as e:
        print(e)
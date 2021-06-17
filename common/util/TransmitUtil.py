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

"""发送数据"""
def send(socket:socket, result:Result):
    jsonStr = json.dumps(result.result, cls=MyEncoder)
    jsonStr += "\0"
    socket.send(jsonStr.encode())


"""接收数据"""
def receive(socket:socket):
    # 字节数组
    recvAll = bytearray()
    while True:
        recvAll.extend(socket.recv(1024*1024)) # 默认1MB 缓冲区大小单位为字节
        if recvAll[-1] == 0: # 末尾为0则读取完毕，则跳出循环
            recvAll.remove(recvAll[-1]) # 移除最后的'/0' 不然转json会报错
            break

    jsonStr = recvAll.decode()
    return json.loads(jsonStr)
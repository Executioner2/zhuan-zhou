# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/19
# ide：PyCharm
# describe：
# editDate：
# editBy：
# version：1.0.0

import sys

import configparser
import os

"""读取数据库配置文件"""
def readDataSourceConfig(path, datasource=None) -> None:
    try:
        conf = configparser.ConfigParser()
        datasource = "datasource01" if datasource == None else datasource
        conf.read(path)
        host = conf.get(datasource, "host")
        port = conf.get(datasource, "port")
        db = conf.get(datasource, "db")
        user = conf.get(datasource, "user")
        password = conf.get(datasource, "password")
        return host, port, db, user, password
    except Exception as e:
        print(e)

"""读取用户配置文件"""
def readUserConfig(path, config=None) -> None:
    try:
        conf = configparser.ConfigParser()
        config = "config01" if config == None else config
        conf.read(path)
        colorRB = conf.get(config, "color_rb")
        headStyle = conf.get(config, "head_style")
        serverIp = conf.get(config, "server_ip")
        serverPort = conf.get(config, "server_port")
        return colorRB, headStyle, serverIp, serverPort
    except Exception as e:
        print(e)

"""写入用户配置文件"""
def wirteUserConfig(path, colorRB, serverIp, serverPort, headStyle=None, config=None):
    conf = configparser.RawConfigParser()
    config = "config01" if config == None else config
    conf.add_section(config)
    conf.set(config, "color_rb", colorRB)
    conf.set(config, "head_style", headStyle)
    conf.set(config, "server_ip", serverIp)
    conf.set(config, "server_port", serverPort)
    # 保存到文件
    with open(path, "w") as f:
        conf.write(f)

"""写入配置文件"""
def wirteConfig(path, params:dict, config=None):
    conf = configparser.RawConfigParser()
    config = "config01" if config == None else config
    conf.add_section(config)
    # 遍历字典设置参数
    for key in params:
        conf.set(config, key, params[key])
    # 保存到文件
    with open(path, "w") as f:
        conf.write(f)

"""读取配置文件"""
def readConfig(path, sections=None) -> None:
    try:
        conf = configparser.ConfigParser()
        conf.read(path)
        sections = "config01" if sections == None else sections
        result = conf.items(sections)  # 返回所有键值对
        return result
    except Exception as e:
        print(e)

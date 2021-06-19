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
def readDataSourceConfig(path, datasource=None):
    conf = configparser.ConfigParser()
    datasource = "datasource01" if datasource == None else datasource
    conf.read(path)
    host = conf.get(datasource, "host")
    port = conf.get(datasource, "port")
    db = conf.get(datasource, "db")
    user = conf.get(datasource, "user")
    password = conf.get(datasource, "password")

    return host, port, db, user, password

"""读取用户配置文件"""
def readUserConfig(path, config=None):
    conf = configparser.ConfigParser()
    config = "config01" if config == None else config
    conf.read(path)
    host = conf.get(config, "host")
    port = conf.get(config, "port")
    db = conf.get(config, "db")
    user = conf.get(config, "user")
    password = conf.get(config, "password")

    return host, port, db, user, password
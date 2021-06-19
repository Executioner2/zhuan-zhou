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

def readConfig(path=None, datasource=None):
    conf = configparser.ConfigParser()
    datasource = "datasource01" if datasource == None else datasource
    if path == None:
        root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0]))))
        conf.read(root_path + "/resource/config/datasource.conf")
    else:
        conf.read(path)
    host = conf.get(datasource, "host")
    port = conf.get(datasource, "port")
    db = conf.get(datasource, "db")
    user = conf.get(datasource, "user")
    password = conf.get(datasource, "password")

    return host, port, db, user, password
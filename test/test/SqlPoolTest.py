# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/19
# ide：PyCharm
# describe：
# editDate：
# editBy：
# version：1.0.0

import pymysql

from dbutils.pooled_db import PooledDB

POOL = PooledDB(
    creator=pymysql,  # 使用链接数据库的模块
    maxconnections=6,  # 连接池允许的最大连接数，0和None表示不限制连接数
    mincached=10,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
    maxcached=20,  # 链接池中最多闲置的链接，0和None不限制
    blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
    maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
    # 连接mysql
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123321',
    database='agc',
    charset='utf8'
)


def func():
    # 检测当前正在运行连接数的是否小于最大链接数，如果不小于则：等待或报raise TooManyConnections异常
    # 否则
    # 则优先去初始化时创建的链接中获取链接 SteadyDBConnection。
    # 然后将SteadyDBConnection对象封装到PooledDedicatedDBConnection中并返回。
    # 如果最开始创建的链接没有链接，则去创建一个SteadyDBConnection对象，再封装到PooledDedicatedDBConnection中并返回。
    # 一旦关闭链接后，连接就返回到连接池让后续线程继续使用。
    conn = POOL.connection()

    # print(th, '链接被拿走了', conn1._con)
    # print(th, '池子里目前有', pool._idle_cache, '\r\n')

    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute('select * from tbl_user')
    result = cursor.fetchall()
    print(result)
    conn.close()

if __name__ == '__main__':

    func()
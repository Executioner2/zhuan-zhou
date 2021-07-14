# zhuan-zhou    agc

#### 这是在下的第一个python微型项目，python也是在写这个项目的过程中学习的。
#### 所以，假如您发现了许多奇奇怪怪的代码风格还请见谅！
#### 此项目未经过严谨细致的测试，如发现BUG烦请自行修改。
<br/>
1、使用命令下载模块  
  `pip install -r requirements.txt` // pip install -r 文件路径
  
2、导入sql表  
  `mysql -uroot -p123321` // 请使用自己的账号密码 
  
  `create database agc;` // 创建数据库   
  
  `use ags;` // 进入到该数据库   
  
  `source tbl_chatting_records.sql;` // 导入聊天记录表（命令格式：source 文件路径） 
  
  `source tbl_user.sql;` // 导入用户表
  
3、运行`server/src/ServerApplication.py`开启服务器窗口

4、运行`client/src/ClientApplication.py`开启客户端窗口

# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/9
# ide：PyCharm
# describe：
# editDate：
# editBy：
# version：1.0.0

import os
import re  # 正则表达式
import socket
import sys

from PyQt5 import QtWidgets, QtCore

from client.src.signal import ClientSignal
from common.result.IndexTableEnum import IndexTableEnum
from common.result.Result import Result
from common.result.ResultCodeEnum import ResultCodeEnum
from common.util import ConfigFileUtil
from common.util import TransmitUtil
from common.util.Base64Util import Base64Util
from model.dto import LoginDto
from model.enum_.HeadStyleEnum import HeadStyleEnum
from ui import LoginWindow_ui

LOGIN_FILE_NAME = "login.ini"
USER_CONFIG_FILE_NAME = "user_config.ini"

class LoginWindow(QtWidgets.QMainWindow, LoginWindow_ui.Ui_Form, QtCore.QObject):
    clientSocket = None
    userConfigFilePath = os.path.dirname(os.path.dirname(sys.argv[0])) + "/resource/config/"
    loginFilePath = os.path.dirname(os.path.dirname(sys.argv[0])) + "/resource/config/"
    fakePassword = None # 假密码
    firstEditLoginInfo = True # 第一次编辑登录信息

    def __init__(self, clientSignal:ClientSignal):
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        self.registerWidget.hide()
        self.configWidget.hide()
        self.setWindowTitle("登录")
        self.clientSignal = clientSignal # 信号类
        # 登录界面到聊天界面的传递对象
        self._loginDto = LoginDto.LoginDto()
        self._loginDto.headStyle = HeadStyleEnum.GREEN.value['style'] # 头像默认为绿色
        # 绑定登录按钮
        self.loginBtn.clicked.connect(self.on_loginBtn_click)
        # 绑定配置按钮
        self.configBtn.clicked.connect(self.on_configBtn_clicked)
        # 绑定注册跳转按钮
        self.registerSkipBtn.clicked.connect(self.on_registerSkipBtn_clicked)
        # 绑定返回到登录页的按钮
        self.backBtn.clicked.connect(self.on_backBtn_clicked)
        # 绑定配置确认按钮
        self.confirmBtn.clicked.connect(self.on_confirmBtn_clicked)
        # 批量绑定相同事件
        for radio in self.radioBtnGroupWidget.children():
            # 判断是否是QRadioButton，如果是则绑定对应槽
            if isinstance(radio, QtWidgets.QRadioButton):
                radio.clicked.connect(lambda: self.selectCustomHeadStyle(False))
        self.customRB.clicked.connect(lambda: self.selectCustomHeadStyle(True))
        # 服务器ip
        self.serverIpLE.editingFinished.connect(self.on_serverIpLE_editingFinished)
        # 服务器port
        self.serverPortLE.editingFinished.connect(self.on_serverPortLE_editingFinished)
        # 别称
        self.crypCheck.clicked.connect(self.on_crypCheck_clicked)
        # register LE失去焦点
        self.registerUsernameLE.blurSignal.connect(self.on_register_blurSignal)
        self.registerPasswordLE.blurSignal.connect(self.on_register_blurSignal)
        self.registerCofirmPasswordLE.blurSignal.connect(self.on_register_blurSignal)
        # 密码输入
        self.passwordLE.keyPressSignal.connect(self.on_loginLE_keyDown)
        # 用户名输入
        self.usernameLE.keyPressSignal.connect(self.on_loginLE_keyDown)
        # 绑定注册提交按钮
        self.registerBtn.clicked.connect(self.on_registerBtn_click)
        # 绑定记住密码
        self.remberPasswordCheck.clicked.connect(self.on_remverPasswordCheck_click)
        # 读取用户配置文件
        self.readUserConfig()
        # 读取登录文件
        self.readLoginFile()

    """读取登录文件"""
    def readLoginFile(self):
        if os.path.exists(self.loginFilePath + LOGIN_FILE_NAME):
            result = ConfigFileUtil.readConfig(self.loginFilePath + LOGIN_FILE_NAME)
            if result[0][1] != None and result[0][1].strip() != "":
                self._loginDto.token = result[0][1].encode()
                self._loginDto.username = result[1][1]
                self.usernameLE.setText(result[1][1])
                self.fakePassword = " " * int(result[2][1])
                self.passwordLE.setText(self.fakePassword) # 填充空格占位
                self.remberPasswordCheck.setChecked(True)
                if result[0][1] != None and result[3][1].strip() != "":
                    self.crypCheck.setChecked(True)
                    self.crypLE.setText(result[3][1])
                    self.crypLE.setEnabled(True)

    """读取用户配置文件"""
    def readUserConfig(self):
        if os.path.exists(self.userConfigFilePath + USER_CONFIG_FILE_NAME):
            configInfo = ConfigFileUtil.readUserConfig(self.userConfigFilePath + USER_CONFIG_FILE_NAME)
            tempRadio = self.radioBtnGroupWidget.findChild(QtWidgets.QRadioButton, configInfo[0])
            if tempRadio == self.customRB:
                tempTuple = configInfo[1].split(",")
                self.RSB.setValue(int(tempTuple[0]))
                self.GSB.setValue(int(tempTuple[1]))
                self.BSB.setValue(int(tempTuple[2]))
                self.selectCustomHeadStyle(True)
            tempRadio.setChecked(True)
            self.serverIpLE.setText(configInfo[2])
            self.serverPortLE.setText(configInfo[3])

    """记住密码"""
    def on_remverPasswordCheck_click(self):
        if self.passwordLE.text() == self.fakePassword:
            self.passwordLE.clear()
            self.usernameLE.clear()
            # 删除登录文件
            if os.path.exists(self.loginFilePath + LOGIN_FILE_NAME):
                os.remove(self.loginFilePath + LOGIN_FILE_NAME)

    """注册请求"""
    def on_registerBtn_click(self):
        flag = self.on_register_blurSignal()
        if flag:
            clientSocket = self.__getClientSocket()
            if clientSocket == None:
                # 返回为空，则连接服务器失败
                msgHint = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, "错误", "连接服务器失败！")
                msgHint.exec_()
            else:  # 连接成功，开始用户注册
                username = self.registerUsernameLE.text()
                password = self.registerPasswordLE.text()
                # 封装成自定义token
                token = Base64Util.createToken(username, password)
                result = Result.ok(IndexTableEnum.REGISTER.value, token)
                print("注册发送过去的对象：", result)
                # 发送
                TransmitUtil.send(clientSocket, result)
                # 服务器返回结果
                serverResult = TransmitUtil.receive(clientSocket)
                print("服务器返回结果", serverResult)
                if serverResult["code"] == ResultCodeEnum.SUCCESS.value[0]:
                    msgBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, "提示", "用户注册成功")
                    msgBox.exec_()
                    # 跳转到登录页
                    self.on_backBtn_clicked()
                elif serverResult["code"] == ResultCodeEnum.REGISTER_USERNAME_ERROR.value[0]:
                    msgBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, "提示", "用户名已被使用，请重新输入")
                    msgBox.exec_()

    """登录lineText按键按下"""
    def on_loginLE_keyDown(self):
        # 满足一个就删除存储的token信息
        if self.firstEditLoginInfo:
            self.passwordLE.clear()
            self._loginDto.token = None
            # 删除登录信息
            if os.path.exists(self.loginFilePath + LOGIN_FILE_NAME):
                os.remove(self.loginFilePath + LOGIN_FILE_NAME)
            self.firstEditLoginInfo = False


    """register LE失去焦点时"""
    def on_register_blurSignal(self, val = None):
        if val in (self.registerUsernameLE.objectName(), None):
            if self.registerUsernameLE.text().strip() == "":
                self.hint.setText("用户名不能为空")
                self.hint.show()
                return False
            elif self.hint.text() == "用户名不能为空":
                self.hint.hide()

        if val in (self.registerPasswordLE.objectName(), None):
            pattern = re.compile(r"^[a-zA-Z]\w{5,17}$")
            result = pattern.match(self.registerPasswordLE.text())
            if self.registerPasswordLE.text().strip() == "":
                self.hint.setText("密码不能为空")
                self.hint.show()
                return False
            elif not result:
                self.hint.setText("密码太弱，请重新输入")
                self.hint.show()
                return False
            elif self.hint.text() in ("密码不能为空", "密码太弱，请重新输入"):
                self.hint.hide()

        if val in (self.registerCofirmPasswordLE.objectName(), None):
            if self.registerCofirmPasswordLE.text().strip() == "":
                self.hint.setText("确认密码不能为空")
                self.hint.show()
                return False
            elif self.registerPasswordLE.text().strip() != self.registerCofirmPasswordLE.text().strip():
                self.hint.setText("两次密码不一致，请重新输入")
                self.hint.show()
                return False
            elif self.hint.text() in ("确认密码不能为空", "两次密码不一致，请重新输入"):
                self.hint.hide()

        return True

    """设置别称"""
    def on_crypCheck_clicked(self):
        flag = True if self.crypCheck.isChecked() else False
        self.crypLE.setEnabled(flag)
        if flag and self.crypLE.text().strip() == "":
            self.crypLE.setText("匿名用户")

    """服务器port输入框编辑完毕"""
    def on_serverPortLE_editingFinished(self):
        pattern = re.compile(r'^\d+$')
        port = self.serverPortLE.text()
        result = pattern.match(port)
        if result:
            # 是数字
            if int(port) < 0 or int(port) > 65535:
                msgHint = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "警告", "端口号必须是0-65535")
                msgHint.exec_()
                return False
        else:
            # 不是数字
            msgHint = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "警告", "端口号必须是整数")
            msgHint.exec_()
            return False

        return True

    """服务器ip输入框编辑完毕"""
    def on_serverIpLE_editingFinished(self):
        pattern = re.compile(r'^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]{1,2})(\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]{1,2})){3}$')
        result = pattern.match(self.serverIpLE.text())
        if not result:
            msgHint = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "警告", "请输入正确的ip地址格式")
            msgHint.exec_()
            return False

        return True

    """选择自定义头像样式"""
    def selectCustomHeadStyle(self, flag:bool):
        if flag:
            # 设置自定义色调可用
            self.RSB.setEnabled(True)
            self.GSB.setEnabled(True)
            self.BSB.setEnabled(True)
        else:
            # 设置自定义色调不可用
            self.RSB.setEnabled(False)
            self.GSB.setEnabled(False)
            self.BSB.setEnabled(False)

    """设置头像样式"""
    def setHeadStyle(self):
        # 如果自定义样式选中
        if self.customRB.isChecked():
            r = self.RSB.value()
            g = self.GSB.value()
            b = self.BSB.value()
            self._loginDto.headStyle = "({}, {}, {})".format(r, g, b)
        else:
            # 遍历判断选中了哪个默认头像
            for radio in self.radioBtnGroupWidget.children():
                if isinstance(radio, QtWidgets.QRadioButton) and radio.objectName() != HeadStyleEnum.CUSTOM.value['name'] and radio.isChecked():
                    self._loginDto.headStyle = HeadStyleEnum.getStyleByName(radio.objectName())
                    break

    """登录"""
    def on_loginBtn_click(self):
        username = self.usernameLE.text().strip()
        password = self.passwordLE.text().strip()

        if not (self.remberPasswordCheck.isChecked() and self._loginDto.token != None):
            if username == "" or password == "":
                msgHint = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "警告", "用户名或密码不能为空！")
                msgHint.exec_()
                return
            else:
                # 封装用户名和密码，创建token
                self._loginDto.token = Base64Util.createToken(self.usernameLE.text(), self.passwordLE.text())
        # 设置头像
        self.setHeadStyle()
        # 设置服务器ip和服务器端口
        self._loginDto.serverIp = self.serverIpLE.text()
        self._loginDto.serverPort = self.serverPortLE.text()
        # 判断是否开启别称，如果开启则设置别称
        if self.crypCheck.isChecked():
            self._loginDto.cryp = "匿名用户" if self.crypLE.text().strip() == "" else self.crypLE.text().strip()

        # 这里直接创建socket，然后用户登录成功后把socket传入ClientSocketThread中去
        clientSocket = self.__getClientSocket()
        if clientSocket == None:
            # 返回为空，则连接服务器失败
            msgHint = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, "错误", "连接服务器失败！")
            msgHint.exec_()
        else: # 连接成功，开始用户登录
            # 封装传输对象
            result = Result.ok(IndexTableEnum.LOGIN.value, self._loginDto)
            print("客户端传输过去的对象", result)
            # 发送
            TransmitUtil.send(clientSocket, result)
            # 服务器返回结果
            serverResult = TransmitUtil.receive(clientSocket)
            print("服务器返回的结果", serverResult)

            if serverResult["code"] == ResultCodeEnum.SUCCESS.value[0]: # 如果为200，则登录成功
                self._loginDto.username = serverResult["data"][0]
                self._loginDto.nickname = serverResult["data"][1]
                # 判断当前是否需要记住密码
                if self.remberPasswordCheck.isChecked():
                    if not os.path.exists(self.loginFilePath): os.makedirs(self.loginFilePath)
                    aliase = self.crypLE.text() if self.crypCheck.isChecked() else ""
                    params = {"token": self._loginDto.token.decode(), "username": username,
                              "length": len(self.passwordLE.text()), "aliase": aliase}
                    ConfigFileUtil.wirteConfig(self.loginFilePath + LOGIN_FILE_NAME, params)
                else:
                    # 删除登录文件
                    if os.path.exists(self.loginFilePath + LOGIN_FILE_NAME):
                        os.remove(self.loginFilePath + LOGIN_FILE_NAME)
                self.clientSignal.skipSignal.emit((self._loginDto, clientSocket)) # 跳转到聊天主窗口
                self.close()
            else:
                msgBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "警告", ResultCodeEnum.getDescribeByCode(serverResult["code"]))
                msgBox.exec_()

    """获取（创建）client socket"""
    def __getClientSocket(self):
        try:
            if not self.clientSocket:
                serverIp = self.serverIpLE.text()
                serverPort = int(self.serverPortLE.text())
                clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = clientSocket.connect((serverIp, serverPort))
                if result == None:
                    print("成功连接上服务器")
                    self.clientSocket = clientSocket

            return self.clientSocket
        except ConnectionRefusedError:
            return None

    """切换到配置页"""
    def on_configBtn_clicked(self):
        # 隐藏登录widget
        self.loginWidget.hide()
        # 隐藏注册widget
        self.registerWidget.hide()
        # 显示配置widget
        self.configWidget.show()
        self.setWindowTitle("配置")

    """切换到注册页"""
    def on_registerSkipBtn_clicked(self):
        # 隐藏登录widget
        self.loginWidget.hide()
        # 隐藏配置widget
        self.configWidget.hide()
        # 显示注册widget
        self.registerWidget.show()
        # 清空用户名和密码
        self.usernameLE.clear()
        self.passwordLE.clear()
        self.crypLE.clear()
        self.crypCheck.setChecked(False)
        self.setWindowTitle("用户注册")

    """切换到登录页"""
    def on_backBtn_clicked(self):
        # 隐藏配置widget
        self.configWidget.hide()
        # 隐藏注册widget
        self.registerWidget.hide()
        # 显示登录widget
        self.loginWidget.show()
        # 清空文本
        self.registerUsernameLE.clear()
        self.registerPasswordLE.clear()
        self.registerCofirmPasswordLE.clear()
        # 隐藏hint
        self.hint.hide()
        self.setWindowTitle("登录")

    """配置确认后切换到登录widget"""
    def on_confirmBtn_clicked(self):
        if not self.on_serverIpLE_editingFinished(): return
        elif not self.on_serverPortLE_editingFinished(): return

        # 保存配置到配置文件
        headStyle = None
        for item in self.radioBtnGroupWidget.children():
            if isinstance(item, QtWidgets.QRadioButton) and item.isChecked():
                colorRB = item.objectName()
                if colorRB == HeadStyleEnum.CUSTOM.value["name"]:
                    headStyle = "{}, {}, {}".format(self.RSB.value(), self.GSB.value(), self.BSB.value())
                break
        if not os.path.exists(self.userConfigFilePath): os.makedirs(self.userConfigFilePath)
        ConfigFileUtil.wirteUserConfig(self.userConfigFilePath + USER_CONFIG_FILE_NAME, colorRB, self.serverIpLE.text(),
                                       self.serverPortLE.text(), headStyle)
        # 隐藏配置widget
        self.configWidget.hide()
        # 显示登录widget
        self.loginWidget.show()
        self.setWindowTitle("登录")
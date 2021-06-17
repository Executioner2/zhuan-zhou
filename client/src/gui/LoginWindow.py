# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/9
# ide：PyCharm
# describe：
# editDate：
# editBy：
# version：1.0.0

import re  # 正则表达式
import socket

from PyQt5 import QtWidgets, QtCore

from common.result.IndexTableEnum import IndexTableEnum
from common.result.Result import Result
from common.util import TransmitUtil
from common.util.TokenUtil import TokenUtil
from model.dto import LoginDto
from model.enum_.HeadStyleEnum import HeadStyleEnum
from ui import LoginWindow_ui


class LoginWindow(QtWidgets.QMainWindow, LoginWindow_ui.Ui_Form, QtCore.QObject):
    # 跳转信号
    skipSignal = QtCore.pyqtSignal(object)

    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("登录")
        # 登录界面到聊天界面的传递对象
        self._loginDto = LoginDto.LoginDto()
        self._loginDto.headStyle = HeadStyleEnum.GREEN.value['style'] # 头像默认为绿色
        # 绑定登录按钮
        self.loginBtn.clicked.connect(self.on_loginBtn_click)
        # 绑定配置按钮
        self.configBtn.clicked.connect(self.on_configBtn_clicked)
        # 绑定注册跳转按钮
        self.registSkipBtn.clicked.connect(self.on_registSkipBtn_clicked)
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
        if username == "" or password == "":
            msgHint = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "警告", "用户名或密码不能为空！")
            msgHint.exec_()
            return

        # 设置头像
        self.setHeadStyle()
        # 设置服务器ip和服务器端口
        self._loginDto.serverIp = self.serverIpLE.text()
        self._loginDto.serverPort = self.serverPortLE.text()
        # 判断是否开启别称，如果开启则设置别称
        if self.crypCheck.isChecked():
            self._loginDto.cryp = "匿名用户" if self.crypLE.text().strip() else self.crypLE.text().strip()

        # 这里直接创建socket，然后用户登录成功后把socket传入ClientSocketThread中去
        clientSocket = self.__createClientSocket()
        if clientSocket == None:
            # 返回为空，则连接服务器失败
            msgHint = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, "错误", "连接服务器失败！")
            msgHint.exec_()
        else: # 连接成功，开始用户登录
            # 封装用户名和密码，创建token
            token = TokenUtil.createToken(self.usernameLE.text(), self.passwordLE.text())
            # 封装传输对象
            result = Result.ok(IndexTableEnum.LOGIN.value, token)
            print("客户端传输过去的对象", result)
            # 发送
            TransmitUtil.send(clientSocket, result)
            # 服务器返回结果
            serverResult = TransmitUtil.receive(clientSocket)
            print("服务器返回的结果", serverResult)
            if serverResult["code"] == 200: # 如果为200，则登录成功
                self.skipSignal.emit(self._loginDto)
                self.close()

    """创建client socket"""
    def __createClientSocket(self):
        try:
            serverIp = self.serverIpLE.text()
            serverPort = int(self.serverPortLE.text())
            clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = clientSocket.connect((serverIp, serverPort))
            if result == None:
                print("成功连接上服务器")
                return clientSocket
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

    """切换到注册页"""
    def on_registSkipBtn_clicked(self):
        # 隐藏登录widget
        self.loginWidget.hide()
        # 隐藏配置widget
        self.configWidget.hide()
        # 显示注册widget
        self.registerWidget.show()

    """切换到登录页"""
    def on_backBtn_clicked(self):
        # 隐藏配置widget
        self.configWidget.hide()
        # 隐藏注册widget
        self.registerWidget.hide()
        # 显示登录widget
        self.loginWidget.show()

    """配置确认后切换到登录widget"""
    def on_confirmBtn_clicked(self):
        if not self.on_serverIpLE_editingFinished():
            pass
        elif not self.on_serverPortLE_editingFinished():
            pass
        else:
            # 隐藏配置widget
            self.configWidget.hide()
            # 显示登录widget
            self.loginWidget.show()



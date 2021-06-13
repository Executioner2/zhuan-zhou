# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/9
# ide：PyCharm
# describe：
# editDate：
# editBy：
# version：1.0.0

from ui import LoginWindow_ui
from PyQt5 import QtWidgets, QtCore
from enum_.HeadStyleEnum import HeadStyleEnum
from dto import LoginDto
import re # 正则表达式


class LoginWindow(QtWidgets.QMainWindow, LoginWindow_ui.Ui_Form, QtCore.QObject):
    # 跳转信号
    skipSignal = QtCore.pyqtSignal(object)

    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        # 隐藏配置widget
        self.configWidget.hide()
        # 登录界面到聊天界面的传递对象
        self._loginDto = LoginDto.LoginDto()
        self._loginDto.headStyle = HeadStyleEnum.GREEN.value['style'] # 头像默认为绿色
        # 绑定登录按钮
        self.loginBtn.clicked.connect(self.login)
        # 绑定配置按钮
        self.configBtn.clicked.connect(self.config)
        # 绑定配置确认按钮
        self.confirmBtn.clicked.connect(self.configConfirm)
        # 批量绑定相同事件
        for radio in self.radioBtnGroupWidget.children():
            # 判断是否是QRadioButton，如果是则绑定对应槽
            if isinstance(radio, QtWidgets.QRadioButton):
                radio.clicked.connect(lambda: self.selectCustomHeadStyle(False))
        self.customRB.clicked.connect(lambda: self.selectCustomHeadStyle(True))
        # 服务器ip
        self.serverIpLE.editingFinished.connect(self.serverIpEditFinish)
        # 服务器port
        self.serverPortLE.editingFinished.connect(self.serverPortEditFinish)
        # 别称
        self.crypCheck.clicked.connect(self.setCryp)

    """设置别称"""
    def setCryp(self):
        flag = True if self.crypCheck.isChecked() else False
        self.crypLE.setEnabled(flag)
        if flag and self.crypLE.text().strip() == "":
            self.crypLE.setText("匿名用户")


    """服务器port输入框编辑完毕"""
    def serverPortEditFinish(self):
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
    def serverIpEditFinish(self):
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
    def login(self):
        # 设置头像
        self.setHeadStyle()
        # 设置服务器ip和服务器端口
        self._loginDto.serverIp = self.serverIpLE.text()
        self._loginDto.serverPort = self.serverPortLE.text()
        # 判断是否开启别称，如果开启则设置别称
        if self.crypCheck.isChecked():
            self._loginDto.cryp = "匿名用户" if self.crypLE.text().strip() else self.crypLE.text().strip()
        self.skipSignal.emit(self._loginDto)
        self.close()

    """切换到配置页"""
    def config(self):
        # 隐藏登录widget
        self.loginWidget.hide()
        # 显示配置widget
        self.configWidget.show()

    """配置确认后切换到登录widget"""
    def configConfirm(self):
        if not self.serverIpEditFinish():
            pass
        elif not self.serverPortEditFinish():
            pass
        else:
            # 隐藏配置widget
            self.configWidget.hide()
            # 显示登录widget
            self.loginWidget.show()



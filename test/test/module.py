# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/3
# ide：PyCharm
# describe：QtCore中的组件测试
# editDate：
# editBy：
# version：1.0.0

from PyQt5.QtWidgets import *
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle("lambda表达式测试")
        self.resize(400, 300)
        button = QPushButton("按钮", self)
        button.move(100, 150)
        button.clicked.connect(lambda :self.onButtonClick("按钮点击了"))

    def onButtonClick(self, msg):
        print(msg)
        print("主窗口位置：x={} y={}".format(self.x(), self.y()))
        print("主窗口大小：width={} height={}".format(self.width(), self.height()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()
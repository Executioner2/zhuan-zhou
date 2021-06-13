# email：1205878539@qq.com
# author：2Executioner
# date：2021/6/13
# ide：PyCharm
# describe：
# editDate：
# editBy：
# version：1.0.0

from PyQt5 import QtWidgets

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
       QtWidgets.QWidget.__init__(self, parent)
       self.resize(300, 100)
    def moveEvent(self, e):
       print("x = {0}; y = {1}".format(e.pos().x(), e.pos().y()))
       QtWidgets.QWidget.moveEvent(self, e)
    def resizeEvent(self, e):
       print("w = {0}; h = {1}".format(e.size().width(),e.size().height()))
       QtWidgets.QWidget.resizeEvent(self, e)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
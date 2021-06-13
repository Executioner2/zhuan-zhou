'''
setFocus() 设置指定控件获取焦点
setFocusPolicy(Policy)  设置焦点获取策略
    Qt.TabFocus() 通过Tab键获取焦点
    Qt.ClickFocus() 通过被单击获取焦点
    Qt.StrongFocus()    可以通过上面两种方式获取焦点
    Qt.NoFocus()    不能通过上面两种方式获取焦点
clearFocus()    取消焦点
FocusWidget()   获取子控件当前聚焦的控件
FocusNextChild()    聚焦下一个子控件
FocusPrevious() 聚焦上一个子控件
FocusNextPreviousChild(bool) True:下一个   False:上一个
setTabOrder(pro_widget,next_widget)    静态方法 设置子控件获取焦点的先后顺序
'''
# 导入相关模块和包
from PyQt5.Qt import *
import sys

# 创建一个app应用
app = QApplication(sys.argv)
# 创建一个窗口
window = QWidget()
# 设置窗口标题
window.setWindowTitle('焦点控制')
# 设置窗口大小
window.resize(500, 500)
# 创建文本框Text_box 并作为window的子类
Text_box = QLineEdit(window)
# 创建文本框Text_box1并作为window的子类
Text_box1 = QLineEdit(window)
# 设置文本框所在位置
Text_box1.move(50, 50)
# 创建文本框Text_box3，并作为window的子类
Text_box2 = QLineEdit(window)
# 设置文本框所在位置
Text_box2.move(100, 100)
# 设置Text_box2作为获得焦点的文本框
Text_box2.setFocus()
# 设置通过Tab键过得焦点
# Text_box2.setFocusPolicy(Qt.TabFocus)
# 展示窗口
window.show()
# 进入事件循环
sys.exit(app.exec_())
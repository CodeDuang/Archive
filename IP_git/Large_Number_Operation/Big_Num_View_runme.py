import subprocess
import sys

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from matplotlib.backends.backend_qt import MainWindow


from Large_Number_Operation import Big_Num_Count_runme, Big_Num_Logical_Operation_runme, Big_Num_Mod_Operation_runme
from Large_Number_Operation import Big_Num_View


class Big_Num_View_runme(QMainWindow, Big_Num_View.Ui_MainWindow):
    def __init__(self):
        super(Big_Num_View_runme, self).__init__()
        self.setupUi(self)
        self.initt()
        self.setWindowTitle("大数运算导航")  # 设置标题
        # self.logical = logical
        # self.count = count
        # self.mod = mod
        # 禁止放大缩小窗口
        self.setFixedSize(self.width(), self.height())  # 设置窗口固定大小
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)  # 禁用放大按钮
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMinimizeButtonHint)  # 禁用缩小按钮
        # 隐藏边框
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)  # 隐藏边框并在其他边框之上
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置背景透明

    def initt(self):
        self.pushButton.clicked.connect(self.btn_logical_lgorithm)  # 大数逻辑算法
        self.pushButton_2.clicked.connect(self.btn_arithmetic_algorithm)  # 大数算术算法
        self.pushButton_3.clicked.connect(self.btn_modular_operation)  # 大数模运算

    def btn_logical_lgorithm(self):
        # self.logical.show()
        logical.show()
        self.close()

    def btn_arithmetic_algorithm(self):
        # self.count.show()
        countt.show()
        self.close()

    def btn_modular_operation(self):
        # self.mod.show()
        mod.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 定义界面实例
    countt = Big_Num_Count_runme.BigNumCountRunMe()
    logical = Big_Num_Logical_Operation_runme.Big_Num_Logical_Operation_runme()
    mod = Big_Num_Mod_Operation_runme.Big_Num_Mod_Operation_runme()
    view = Big_Num_View_runme()
    view.show()

    sys.exit(app.exec_())

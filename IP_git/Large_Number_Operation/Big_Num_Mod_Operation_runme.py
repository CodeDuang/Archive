import sys

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from matplotlib.backends.backend_qt import MainWindow

from Large_Number_Operation import Big_Num_Mod_Operation


class Big_Num_Mod_Operation_runme(QMainWindow, Big_Num_Mod_Operation.Ui_MainWindow):
    def __init__(self):
        super(Big_Num_Mod_Operation_runme, self).__init__()
        self.setupUi(self)
        self.initt()
        self.setWindowTitle("大数模运算")
        # 禁止放大缩小窗口
        # self.setFixedSize(self.width(), self.height())  # 设置窗口固定大小
        # self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)  # 禁用放大按钮
        # self.setWindowFlags(self.windowFlags() & ~Qt.WindowMinimizeButtonHint)  # 禁用缩小按钮


    def initt(self):
        self.pushButton_5.clicked.connect(self.btn_jia)
        self.pushButton_6.clicked.connect(self.btn_jian)
        self.pushButton_7.clicked.connect(self.btn_chen)
        self.pushButton_8.clicked.connect(self.btn_chu)
        self.pushButton_9.clicked.connect(self.btn_ni)
        self.pushButton_12.clicked.connect(self.btn_mi)


    def btn_jia(self):
        try:
            a = int(self.textEdit_3.toPlainText())  # 数1
        except:
            QMessageBox.warning(None, "Warning", "大数1需要输入数字")
            return
        try:
            b = int(self.textEdit.toPlainText())  # 数2
        except:
            QMessageBox.warning(None, "Warning", "大数2需要输入数字")
            return
        try:
            c = int(self.lineEdit.text())  # 模
        except:
            QMessageBox.warning(None, "Warning", "模需要输入数字")
            return
        try:
            self.textEdit_2.setText(str((a % c + b % c) % c))
        except:
            QMessageBox.warning(None, "Warning", "未知错误，请检查输入是否正确")

    def btn_jian(self):
        try:
            a = int(self.textEdit_3.toPlainText())  # 数1
        except:
            QMessageBox.warning(None, "Warning", "大数1需要输入数字")
            return
        try:
            b = int(self.textEdit.toPlainText())  # 数2
        except:
            QMessageBox.warning(None, "Warning", "大数2需要输入数字")
            return
        try:
            c = int(self.lineEdit.text())  # 模
        except:
            QMessageBox.warning(None, "Warning", "模需要输入数字")
            return
        try:
            self.textEdit_2.setText(str((a % c + b % c) % c))
        except:
            QMessageBox.warning(None, "Warning", "未知错误，请检查输入是否正确")
        try:
            self.textEdit_2.setText(str((a % c - b % c) % c))
        except:
            QMessageBox.warning(None, "Warning", "未知错误，请检查输入是否正确")

    def btn_chen(self):
        try:
            a = int(self.textEdit_3.toPlainText())  # 数1
        except:
            QMessageBox.warning(None, "Warning", "大数1需要输入数字")
            return
        try:
            b = int(self.textEdit.toPlainText())  # 数2
        except:
            QMessageBox.warning(None, "Warning", "大数2需要输入数字")
            return
        try:
            c = int(self.lineEdit.text())  # 模
        except:
            QMessageBox.warning(None, "Warning", "模需要输入数字")
            return
        try:
            self.textEdit_2.setText(str((a % c) * (b % c) % c))
        except:
            QMessageBox.warning(None, "Warning", "未知错误，请检查输入是否正确")

    def btn_chu(self):
        try:
            a = int(self.textEdit_3.toPlainText())  # 数1
        except:
            QMessageBox.warning(None, "Warning", "大数1需要输入数字")
            return
        try:
            b = int(self.textEdit.toPlainText())  # 数2
        except:
            QMessageBox.warning(None, "Warning", "大数2需要输入数字")
            return
        try:
            self.textEdit_2.setText(str(a % b))
        except:
            QMessageBox.warning(None, "Warning", "未知错误，请检查输入是否正确")

    def btn_ni(self):
        a = self.textEdit_3.toPlainText()  # 数1
        b = self.textEdit.toPlainText()  # 数2
        c = self.lineEdit.text()  # 模
        self.textEdit_2.clear()

        if a != '':
            try:
                a = int(a)
                c = int(c)
            except:
                QMessageBox.warning(None, "Warning", "大数1、模应输入数字")
                return
            try:
                self.textEdit_2.append("大数1与模求模逆:\n" + self.findModReverse(int(a), int(c)))
            except:
                self.textEdit_2.append("大数1与模求模逆:\n不存在")
        if b != '':
            try:
                b = int(b)
                c = int(c)
            except:
                QMessageBox.warning(None, "Warning", "大数2、模应输入数字")
                return
            try:
                self.textEdit_2.append("大数2与模求模逆:\n" + self.findModReverse(int(b), int(c)))
            except:
                self.textEdit_2.append("大数2与模求模逆:\n不存在")

    def btn_mi(self):
        try:
            a = int(self.textEdit_3.toPlainText())  # 数1
        except:
            QMessageBox.warning(None, "Warning", "大数1需要输入数字")
            return
        try:
            b = int(self.textEdit.toPlainText())  # 数2
            if len(self.textEdit.toPlainText()) >= 6:
                result = QMessageBox.warning(None, "Warning", "建议”大数2“长度小于6,是否重新设置“大数2”", QMessageBox.Ok,
                                             QMessageBox.No)
                if result == QMessageBox.Ok:  # 判断弹窗是否选中ok，是的话
                    return
        except:
            QMessageBox.warning(None, "Warning", "大数2需要输入数字")
            return
        try:
            c = int(self.lineEdit.text())  # 模
        except:
            QMessageBox.warning(None, "Warning", "模需要输入数字")
            return
        try:
            self.textEdit_2.setText("模幂运算根据“大数2”的长度，需要花费不同的时间，请稍等。。。")
            QApplication.processEvents()  # 刷新面板
            self.textEdit_2.setText(str(((a % c) ** b) % c))
        except:
            QMessageBox.warning(None, "Warning", "未知错误，请检查输入是否正确")

    # 模逆运算算法1
    # 要定义这个运算，需要三个整数。a的模逆元素（对n取模）为b，意味着a*b mod m=1，则称a关于m的模逆为b
    def gcd(self, a, b):
        while a != 0:
            a, b = b % a, a
        return b

    # 模逆运算算法2
    # 定义一个函数，参数分别为a,n，返回值为b
    def findModReverse(self, a, m):  # 这个扩展欧几里得算法求模逆

        if self.gcd(a, m) != 1:
            return None
        u1, u2, u3 = 1, 0, a
        v1, v2, v3 = 0, 1, m
        while v3 != 0:
            q = u3 // v3
            v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
        return str(u1 % m)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mod = Big_Num_Mod_Operation_runme()
    mod.show()
    sys.exit(app.exec_())

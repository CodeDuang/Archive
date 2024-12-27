import sys

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from Large_Number_Operation import Big_Num_Count


class BigNumCountRunMe(QMainWindow, Big_Num_Count.Ui_MainWindow):
    def __init__(self):
        super(BigNumCountRunMe, self).__init__()
        self.setupUi(self)
        self.initt()
        self.setWindowTitle("大数算数运算")
        # # 禁止放大缩小窗口
        # self.setFixedSize(self.width(), self.height())  # 设置窗口固定大小
        # self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)  # 禁用放大按钮
        # self.setWindowFlags(self.windowFlags() & ~Qt.WindowMinimizeButtonHint)  # 禁用缩小按钮

    # 大数加法
    def solve(self, s, t):
        maxlen = len(s)
        if maxlen < len(t):
            maxlen = len(t)
        s = s.zfill(maxlen)
        t = t.zfill(maxlen)
        shiwei = 0  # 进位
        summ = ''
        for i in range(-1, -maxlen - 1, -1):

            temp = ord(s[i]) + ord(t[i]) - 96 + shiwei
            if temp >= 10:
                shiwei = 1
                temp = temp - 10
            else:
                shiwei = 0
            summ += str(temp)
        if shiwei != 0:
            summ += str(shiwei)
        return summ[::-1]

    def initt(self):
        self.pushButton_5.clicked.connect(self.btn_sum)  # 大数加法
        self.pushButton_6.clicked.connect(self.btn_subtraction)  # 大数减法
        self.pushButton_7.clicked.connect(self.btn_multiplication)  # 大数乘法
        self.pushButton_8.clicked.connect(self.btn_division)  # 大数除法



    def btn_sum(self):
        a = self.textEdit_3.toPlainText()
        b = self.textEdit.toPlainText()
        try:
            x = int(a)
            y = int(b)
            self.textEdit_2.setText(self.solve(a, b))
        except:
            QMessageBox.warning(None, "Warning", "请输入10进制数字")

    def btn_subtraction(self):
        a = self.textEdit_3.toPlainText()
        b = self.textEdit.toPlainText()
        try:
            self.textEdit_2.setText(str(int(a) - int(b)))
        except:
            QMessageBox.warning(None, "Warning", "请输入10进制数字")

    def btn_multiplication(self):
        a = self.textEdit_3.toPlainText()
        b = self.textEdit.toPlainText()
        try:
            self.textEdit_2.setText(str(int(a) * int(b)))
        except:
            QMessageBox.warning(None, "Warning", "请输入10进制数字")

    def btn_division(self):
        a = self.textEdit_3.toPlainText()
        b = self.textEdit.toPlainText()
        try:
            self.textEdit_2.setText(str(int(a) // int(b)))
        except:
            QMessageBox.warning(None, "Warning", "请输入10进制数字")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    count = BigNumCountRunMe()
    count.show()
    sys.exit(app.exec_())

import sys

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from matplotlib.backends.backend_qt import MainWindow

from Large_Number_Operation import Big_Num_Logical_Operation


class Big_Num_Logical_Operation_runme(QMainWindow, Big_Num_Logical_Operation.Ui_MainWindow):
    def __init__(self):
        super(Big_Num_Logical_Operation_runme, self).__init__()
        self.setupUi(self)
        self.initt()
        self.setWindowTitle('大数逻辑运算(16进制)')

        # # 禁止放大缩小窗口
        # self.setFixedSize(self.width(), self.height())  # 设置窗口固定大小
        # self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)  # 禁用放大按钮
        # self.setWindowFlags(self.windowFlags() & ~Qt.WindowMinimizeButtonHint)  # 禁用缩小按钮

    def initt(self):
        self.pushButton_5.clicked.connect(self.btn_yi_huo)  # 异或运算
        self.pushButton_7.clicked.connect(self.btn_huo)  # 或运算
        self.pushButton_8.clicked.connect(self.btn_yu)  # 与运算


    def btn_yi_huo(self):
        a = self.textEdit_3.toPlainText()
        b = self.textEdit.toPlainText()
        len_a = len(a)
        len_b = len(b)
        strr = []
        if len_a > len_b:
            b = '0' * (len_a - len_b) + b
        else:
            a = '0' * (len_b - len_a) + a
        try:
            for i in range(max(len_a, len_b)):
                x = int(a[i], 16)
                y = int(b[i], 16)
                strr.append(hex(x ^ y)[2:])
            self.textEdit_2.setText(''.join(strr))
        except:
            QMessageBox.warning(None, "Warning", "请输入十六进制数字")

    def btn_huo(self):
        a = self.textEdit_3.toPlainText()
        b = self.textEdit.toPlainText()
        len_a = len(a)
        len_b = len(b)
        strr = []
        if len_a > len_b:
            b = '0' * (len_a - len_b) + b
        else:
            a = '0' * (len_b - len_a) + a
        try:
            for i in range(max(len_a, len_b)):
                x = int(a[i], 16)
                y = int(b[i], 16)
                strr.append(hex(x | y)[2:])
            self.textEdit_2.setText(''.join(strr))
        except:
            QMessageBox.warning(None, "Warning", "请输入十六进制数字")

    def btn_yu(self):
        a = self.textEdit_3.toPlainText()
        b = self.textEdit.toPlainText()
        len_a = len(a)
        len_b = len(b)
        strr = []

        if len_a > len_b:
            b = '0' * (len_a - len_b) + b
        else:
            a = '0' * (len_b - len_a) + a

        try:
            for i in range(max(len_a, len_b)):
                x = int(a[i], 16)
                y = int(b[i], 16)
                strr.append(hex(x & y)[2:])
            for i in range(len(strr)):
                if strr[i] != '0':
                    strr = strr[i:]
                    break
            self.textEdit_2.setText(''.join(strr))
        except:
            QMessageBox.warning(None, "Warning", "请输入十六进制数字")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    logical = Big_Num_Logical_Operation_runme()
    logical.show()
    sys.exit(app.exec_())

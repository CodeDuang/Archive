import sys
import time
from random import choice

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

from Elliptic_Operator import Get_Elliptic_Operator, SM2


class GetEllipticOperatorRunMe(QMainWindow, Get_Elliptic_Operator.Ui_MainWindow):
    def __init__(self):
        super(GetEllipticOperatorRunMe, self).__init__()
        self.setupUi(self)
        self.initt()
        self.setWindowTitle("椭圆曲线算子")

        # 禁止放大缩小窗口
        # self.setFixedSize(self.width(), self.height())  # 设置窗口固定大小
        # self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)  # 禁用放大按钮
        # self.setWindowFlags(self.windowFlags() & ~Qt.WindowMinimizeButtonHint)  # 禁用缩小按钮

    def initt(self):
        self.pushButton.clicked.connect(self.btn_encryption)  # 加密按钮
        self.pushButton_2.clicked.connect(self.btn_decrypt)  # 解密按钮

        # 获取相关数据
        print("此为算法第1部分，获取相关数据".center(100, '='))
        self.args = SM2.get_args()  # 获取椭圆曲线系统参数
        p, a, b, h, G, n = self.args  # 序列解包
        self.p, self.a, self.b, self.h, self.xG, self.yG, n = tuple(
            map(lambda a: hex(a)[2:], (p, a, b, h, G[0], G[1], n)))  # 将参数转换为十六进制串便于输出
        print("椭圆曲线系统所在素域的p是：", self.p)
        print("椭圆曲线系统的参数a是：", self.a)
        print("椭圆曲线系统的参数b是：", self.b)
        print("椭圆曲线系统的余因子h是：", self.h)
        print("椭圆曲线系统的基点G的横坐标xG是：", self.xG)
        print("椭圆曲线系统的基点G的纵坐标yG是：", self.yG)

        print("下面获取接收方B的公私钥")
        self.key_B = SM2.get_key()  # 设置消息接收方的公私钥
        PB, dB = self.key_B  # 序列解包，PB是公钥，是以元组形式存储的点(xB, yB), dB是私钥，是整数
        self.xB, self.yB, self.dB = tuple(map(lambda a: hex(a)[2:], (PB[0], PB[1], dB)))
        print("接收方B的公钥PB的横坐标xB是：", self.xB)
        print("接收方B的公钥PB的纵坐标yB是：", self.yB)
        print("接收方B的私钥dB是：", self.dB)

    # 加密
    def btn_encryption(self):
        self.mouse_stop()
        print("下面获取明文")
        M = self.textEdit.toPlainText()
        print("获取的ascii字符串明文是：", M)
        print("此为算法第2部分，加密部分".center(100, '='))
        try:
            C = SM2.encry_sm2(self.args, self.key_B[0], M)  # 加密算法的参数是椭圆系统参数，B的公钥PB，ascii字符串形式的明文消息M。返回十六进制串形式的密文消息
        except:
            QMessageBox.warning(None, "Warning", "明文请输入ascii字符串！（不要有中文字符）")
            return
        # 将加密结果C显示在方框中
        self.textEdit_2.setText(C)

    def btn_decrypt(self):
        self.mouse_stop()
        print("此为算法第3部分，解密部分".center(100, '='))
        C = self.textEdit_2.toPlainText()
        try:
            de_M = SM2.decry_sm2(self.args, self.key_B[1], C)  # 解密算法的参数是椭圆曲线系统参数，B的私钥dB，十六进制串形式的密文消息。返回ascii字符串形式的明文消息M
        except:
            QMessageBox.warning(None, "Warning", "请输入正确密文！")
            return
        # 将解密结果de_M显示在方框中
        self.textEdit.setText(de_M)

    def mouse_stop(self, n=0, m=1):
        self.setCursor(QCursor(Qt.BusyCursor))  # FIXME:设置鼠标匆忙（用于延迟）
        QApplication.processEvents()  # 刷新面板
        time.sleep(choice([i/10 for i in range(n*10, m*10)]))
        self.setCursor(QCursor(Qt.ArrowCursor))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    count = GetEllipticOperatorRunMe()
    count.show()
    sys.exit(app.exec_())

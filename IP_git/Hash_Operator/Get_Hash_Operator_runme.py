import binascii
import sys
import time
from random import choice

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog

from Hash_Operator import Get_Hash_Operator

import hashlib, hmac


class GetHashOperatorRunMe(QMainWindow, Get_Hash_Operator.Ui_MainWindow):
    def __init__(self):
        super(GetHashOperatorRunMe, self).__init__()
        self.setupUi(self)
        self.initt()
        self.setWindowTitle("哈希函数算子")

        # # 禁止放大缩小窗口
        # self.setFixedSize(self.width(), self.height())  # 设置窗口固定大小
        # self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)  # 禁用放大按钮
        # self.setWindowFlags(self.windowFlags() & ~Qt.WindowMinimizeButtonHint)  # 禁用缩小按钮

    def initt(self):
        self.pushButton.clicked.connect(self.btn_make)  # 加密按钮
        self.pushButton_2.clicked.connect(self.btn_clear)  # 清空按钮
        self.pushButton_3.clicked.connect(self.btn_file)  # ...按钮


    def btn_make(self):
        # 判断是否会出现文件或文本为空
        if self.tabWidget.currentIndex() == 0:  # 文件
            try:
                with open(self.lineEdit.text(), 'rb') as f:
                    pass
                f.close()
                self.mouse_stop()
            except:
                QMessageBox.warning(None, "Warning", "请选择正确文件.")
                return
        else:
            text = self.textEdit.toPlainText().encode('utf-8')
            if len(text) == 0:
                QMessageBox.warning(None, "Warning", "请输入加密字符.")
                return


        # 判错完毕，开始实现相关功能
        text = self.comboBox.currentText()
        if text == "MD5":
            self.md5_make()
        elif text == "SHA-256":
            self.sha_make()
        elif text == "HMAC":
            self.hmac_make()
        else:
            QMessageBox.warning(None, "Warning", "未知的哈希函数算子.")

    # 清空按钮：清空消息框
    def btn_clear(self):
        self.textBrowser.clear()

    # ...按钮：选取文件，并显示出来
    def btn_file(self):
        filelist = QFileDialog.getOpenFileName(None, "选取加密文件", "./", "All Files(*)")
        if filelist[0] != '':
            print(filelist)  # 注意接收的filelist是一个二元组，不要搞错了
            self.lineEdit.setText(filelist[0])

    # md加密：首先判断是文件还是文本，然后分别将内容导入text变量并编码，最后用md5加密text
    def md5_make(self):
        md5 = hashlib.md5()  # 定义md5对象
        if self.tabWidget.currentIndex() == 0:  # 文件
            # text = self.lineEdit.text()
            with open(self.lineEdit.text(), 'rb') as f:
                text = f.read()
            f.close()
        else:  # 文本
            text = self.textEdit.toPlainText().encode('utf-8')
        # 加密
        md5.update(text)
        outt = md5.hexdigest()  # 加密结果传给outt
        self.textBrowser.setText(outt)  # 输出

    # SHA-256加密：
    def sha_make(self):
        sha256 = hashlib.sha256()  # 定义sha256对象
        if self.tabWidget.currentIndex() == 0:  # 文件
            # text = self.lineEdit.text()
            with open(self.lineEdit.text(), 'rb') as f:
                text = f.read()
            f.close()
        else:  # 文本
            text = self.textEdit.toPlainText().encode('utf-8')
        # 加密
        sha256.update(text)
        outt = sha256.hexdigest()  # 加密结果传给outt
        self.textBrowser.setText(outt)  # 输出

    def hmac_make(self):
        h1 = hmac.new(b'hash', digestmod='sha1')
        if self.tabWidget.currentIndex() == 0:  # 文件
            # text = self.lineEdit.text()
            with open(self.lineEdit.text(), 'rb') as f:
                text = f.read()
            f.close()
        else:  # 文本
            text = self.textEdit.toPlainText().encode('utf-8')
        # 加密
        h1.update(text)
        outt = h1.hexdigest()
        self.textBrowser.setText(outt)  # 输出

    def mouse_stop(self, n=0, m=1):
        self.setCursor(QCursor(Qt.BusyCursor))  # 设置鼠标匆忙（用于延迟）
        QApplication.processEvents()  # 刷新面板
        time.sleep(choice([i/10 for i in range(n*10, m*10)]))
        self.setCursor(QCursor(Qt.ArrowCursor))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    count = GetHashOperatorRunMe()
    count.show()
    sys.exit(app.exec_())

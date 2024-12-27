import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

from Help import BUG


class BUGRunMe(QMainWindow, BUG.Ui_MainWindow):
    def __init__(self):
        super(BUGRunMe, self).__init__()
        self.setupUi(self)
        self.initt()
        self.setWindowTitle("提交Bug")  # 设置标题

    def initt(self):
        self.pushButton.clicked.connect(self.btn_tijiao)
        self.pushButton_2.clicked.connect(self.close)

    def btn_tijiao(self):
        QMessageBox.information(self, u'提示消息', u'提交成功')
        self.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 初始化界面实例
    har = BUGRunMe()

    # 展示界面
    har.show()
    sys.exit(app.exec_())
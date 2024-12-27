import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget

from Help import About_EDA


class AboutEDARunMe(QMainWindow, About_EDA.Ui_MainWindow):
    def __init__(self):
        super(AboutEDARunMe, self).__init__()
        self.setupUi(self)
        self.initt()
        self.setWindowTitle("关于")  # 设置标题
        self.setFixedSize(self.width(), self.height())  # 禁止缩放
        # 隐藏边框
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)  # 隐藏边框并在其他边框之上
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置背景透明

    def initt(self):
        self.pushButton.clicked.connect(self.btn_close)
        self.center()  # 使得窗口出现在屏幕中心

    def btn_close(self):
        self.close()

    def center(self):
        # 获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标系
        size = self.geometry()
        newLeft = int((screen.width() - size.width()) / 2)
        newTop = int((screen.height() - size.height()) / 2)

        self.move(newLeft, newTop)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 初始化界面实例
    har = AboutEDARunMe()

    # 展示界面
    har.show()
    sys.exit(app.exec_())

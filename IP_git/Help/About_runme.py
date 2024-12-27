import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget

from Help import About


class AboutRunMe(QMainWindow, About.Ui_MainWindow):
    def __init__(self):
        super(AboutRunMe, self).__init__()
        self.setupUi(self)
        self.initt()
        self.setFixedSize(self.width(), self.height())  # 禁止缩放
        # 隐藏边框
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)  # 隐藏边框并在其他边框之上
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置背景透明

    def initt(self):
        self.pushButton.clicked.connect(self.close)
        self.center()  # 使得窗口出现在屏幕中心

    def center(self):
        # 获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标系
        size = self.geometry()
        newLeft = int((screen.width() - size.width()) / 2)
        newTop = int((screen.height() - size.height()) / 2)

        self.move(newLeft, newTop)


if __name__ == "__main__":
    ######使用下面的方式一定程度上可以解决界面模糊问题--解决电脑缩放比例问题
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    # 解决图片在不同分辨率显示模糊问题
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    # 定义页面对象
    loadd = AboutRunMe()

    loadd.show()
    sys.exit(app.exec_())

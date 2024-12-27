import sys

from PyQt5 import Qt
from PyQt5.QtWidgets import QMainWindow, QTabWidget, QApplication, QWidget, QHBoxLayout, QLabel, QTabBar

from Help import help_doc, Know


class KnowRunMe(QMainWindow, Know.Ui_MainWindow):
    def __init__(self):
        super(KnowRunMe, self).__init__()
        self.setupUi(self)
        self.initt()
        self.setWindowTitle("了解文档")  # 设置标题
        # self.setFixedSize(self.width(), self.height())  # 禁止缩放

    def initt(self):
        for i in range(16):
            self.tabWidget.setTabVisible(i, False)  # 隐藏标签

        # 按钮绑定槽函数
        self.pushButton_2.clicked.connect(self.btn_about_EDA)  # 了解IP核
        self.pushButton.clicked.connect(self.btn_about_Trojan)  # 了解哈希函数算子
        self.pushButton_5.clicked.connect(self.btn_about_Fault)  # 了解随机数生成
        self.pushButton_8.clicked.connect(self.btn_about_AnalysisOfSide)  # 了解大数运算单元
        self.pushButton_11.clicked.connect(self.btn_about_Layout)  # 了解椭圆曲线算子

        self.tabWidget.setCurrentIndex(0)  # 初始置为第一页

    def btn_about_EDA(self):
        self.label.setText("了解IP核")
        self.tabWidget.setCurrentIndex(0)
        # self.pushButton_2.setChecked(False)
        self.pushButton.setChecked(False)
        self.pushButton_5.setChecked(False)
        self.pushButton_8.setChecked(False)
        self.pushButton_11.setChecked(False)

    def btn_about_Trojan(self):
        self.label.setText("了解哈希函数算子")
        self.tabWidget.setCurrentIndex(1)
        self.pushButton_2.setChecked(False)
        # self.pushButton.setChecked(False)
        self.pushButton_5.setChecked(False)
        self.pushButton_8.setChecked(False)
        self.pushButton_11.setChecked(False)

    def btn_about_Fault(self):
        self.label.setText("了解随机数生成")
        self.tabWidget.setCurrentIndex(2)
        self.pushButton_2.setChecked(False)
        self.pushButton.setChecked(False)
        # self.pushButton_5.setChecked(False)
        self.pushButton_8.setChecked(False)
        self.pushButton_11.setChecked(False)

    def btn_about_AnalysisOfSide(self):
        self.label.setText("了解大数运算单元")
        self.tabWidget.setCurrentIndex(3)
        self.pushButton_2.setChecked(False)
        self.pushButton.setChecked(False)
        self.pushButton_5.setChecked(False)
        # self.pushButton_8.setChecked(False)
        self.pushButton_11.setChecked(False)

    def btn_about_Layout(self):
        self.label.setText("了解椭圆曲线算子")
        self.tabWidget.setCurrentIndex(4)
        self.pushButton_2.setChecked(False)
        self.pushButton.setChecked(False)
        self.pushButton_5.setChecked(False)
        self.pushButton_8.setChecked(False)
        # self.pushButton_11.setChecked(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 初始化界面实例
    har = KnowRunMe()

    # 展示界面
    har.show()
    sys.exit(app.exec_())

import sys

from PyQt5 import Qt
from PyQt5.QtWidgets import QMainWindow, QTabWidget, QApplication, QWidget, QHBoxLayout, QLabel, QTabBar

from Help import help_doc


class HelpRunMe(QMainWindow, help_doc.Ui_MainWindow):
    def __init__(self):
        super(HelpRunMe, self).__init__()
        self.setupUi(self)
        self.initt()
        self.setWindowTitle("帮助文档")  # 设置标题
        # self.setFixedSize(self.width(), self.height())  # 禁止缩放

    def initt(self):
        for i in range(16):
            self.tabWidget.setTabVisible(i, False)  # 隐藏标签

        # 按钮绑定槽函数
        self.pushButton_2.clicked.connect(self.btn_about_EDA)  # 哈希函数算子使用指南
        self.pushButton.clicked.connect(self.btn_about_Trojan)  # 随机数生成使用指南
        self.pushButton_5.clicked.connect(self.btn_about_Fault)  # 大数运算单元使用指南
        self.pushButton_8.clicked.connect(self.btn_about_AnalysisOfSide)  # 椭圆曲线算子使用指南

        self.tabWidget.setCurrentIndex(0) #初始置为第一页

    def btn_about_EDA(self):
        self.label.setText("哈希函数算子使用指南")
        self.tabWidget.setCurrentIndex(0)
        # self.pushButton_2.setChecked(False)
        self.pushButton.setChecked(False)
        self.pushButton_5.setChecked(False)
        self.pushButton_8.setChecked(False)



    def btn_about_Trojan(self):
        self.label.setText("随机数生成使用指南")
        self.tabWidget.setCurrentIndex(1)
        self.pushButton_2.setChecked(False)
        # self.pushButton.setChecked(False)
        self.pushButton_5.setChecked(False)
        self.pushButton_8.setChecked(False)


    def btn_about_Fault(self):
        self.label.setText("大数运算单元使用指南")
        self.tabWidget.setCurrentIndex(2)
        self.pushButton_2.setChecked(False)
        self.pushButton.setChecked(False)
        # self.pushButton_5.setChecked(False)
        self.pushButton_8.setChecked(False)


    def btn_about_AnalysisOfSide(self):
        self.label.setText("椭圆曲线算子使用指南")
        self.tabWidget.setCurrentIndex(3)
        self.pushButton_2.setChecked(False)
        self.pushButton.setChecked(False)
        self.pushButton_5.setChecked(False)
        # self.pushButton_8.setChecked(False)





if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 初始化界面实例
    har = HelpRunMe()

    # 展示界面
    har.show()
    sys.exit(app.exec_())

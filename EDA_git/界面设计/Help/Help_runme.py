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
        self.pushButton_2.clicked.connect(self.btn_about_EDA)  # 关于EDA
        self.pushButton.clicked.connect(self.btn_about_Trojan)  # 关于硬件木马分析
        self.pushButton_5.clicked.connect(self.btn_about_Fault)  # 关于故障注入
        self.pushButton_8.clicked.connect(self.btn_about_AnalysisOfSide)  # 关于侧信道泄露分析
        self.pushButton_11.clicked.connect(self.btn_about_Layout)  # 关于版图安全
        self.pushButton_14.clicked.connect(self.btn_about_Algorithm)  # 关于算法门限安全
        # ----------------------------------------------------------------------------
        self.pushButton_3.clicked.connect(self.btn_gn_Trojan)  # 硬件木马分析功能介绍
        self.pushButton_4.clicked.connect(self.btn_sy_Trojan)  # 硬件木马分析使用指南
        self.pushButton_6.clicked.connect(self.btn_gn_Fault)  # 故障注入功能介绍
        self.pushButton_7.clicked.connect(self.btn_sy_Fault)  # 故障注入使用指南
        self.pushButton_9.clicked.connect(self.btn_gn_AnalysisOfSide)  # 侧信道泄露分析功能介绍
        self.pushButton_10.clicked.connect(self.btn_sy_AnalysisOfSide)  # 侧信道泄露分析使用指南
        self.pushButton_12.clicked.connect(self.btn_gn_Layout)  # 版图安全功能介绍
        self.pushButton_13.clicked.connect(self.btn_sy_Layout)  # 版图安全使用指南
        self.pushButton_15.clicked.connect(self.btn_gn_Algorithm)  # 算法门限安全功能介绍
        self.pushButton_16.clicked.connect(self.btn_sy_Algorithm)  # 算法门限安全使用指南

        self.tabWidget.setCurrentIndex(0) #初始置为第一页

    def btn_about_EDA(self):
        self.label.setText("关于EDA")
        self.tabWidget.setCurrentIndex(0)
        # self.pushButton_2.setChecked(False)
        self.pushButton.setChecked(False)
        self.pushButton_5.setChecked(False)
        self.pushButton_8.setChecked(False)
        self.pushButton_11.setChecked(False)
        self.pushButton_14.setChecked(False)
        self.pushButton_3.setChecked(False)
        self.pushButton_4.setChecked(False)
        self.pushButton_6.setChecked(False)
        self.pushButton_7.setChecked(False)
        self.pushButton_9.setChecked(False)
        self.pushButton_10.setChecked(False)
        self.pushButton_12.setChecked(False)
        self.pushButton_13.setChecked(False)
        self.pushButton_15.setChecked(False)
        self.pushButton_16.setChecked(False)


    def btn_about_Trojan(self):
        self.label.setText("关于硬件木马分析")
        self.tabWidget.setCurrentIndex(1)
        self.pushButton_2.setChecked(False)
        # self.pushButton.setChecked(False)
        self.pushButton_5.setChecked(False)
        self.pushButton_8.setChecked(False)
        self.pushButton_11.setChecked(False)
        self.pushButton_14.setChecked(False)
        self.pushButton_3.setChecked(False)
        self.pushButton_4.setChecked(False)
        self.pushButton_6.setChecked(False)
        self.pushButton_7.setChecked(False)
        self.pushButton_9.setChecked(False)
        self.pushButton_10.setChecked(False)
        self.pushButton_12.setChecked(False)
        self.pushButton_13.setChecked(False)
        self.pushButton_15.setChecked(False)
        self.pushButton_16.setChecked(False)

    def btn_about_Fault(self):
        self.label.setText("关于故障注入")
        self.tabWidget.setCurrentIndex(2)
        self.pushButton_2.setChecked(False)
        self.pushButton.setChecked(False)
        # self.pushButton_5.setChecked(False)
        self.pushButton_8.setChecked(False)
        self.pushButton_11.setChecked(False)
        self.pushButton_14.setChecked(False)
        self.pushButton_3.setChecked(False)
        self.pushButton_4.setChecked(False)
        self.pushButton_6.setChecked(False)
        self.pushButton_7.setChecked(False)
        self.pushButton_9.setChecked(False)
        self.pushButton_10.setChecked(False)
        self.pushButton_12.setChecked(False)
        self.pushButton_13.setChecked(False)
        self.pushButton_15.setChecked(False)
        self.pushButton_16.setChecked(False)

    def btn_about_AnalysisOfSide(self):
        self.label.setText("关于侧信道泄露分析")
        self.tabWidget.setCurrentIndex(3)
        self.pushButton_2.setChecked(False)
        self.pushButton.setChecked(False)
        self.pushButton_5.setChecked(False)
        # self.pushButton_8.setChecked(False)
        self.pushButton_11.setChecked(False)
        self.pushButton_14.setChecked(False)
        self.pushButton_3.setChecked(False)
        self.pushButton_4.setChecked(False)
        self.pushButton_6.setChecked(False)
        self.pushButton_7.setChecked(False)
        self.pushButton_9.setChecked(False)
        self.pushButton_10.setChecked(False)
        self.pushButton_12.setChecked(False)
        self.pushButton_13.setChecked(False)
        self.pushButton_15.setChecked(False)
        self.pushButton_16.setChecked(False)

    def btn_about_Layout(self):
        self.label.setText("关于版图安全")
        self.tabWidget.setCurrentIndex(4)
        self.pushButton_2.setChecked(False)
        self.pushButton.setChecked(False)
        self.pushButton_5.setChecked(False)
        self.pushButton_8.setChecked(False)
        # self.pushButton_11.setChecked(False)
        self.pushButton_14.setChecked(False)
        self.pushButton_3.setChecked(False)
        self.pushButton_4.setChecked(False)
        self.pushButton_6.setChecked(False)
        self.pushButton_7.setChecked(False)
        self.pushButton_9.setChecked(False)
        self.pushButton_10.setChecked(False)
        self.pushButton_12.setChecked(False)
        self.pushButton_13.setChecked(False)
        self.pushButton_15.setChecked(False)
        self.pushButton_16.setChecked(False)

    def btn_about_Algorithm(self):
        self.label.setText("关于算法门限安全")
        self.tabWidget.setCurrentIndex(5)
        self.pushButton_2.setChecked(False)
        self.pushButton.setChecked(False)
        self.pushButton_5.setChecked(False)
        self.pushButton_8.setChecked(False)
        self.pushButton_11.setChecked(False)
        # self.pushButton_14.setChecked(False)
        self.pushButton_3.setChecked(False)
        self.pushButton_4.setChecked(False)
        self.pushButton_6.setChecked(False)
        self.pushButton_7.setChecked(False)
        self.pushButton_9.setChecked(False)
        self.pushButton_10.setChecked(False)
        self.pushButton_12.setChecked(False)
        self.pushButton_13.setChecked(False)
        self.pushButton_15.setChecked(False)
        self.pushButton_16.setChecked(False)

    # _____________________________________________
    def btn_gn_Trojan(self):
        self.label.setText("硬件木马分析功能介绍")
        self.tabWidget.setCurrentIndex(6)
        self.pushButton_2.setChecked(False)
        self.pushButton.setChecked(False)
        self.pushButton_5.setChecked(False)
        self.pushButton_8.setChecked(False)
        self.pushButton_11.setChecked(False)
        self.pushButton_14.setChecked(False)
        # self.pushButton_3.setChecked(False)
        self.pushButton_4.setChecked(False)
        self.pushButton_6.setChecked(False)
        self.pushButton_7.setChecked(False)
        self.pushButton_9.setChecked(False)
        self.pushButton_10.setChecked(False)
        self.pushButton_12.setChecked(False)
        self.pushButton_13.setChecked(False)
        self.pushButton_15.setChecked(False)
        self.pushButton_16.setChecked(False)

    def btn_sy_Trojan(self):
        self.label.setText("硬件木马分析使用指南")
        self.tabWidget.setCurrentIndex(7)
        self.pushButton_2.setChecked(False)
        self.pushButton.setChecked(False)
        self.pushButton_5.setChecked(False)
        self.pushButton_8.setChecked(False)
        self.pushButton_11.setChecked(False)
        self.pushButton_14.setChecked(False)
        self.pushButton_3.setChecked(False)
        # self.pushButton_4.setChecked(False)
        self.pushButton_6.setChecked(False)
        self.pushButton_7.setChecked(False)
        self.pushButton_9.setChecked(False)
        self.pushButton_10.setChecked(False)
        self.pushButton_12.setChecked(False)
        self.pushButton_13.setChecked(False)
        self.pushButton_15.setChecked(False)
        self.pushButton_16.setChecked(False)

    def btn_gn_Fault(self):
        self.label.setText("故障注入功能介绍")
        self.tabWidget.setCurrentIndex(8)
        self.pushButton_2.setChecked(False)
        self.pushButton.setChecked(False)
        self.pushButton_5.setChecked(False)
        self.pushButton_8.setChecked(False)
        self.pushButton_11.setChecked(False)
        self.pushButton_14.setChecked(False)
        self.pushButton_3.setChecked(False)
        self.pushButton_4.setChecked(False)
        # self.pushButton_6.setChecked(False)
        self.pushButton_7.setChecked(False)
        self.pushButton_9.setChecked(False)
        self.pushButton_10.setChecked(False)
        self.pushButton_12.setChecked(False)
        self.pushButton_13.setChecked(False)
        self.pushButton_15.setChecked(False)
        self.pushButton_16.setChecked(False)

    def btn_sy_Fault(self):
        self.label.setText("故障注入使用指南")
        self.tabWidget.setCurrentIndex(9)
        self.pushButton_2.setChecked(False)
        self.pushButton.setChecked(False)
        self.pushButton_5.setChecked(False)
        self.pushButton_8.setChecked(False)
        self.pushButton_11.setChecked(False)
        self.pushButton_14.setChecked(False)
        self.pushButton_3.setChecked(False)
        self.pushButton_4.setChecked(False)
        self.pushButton_6.setChecked(False)
        # self.pushButton_7.setChecked(False)
        self.pushButton_9.setChecked(False)
        self.pushButton_10.setChecked(False)
        self.pushButton_12.setChecked(False)
        self.pushButton_13.setChecked(False)
        self.pushButton_15.setChecked(False)
        self.pushButton_16.setChecked(False)

    def btn_gn_AnalysisOfSide(self):
        self.label.setText("侧信道泄露分析功能介绍")
        self.tabWidget.setCurrentIndex(10)
        self.pushButton_2.setChecked(False)
        self.pushButton.setChecked(False)
        self.pushButton_5.setChecked(False)
        self.pushButton_8.setChecked(False)
        self.pushButton_11.setChecked(False)
        self.pushButton_14.setChecked(False)
        self.pushButton_3.setChecked(False)
        self.pushButton_4.setChecked(False)
        self.pushButton_6.setChecked(False)
        self.pushButton_7.setChecked(False)
        # self.pushButton_9.setChecked(False)
        self.pushButton_10.setChecked(False)
        self.pushButton_12.setChecked(False)
        self.pushButton_13.setChecked(False)
        self.pushButton_15.setChecked(False)
        self.pushButton_16.setChecked(False)

    def btn_sy_AnalysisOfSide(self):
        self.label.setText("侧信道泄露分析使用指南")
        self.tabWidget.setCurrentIndex(11)
        self.pushButton_2.setChecked(False)
        self.pushButton.setChecked(False)
        self.pushButton_5.setChecked(False)
        self.pushButton_8.setChecked(False)
        self.pushButton_11.setChecked(False)
        self.pushButton_14.setChecked(False)
        self.pushButton_3.setChecked(False)
        self.pushButton_4.setChecked(False)
        self.pushButton_6.setChecked(False)
        self.pushButton_7.setChecked(False)
        self.pushButton_9.setChecked(False)
        # self.pushButton_10.setChecked(False)
        self.pushButton_12.setChecked(False)
        self.pushButton_13.setChecked(False)
        self.pushButton_15.setChecked(False)
        self.pushButton_16.setChecked(False)

    def btn_gn_Layout(self):
        self.label.setText("版图安全功能介绍")
        self.tabWidget.setCurrentIndex(12)
        self.pushButton_2.setChecked(False)
        self.pushButton.setChecked(False)
        self.pushButton_5.setChecked(False)
        self.pushButton_8.setChecked(False)
        self.pushButton_11.setChecked(False)
        self.pushButton_14.setChecked(False)
        self.pushButton_3.setChecked(False)
        self.pushButton_4.setChecked(False)
        self.pushButton_6.setChecked(False)
        self.pushButton_7.setChecked(False)
        self.pushButton_9.setChecked(False)
        self.pushButton_10.setChecked(False)
        # self.pushButton_12.setChecked(False)
        self.pushButton_13.setChecked(False)
        self.pushButton_15.setChecked(False)
        self.pushButton_16.setChecked(False)

    def btn_sy_Layout(self):
        self.label.setText("版图安全使用指南")
        self.tabWidget.setCurrentIndex(13)
        self.pushButton_2.setChecked(False)
        self.pushButton.setChecked(False)
        self.pushButton_5.setChecked(False)
        self.pushButton_8.setChecked(False)
        self.pushButton_11.setChecked(False)
        self.pushButton_14.setChecked(False)
        self.pushButton_3.setChecked(False)
        self.pushButton_4.setChecked(False)
        self.pushButton_6.setChecked(False)
        self.pushButton_7.setChecked(False)
        self.pushButton_9.setChecked(False)
        self.pushButton_10.setChecked(False)
        self.pushButton_12.setChecked(False)
        # self.pushButton_13.setChecked(False)
        self.pushButton_15.setChecked(False)
        self.pushButton_16.setChecked(False)

    def btn_gn_Algorithm(self):
        self.label.setText("算法门限安全功能介绍")
        self.tabWidget.setCurrentIndex(14)
        self.pushButton_2.setChecked(False)
        self.pushButton.setChecked(False)
        self.pushButton_5.setChecked(False)
        self.pushButton_8.setChecked(False)
        self.pushButton_11.setChecked(False)
        self.pushButton_14.setChecked(False)
        self.pushButton_3.setChecked(False)
        self.pushButton_4.setChecked(False)
        self.pushButton_6.setChecked(False)
        self.pushButton_7.setChecked(False)
        self.pushButton_9.setChecked(False)
        self.pushButton_10.setChecked(False)
        self.pushButton_12.setChecked(False)
        self.pushButton_13.setChecked(False)
        # self.pushButton_15.setChecked(False)
        self.pushButton_16.setChecked(False)

    def btn_sy_Algorithm(self):
        self.label.setText("算法门限安全使用指南")
        self.tabWidget.setCurrentIndex(15)
        self.pushButton_2.setChecked(False)
        self.pushButton.setChecked(False)
        self.pushButton_5.setChecked(False)
        self.pushButton_8.setChecked(False)
        self.pushButton_11.setChecked(False)
        self.pushButton_14.setChecked(False)
        self.pushButton_3.setChecked(False)
        self.pushButton_4.setChecked(False)
        self.pushButton_6.setChecked(False)
        self.pushButton_7.setChecked(False)
        self.pushButton_9.setChecked(False)
        self.pushButton_10.setChecked(False)
        self.pushButton_12.setChecked(False)
        self.pushButton_13.setChecked(False)
        self.pushButton_15.setChecked(False)
        # self.pushButton_16.setChecked(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 初始化界面实例
    har = HelpRunMe()

    # 展示界面
    har.show()
    sys.exit(app.exec_())

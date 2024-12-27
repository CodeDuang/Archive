import sys
import time
from random import randint

from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import QSize, Qt, QTimer
from PyQt5.QtGui import QCursor, QGuiApplication, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMainWindow, QApplication, QListView, QFileDialog

from Algorithm_Threshold_Detection.Algorithm_Threshold_Detection_Main_runme import AlgorithmThresholdDetectionRunMe
from Analysis_Of_Side_Channel_Leakage.Channel_Analysis_runme import ChannelAnalysisRunMe
from Fault_Injection.EDA_runme import EDARunMe
from Help.About_EDA_runme import AboutEDARunMe
from Help.BUG_runme import BUGRunMe
from Help.Help_runme import HelpRunMe
from Layout_Security_Check.LayoutSecurityCheck_runme import LayoutSecurityCheckRunMe
from Trojan_Analysis import HardwareTrojan_runme, InputData_runme
from Fault_Injection import EDA_runme, HDL_runme, Fault_Configuration_runme
from Analysis_Of_Side_Channel_Leakage import Channel_Analysis_runme
import All_Start
from Algorithm_Threshold_Detection import Algorithm_Threshold_Detection_Main_runme, Algorithm_Threshold_Detection_Main, \
    Setting_runme, Setting
from Layout_Security_Check import LayoutSecurityCheck_runme, LayoutSecurityCheck

from Report import report, report_runme, report_injection, report_injection_runme
from Load.Loading_runme import LoadingRunMe, WorkerThread
from Trojan_Analysis.HardwareTrojan_runme import HardwareTrojanRunMe


class AllStartRunMe(QMainWindow, All_Start.Ui_MainWindow):
    def __init__(self):
        super(AllStartRunMe, self).__init__()
        self.setupUi(self)
        self.initt()
        self.setWindowTitle("安全芯片EDA设计工具")  # 设置标题
        # self.setFixedSize(self.width(), self.height())  # 禁止缩放

    # 点击右上角叉叉触发事件
    def closeEvent(self, event):  # 函数名固定不可变
        about_EDA.close()  # 注意需要确保关于界面是关闭的
        reply = QtWidgets.QMessageBox.question(self, u'警告', u'确认关闭软件?', QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)
        # QtWidgets.QMessageBox.question(self,u'弹窗名',u'弹窗内容',选项1,选项2)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()  # 关闭窗口
        else:
            event.ignore()  # 忽视点击X事件

    def initt(self):
        self.tabWidget_2.setTabBarAutoHide(True)
        self.pushButton_7.clicked.connect(self.btn_fault_injection)  # 故障注入工具
        # self.pushButton.setIcon(QtGui.QIcon('fault_injection.png'))
        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))
        # self.pushButton.setIconSize(QSize(70, 70))

        self.pushButton_8.clicked.connect(self.btn_analysis_of_side_channel_leakage)  # 侧行道泄露分析
        # self.pushButton_2.setIcon(QtGui.QIcon('analysis_of_side.png'))
        self.pushButton_8.setCursor(QCursor(Qt.PointingHandCursor))
        # self.pushButton_2.setIconSize(QSize(75, 75))

        self.pushButton_6.clicked.connect(self.btn_trojan_analysis)  # 硬件木马分析
        # self.pushButton_3.setIcon(QtGui.QIcon('trojan_analysis.png'))
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        # self.pushButton_3.setIconSize(QSize(70, 70))

        self.pushButton_9.clicked.connect(self.btn_layout_security_check)  # 版图安全检测
        # self.pushButton_4.setIcon(QtGui.QIcon('Layout_Security_Check.png'))
        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        # self.pushButton_4.setIconSize(QSize(80, 80))

        self.pushButton_18.clicked.connect(self.btn_algorithm_threshold_detection)  # 算法门限检测
        # self.pushButton_5.setIcon(QtGui.QIcon('算法门限检测.png'))
        self.pushButton_18.setCursor(QCursor(Qt.PointingHandCursor))
        # self.pushButton_5.setIconSize(QSize(70, 70))

        self.pushButton_14.clicked.connect(self.btn_sidebar_visitable)  # 侧边栏隐藏
        self.pushButton_17.clicked.connect(self.menu_action_help)  # 帮助

        self.action.triggered.connect(self.menu_action_about_EDA)  # 菜单:帮助-关于
        self.action_9.triggered.connect(self.menu_action_help)  # 菜单：帮助-文档
        self.action_7.triggered.connect(self.btn_sidebar_change_visitable)  # 侧边栏状态切换
        self.action_4.triggered.connect(self.menu_action_changeViewTo_AnalysisOfSide)  # Channel Analysis
        self.action_3.triggered.connect(self.menu_action_changeViewTo_Fault)  # Fault Injection
        self.action_5.triggered.connect(self.menu_action_changeViewTo_Layout)  # Layout Security Check
        self.action_2.triggered.connect(self.menu_action_changeViewTo_Trojan)  # Trojan Analysis
        self.action_6.triggered.connect(self.menu_action_changeViewTo_Algorithm)  # Algorithm Threshold Detection
        self.action_14.triggered.connect(self.menu_action_close)  # 退出
        self.action_16.triggered.connect(self.menu_action_mini)  # 最小化
        self.action_12.triggered.connect(self.showMaximized)  # 最大化
        self.action_26.triggered.connect(self.showNormal)  # 正常化
        self.action_19.triggered.connect(self.menubar.hide)  # 隐藏菜单栏
        self.pushButton.clicked.connect(self.menubar.show)  # 显示菜单栏
        self.action_20.triggered.connect(self.menu_action_easy_0)  # easy to use-故障注入工具
        self.action_21.triggered.connect(self.menu_action_easy_1)  # easy to use-侧信道泄露分析
        self.action_22.triggered.connect(self.menu_action_easy_2)  # easy to use-...
        self.action_23.triggered.connect(self.menu_action_easy_3)  # easy to use-...
        self.action_24.triggered.connect(self.menu_action_easy_4)  # easy to use-...
        self.action_BUG.triggered.connect(self.menu_action_BUG)  # 提交BUG
        self.action_25.triggered.connect(self.menu_action_preferences)  # 偏好设置
        self.action_28.triggered.connect(self.menu_action_changelog)  # 修改日志

        # self.action_8.triggered.connect(self.open_file)  # 打开文件

        # self.model = QStandardItemModel()
        # # self.model.appendRow(QStandardItem("123"))
        # self.listView.setModel(self.model)
        # self.listView.setEditTriggers(QListView.NoEditTriggers)  # 设置元素为只读

        self.toolBox.currentChanged.connect(self.on_current_changed)  # toolBox监听

    def menu_action_changelog(self):
        # 打开文件夹 并选择指定文件
        import os
        os.system(r"explorer /open,changelog.txt")

    def menu_action_preferences(self):
        # 打开文件夹 并选择指定文件
        import os
        os.system(r"explorer /open,Preferences.txt")

    def menu_action_BUG(self):
        self.bug = BUGRunMe()
        self.bug.show()

    def on_current_changed(self, a=-1):
        if a == -1:
            a = self.toolBox.currentIndex()
        if a == 0:
            self.toolBox.setItemText(0, "▾ 故障注入工具")
            self.toolBox.setItemText(1, "▸ 侧信道泄露分析")
            self.toolBox.setItemText(2, "▸ 算法门限检测")
            self.toolBox.setItemText(3, "▸ 版图安全检验")
            self.toolBox.setItemText(4, "▸ 硬件木马分析")
        elif a == 1:
            self.toolBox.setItemText(0, "▸ 故障注入工具")
            self.toolBox.setItemText(1, "▾ 侧信道泄露分析")
            self.toolBox.setItemText(2, "▸ 算法门限检测")
            self.toolBox.setItemText(3, "▸ 版图安全检验")
            self.toolBox.setItemText(4, "▸ 硬件木马分析")
        elif a == 2:
            self.toolBox.setItemText(0, "▸ 故障注入工具")
            self.toolBox.setItemText(1, "▸ 侧信道泄露分析")
            self.toolBox.setItemText(2, "▾ 算法门限检测")
            self.toolBox.setItemText(3, "▸ 版图安全检验")
            self.toolBox.setItemText(4, "▸ 硬件木马分析")
        elif a == 3:
            self.toolBox.setItemText(0, "▸ 故障注入工具")
            self.toolBox.setItemText(1, "▸ 侧信道泄露分析")
            self.toolBox.setItemText(2, "▸ 算法门限检测")
            self.toolBox.setItemText(3, "▾ 版图安全检验")
            self.toolBox.setItemText(4, "▸ 硬件木马分析")
        elif a == 4:
            self.toolBox.setItemText(0, "▸ 故障注入工具")
            self.toolBox.setItemText(1, "▸ 侧信道泄露分析")
            self.toolBox.setItemText(2, "▸ 算法门限检测")
            self.toolBox.setItemText(3, "▸ 版图安全检验")
            self.toolBox.setItemText(4, "▾ 硬件木马分析")

    def btn_sidebar_change_visitable(self):
        if self.action_7.isChecked():
            self.tabWidget.setVisible(True)
        else:
            self.tabWidget.setVisible(False)

    def btn_sidebar_visitable(self):
        self.action_7.setChecked(False)
        self.tabWidget.setVisible(False)

    def btn_fault_injection(self):
        # self.eda = EDA_runme.EDARunMe()  # 故障注入界面
        self.eda = Fault()
        self.eda.show()
        self.hide()

    def btn_trojan_analysis(self):
        # self.har = HardwareTrojan_runme.HardwareTrojanRunMe()  # 硬件木马分析界面
        self.har = Trojan()
        self.har.show()
        self.hide()

    def btn_analysis_of_side_channel_leakage(self):
        # self.cha = Channel_Analysis_runme.ChannelAnalysisRunMe()  # 侧行道泄露分析界面
        self.cha = AnalysisOfSide()
        self.cha.show()
        self.hide()

    def btn_layout_security_check(self):
        # self.layoutt = LayoutSecurityCheck_runme.LayoutSecurityCheckRunMe()
        self.layoutt = LayoutSecurity()
        self.layoutt.show()
        self.hide()

    def btn_algorithm_threshold_detection(self):
        # self.alg = Algorithm_Threshold_Detection_Main_runme.AlgorithmThresholdDetectionRunMe()  # 算法门限检测
        self.alg = Algorithm()
        self.alg.show()
        self.hide()

    def menu_action_about_EDA(self):
        about_EDA.show()

    def menu_action_help(self):
        help_doc.show()

    def menu_action_changeViewTo_Algorithm(self):
        self.hide()
        alg.show()

    def menu_action_changeViewTo_Fault(self):
        self.hide()
        eda.show()

    def menu_action_changeViewTo_Layout(self):
        self.hide()
        layoutt.show()

    def menu_action_changeViewTo_Trojan(self):
        self.hide()
        har.show()

    def menu_action_changeViewTo_AnalysisOfSide(self):
        self.hide()
        cha.show()

    def menu_action_close(self):
        self.close()

    def menu_action_mini(self):
        self.showMinimized()

    def menu_action_easy_0(self):
        self.on_current_changed(0)
        self.toolBox.setCurrentIndex(0)

    def menu_action_easy_1(self):
        self.on_current_changed(1)
        self.toolBox.setCurrentIndex(1)

    def menu_action_easy_2(self):
        self.on_current_changed(2)
        self.toolBox.setCurrentIndex(2)

    def menu_action_easy_3(self):
        self.on_current_changed(3)
        self.toolBox.setCurrentIndex(3)

    def menu_action_easy_4(self):
        self.on_current_changed(4)
        self.toolBox.setCurrentIndex(4)


# 继承Loading.LoadingRunMe,以方便在该类中设置定时器，消失后调取主页面(复写了time_out())
class Loadd(LoadingRunMe):
    def __init__(self):
        super(Loadd, self).__init__()
        # self.time_out()

    def time_out(self):
        # 创建定时器，设置定时器的超时槽函数为关闭登录窗口和打开主页面的函数
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.close_and_open_main)
        # timee = randint(5000,10000)
        self.timer.start(1)  # 设置定时器的间隔为5000毫秒（5秒）

    def close_and_open_main(self):
        self.timer.stop()  # 停止定时器
        self.close()  # 关闭登录窗口
        # all_start = AllStartRunMe()  # 综合导航栏界面
        all_start.show()


# 侧信道分析新类(用于菜单切换界面)
class AnalysisOfSide(ChannelAnalysisRunMe):
    def __init__(self):
        super(AnalysisOfSide, self).__init__()

        # 绑定菜单槽函数
        self.actionAlgorithm_Threshold_Detection.triggered.connect(self.menu_action_changeViewTo_Algorithm)
        self.actionFault_Injection.triggered.connect(self.menu_action_changeViewTo_Fault)
        self.actionLayout_Security_Check.triggered.connect(self.menu_action_changeViewTo_Layout)
        self.actionTrojan_Analysis.triggered.connect(self.menu_action_changeViewTo_Trojan)
        self.action.triggered.connect(self.menu_action_changeViewTo_begin)

        self.actionChannel_Analysis.triggered.connect(self.menu_action_help_gn)
        self.actionChannel_Analysis_2.triggered.connect(self.menu_action_help_sy)
        self.action_EDA.triggered.connect(self.menu_action_about_EDA)
        self.action_Channel_Analysis.triggered.connect(self.menu_action_help_about)

        self.action_BUG.triggered.connect(self.menu_action_BUG)  # 提交BUG
        self.action_23.triggered.connect(self.menu_action_preferences)  # 偏好设置
        self.action_25.triggered.connect(self.menu_action_changelog)  # 修改日志

    def menu_action_changelog(self):
        # 打开文件夹 并选择指定文件
        import os
        os.system(r"explorer /open,changelog.txt")

    def menu_action_preferences(self):
        # 打开文件夹 并选择指定文件
        import os
        os.system(r"explorer /open,Preferences.txt")

    def menu_action_BUG(self):
        self.bug = BUGRunMe()
        self.bug.show()

    # 点击右上角叉叉触发事件
    def closeEvent(self, event):  # 函数名固定不可变
        self.menu_action_changeViewTo_begin()

    def menu_action_changeViewTo_Algorithm(self):
        self.hide()
        alg.show()

    def menu_action_changeViewTo_Fault(self):
        self.hide()
        eda.show()

    def menu_action_changeViewTo_Layout(self):
        self.hide()
        layoutt.show()

    def menu_action_changeViewTo_Trojan(self):
        self.hide()
        har.show()

    def menu_action_changeViewTo_begin(self):
        self.hide()
        all_start.show()

    def menu_action_help_gn(self):
        help_doc.show()

    def menu_action_help_sy(self):
        help_doc.show()

    def menu_action_help_about(self):
        help_doc.show()

    def menu_action_about_EDA(self):
        about_EDA.show()


# 算法门限新类(用于菜单切换界面)
class Algorithm(AlgorithmThresholdDetectionRunMe):
    def __init__(self):
        super(Algorithm, self).__init__()

        # 绑定菜单槽函数
        self.actionChannel_Analysis.triggered.connect(self.menu_action_changeViewTo_AnalysisOfSide)
        self.actionFault_Injection.triggered.connect(self.menu_action_changeViewTo_Fault)
        self.actionLayout_Security_Check.triggered.connect(self.menu_action_changeViewTo_Layout)
        self.actionTrojan_Analysis.triggered.connect(self.menu_action_changeViewTo_Trojan)
        self.action_3.triggered.connect(self.menu_action_changeViewTo_begin)

        self.actionChannel_Analysis_5.triggered.connect(self.menu_action_help_gn)
        self.actionChannel_Analysis_2.triggered.connect(self.menu_action_help_sy)
        self.action_EDA.triggered.connect(self.menu_action_about_EDA)
        self.action_Channel_Analysis.triggered.connect(self.menu_action_help_about)

        self.action_22.triggered.connect(self.menu_action_changelog)  # 修改日志
        self.action_24.triggered.connect(self.menu_action_preferences)  # 偏好设置
        self.action_BUG.triggered.connect(self.menu_action_BUG)  # 提交BUG

    def menu_action_changelog(self):
        # 打开文件夹 并选择指定文件
        import os
        os.system(r"explorer /open,changelog.txt")

    def menu_action_preferences(self):
        # 打开文件夹 并选择指定文件
        import os
        os.system(r"explorer /open,Preferences.txt")

    def menu_action_BUG(self):
        self.bug = BUGRunMe()
        self.bug.show()

    # 点击右上角叉叉触发事件
    def closeEvent(self, event):  # 函数名固定不可变
        self.menu_action_changeViewTo_begin()

    def menu_action_changeViewTo_AnalysisOfSide(self):
        self.hide()
        cha.show()

    def menu_action_changeViewTo_Fault(self):
        self.hide()
        eda.show()

    def menu_action_changeViewTo_Layout(self):
        self.hide()
        layoutt.show()

    def menu_action_changeViewTo_Trojan(self):
        self.hide()
        har.show()

    def menu_action_changeViewTo_begin(self):
        self.hide()
        all_start.show()

    def menu_action_help_gn(self):
        help_doc.show()

    def menu_action_help_sy(self):
        help_doc.show()

    def menu_action_help_about(self):
        help_doc.show()

    def menu_action_about_EDA(self):
        about_EDA.show()


# 故障注入新类(用于菜单切换界面)
class Fault(EDARunMe):
    def __init__(self):
        super(Fault, self).__init__()

        # 绑定菜单槽函数
        self.actionChannel_Analysis_3.triggered.connect(self.menu_action_changeViewTo_AnalysisOfSide)
        self.actionAlgorithm_Threshold_Detection.triggered.connect(self.menu_action_changeViewTo_Algorithm)
        self.actionLayout_Security_Check.triggered.connect(self.menu_action_changeViewTo_Layout)
        self.actionTrojan_Analysis.triggered.connect(self.menu_action_changeViewTo_Trojan)
        self.action_3.triggered.connect(self.menu_action_changeViewTo_begin)

        self.actionChannel_Analysis.triggered.connect(self.menu_action_help_gn)
        self.actionChannel_Analysis_2.triggered.connect(self.menu_action_help_sy)
        self.action_EDA.triggered.connect(self.menu_action_about_EDA)
        self.action_Channel_Analysis.triggered.connect(self.menu_action_help_about)

        self.action_BUG.triggered.connect(self.menu_action_BUG)  # 提交BUG
        self.action_22.triggered.connect(self.menu_action_preferences)  # 偏好设置
        self.action_24.triggered.connect(self.menu_action_changelog)  # 修改日志

    def menu_action_changelog(self):
        # 打开文件夹 并选择指定文件
        import os
        os.system(r"explorer /open,changelog.txt")

    def menu_action_preferences(self):
        # 打开文件夹 并选择指定文件
        import os
        os.system(r"explorer /open,Preferences.txt")

    def menu_action_BUG(self):
        self.bug = BUGRunMe()
        self.bug.show()

    # 点击右上角叉叉触发事件
    def closeEvent(self, event):  # 函数名固定不可变
        self.menu_action_changeViewTo_begin()

    # 写槽函数内容
    def menu_action_changeViewTo_AnalysisOfSide(self):
        self.hide()
        cha.show()

    def menu_action_changeViewTo_Algorithm(self):
        self.hide()
        alg.show()

    def menu_action_changeViewTo_Layout(self):
        self.hide()
        layoutt.show()

    def menu_action_changeViewTo_Trojan(self):
        self.hide()
        har.show()

    def menu_action_changeViewTo_begin(self):
        self.hide()
        all_start.show()

    def menu_action_help_gn(self):
        help_doc.show()

    def menu_action_help_sy(self):
        help_doc.show()

    def menu_action_help_about(self):
        help_doc.show()

    def menu_action_about_EDA(self):
        about_EDA.show()


# 版图安全新类(用于菜单切换界面)
class LayoutSecurity(LayoutSecurityCheckRunMe):
    def __init__(self):
        super(LayoutSecurity, self).__init__()

        # 绑定菜单槽函数
        self.actionChannel_Analysis_3.triggered.connect(self.menu_action_changeViewTo_AnalysisOfSide)
        self.actionAlgorithm_Threshold_Detection.triggered.connect(self.menu_action_changeViewTo_Algorithm)
        self.actionFault_Injection.triggered.connect(self.menu_action_changeViewTo_Fault)
        self.actionTrojan_Analysis.triggered.connect(self.menu_action_changeViewTo_Trojan)
        self.action_3.triggered.connect(self.menu_action_changeViewTo_begin)

        self.actionChannel_Analysis.triggered.connect(self.menu_action_help_gn)
        self.actionChannel_Analysis_2.triggered.connect(self.menu_action_help_sy)
        self.action_EDA.triggered.connect(self.menu_action_about_EDA)
        self.action_Channel_Analysis.triggered.connect(self.menu_action_help_about)

        self.action_BUG.triggered.connect(self.menu_action_BUG)  # 提交BUG
        self.action_22.triggered.connect(self.menu_action_preferences)  # 偏好设置
        self.action_24.triggered.connect(self.menu_action_changelog)  # 修改日志

    def menu_action_changelog(self):
        # 打开文件夹 并选择指定文件
        import os
        os.system(r"explorer /open,changelog.txt")

    def menu_action_preferences(self):
        # 打开文件夹 并选择指定文件
        import os
        os.system(r"explorer /open,Preferences.txt")

    def menu_action_BUG(self):
        self.bug = BUGRunMe()
        self.bug.show()

    # 点击右上角叉叉触发事件
    def closeEvent(self, event):  # 函数名固定不可变
        self.menu_action_changeViewTo_begin()

    def menu_action_changeViewTo_AnalysisOfSide(self):
        self.hide()
        cha.show()

    def menu_action_changeViewTo_Algorithm(self):
        self.hide()
        alg.show()

    def menu_action_changeViewTo_Fault(self):
        self.hide()
        eda.show()

    def menu_action_changeViewTo_Trojan(self):
        self.hide()
        har.show()

    def menu_action_changeViewTo_begin(self):
        self.hide()
        all_start.show()

    def menu_action_help_gn(self):
        help_doc.show()

    def menu_action_help_sy(self):
        help_doc.show()

    def menu_action_help_about(self):
        help_doc.show()

    def menu_action_about_EDA(self):
        about_EDA.show()


# 硬件木马分析新类(用于菜单切换界面)
class Trojan(HardwareTrojanRunMe):
    def __init__(self):
        super(Trojan, self).__init__()

        # 绑定菜单槽函数
        self.actionChannel_Analysis_3.triggered.connect(self.menu_action_changeViewTo_AnalysisOfSide)
        # 绑定菜单槽函数
        self.actionAlgorithm_Threshold_Detection.triggered.connect(self.menu_action_changeViewTo_Algorithm)
        self.actionFault_Injection.triggered.connect(self.menu_action_changeViewTo_Fault)
        self.actionLayout_Security_Check.triggered.connect(self.menu_action_changeViewTo_Layout)
        self.action_6.triggered.connect(self.menu_action_changeViewTo_begin)

        self.actionChannel_Analysis.triggered.connect(self.menu_action_help_gn)
        self.actionChannel_Analysis_2.triggered.connect(self.menu_action_help_sy)
        self.action_EDA.triggered.connect(self.menu_action_about_EDA)
        self.action_Channel_Analysis.triggered.connect(self.menu_action_help_about)

        self.action_BUG.triggered.connect(self.menu_action_BUG)  # 提交BUG
        self.action_23.triggered.connect(self.menu_action_preferences)  # 偏好设置
        self.action_25.triggered.connect(self.menu_action_changelog)  # 修改日志

    def menu_action_changelog(self):
        # 打开文件夹 并选择指定文件
        import os
        os.system(r"explorer /open,changelog.txt")

    def menu_action_preferences(self):
        # 打开文件夹 并选择指定文件
        import os
        os.system(r"explorer /open,Preferences.txt")

    def menu_action_BUG(self):
        self.bug = BUGRunMe()
        self.bug.show()

    # 点击右上角叉叉触发事件
    def closeEvent(self, event):  # 函数名固定不可变
        self.menu_action_changeViewTo_begin()

    def menu_action_changeViewTo_AnalysisOfSide(self):
        self.hide()
        cha.show()

    def menu_action_changeViewTo_Algorithm(self):
        self.hide()
        alg.show()

    def menu_action_changeViewTo_Fault(self):
        self.hide()
        eda.show()

    def menu_action_changeViewTo_Layout(self):
        self.hide()
        layoutt.show()

    def menu_action_changeViewTo_begin(self):
        self.hide()
        all_start.show()

    def menu_action_help_gn(self):
        help_doc.show()

    def menu_action_help_sy(self):
        help_doc.show()

    def menu_action_help_about(self):
        help_doc.show()

    def menu_action_about_EDA(self):
        about_EDA.show()


if __name__ == "__main__":
    ######使用下面的方式一定程度上可以解决界面模糊问题--解决电脑缩放比例问题
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    # # 适应高DPI设备
    # QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    # 解决图片在不同分辨率显示模糊问题
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app = QApplication(sys.argv)

    # 定义页面对象
    all_start = AllStartRunMe()  # 综合导航栏界面（要先声明）
    alg = Algorithm()  # TODO:确认是否要加这段用于菜单切换窗口，会导致窗口不更新
    cha = AnalysisOfSide()  # TODO:确认是否要加这段用于菜单切换窗口，会导致窗口不更新
    eda = Fault()  # TODO:确认是否要加这段用于菜单切换窗口，会导致窗口不更新
    layoutt = LayoutSecurity()  # TODO:确认是否要加这段用于菜单切换窗口，会导致窗口不更新
    har = Trojan()  # TODO:确认是否要加这段用于菜单切换窗口，会导致窗口不更新
    about_EDA = AboutEDARunMe()

    help_doc = HelpRunMe()
    loadd = Loadd()  # 加载页面
    loadd.show()
    # loadd.hide()

    # all_start.show()
    sys.exit(app.exec_())

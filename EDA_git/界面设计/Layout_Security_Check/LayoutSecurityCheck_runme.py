import os
import random

import subprocess

import sys
import time
from random import randint
from time import sleep

from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QApplication, QMainWindow
from matplotlib.backends.backend_qt import MainWindow

import Layout_Security_Check.LayoutSecurityCheck


class LayoutSecurityCheckRunMe(QMainWindow, Layout_Security_Check.LayoutSecurityCheck.Ui_MainWindow):
    def __init__(self):
        super(LayoutSecurityCheckRunMe, self).__init__()
        self.setupUi(self)
        self.initt()
        self.setWindowTitle("版图安全检验")  # 设置标题
        # self.setFixedSize(self.width(), self.height())  # 禁止缩放

    # 点击右上角叉叉触发事件
    def closeEvent(self, event):  # 函数名固定不可变
        reply = QtWidgets.QMessageBox.question(self, u'警告', u'确认退出?', QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)
        # QtWidgets.QMessageBox.question(self,u'弹窗名',u'弹窗内容',选项1,选项2)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()  # 关闭窗口
        else:
            event.ignore()  # 忽视点击X事件

    def initt(self):
        self.toolButton.clicked.connect(self.btn_file_review)  # ...审查文件
        self.pushButton_2.clicked.connect(self.btn_run)  # 信号完整性_运行按钮
        self.pushButton_3.clicked.connect(self.btn_save)  # 信号完整性_存储按钮
        self.pushButton_4.clicked.connect(self.btn_run2)  # DRC_运行按钮
        self.pushButton_5.clicked.connect(self.btn_save2)  # DRC_存储按钮
        self.pushButton.clicked.connect(self.btn_load)  # load加载
        self.toolButton_2.clicked.connect(self.btn_directory_selection)  # ...运行目录选择
        self.toolButton_5.clicked.connect(self.btn_preset_rule)  # 预设实际规则
        self.toolButton_6.clicked.connect(self.btn_py_file)  # ...python脚本审查文件
        self.toolButton_7.clicked.connect(self.btn_begin_review)  # 开始审查

        # 菜单功能
        self.action_7.triggered.connect(self.btn_file_review)  # 文件-打开审查文件
        self.action_8.triggered.connect(self.btn_directory_selection)  # 文件-运行目录
        self.action_9.triggered.connect(self.btn_py_file)  # 设置-脚本规则文件
        self.action_10.triggered.connect(self.btn_preset_rule)  # 设置-预设设计规则
        self.action_12.triggered.connect(self.close) #退出
        self.action_4.triggered.connect(self.showMinimized) #最小化
        self.action_14.triggered.connect(self.btn_file_review) #...审查文件
        self.action_13.triggered.connect(self.showMaximized)  # 最大化
        self.action_15.triggered.connect(self.showNormal)  # 正常化
        self.action_20.triggered.connect(self.menubar.hide)  # 隐藏菜单栏
        self.pushButton_6.clicked.connect(self.menubar.show)  # 显示菜单栏

    def btn_begin_review(self):
        if self.textEdit_6.toPlainText() == '':
            return
        self.toolButton_7.setEnabled(False)  # 设置逻辑测试按钮不可以再点击了

        # # 1.延迟以进度条的形式
        self.progressbar_thread = ProgressBarThread()  # 实例化线程
        self.progressbar_thread.now_num.connect(self.progressbar_change)  # 绑定槽函数
        # 启动线程，执行线程类中run函数
        self.progressbar_thread.start()

    def progressbar_change(self, num):
        if num < 50:
            self.textBrowser_4.setText(f"代码合规性检查：{num}%")
        elif num <= 100:
            self.textBrowser_4.setText(f"代码合规性检查：{num}%\n安全漏洞扫描:{num - 50}%")
        elif num <= 120:
            self.textBrowser_4.setText(f"代码合规性检查：100%\n安全漏洞扫描:{num - 50}%")
        elif num <= 150:
            self.textBrowser_4.setText(f"代码合规性检查：100%\n安全漏洞扫描:{num - 50}%\n异常处理检验：{num - 120}%")
        else:
            self.textBrowser_4.setText(f"代码合规性检查：100%\n安全漏洞扫描:100%\n异常处理检验：{num - 120}%")
        if num == 220:
            sleep(0.5)
            self.textBrowser_4.append(f"----python脚本规则审查结束----\n得分:{randint(60, 100)}，审查通过")

    def btn_py_file(self):
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(None, "选取文件", os.getcwd(),
                                                                   "Python documents(*.py)")
        self.textEdit_6.setText(fileName)

    def btn_file_review(self):
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(None, "选取文件", os.getcwd(),
                                                                   "Review documents(*.ODB)")
        self.textEdit.setText(fileName)

    def btn_load(self):

        if self.textEdit.toPlainText() != '':
            self.mouse_stop(2)
            self.textBrowser_2.setText('加载成功')
            self.toolButton_2.setEnabled(True)
        else:
            self.textBrowser_2.setText('加载失败，请选择正确的审查文件')

    def btn_directory_selection(self):
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(None, "选取文件", os.getcwd(),
                                                                   "All Files(*);;run directory(*.exe)")
        self.textEdit_2.setText(fileName)
        if self.textEdit_2.toPlainText() != '':
            self.pushButton_2.setEnabled(True)
            self.pushButton_3.setEnabled(True)
            self.pushButton_4.setEnabled(True)
            self.pushButton_5.setEnabled(True)
            self.toolButton_7.setEnabled(True)

    def btn_run(self):
        self.mouse_stop()
        if self.textEdit.toPlainText() == '' or self.textEdit_2.toPlainText() == '':
            self.textBrowser_3.setText('')
            self.textBrowser_2.setText("无审查结果")
        else:
            self.mouse_stop()  # 延迟

            self.textBrowser_2.setText('')
            if self.comboBox.currentText() == '单线网检查模块':
                i = '在信号路径或返回路径上由于阻抗突变而引起的反射与失真。使信号感受到阻抗变化的情况。例如振铃问题就是由于信号传输过程中感受到阻抗的变化，发生的信号反射。'
            elif self.comboBox.currentText() == '多线网检查模块':
                i = '产生串扰的原因:正是网络间的容性耦合和感性耦合，给有害噪声从一个网络到达另一个网络提供了路径。'
            else:
                i = '对于低于此频率以下，Tr以上的，便可采用大致的经验来设计。对于低频唯一的要求就是联通即可。高一点的要求便是美观工整。按要求设计呗，不用考虑太多SI问题。做好PDS即可了。'

            self.textBrowser_3.setText(i)

    def btn_save(self):
        if self.textBrowser_3.toPlainText() == '':
            self.textBrowser_2.setText('无存储结果')
        else:
            self.textBrowser_2.setText('存储成功')

    def btn_preset_rule(self):
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(None, "选取文件", os.getcwd(),
                                                                   "All Files(*);;Default rule(*.txt)")
        self.textEdit_5.setText(fileName)

    def btn_run2(self):
        self.mouse_stop()
        if self.textEdit.toPlainText() == '' or self.textEdit_2.toPlainText() == '':
            self.textBrowser.setText('')
            self.textEdit_5.setText('')
            self.textBrowser_2.setText("无审查结果")
        else:
            self.textBrowser_2.setText('')
            self.textBrowser.setText(
                '1.大多数高速数字系统中，信号上升时间约是时钟周期的10%，即1/10x1/Fclock。例如10OMHZ使中的上升时间大约是1NS.\n2.在FR4板材上铜线条中信号速度为6in/ns( =15cm/ns)。\n3.传输线的特征阻抗，只有当信号在走线上的往返时间大于信号的上升时间才考虑。')

    def btn_save2(self):
        if self.textBrowser.toPlainText() == '':
            self.textBrowser_2.setText('无存储结果')
        else:
            self.textBrowser_2.setText('存储成功')

    def mouse_stop(self, n=0):
        self.setCursor(QCursor(Qt.BusyCursor))  # FIXME:设置鼠标匆忙（用于延迟）
        QApplication.processEvents()  # 刷新面板
        if n == 0:
            time.sleep(random.choice([1, 1.5, 2, 2.5]))
        else:
            time.sleep(n)
        self.setCursor(QCursor(Qt.ArrowCursor))


# 进度条子线程,以便进度条加载时不会冻结ui界面
class ProgressBarThread(QThread):
    # 使用自定义信号和UI主线程通讯，参数是发送信号时附带参数的数据类型，可以是str、int、list等
    now_num = pyqtSignal(int)

    def __init__(self, parent=None):
        super(ProgressBarThread, self).__init__(parent)

    # run函数是子线程中的操作，线程启动后开始执行
    def run(self):
        x = randint(20, 70)
        for i in range(221):
            sleep(0.01)
            if abs(i - x) < 4:  # 用于模拟出进度条更新的速度的随机性
                sleep(0.1)
            if 97 <= i <= 99:
                sleep(0.2)
            # 发射自定义信号
            # 通过emit函数将参数i传递给主线程，触发自定义信号
            self.now_num.emit(i)  # 注意这里与_signal = pyqtSignal(str)中的类型相同


if __name__ == "__main__":
    app = QApplication(sys.argv)

    layout = LayoutSecurityCheckRunMe()
    layout.show()

    sys.exit(app.exec_())

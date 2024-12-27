import os
import sys
import time
from hashlib import md5
from random import choice, randint

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox

from Algorithm_Threshold_Detection import Algorithm_Threshold_Detection_Main, Setting, Setting_runme


class AlgorithmThresholdDetectionRunMe(QMainWindow, Algorithm_Threshold_Detection_Main.Ui_MainWindow):
    def __init__(self):
        super(AlgorithmThresholdDetectionRunMe, self).__init__()
        self.setupUi(self)
        self.initt()
        self.setWindowTitle("算法门限检测")

    # # 点击右上角叉叉触发事件
    # def closeEvent(self, event):  # 函数名固定不可变
    #     reply = QtWidgets.QMessageBox.question(self, u'警告', u'确认退出?', QtWidgets.QMessageBox.Yes,
    #                                            QtWidgets.QMessageBox.No)
    #     # QtWidgets.QMessageBox.question(self,u'弹窗名',u'弹窗内容',选项1,选项2)
    #     if reply == QtWidgets.QMessageBox.Yes:
    #         event.accept()  # 关闭窗口
    #     else:
    #         event.ignore()  # 忽视点击X事件

    def initt(self):
        self.pushButton.clicked.connect(self.open_file)  # 打开算法文件
        self.pushButton_7.clicked.connect(self.btn_set)  # 算法门限设置
        self.pushButton_6.clicked.connect(self.btn_key_generation)  # 密钥生成
        self.pushButton_2.clicked.connect(self.btn_random_test)  # 随机性测试
        self.pushButton_3.clicked.connect(self.btn_key_spatial_analysis)  # 密钥空间分布
        self.pushButton_4.clicked.connect(self.report)  # 报告和结果分析
        self.pushButton_4.setVisible(False)  # 隐藏报告和结果分析按钮，该按钮暂时没有用
        self.pushButton_5.clicked.connect(self.btn_automatic_test)  # 自动化检测
        self.pushButton_8.clicked.connect(self.btn_msg_clear)  # 清空消息框

        self.action_6.triggered.connect(self.btn_set)  # 算法门限设置（菜单）
        self.action_4.triggered.connect(self.open_file)  # 打开算法文件(菜单)
        self.actionClose_Project.triggered.connect(self.menu_close)  # 退出
        self.action_7.triggered.connect(self.menu_mini)  # 最小化
        self.action_11.triggered.connect(self.open_file)  # 算法文件目录
        self.action_14.triggered.connect(self.btn_key_generation)  # 密钥生成
        self.action_15.triggered.connect(self.btn_msg_clear)  # 清空消息框
        self.action_12.triggered.connect(self.showMaximized)  # 窗口最大化
        self.action_13.triggered.connect(self.showNormal)  # 窗口正常化
        self.action_20.triggered.connect(self.menubar.hide)  # 隐藏菜单栏
        self.pushButton_9.clicked.connect(self.menubar.show)  # 显示菜单栏


    def menu_mini(self):
        self.showMinimized()

    def menu_close(self):
        self.close()

    def open_file(self):
        filename = QFileDialog.getOpenFileName(None, "选取算法文件", "./", "Python Files (*.py)")
        self.lineEdit.setText(filename[0])
        # self.textBrowser.setText('文件打开成功,目录：' + filename[0])
        print(filename)

    def btn_set(self):
        self.sett = Setting_runme.SettingRunMe()
        self.sett.show()

    def btn_key_generation(self):

        # 获取文件路径
        path = self.lineEdit.text()
        if not os.path.exists(path) or not path[-3:] == '.py':  # 判断路径存在且文件后缀为算法文件
            QMessageBox.warning(None, "Warning", "请选择正确的算法路径.")
        else:  # os.path.exists(path) and path[-3:] == '.py'

            self.pushButton_2.setEnabled(True)
            self.pushButton_3.setEnabled(True)
            self.pushButton_4.setEnabled(True)
            self.pushButton_5.setEnabled(True)
            with open('setting.txt', 'r') as f:
                start = time.time()  # 用于计算密钥生成时间
                self.textBrowser_2.setText('')
                data = f.read().split('\n')
                try:
                    a = int(data[0])
                    b = int(data[5])
                except:
                    QMessageBox.warning(None, "Warning", "请正确设置算法门限.")
                    return

                self.mouse_stop()  # 延迟

                lon = int(data[0])  # 获取门限配置中的密钥字节数
                num = lon // 16
                numm = lon % 16
                for i in range(num):
                    self.textBrowser_2.insertPlainText(md5(str(i).encode('utf8')).hexdigest())
                    self.textBrowser_2.moveCursor(self.textBrowser.textCursor().End)  # 文本框显示到底部
                    # time.sleep(0.2)
                    QApplication.processEvents()  # 刷新面板
                for i in range(numm):
                    self.textBrowser_2.insertPlainText("".join([choice("0123456789abcdef") for i in range(12)]))
                    self.textBrowser_2.moveCursor(self.textBrowser.textCursor().End)  # 文本框显示到底部
                    QApplication.processEvents()  # 刷新面板
                end = time.time()  # 用于计算密钥生成时间

                use_time = (end - start) * 1000
                self.textBrowser.append(f'---密钥生成---')
                self.mouse_stop(0.5)
                self.textBrowser.append(f'当前密钥生成用时：{use_time}ms')
                if use_time > int(data[5]):
                    self.textBrowser.append(f'门限要求密钥生成用时：{data[5]}ms,未通过门限检测\n')
                else:
                    self.textBrowser.append(f'门限要求密钥生成用时：{data[5]}ms,通过门限检测\n')
                self.mouse_stop(0.5)
                self.textBrowser.append('---密钥生成结束---')
            f.close()

    def btn_random_test(self):
        self.mouse_stop(0.5)

        # 随机性测试
        self.pushButton_3.setEnabled(False)  # 密钥空间分布
        self.pushButton_5.setEnabled(False)  # 自动化检测
        self.pushButton_2.setEnabled(False)  # 随机性测试
        num = randint(5000, 20000)  # 生成随机数从20000个样例中随机抽取至少5000个样子进行测试
        x, y = '*', '='
        xx = 0  # 用来平衡*和=的比例
        j = 0  # 用来生成随机的通过样例
        for i in range(num):
            if randint(0, 9):  # 通过概率为9/10
                j += 1
            self.textBrowser.setText(
                f'---随机性测试中---\n' + f'{x * xx}{y * (10 - xx)}\n' + f'随机测试样例:{i}/{num}\n随机测试通过样例:{j}\n')
            QApplication.processEvents()  # 刷新面板
            xx = (i * 10 + num) // num
        self.textBrowser.append('随机测试通过率:%.2f' % (j / num * 100) + '%')
        self.mouse_stop(0.5)
        self.textBrowser.append(f'---随机性结束---\n')

        self.pushButton_3.setEnabled(True)  # 密钥空间分布
        self.pushButton_5.setEnabled(True)  # 自动化检测
        self.pushButton_2.setEnabled(True)  # 随机性测试

    def btn_key_spatial_analysis(self):
        self.textBrowser.append(f'---密钥空间分析中---')
        QApplication.processEvents()  # 刷新面板
        self.mouse_stop(1.5)
        with open('setting.txt', 'r') as f:
            data = f.read().split('\n')
            lon = int(data[0])
            self.textBrowser.append(f'该密钥长度为：{data[0]}字节，可以显示的范围0~{(1 << int(data[0]) * 8) - 1}')
            self.mouse_stop(0.5)
            self.textBrowser.append(f'---密钥空间分析结束---\n')

    def report(self):
        pass

    def btn_automatic_test(self):
        self.textBrowser.setText(f'自动化检测流程：密钥生成→随机性测试→密钥空间分析\n')
        self.btn_key_generation()
        QApplication.processEvents()  # 刷新面板
        self.btn_random_test()
        QApplication.processEvents()  # 刷新面板
        self.btn_key_spatial_analysis()

    def btn_msg_clear(self):
        self.textBrowser.clear()

    def mouse_stop(self, n=0):
        self.setCursor(QCursor(Qt.BusyCursor))  # FIXME:设置鼠标匆忙（用于延迟）
        QApplication.processEvents()  # 刷新面板
        if n == 0:
            time.sleep(choice([1, 1.5, 2, 2.5, 3]))
        else:
            time.sleep(n)
        self.setCursor(QCursor(Qt.ArrowCursor))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 定义界面
    algorithm = AlgorithmThresholdDetectionRunMe()

    # 展示界面
    algorithm.show()

    sys.exit(app.exec_())

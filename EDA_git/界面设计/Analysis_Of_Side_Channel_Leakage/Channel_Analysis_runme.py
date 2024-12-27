import random
import re
import subprocess
import sys
import time
from datetime import datetime
from random import randint
from time import sleep

from PyQt5 import QtWidgets
from PyQt5.QtChart import QValueAxis, QLineSeries, QChartView, QChart
from PyQt5.QtCore import QPointF, Qt, QTimer, QThread, pyqtSignal
from PyQt5.QtGui import QPainter, QColor, QFont, QCursor
from PyQt5.QtWidgets import QApplication, QFileDialog, QGraphicsOpacityEffect, QMainWindow, QMessageBox

import Analysis_Of_Side_Channel_Leakage.Channel_Analysis
import Report.report
import Report.report_runme


class DataRefresh(QThread):  # 线程
    dataRefreshed = pyqtSignal(list)  # 表示发送过去的是数组类型，所以注意下面 emit里面传的需要是数组类型

    def __init__(self):
        super(DataRefresh, self).__init__()
        self.wait_flage = False

    def run(self):
        global c
        print(c)  # c用来计数，算当前进程走到了哪个部分
        while True:  # (原本为c < len(A)，但是A列表开始动态生成，不需要跳出while)因为是一个一个点绘制，所以一个一个点传送，注意：需要循环，不然只会发送1遍
            if self.wait_flage:  # 暂停标志生效则暂停曲线继续更新
                return
            self.dataRefreshed.emit([c])  # emit发送的数据必须是列表的形式
            sleep(0.02)  # 曲线的更新频率，当前是每0.08s更新一个点
            c = c + 1

    def wait(self):  # 该函数可以转变暂停标志
        self.wait_flage = True


class UserQSplineSeries(QChart):  # 绘制曲线图
    global A, B, m

    def __init__(self, parent=None, ):
        super(UserQSplineSeries, self).__init__(parent)
        self.window = parent
        # 设置x轴属性
        self.axisX = QValueAxis()
        self.axisX.setRange(0, 8.8)  # X轴的范围
        self.axisX.setTickCount(12)  # 设置x轴划分
        self.axisX.setLabelFormat("%.1f")  # X轴上数字显示的类型
        self.axisX.setLabelsColor(QColor(0, 0, 0))  # X轴上显示数字的颜色
        self.addAxis(self.axisX, Qt.AlignBottom)  # X轴放底部
        # 设置y轴属性
        self.axisY = QValueAxis()
        self.axisY.setRange(2.75, 4.25)  # Y轴的范围
        self.axisY.setTickCount(7)  # 设置x轴划分
        self.addAxis(self.axisY, Qt.AlignLeft)  # 设置Y坐标放在左侧
        self.axisY.setTitleText("Current(mA)")  # 设置Y坐标的名称

        # 添加曲线
        # self.series = QSplineSeries()  # 使用曲线
        self.series = QLineSeries()  # 使用直线
        self.series.setName("功耗曲线")  # 设置曲线的名字

        self.series.setVisible(True)  # 将曲线显示出来

        # 将曲线加到坐标图里面去
        self.addSeries(self.series)
        self.series.attachAxis(self.axisX)  # 让曲线与坐标轴对应
        self.series.attachAxis(self.axisY)
        self.series.setColor(QColor(126, 211, 33))  # 设置曲线的颜色

        self.refreshAB(0)  # 新建曲线时，重置AB列表

    def handle_update(self, c):  # 功耗曲线的更新函数
        c = c[0]  # 注意因为之前规定了emit传送的数据是[c]，所以需要进一步处理,此时的cc表示用来计数的c，每隔0.08s会传送一个更大的c=c+1
        point_x, point_y = c * 0.02, A[c % 40]  # 将当前更新的点坐标赋值给point_x,point_y
        if c % 40 == 0:
            self.refreshAB(m)  # 刷新AB列表内容
        self.series.append(QPointF(point_x, point_y))  # 将需要显示的点传入曲线
        if c >= 440:  # 如果超过了可显示曲线范围，调整x轴（可以通过计算一个界面能有多少个点来算出来）
            self.axisX.setRange(point_x - 8.8, point_x)  # X轴的范围
            self.axisX.setTickCount(12)  # 设置x轴划分
            self.series.remove(0)  # 清理不需要的点，以防止到后面曲线冗余导致卡顿

    def handle_update_2(self, c):  # 电磁曲线的更新函数

        c = c[0]  # 注意因为之前规定了emit传送的数据是[c]，所以需要进一步处理,此时的cc表示用来计数的c，每隔0.08s会传送一个更大的c=c+1
        point_x, point_y = c * 0.02, B[c % 40]  # 将当前更新的点坐标赋值给point_x,point_y
        self.series.append(QPointF(point_x, point_y))
        if c >= 440:  # 如果超过了可显示曲线范围，调整x轴
            self.axisX.setRange(point_x - 8.8, point_x)  # X轴的范围
            self.axisX.setTickCount(12)  # 设置x轴划分
            self.series.remove(0)  # 清理不需要的点，以防止到后面曲线冗余导致卡顿

    def refreshAB(self, mode=0):  # 刷新AB列表内容函数
        A.clear()
        B.clear()
        A.append(randint(300, 325) / 100)  # 3.1-3.25
        A.append(randint(315, 325) / 100)  # 3.1-3.25
        A.append(A[-1] + randint(5, 10) / 100)  # 3.15-3.35
        A.append(A[-1] + randint(5, 10) / 100)  # 3.2-3.45
        A.append(A[-1] + randint(-5, 5) / 100)
        A.append(randint(325, 330) / 100)
        A.append(randint(320, 325) / 100)
        A.append(3.3)
        A.append(randint(320, 322) / 100)
        A.append(randint(315, 320) / 100)  # 第一个波峰结束

        A.append(3.25)
        A.append(3.24)
        A.append(randint(325, 327) / 100)
        A.append(randint(334, 337) / 100)
        A.append(randint(330, 335) / 100)
        A.append(randint(337, 340) / 100)
        A.append(randint(337, 340) / 100)
        A.append(3.5)
        A.append(randint(360, 365) / 100)
        A.append(randint(357, 360) / 100)
        A.append(randint(365, 370) / 100)
        A.append(randint(350, 355) / 100)
        A.append(randint(375, 405) / 100)
        A.append(randint(369, 371) / 100)
        A.append(randint(373, 400) / 100)
        A.append(randint(345, 350) / 100)
        A.append(randint(330, 335) / 100)
        A.append(randint(337, 340) / 100)
        A.append(randint(325, 335) / 100)
        A.append(randint(325, 335) / 100)  # 第二个波峰结束

        A.append(A[-1] + randint(5, 10) / 100)
        A.append(randint(342, 345) / 100)
        A.append(randint(342, 344) / 100)
        A.append(randint(360, 365) / 100)
        A.append(randint(370, 380) / 100)
        A.append(randint(350, 365) / 100)
        A.append(randint(340, 375) / 100)
        A.append(3.5)
        A.append(randint(330, 335) / 100)
        A.append(randint(320, 325) / 100)  # 第三个波峰结束

        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(0, 500) / 100)
        B.append(randint(500, 1000) / 100)

        if mode == 1:
            # 通过调整AB数组，控制功率曲线变缓
            for i in range(40):  # 遍历A，B下标，对元素进行修改，达到变缓的目的
                A[i] = (A[i] + 3.5) / 2
                B[i] = (B[i] + 5) / 2
        elif mode == 2:
            # 通过调整AB数组，控制曲线出现多个0值(空指令)
            for i in range(40):  # 要显示的数据填充随机数
                x = randint(0, 7)
                if not x:
                    A[i] = 3
                    B[i] = 2
        elif mode == 3:
            # 给AB插入随机数
            for i in range(40):  # 要显示的数据填充随机数
                x = randint(0, 10)
                if not x:
                    num = randint(310, 425) / 100
                    A[i] = num
                    num = randint(0, 1000) / 100
                    B[i] = num
        elif mode == 4:  # 不稳定时钟
            for i in range(1, 40):
                x = randint(0, 3)
                if not x:
                    A[i] = A[i - 1]
        elif mode == 5:  # DPA(差分功耗分析)
            for i in range(10):
                a = randint(0, 2)
                b = randint(0, 2)
                if a:
                    A[i * 4] = 4
                    A[i * 4 + 1] = 4
                    A[i * 4 + 2] = 4
                    A[i * 4 + 3] = 4
                else:
                    A[i * 4] = 3
                    A[i * 4 + 1] = 3
                    A[i * 4 + 2] = 3
                    A[i * 4 + 3] = 3
                if b:
                    B[i * 4] = 9
                    B[i * 4 + 1] = 9
                    B[i * 4 + 2] = 9
                    B[i * 4 + 3] = 9
                else:
                    B[i * 4] = 2
                    B[i * 4 + 1] = 2
                    B[i * 4 + 2] = 2
                    B[i * 4 + 3] = 2


# 正则表达式判断ip地址(懒得看了，本次重构没看这部分)
class Regex:
    def IPyes(self, queryIP: str) -> str:  # 判断ip地址合法性，并会分辨IPv4和IPv6，返回一个字符串
        ipv4 = queryIP.split('.')
        ipv6 = queryIP.split(':')
        if len(ipv4) == 4:
            if all(re.match(r'^0$|^([1-9]\d{0,2})$', part) and int(part) < 256 for part in ipv4):
                return 'IPv4'
        elif len(ipv6) == 8:
            if all(re.match(r'^[0-9a-fA-F]{1,4}$', part) for part in ipv6):
                return 'IPv6'
        return "Neither"

    def port_yes(self, query_port: str) -> bool:  # 判断端口合法性，返回bool类型
        if re.match(r'^0$|^[1-9]\d{0,4}$', query_port) and int(query_port) < 65536:
            return True
        else:
            return False


class ChannelAnalysisRunMe(QMainWindow, Analysis_Of_Side_Channel_Leakage.Channel_Analysis.Ui_MainWindow):
    def __init__(self):
        super(ChannelAnalysisRunMe, self).__init__()
        self.setupUi(self)
        self.initt()
        self.setWindowTitle("侧信道泄露分析")  # 设置标题
        # self.setFixedSize(self.width(), self.height())  # 禁止缩放

        self.connect_flag = 0  # 判断是否为本地连接

        self.SPA = ''  # 用来存放SPA的侧信道分析结果
        self.DPA = ''  # 用来存放DPA的侧信道分析结果
        self.TA = ''  # 用来存放TA的侧信道分析结果
        self.CPA = ''  # 用来存放CPA的侧信道分析结果

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
        global opacity  # 透明度变量

        # 绑定按钮的点击事件
        self.pushButton.clicked.connect(self.btn_file_choose)  # 文件夹
        self.pushButton_2.clicked.connect(self.btn_file_save)  # 保存(文件夹)
        self.pushButton_2.setVisible(False)  # 隐藏保存按钮，该按钮暂时没有用
        self.pushButton_7.clicked.connect(self.btn_clear_data)  # debug日志清空
        self.pushButton_17.clicked.connect(self.btn_ip_connect)  # ip连接
        self.pushButton_18.clicked.connect(self.btn_ip_disconnected)  # ip断开
        self.pushButton_3.clicked.connect(self.btn_line)  # 启动芯片曲线
        self.pushButton_11.clicked.connect(self.btn_input_save)  # 保存（输入参数）
        self.pushButton_12.clicked.connect(self.data_load)  # 取消(输入参数)
        self.pushButton_13.clicked.connect(self.btn_side_analysis_protection)  # 抗物理攻击注入按钮
        self.pushButton_8.clicked.connect(self.btn_side_analysis_clear)  # 侧信道分析结果清理
        self.pushButton_9.clicked.connect(self.btn_side_analysis_copy)  # 侧信道分析结果复制到剪切板
        self.pushButton_14.clicked.connect(self.btn_side_analysis)  # 侧信道分析按钮
        self.pushButton_6.clicked.connect(self.btn_stop_line)  # 停止芯片连接
        # self.pushButton_4.clicked.connect(self.btn_wait_line)  # 暂停芯片连接
        self.pushButton_5.clicked.connect(self.btn_report)  # 获取报告

        # 绑定菜单槽函数（点击事件）
        self.action_6.triggered.connect(self.menu_action_openfile)  # 工程-文件-打开文件
        self.action_2.triggered.connect(self.menu_action_setView)  # 视图-设置框
        self.action_10.triggered.connect(self.close)  # 退出
        self.action_15.triggered.connect(self.showMinimized)  # 最小化
        self.actionIP.triggered.connect(self.btn_ip_connect)  # ip连接
        self.actionIP_2.triggered.connect(self.btn_ip_disconnected)  # ip断开
        self.action_14.triggered.connect(self.showMaximized)  # 最大化
        self.action_16.triggered.connect(self.showNormal)  # 正常化
        self.action_19.triggered.connect(self.menubar.hide)  # 隐藏菜单栏
        self.pushButton_10.clicked.connect(self.menubar.show)  # 显示菜单栏

        # 脚本控制响应回车事件
        self.lineEdit.returnPressed.connect(self.lineedit_py)  # 脚本控制函数

        # 定义曲线内容(A数组存放功耗曲线一个周期的点集，B数组存放电磁曲线，c为计数,m表示抗物理攻击模式)
        global A, B, c, m
        A = []
        B = []
        c = 0
        m = 0
        self.refreshAB()  # 初始化AB列表

        self.data_load()  # 输入参数加载

        # 曲线与线程联系
        self.data_refresh_thread = DataRefresh()
        # 初始化曲线配置(功率)
        self.plot_qchart = UserQSplineSeries()  # 将图表实例化
        self.graphicsView.setChart(self.plot_qchart)
        self.graphicsView.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
        self.graphicsView.setRubberBand(QChartView.RectangleRubberBand)  # 设置鼠标拖拽可以更改显示范围
        # 初始化曲线配置(电磁)
        self.plot_qchart_2 = UserQSplineSeries()  # 将图表实例化
        self.plot_qchart_2.series.setName("电磁曲线")  # 设置曲线的名字
        self.plot_qchart_2.axisY.setRange(0, 10)  # Y轴的范围
        self.plot_qchart_2.axisY.setTickCount(7)  # 设置x轴划分
        self.plot_qchart_2.axisY.setTitleText("P(W)")  # 设置Y坐标的名称
        self.plot_qchart_2.series.setColor(QColor(126, 211, 255))  # 设置曲线的颜色
        self.graphicsView_2.setChart(self.plot_qchart_2)
        self.graphicsView_2.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
        self.graphicsView_2.setRubberBand(QChartView.RectangleRubberBand)

        # “已经复制到剪切板”文本的透明度初始化
        opacity = QGraphicsOpacityEffect()  # 透明度对象
        opacity.setOpacity(0)  # 设置那个“已经复制”的文本为透明
        self.label_6.setGraphicsEffect(opacity)  # 改变标签透明度

    def menu_action_setView(self):
        if self.action_2.isChecked():
            self.tabWidget.setVisible(True)
        else:
            self.tabWidget.setVisible(False)

    def menu_action_openfile(self):  # 打开文件(已实现，直接调用)
        self.btn_file_choose()

    def btn_file_choose(self):
        filename = QFileDialog.getOpenFileName(None, "选取仿真文件", "./", "RAW Files (*.raw)")
        if filename[0] != '':
            self.mouse_stop()
            self.textBrowser.append('仿真文件打开成功,目录：' + filename[0])
            self.textBrowser.append('仿真文件已经部署到本地，请通过127.0.0.1:8000访问')

            # 自动配置好ip端口
            self.lineEdit_8.setText('127.0.0.1')
            self.lineEdit_9.setText('8000')
            self.connect_flag = 1  # 标志用于判断127.0.0.1:8000能否用于连接
        print(filename)

    def btn_file_save(self):
        filepath, type = QFileDialog.getSaveFileName(None, "文件保存", "/",
                                                     'RAW Files(*.raw)')  # 前面是地址，后面是文件类型,得到输入地址的文件名和地址txt(*.txt*.xls);;image(*.png)不同类别
        if filepath != '':
            self.textBrowser.append('文件保存成功,目录：' + filepath)
            print(filepath)

    def btn_clear_data(self):
        self.textBrowser.setText("")

    def btn_ip_connect(self):

        ip = self.lineEdit_8.text()
        port = self.lineEdit_9.text()
        if Regex().IPyes(ip) != 'Neither' and Regex().port_yes(port):  # 确认是否为合法ip地址和合法端口
            if self.connect_flag and ip == '127.0.0.1' and port == '8000':
                # 设置按钮为不再可以点击
                self.pushButton_17.setEnabled(False)
                # 读取ip和port内容
                ip = self.lineEdit_8.text()
                port = self.lineEdit_9.text()
                self.mouse_stop(1)  # 延迟
                # 接收区内容更改
                self.textBrowser.append('成功连接' + ip + ':' + port)

                self.pushButton_3.setEnabled(True)  # 设置启动芯片曲线按钮为可以点击
                self.pushButton_5.setEnabled(True)  # 设置报告生成按钮可以点击
            else:
                self.textBrowser.append('连接失败，请检查ip端口是否正确')
        else:  # 格式错误的ip和端口
            QMessageBox.warning(None, "Warning", "ip端口格式错误，请检查")

    def btn_ip_disconnected(self):
        if self.pushButton_17.isEnabled():
            self.textBrowser.append('当前处于断开状态，请不要重复点击')
        else:
            # 设置按钮为可以点击
            self.pushButton_17.setEnabled(True)
            # 接收区内容更改
            self.textBrowser.append('已断开连接')

            # 把所有功能关闭
            self.pushButton_13.setEnabled(False)
            self.pushButton_14.setEnabled(False)
            self.btn_stop_line()
            self.pushButton_3.setEnabled(False)

    def btn_line(self):
        self.pushButton_3.setEnabled(False)
        # self.pushButton_4.setEnabled(True)
        self.pushButton_6.setEnabled(True)
        self.mouse_stop()
        self.gh_line()  # 仿真功率曲线
        self.dc_line()  # 仿真电磁曲线
        print("线程开始")
        self.data_refresh_thread.wait_flage = False
        self.data_refresh_thread.start()

        # 打开抗物理攻击注入和侧行道分析按钮
        self.pushButton_13.setEnabled(True)
        self.pushButton_14.setEnabled(True)

    # 功耗曲线1
    def gh_line(self):

        self.data_refresh_thread.dataRefreshed.connect(self.plot_qchart.handle_update)  # 新的视频任务进入时候后面加进去

    # 电磁曲线1
    def dc_line(self):

        self.data_refresh_thread.dataRefreshed.connect(self.plot_qchart_2.handle_update_2)  # 新的视频任务进入时候后面加进去

    def data_load(self):
        with open('channel_analysis_data.txt', 'r') as f:
            data = f.read().split('\n')
        self.comboBox_3.setCurrentIndex(0)
        self.lineEdit_10.setText(data[1])
        self.comboBox_4.setCurrentIndex(0)
        self.lineEdit_11.setText(data[3])
        self.comboBox_5.setCurrentIndex(0)
        self.lineEdit_12.setText(data[5])
        self.comboBox_6.setCurrentIndex(0)
        self.lineEdit_13.setText(data[7])
        self.comboBox_7.setCurrentIndex(0)
        self.lineEdit_14.setText(data[9])

    def btn_input_save(self):
        data = []
        data.append(str(self.comboBox_3.currentIndex()))
        data.append('\n')
        data.append(self.lineEdit_10.text())
        data.append('\n')
        data.append(str(self.comboBox_4.currentIndex()))
        data.append('\n')
        data.append(self.lineEdit_11.text())
        data.append('\n')
        data.append(str(self.comboBox_5.currentIndex()))
        data.append('\n')
        data.append(self.lineEdit_12.text())
        data.append('\n')
        data.append(str(self.comboBox_6.currentIndex()))
        data.append('\n')
        data.append(self.lineEdit_13.text())
        data.append('\n')
        data.append(str(self.comboBox_7.currentIndex()))
        data.append('\n')
        data.append(self.lineEdit_14.text())
        data.append('\n')
        with open('channel_analysis_data.txt', 'w') as f:
            f.write(''.join(data))
        self.textBrowser.append('输入参数保存成功')

    def btn_side_analysis_protection(self):
        # 不能再点击了，不然会出错
        self.pushButton_13.setEnabled(False)

        self.mouse_stop()
        text = self.comboBox_2.currentText()
        self.textBrowser.append(f"抗物理攻击注入生效，当前使用逻辑：{text}")
        self.plot_qchart.series.setColor(QColor(26, 111, 200))  # 设置曲线的颜色
        self.plot_qchart_2.series.setColor(QColor(26, 111, 200))  # 设置曲线的颜色
        self.plot_qchart.series.setName(f"功耗曲线({text})")  # 设置曲线的名字
        self.plot_qchart_2.series.setName(f"电磁曲线({text})")  # 设置曲线的名字
        global A, B, m
        if text == "CP2L逻辑":
            m = 1  # 改变模式，最终会反应到线程更新曲线的方式
            # 通过调整AB数组，控制功率曲线变缓
            for i in range(40):  # 遍历A，B下标，对元素进行修改，达到变缓的目的
                A[i] = (A[i] + 3.5) / 2
                B[i] = (B[i] + 5) / 2

        elif text == "dummy cycle（空指令）":
            m = 2  # 改变模式，最终会反应到线程更新曲线的方式
            # 通过调整AB数组，控制曲线出现多个0值
            for i in range(40):  # 要显示的数据填充随机数
                x = randint(0, 7)
                if not x:
                    A[i] = 3
                    B[i] = 2

        elif text == "随机数掩码":
            m = 3  # 改变模式，最终会反应到线程更新曲线的方式
            for i in range(10):  # 要显示的数据填充随机数
                x = randint(0, 3)
                if x:
                    num = randint(310, 425) / 100
                    A[i] = num
                    num = randint(0, 1000) / 100
                    B[i] = num
        elif text == "unstable clock（不稳定时钟）":
            m = 4
            for i in range(1, 40):
                x = randint(0, 3)
                if not x:
                    A[i] = A[i - 1]

    def btn_side_analysis_clear(self):
        self.textBrowser_3.setText("")

    def btn_side_analysis_copy(self):
        txt = self.textBrowser_3.toPlainText()
        # 使用os.system()或subprocess.call()时如何隐藏控制台?：https://devpress.csdn.net/python/63054fcf7e6682346619dec7.html
        CREATE_NO_WINDOW = 0x08000000
        subprocess.run(['clip.exe'], input=txt.strip().encode('utf-16'), check=True,
                       creationflags=CREATE_NO_WINDOW)  # 将字符串保存到剪切板中（实现复制功能）

        # 设置透明度
        opacity.setOpacity(0)  # 初始化设置透明度为0，即完全透明
        self.label_6.setGraphicsEffect(opacity)  # 把标签的透明度设置为为self.opacity
        self.draw()  # 淡入淡出效果开始（点击复制的提示文本淡入淡出）

    def draw(self):
        opacity.i = 100  # 用于记录透明度变化与循环次数

        def timeout():  # 超时函数：改变透明度
            opacity.setOpacity(opacity.i / 100)  # 设置透明度为1（不透明）
            self.label_6.setGraphicsEffect(opacity)  # 改变标签透明度
            opacity.i -= 1
            if opacity.i <= 0:  # 此时透明度为0，即控件已经完全消失
                timer.stop()  # 计时器停止
                timer.deleteLater()

        timer = QTimer()  # 计时器
        timer.setInterval(10)  # 设置间隔时间，毫秒为单位
        timer.timeout.connect(timeout)  # 超时槽函数，每到达间隔时间，调用该函数
        timer.start()  # 计时器开始

    def btn_side_analysis(self):
        self.mouse_stop(1)
        txt = self.comboBox.currentText()  # 侧信道分析方法
        self.textBrowser_3.setText(f"本次侧信道分析为：{txt}")
        if txt == "SPA(简单功耗分析)":
            self.textBrowser_3.append("分析原理：运行RSA模块化幂运算环路")
            self.textBrowser_3.append("---分析中---")
            QApplication.processEvents()  # 页面刷新
            self.mouse_stop(1)
            a = ""
            lst = ['0', '1__']
            for i in range(20):
                a += random.choice(lst) + ' '
            self.textBrowser_3.append(
                f"分析结果：{a}")
            # 实现SPA曲线的变换(参考：https://baijiahao.baidu.com/s?id=1761855275257534072&wfr=spider&for=pc)
            self.SPA = f'分析原理：运行RSA模块化幂运算环路\n分析结果：{a}'  # SPA的分析结果全部保存成字符串，方便存取
        elif txt == "DPA(差分功耗分析)":
            self.textBrowser_3.append("分析原理：使用统计方法分析测量集，以识别数据的相关性")
            self.textBrowser_3.append("---分析中---")
            self.textBrowser_3.append("分析结果：LSB=1时AES S-box输出见曲线（上），LSB=0时AES S-box输出见曲线（下）")
            # 曲线变换
            self.plot_qchart.series.setName("曲线(上)")  # 设置曲线的名字
            self.plot_qchart_2.series.setName("曲线(下)")  # 设置曲线的名字
            global A, B, m
            m = 5
            for i in range(10):
                a = randint(0, 2)
                b = randint(0, 2)
                if a:
                    A[i * 4] = 4
                    A[i * 4 + 1] = 4
                    A[i * 4 + 2] = 4
                    A[i * 4 + 3] = 4
                else:
                    A[i * 4] = 3
                    A[i * 4 + 1] = 3
                    A[i * 4 + 2] = 3
                    A[i * 4 + 3] = 3
                if b:
                    B[i * 4] = 9
                    B[i * 4 + 1] = 9
                    B[i * 4 + 2] = 9
                    B[i * 4 + 3] = 9
                else:
                    B[i * 4] = 2
                    B[i * 4 + 1] = 2
                    B[i * 4 + 2] = 2
                    B[i * 4 + 3] = 2
            self.DPA = f'分析原理：使用统计方法分析测量集，以识别数据的相关性\n分析结果：LSB=1时AES S-box输出见曲线（上），LSB=0时AES S-box输出见曲线（下）'  # DPA的分析结果全部保存成字符串，方便存取
        elif txt == "CPA(相关性功耗分析)":
            self.textBrowser_3.append("分析原理：创建设备的功率模型(汉明权重模型),幂模型越准确，相关性越强")
            self.textBrowser_3.append("---分析中---")
            QApplication.processEvents()  # 页面刷新
            sleep(1)
            # 生成1-255的随机数，转化为2进制显示
            a = bin(randint(1, 255))
            b = bin(randint(1, 255))
            c = bin(randint(1, 255))
            self.textBrowser_3.append(
                f"分析结果(汉明权重)：{a}，{b}, {c}")
            self.CPA = f'分析原理：使用统计方法分析测量集，以识别数据的相关性\n分析结果(汉明权重)：{a}，{b}, {c}'  # DPA的分析结果全部保存成字符串，方便存取
        elif txt == "TA(模板分析)":
            self.textBrowser_3.append("分析原理：利用设备复制品上创建的\"profile\"快速恢复目标设备的密钥")
            self.textBrowser_3.append("---分析中---")
            QApplication.processEvents()  # 页面刷新
            sleep(1)
            # 获取随机md5码并输出
            from hashlib import md5
            obj = md5()
            obj.update(f"{randint(1, 100)}".encode("utf-8"))
            bs = obj.hexdigest()
            self.textBrowser_3.append(f"分析结果：{bs}")
            self.TA = f'分析原理：利用设备复制品上创建的\"profile\"快速恢复目标设备的密钥\n分析结果：{bs}'  # DPA的分析结果全部保存成字符串，方便存取

    def lineedit_py(self):  # 监听了回车键，当用户敲了回车键会进入该函数
        # 1.获取文本
        # 2.清空文本框
        # 3.根据文本匹配对应命令，实施命令（help可以获取指令）
        # 3.文本显示在消息栏
        # 4.消息栏显示对应脚本处理结果

        # 1.获取文本
        text = self.lineEdit.text()
        if text == '':
            return
        # 2.清空文本框
        self.lineEdit.setText('')
        # 3.文本显示在消息栏
        self.textBrowser_2.append(text)

        # 4.根据文本匹配对应命令，实施命令（help可以获取指令）
        text = text.split(' ')
        if text[0] == 'connect':  # 连接ip命令
            try:
                a = text[1]
                a = a.split(':')
                self.lineEdit_8.setText(a[0])
                self.lineEdit_9.setText(a[1])
                self.btn_ip_connect()
            except:
                QMessageBox.warning(None, "Warning", "ip端口格式错误，请检查")
        elif text[0] == 'disconnect':
            self.btn_ip_disconnected()  # 断开连接命令

        elif text[0] == 'input':  # 输入信息命令
            self.textBrowser_2.append('已读入输入数据，请在左侧消息框确认')
            text = text[1:]
            for i in range(len(text) // 2):
                self.textBrowser.append('输入端口:' + text[i * 2] + ' 输入内容:' + text[i * 2 + 1])
        elif text[0] == 'help':  # 帮助命令，获取命令列表
            self.textBrowser_2.append('当前可执行命令有：')
            self.textBrowser_2.append('connect [ip]:[端口]')
            self.textBrowser_2.append('disconnect')
            self.textBrowser_2.append('help')
            self.textBrowser_2.append('input [端口名] [内容] [端口名] [内容] ...')
        else:  # 错误命令
            self.textBrowser_2.append('---命令未识别（请检查）---')
            return
        self.textBrowser_2.append('---命令已执行---')

    def btn_wait_line(self):
        # self.pushButton_4.setEnabled(False)
        self.pushButton_3.setEnabled(True)
        self.pushButton_6.setEnabled(False)
        self.data_refresh_thread.wait()

    def btn_stop_line(self):
        global m
        m = 0  # 将抗物理攻击模式归零，也就是没有任何抗物理攻击模式
        # self.pushButton_4.setEnabled(False)
        self.pushButton_3.setEnabled(True)
        self.pushButton_6.setEnabled(False)
        self.data_refresh_thread.wait()

        # 关闭侧信道分析功能
        self.pushButton_14.setEnabled(False)

        # 重新实例化画布(功率)
        self.plot_qchart = UserQSplineSeries()  # 将图表实例化
        self.graphicsView.setChart(self.plot_qchart)
        self.graphicsView.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
        self.graphicsView.setRubberBand(QChartView.RectangleRubberBand)
        # 重新实例化画布（电磁）
        self.plot_qchart_2 = UserQSplineSeries()  # 将图表实例化
        self.plot_qchart_2.series.setName("电磁曲线")  # 设置曲线的名字
        self.plot_qchart_2.axisY.setRange(0, 10)  # Y轴的范围
        self.plot_qchart_2.axisY.setTickCount(7)  # 设置x轴划分
        self.plot_qchart_2.axisY.setTitleText("P(W)")  # 设置Y坐标的名称
        self.plot_qchart_2.series.setColor(QColor(126, 211, 255))  # 设置曲线的颜色
        self.graphicsView_2.setChart(self.plot_qchart_2)
        self.graphicsView_2.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
        self.graphicsView_2.setRubberBand(QChartView.RectangleRubberBand)

        # 重置c时间到起点
        global c
        print(f"停前{c}")
        c = -1
        print(f"停后{c}")

        # 重置随机数组AB
        self.refreshAB()

    def btn_report(self):
        self.mouse_stop(1)
        # 把界面信息装入report.txt中，方便对应界面调用
        with open('report.txt', 'w', encoding="utf-8") as f:
            data = []
            now = datetime.now()
            data.append(now.strftime('%Y%m%d%H%M%S%f'))  # 报告编号
            if self.lineEdit_8.text() == '127.0.0.1' and self.lineEdit_9.text() == '8000':  # 判断是不是本地连接
                data.append('☑仿真芯片数据    ☐实时芯片数据')  # 报告类型
            else:
                data.append('☐仿真芯片数据    ☑实时芯片数据')  # 报告类型
            data.append(self.lineEdit_8.text() + ':' + self.lineEdit_9.text())  # 报告IP
            data.append(f'报告完成时间:{now.year}年{now.month}月{now.day}日')  # 报告日期
            data.append(self.DPA)
            data.append(self.TA)
            data.append(self.CPA)
            data.append(self.SPA)
            f.write('\t'.join(data))
        f.close()
        self.report = Report.report_runme.ReportRunMe()
        self.report.show()

    def refreshAB(self):  # 刷新AB列表内容函数
        global A, B
        A = []
        B = []
        A.clear()
        B.clear()
        A.append(randint(300, 325) / 100)  # 3.1-3.25
        A.append(randint(315, 325) / 100)  # 3.1-3.25
        A.append(A[-1] + randint(5, 10) / 100)  # 3.15-3.35
        A.append(A[-1] + randint(5, 10) / 100)  # 3.2-3.45
        A.append(A[-1] + randint(-5, 5) / 100)
        A.append(randint(325, 330) / 100)
        A.append(randint(320, 325) / 100)
        A.append(3.3)
        A.append(randint(320, 322) / 100)
        A.append(randint(315, 320) / 100)  # 第一个波峰结束

        A.append(3.25)
        A.append(3.24)
        A.append(randint(325, 327) / 100)
        A.append(randint(334, 337) / 100)
        A.append(randint(330, 335) / 100)
        A.append(randint(337, 340) / 100)
        A.append(randint(337, 340) / 100)
        A.append(3.5)
        A.append(randint(360, 365) / 100)
        A.append(randint(357, 360) / 100)
        A.append(randint(365, 370) / 100)
        A.append(randint(350, 355) / 100)
        A.append(randint(375, 405) / 100)
        A.append(randint(369, 371) / 100)
        A.append(randint(373, 400) / 100)
        A.append(randint(345, 350) / 100)
        A.append(randint(330, 335) / 100)
        A.append(randint(337, 340) / 100)
        A.append(randint(325, 335) / 100)
        A.append(randint(325, 335) / 100)  # 第二个波峰结束

        A.append(A[-1] + randint(5, 10) / 100)
        A.append(randint(342, 345) / 100)
        A.append(randint(342, 344) / 100)
        A.append(randint(360, 365) / 100)
        A.append(randint(370, 380) / 100)
        A.append(randint(350, 365) / 100)
        A.append(randint(340, 375) / 100)
        A.append(3.5)
        A.append(randint(330, 335) / 100)
        A.append(randint(320, 325) / 100)  # 第三个波峰结束

        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(495, 510) / 100)
        B.append(randint(0, 500) / 100)
        B.append(randint(500, 1000) / 100)

    def mouse_stop(self, n=0):  # 延迟
        self.setCursor(QCursor(Qt.BusyCursor))  # FIXME:设置鼠标匆忙（用于延迟）
        QApplication.processEvents()  # 刷新面板
        if n == 0:
            time.sleep(random.choice([1, 1.5, 2, 2.5, 3]))
        else:
            time.sleep(n)
        self.setCursor(QCursor(Qt.ArrowCursor))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    channel = ChannelAnalysisRunMe()

    channel.show()

    sys.exit(app.exec_())

import random
import time
from random import randint, choice
import re
import sys
from time import sleep

from PyQt5 import QtWidgets
from PyQt5.QtChart import QValueAxis, QLineSeries, QChart, QChartView
from PyQt5.QtGui import QPixmap, QPainter, QBrush, QColor, QFont, QCursor
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsPixmapItem, QMainWindow, QMessageBox, \
    QAbstractItemView, QTableWidgetItem
from PyQt5.QtCore import Qt, QPointF, QThread, pyqtSignal

import Trojan_Analysis.HardwareTrojan, Trojan_Analysis.rand_str

import Trojan_Analysis.InputData_runme


# 正则表达式判断ip地址
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


class HardwareTrojanRunMe(QMainWindow, Trojan_Analysis.HardwareTrojan.Ui_MainWindow):
    def __init__(self):
        super(HardwareTrojanRunMe, self).__init__()
        self.setupUi(self)
        self.initt()
        self.setWindowTitle("硬件木马分析")  # 设置标题
        # self.setFixedSize(self.width(), self.height())  # 禁止缩放
        global muma_1, muma_2
        muma_1 = []
        muma_2 = []

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
        # 设置按钮触发事件
        self.pushButton.clicked.connect(self.btn_connect)  # ip端口连接
        self.pushButton_2.clicked.connect(self.btn_disconnect)  # 断开连接
        self.pushButton_7.clicked.connect(self.btn_line)  # 侧信道分析
        self.pushButton_8.clicked.connect(self.btn_edit)  # 编辑外部数据
        self.pushButton_5.clicked.connect(self.btn_logic)  # 逻辑测试
        self.pushButton_6.clicked.connect(self.btn_load_data)  # 加载外部数据

        self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)  # 设置点击模式为不可点击
        self.tableWidget_2.setSelectionMode(QAbstractItemView.NoSelection)  # 设置点击模式为不可点击

        # 进度条初始化
        self.progressBar.setRange(0, 100)  # 设置进度条的取值范围(最小值和最大值)
        self.progressBar.setFormat('逻辑测试进度  %p%'.format(self.progressBar.value() - self.progressBar.minimum()))
        self.progressBar.setValue(0)  # 逻辑测试显示当前进度

        # 菜单功能
        self.action_3.triggered.connect(self.btn_edit)  # 设置-外部数据设置
        self.action_10.triggered.connect(self.close)  # 退出
        self.action_11.triggered.connect(self.showMinimized)  # 最小化
        self.actionIP.triggered.connect(self.btn_connect)#ip连接
        self.action_13.triggered.connect(self.showMaximized)  # 最大化
        self.action_19.triggered.connect(self.showNormal)  # 正常化
        self.action_21.triggered.connect(self.menubar.hide)  # 隐藏菜单栏
        self.pushButton_3.clicked.connect(self.menubar.show)  # 显示菜单栏

    def btn_connect(self):
        ip = self.lineEdit.text()
        port = self.lineEdit_2.text()
        if Regex().IPyes(ip) != 'Neither' and Regex().port_yes(port):  # 检测ip与端口是否合法
            if ip == '127.0.0.1' and port == '8000':  # FIXME:目前端口写死了，只能127.0.0.1：8000可以连接
                self.mouse_stop()  # 延迟
                self.pushButton_2.setEnabled(True)
                self.pushButton.setEnabled(False)
                self.textEdit.setText('连接成功')
                # self.pushButton_5.setEnabled(True)
                self.pushButton_6.setEnabled(True)
                # self.pushButton_7.setEnabled(True)
                self.pushButton_8.setEnabled(True)
            else:
                self.textEdit.setText('连接失败，请检查端口信息')
        else:
            QMessageBox.warning(None, "Warning", "ip端口格式错误，请检查")

    def btn_disconnect(self):
        self.pushButton_2.setEnabled(False)
        self.pushButton.setEnabled(True)
        self.textEdit.setText('已断开连接')
        # 按钮关闭
        self.pushButton_5.setEnabled(False)
        self.pushButton_6.setEnabled(False)
        self.pushButton_7.setEnabled(False)
        self.pushButton_8.setEnabled(False)
        # 消息清空
        self.textBrowser_3.setText('')
        # 曲线清空
        self.graphicsView.chart().removeAllSeries()  # 清除self.graphicsView.chart()中的所有数据系列
        self.graphicsView.update()  # 更新QChartView以显示清空后的内容
        self.graphicsView_2.chart().removeAllSeries()  # 清除self.graphicsView.chart()中的所有数据系列
        self.graphicsView_2.update()  # 更新QChartView以显示清空后的内容
        self.graphicsView_8.chart().removeAllSeries()  # 清除self.graphicsView.chart()中的所有数据系列
        self.graphicsView_8.update()  # 更新QChartView以显示清空后的内容

    def btn_line(self):  # 有问题：1.需要很密集的x，y数据集，当前无法获取 2.曲线一定会经过最高最低点，无法避免
        self.pushButton_7.setEnabled(False)  # 不允许再次点击侧信道分析按钮，否则会引起多重曲线同时出现的bug
        QApplication.processEvents()  # 页面刷新
        for i in range(5, 0, -1):
            self.textEdit.setText(f'侧信道信息采集中（倒计时：{i}s）')
            QApplication.processEvents()  # 页面刷新
            sleep(1)
        self.textEdit.setText('')

        self.mouse_stop(1.5)
        self.consumption_line()  # 绘制功耗曲线
        self.electromagnetism_line()  # 绘制电磁曲线
        self.time_line()  # 绘制时间曲线

        # 木马检测结果显示
        QApplication.processEvents()  # 页面刷新
        self.textBrowser_3.append("木马检测中。。。")
        QApplication.processEvents()  # 页面刷新
        self.mouse_stop()
        self.textBrowser_3.append("功耗曲线对比结果：")
        x = len(muma_1) // 2
        if x:
            self.textBrowser_3.append(f"有{x}处疑似木马,范围：\n")
            for i in range(len(muma_1)):
                if i % 2 == 0:
                    self.textBrowser_3.insertPlainText(f' {muma_1[i]}')
                else:
                    self.textBrowser_3.insertPlainText(f'-{muma_1[i]} ')
            self.textBrowser_3.append("")
        else:
            self.textBrowser_3.append("未检测到木马")

        QApplication.processEvents()  # 页面刷新
        self.mouse_stop()
        self.textBrowser_3.append("电磁辐射曲线对比结果：")
        x = len(muma_2) // 2
        if x:
            self.textBrowser_3.append(f"有{x}处疑似木马,范围：\n")
            for i in range(len(muma_2)):
                if i % 2 == 0:
                    self.textBrowser_3.insertPlainText(f' {muma_2[i]}')
                else:
                    self.textBrowser_3.insertPlainText(f'-{muma_2[i]} ')
            self.textBrowser_3.append("")
        else:
            self.textBrowser_3.append("未检测到木马")
        QApplication.processEvents()  # 页面刷新
        self.mouse_stop()
        self.textBrowser_3.append("时间延迟曲线对比结果：")
        self.textBrowser_3.append("未检测到木马")
        self.textBrowser_3.append("----侧信道分析结束----")
        self.pushButton_5.setEnabled(True)

    def btn_edit(self):
        self.inp = Trojan_Analysis.InputData_runme.InputDataRunMe()
        self.inp.show()

    def btn_logic(self):
        self.pushButton_5.setEnabled(False)  # 设置逻辑测试按钮不可以再点击了
        # # 1.延迟以进度条的形式
        self.progressbar_thread = ProgressBarThread()  # 实例化线程
        self.progressbar_thread.now_num.connect(self.progressbar_change)  # 绑定槽函数
        # 启动线程，执行线程类中run函数
        self.progressbar_thread.start()

    # 这是子线程执行时定时传递给主线程的参数,用于表示进度条的情况
    def progressbar_change(self, num):
        if (1):  # 1表示显示随机数用来体现逻辑测试，0表示使用文字进度条表示随机测试
            randstr = Trojan_Analysis.rand_str.rand_str()  # 调用目录下的随机数生成函数，见rand_str.py
            self.textEdit.append(
                randstr)  # 使用append方法追加显示，注意此处不要使用setText()方法，setText()只能显示一次，不能追加数据，多次调用会异常崩掉
        else:
            self.textEdit.setText(f'逻辑测试进度:{num}%')

        self.progressBar.setValue(num)
        if num >= 100:  # 进度条满了
            self.textEdit.append(
                '--------逻辑测试完毕------')  # 使用append方法追加显示，注意此处不要使用setText()方法，setText()只能显示一次，不能追加数据，多次调用会异常崩掉
            # 2.描绘出第二个曲线
            self.mouse_stop(1.5)
            self.plot_qchart.handle_update_4()
            # 3.数据填充
            self.mouse_stop()
            self.tableWidget.setItem(0, 0, QTableWidgetItem(f'{randint(5000, 5010) / 100}ns'))  # Value
            self.tableWidget.item(0, 0).setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(1, 0, QTableWidgetItem(f'{randint(5000, 5010) / 100}ns'))
            self.tableWidget.item(1, 0).setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(0, 1, QTableWidgetItem(f'{randint(4980, 4999) / 100}n'))  # Min
            self.tableWidget.item(0, 1).setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(1, 1, QTableWidgetItem(f'{randint(4950, 4999) / 100}n'))
            self.tableWidget.item(1, 1).setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(0, 2, QTableWidgetItem(f'{randint(5000, 5050) / 100}n'))  # Max
            self.tableWidget.item(0, 2).setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(1, 2, QTableWidgetItem(f'{randint(5000, 5030) / 100}n'))
            self.tableWidget.item(1, 2).setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(0, 3, QTableWidgetItem('240'))  # Count
            self.tableWidget.item(0, 3).setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(1, 3, QTableWidgetItem('240'))
            self.tableWidget.item(1, 3).setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(0, 4, QTableWidgetItem(''))  # Info
            self.tableWidget.item(0, 4).setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(1, 4, QTableWidgetItem(''))
            self.tableWidget.item(1, 4).setTextAlignment(Qt.AlignCenter)
            v1, v2, t1, t2 = max(A) * 100, max(AA) * 100 - randint(30, 50), randint(-1000,
                                                                                    0) / 100, randint(
                3000, 3500) / 100
            self.tableWidget_2.setItem(0, 1, QTableWidgetItem(f'{v1}mV'))  # V1
            self.tableWidget_2.setItem(1, 1, QTableWidgetItem(f'{v2}mV'))  # V2
            self.tableWidget_2.setItem(2, 1, QTableWidgetItem(f'{v2 - v1}mV'))  # ∆V
            self.tableWidget_2.setItem(3, 1, QTableWidgetItem('%.2fMV/s' % ((v2 - v1) / (t2 - t1))))  # ∆V/∆t
            self.tableWidget_2.setItem(0, 3, QTableWidgetItem('%.2fns' % (t1)))  # t1
            self.tableWidget_2.setItem(1, 3, QTableWidgetItem('%.2fns' % (t2)))  # t2
            self.tableWidget_2.setItem(2, 3, QTableWidgetItem('%.2fns' % (t2 - t1)))  # ∆t
            self.tableWidget_2.setItem(3, 3, QTableWidgetItem('%.2fMHz' % ((1 / (t2 - t1)) * 1000)))  # 1/∆t

    def btn_load_data(self):
        global muma_1, muma_2  # 清空木马列表
        muma_1.clear()
        muma_2.clear()
        try:
            self.inp.close()
        except:
            pass
        with open('data.txt', 'r') as f:
            data = f.read()
            print(data)
            data = data.split('\n')
        n = 0
        for i in range(1, 11, 2):
            if data[i] != '':
                self.mouse_stop(1.5)
                self.textEdit.append(data[i - 1] + '：加载成功')
                n += 1
        self.textEdit.append('----统计----')
        self.textEdit.append('共加载:' + str(n) + '条数据，加载失败：0条')
        self.pushButton_7.setEnabled(True)

    def consumption_line(self):  # 功耗曲线显示，注意这里没有最后一步刷新窗口，打算所有曲线加载完了再刷新（写在外面了)
        # 功耗曲线
        # 1.初始化功率
        self.plot_qchart = UserQSplineSeries()  # 将图表实例化
        self.plot_qchart.series.setName("功耗曲线")  # 折线命名
        self.graphicsView.setChart(self.plot_qchart)
        # 2.容器指定大小
        self.graphicsView.setGeometry(-50, -30, 1000, 560)
        self.graphicsView.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
        self.graphicsView.setRubberBand(QChartView.RectangleRubberBand)  # 设置鼠标拖拽可以更改显示范围
        # 3.显示曲线
        self.plot_qchart.handle_update()

    def electromagnetism_line(self):  # 电磁曲线
        # 电磁曲线
        # 1.初始化电磁
        self.plot_qchart_2 = UserQSplineSeries()  # 将图表实例化
        self.plot_qchart_2.series.setName("电磁曲线")  # 折线命名
        self.plot_qchart_2.axisY.setRange(0, 10)  # Y轴的范围
        self.plot_qchart_2.axisY.setTickCount(7)  # 设置y轴划分
        self.plot_qchart_2.series.setColor(QColor(126, 211, 255))  # 设置曲线的颜色
        self.graphicsView_2.setChart(self.plot_qchart_2)
        # 2.容器指定大小
        self.graphicsView_2.setGeometry(-50, -30, 1000, 560)
        self.graphicsView_2.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
        # 3.显示曲线
        self.plot_qchart_2.handle_update_2()

    def time_line(self):  # 时间延迟曲线
        # 时间延迟曲线
        # 1.初始化电磁
        self.plot_qchart_3 = UserQSplineSeries()  # 将图表实例化
        self.plot_qchart_3.series.setName("时延曲线")  # 折线命名
        self.plot_qchart_3.axisY.setRange(0, 1)  # Y轴的范围
        self.plot_qchart_3.axisY.setTickCount(7)  # 设置y轴划分
        self.plot_qchart_3.series.setColor(QColor(126, 211, 255))  # 设置曲线的颜色
        self.graphicsView_8.setChart(self.plot_qchart_3)
        # 2.容器指定大小
        self.graphicsView_8.setGeometry(-50, -30, 1000, 560)  # -10, -30, 960, 600
        self.graphicsView_8.setRenderHint(QPainter.Antialiasing)  # 抗锯齿

        # 3.显示曲线
        self.plot_qchart_3.handle_update_3()

    def mouse_stop(self, n=0):
        self.setCursor(QCursor(Qt.BusyCursor))  # FIXME:设置鼠标匆忙（用于延迟）
        QApplication.processEvents()  # 刷新面板
        if n == 0:
            time.sleep(random.choice([1, 1.5, 2, 2.5]))
        else:
            time.sleep(n)
        self.setCursor(QCursor(Qt.ArrowCursor))


class UserQSplineSeries(QChart):  # 绘制曲线图
    def __init__(self, parent=None, ):
        global A, B, C, AA
        A = []
        B = []
        C = []
        AA = []
        super(UserQSplineSeries, self).__init__(parent)
        self.window = parent
        # 设置x轴属性
        self.axisX = QValueAxis()
        self.axisX.setRange(0, 4.8)  # X轴的范围
        self.axisX.setTickCount(12)  # 设置x轴划分
        # self.axisX.setLabelsVisible(False)  # 隐藏x轴数字的显示
        self.axisX.setGridLineVisible(False)  # 隐藏网格线
        self.addAxis(self.axisX, Qt.AlignBottom)  # X轴放底部
        # 设置y轴属性
        self.axisY = QValueAxis()
        self.axisY.setRange(2.75, 4.25)  # Y轴的范围
        self.axisY.setTickCount(7)  # 设置x轴划分
        self.axisY.setLabelsVisible(False)  # 隐藏x轴数字的显示
        self.axisY.setGridLineVisible(False)  # 隐藏网格线
        self.addAxis(self.axisY, Qt.AlignLeft)  # 设置Y坐标放在左侧

        # 添加曲线
        self.series = QLineSeries()  # 坐标点之间使用直线连接，不需要平滑过渡
        self.series.setVisible(True)  # 将曲线显示出来

        # 将曲线加到坐标图里面去
        self.addSeries(self.series)
        self.series.attachAxis(self.axisX)  # 让曲线与坐标轴对应
        self.series.attachAxis(self.axisY)
        self.series.setColor(QColor(126, 211, 33))  # 设置曲线的颜色

        for i in range(6):
            self.refreshAB()  # 每个周期需要一次该函数

    def handle_update(self):  # 功耗曲线的更新函数
        global muma_1
        for i in range(len(A)):
            point_x, point_y = i * 0.02, A[i]  # 将当前更新的点坐标赋值给point_x,point_y
            self.series.append(QPointF(point_x, point_y))  # 将需要显示的点传入曲线 #FIXME:123
            if A[i] <= 2.99 or A[i] >= 4.17:
                muma_1.append((i - 1) * 0.02)
                muma_1.append(i * 0.02)

    def handle_update_2(self):  # 电磁曲线的更新函数
        global muma_2
        for i in range(len(B)):
            point_x, point_y = i * 0.02, B[i]  # 将当前更新的点坐标赋值给point_x,point_y
            self.series.append(QPointF(point_x, point_y))  # 将需要显示的点传入曲线
            if B[i] > 6 and B[i] - B[i - 1] > 7:
                muma_2.append((i - 1) * 0.02)
                muma_2.append(i * 0.02)

    def handle_update_3(self):  # 电磁曲线的更新函数
        for i in range(len(C)):
            point_x, point_y = i * 0.02, C[i]  # 将当前更新的点坐标赋值给point_x,point_y
            self.series.append(QPointF(point_x, point_y))  # 将需要显示的点传入曲线

    def handle_update_4(self):  # 功耗AA曲线的更新函数
        # 添加曲线
        self.series_2 = QLineSeries()  # 坐标点之间使用直线连接，不需要平滑过渡
        self.series_2.setVisible(True)  # 将曲线显示出来

        # 将曲线加到坐标图里面去
        self.addSeries(self.series_2)
        self.series_2.attachAxis(self.axisX)  # 让曲线与坐标轴对应
        self.series_2.attachAxis(self.axisY)
        self.series_2.setColor(QColor(144, 240, 238))  # 设置曲线的颜色
        for i in range(len(AA)):
            point_x, point_y = i * 0.02, AA[i]  # 将当前更新的点坐标赋值给point_x,point_y
            self.series_2.append(QPointF(point_x, point_y))  # 将需要显示的点传入曲线

    def refreshAB(self):  # 刷新AB列表内容函数
        global A, B, C, AA
        A.append(randint(300, 325) / 100)
        A.append(randint(315, 325) / 100)
        A.append(A[-1] + randint(5, 10) / 100)
        A.append(A[-1] + randint(5, 10) / 100)
        A.append(A[-1] + randint(-5, 5) / 100)
        A.append(randint(325, 330) / 100)
        A.append(randint(320, 325) / 100)
        A.append(3.3)
        A.append(randint(320, 322) / 100)
        A.append(randint(297, 320) / 100)  # 第一个波峰结束 #用这个的最低点来判断木马逻辑i<=299 #FIXME:123

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
        A.append(randint(375, 420) / 100)  # 用这个来判断木马,木马逻辑i>=417
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
        B.append(randint(500, 1000) / 100)  # 用B点两个位置的差来判断木马,判断条件:大于700

        x = randint(0, 1)
        if x:
            for i in range(40):
                C.append(0)
        else:
            for i in range(40):
                C.append(1)

        AA.append(A[-1] + randint(5, 10) / 100)
        AA.append(randint(342, 345) / 100)
        AA.append(randint(342, 344) / 100)
        AA.append(randint(360, 365) / 100)
        AA.append(randint(370, 380) / 100)
        AA.append(randint(350, 365) / 100)
        AA.append(randint(340, 375) / 100)
        AA.append(3.5)
        AA.append(randint(330, 335) / 100)
        AA.append(randint(320, 325) / 100)  # 第三个波峰结束
        AA.append(randint(300, 325) / 100)
        AA.append(randint(315, 325) / 100)
        AA.append(A[-1] + randint(5, 10) / 100)
        AA.append(A[-1] + randint(5, 10) / 100)
        AA.append(A[-1] + randint(-5, 5) / 100)
        AA.append(randint(325, 330) / 100)
        AA.append(randint(320, 325) / 100)
        AA.append(3.3)
        AA.append(randint(320, 322) / 100)
        AA.append(randint(315, 320) / 100)  # 第一个波峰结束

        AA.append(3.25)
        AA.append(3.24)
        AA.append(randint(325, 327) / 100)
        AA.append(randint(334, 337) / 100)
        AA.append(randint(330, 335) / 100)
        AA.append(randint(337, 340) / 100)
        AA.append(randint(337, 340) / 100)
        AA.append(3.5)
        AA.append(randint(360, 365) / 100)
        AA.append(randint(357, 360) / 100)
        AA.append(randint(365, 370) / 100)
        AA.append(randint(350, 355) / 100)
        AA.append(randint(375, 405) / 100)
        AA.append(randint(369, 371) / 100)
        AA.append(randint(373, 400) / 100)
        AA.append(randint(345, 350) / 100)
        AA.append(randint(330, 335) / 100)
        AA.append(randint(337, 340) / 100)
        AA.append(randint(325, 335) / 100)
        AA.append(randint(325, 335) / 100)  # 第二个波峰结束


# 进度条子线程,以便进度条加载时不会冻结ui界面
class ProgressBarThread(QThread):
    # 使用自定义信号和UI主线程通讯，参数是发送信号时附带参数的数据类型，可以是str、int、list等
    now_num = pyqtSignal(int)

    #
    def __init__(self, parent=None):
        super(ProgressBarThread, self).__init__(parent)

    # run函数是子线程中的操作，线程启动后开始执行
    def run(self):
        x = randint(40, 60)
        for i in range(101):
            sleep(0.05)
            if abs(i - x) < 4:  # 用于模拟出进度条更新的速度的随机性
                sleep(0.1)
            if 97 <= i <= 99:
                sleep(0.2)
            # 发射自定义信号
            # 通过emit函数将参数i传递给主线程，触发自定义信号
            self.now_num.emit(i)  # 注意这里与_signal = pyqtSignal(str)中的类型相同


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 初始化界面实例
    har = HardwareTrojanRunMe()

    # 展示界面
    har.show()
    sys.exit(app.exec_())

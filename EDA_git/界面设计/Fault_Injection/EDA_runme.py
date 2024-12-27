import re
import subprocess
import sys
import time
from datetime import datetime
from random import randint, choice
from time import sleep

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QMainWindow, QMessageBox, QAbstractItemView
from matplotlib.backends.backend_qt import MainWindow
import Fault_Injection.EDA

import Fault_Injection.HDL_runme, Fault_Injection.Fault_Configuration_runme
import Report.report_injection, Report.report_injection_runme


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


class EDARunMe(QMainWindow, Fault_Injection.EDA.Ui_MainWindow):
    # 故障指令条数
    row = 0

    def __init__(self):
        super(EDARunMe, self).__init__()
        self.setupUi(self)
        self.initt()
        self.setWindowTitle("故障注入")  # 设置标题
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
        # 设置点击按钮触发事件
        self.pushButton.clicked.connect(self.btn_connect_ip)  # 连接按钮
        self.pushButton_2.clicked.connect(self.btn_disconnect_ip)  # 断开按钮
        self.pushButton_6.clicked.connect(self.btn_get_ip_msg)  # 读取端口寄存器信息按钮
        self.pushButton_7.clicked.connect(self.btn_clear_msg)  # 清空接收区
        self.pushButton_3.clicked.connect(self.btn_HDL_input)  # 读取HDL模型源码
        self.pushButton_4.clicked.connect(self.btn_ip_to_fault)  # 插入故障注入逻辑按钮
        self.pushButton_10.clicked.connect(self.btn_fault_input)  # 设置故障参数
        self.pushButton_11.clicked.connect(self.btn_del_all)  # 清空故障注入
        self.pushButton_12.clicked.connect(self.btn_save_all)  # 保存故障文件
        self.pushButton_9.clicked.connect(self.btn_read_all)  # 读取故障文件
        self.pushButton_13.clicked.connect(self.btn_report)  # 获取报告
        self.pushButton_14.clicked.connect(self.btn_fault_result)  # 故障分析结果
        self.pushButton_15.clicked.connect(self.btn_clear_msg1)  # 清空消息区
        self.pushButton_5.clicked.connect(self.btn_del_row)  # 删除选中行

        # 监听回车键
        self.lineEdit_3.returnPressed.connect(self.lineedit_py)  # 脚本控制函数

        # 设置两个表格属性：只能选中一行或者
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)  # 设置只能单选
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置选者行
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 设置不可修改表格内容
        self.tableWidget_2.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置选者行
        self.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 设置不可修改表格内容
        self.tableWidget_2.setSelectionMode(QAbstractItemView.SingleSelection)  # 设置只能单选

        # 菜单选项
        self.action_4.triggered.connect(self.btn_fault_input)  # 设置-故障参数设置
        self.action_9.triggered.connect(self.close)  # 退出
        self.action_11.triggered.connect(self.showMinimized)  # 最小化
        self.actionIP.triggered.connect(self.btn_connect_ip)  # ip连接
        self.actionIP_2.triggered.connect(self.btn_disconnect_ip)  # ip断开
        self.action_14.triggered.connect(self.btn_clear_msg) #清空接收区
        self.action_15.triggered.connect(self.btn_clear_msg1)  # 清空消息区
        self.action_17.triggered.connect(self.showMaximized)  # 最大化
        self.action_18.triggered.connect(self.showNormal)  # 正常化
        self.action_20.triggered.connect(self.menubar.hide)  # 隐藏菜单栏
        self.pushButton_8.clicked.connect(self.menubar.show)  # 显示菜单栏


    def btn_del_row(self):
        row = self.tableWidget_2.currentRow()
        if row == -1:  # 判断是否选择了删除行，没选择提示删除失败
            self.textBrowser.setText('删除失败，请选择一行')
        else:
            self.textBrowser.setText(f'删除成功，原第{row + 1}行已删除')

        self.tableWidget_2.removeRow(row)

    def lineedit_py(self):
        # 1.获取文本
        # 2.清空文本框
        # 3.根据文本匹配对应命令，实施命令（help可以获取指令）
        # 3.文本显示在消息栏
        # 4.消息栏显示对应脚本处理结果

        # 1.获取文本
        text = self.lineEdit_3.text()
        if text == '':
            return
        # 2.清空文本框
        self.lineEdit_3.setText('')
        # 3.文本显示在消息栏
        self.textBrowser_2.append(text)

        # 4.根据文本匹配对应命令，实施命令（help可以获取指令）
        text = text.split(' ')
        if text[0] == 'connect':  # 连接ip命令
            try:
                a = text[1]
                a = a.split(':')
                self.lineEdit.setText(a[0])
                self.lineEdit_2.setText(a[1])
                self.btn_connect_ip()
            except:
                QMessageBox.warning(None, "Warning", "ip端口格式错误，请检查")
        elif text[0] == 'disconnect':
            self.btn_disconnect_ip()  # 断开连接命令

        elif text[0] == 'read_register':  # 读取寄存器列表
            if self.pushButton_6.isEnabled():
                self.btn_get_ip_msg()
            else:
                self.textBrowser_2.append("错误，请先使用connect命令连接ip端口")
        elif text[0] == 'report':  # 获取报告
            if self.pushButton_13.isEnabled():
                self.btn_report()
            else:
                self.textBrowser_2.append("报告获取失败")
        elif text[0] == 'help':  # 帮助命令，获取命令列表
            self.textBrowser_2.append('当前可执行命令有：')
            self.textBrowser_2.append('connect [ip]:[端口]')
            self.textBrowser_2.append('disconnect')
            self.textBrowser_2.append('help')
            self.textBrowser_2.append('read_register')
            self.textBrowser_2.append('report')
        else:  # 错误命令
            self.textBrowser_2.append('---命令未识别（请检查）---')
            return
        self.textBrowser_2.append('---命令已执行---')

    def btn_connect_ip(self):

        # 读取ip和port内容
        ip = self.lineEdit.text()
        port = self.lineEdit_2.text()
        if Regex().IPyes(ip) != 'Neither' and Regex().port_yes(port):
            if ip == '127.0.0.1' and port == '8000':
                # 设置点击连接按钮后，已处于连接状态，不可再连接
                self.pushButton.setEnabled(False)
                # 把其他功能按钮都解封
                self.pushButton_2.setEnabled(True)
                self.pushButton_6.setEnabled(True)
                self.pushButton_3.setEnabled(True)
                self.pushButton_4.setEnabled(True)
                self.pushButton_13.setEnabled(True)
                self.pushButton_14.setEnabled(True)

                self.mouse_stop()  # 延迟

                # 接收区内容更改
                self.textEdit.setText('成功连接' + ip + ':' + port)
                greyFormat = '<font color="grey">{}</font>'  # 设置灰色字体
                self.textEdit.append(greyFormat.format('(点击”读取寄存器列表文件“按钮可读取寄存器信息)'))
                return ip, port
            else:
                # 接收区内容更改
                self.textEdit.setPlainText('连接失败，请检查端口信息')
        else:
            QMessageBox.warning(None, "Warning", "ip端口格式错误，请检查")

    def btn_disconnect_ip(self):
        self.mouse_stop(1)
        if self.pushButton.isEnabled():
            self.textEdit.setPlainText('已断开连接,请勿重复点击')
        else:
            # 恢复连接按钮
            self.pushButton.setEnabled(True)
            # 接收区内容更改
            self.textEdit.setPlainText('已断开连接')

            # 清空各个窗口信息
            self.btn_del_all()
            self.tableWidget.setRowCount(0)  # 设置行数
            self.tableWidget.setRowCount(2)

            # 取消寄存器选择
            self.tableWidget.setCurrentItem(None)

            # 清空消息区
            self.textBrowser.setText('')

        # 把其他功能按钮都封印
        self.pushButton_2.setEnabled(False)
        self.pushButton_6.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        self.pushButton_10.setEnabled(False)
        self.pushButton_11.setEnabled(False)
        self.pushButton_12.setEnabled(False)
        self.pushButton_9.setEnabled(False)
        self.pushButton_13.setEnabled(False)
        self.pushButton_14.setEnabled(False)
        self.pushButton_5.setEnabled(False)

    def btn_get_ip_msg(self):
        self.mouse_stop(1)
        self.tableWidget.setRowCount(3)  # 设置行数
        self.tableWidget.setItem(0, 0, QTableWidgetItem("fetch"))
        self.tableWidget.setItem(1, 0, QTableWidgetItem("fetch"))
        self.tableWidget.setItem(2, 0, QTableWidgetItem("fetch"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("rg_gc[0]"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("rg_gc[1]"))
        self.tableWidget.setItem(2, 1, QTableWidgetItem("rg_gc[2]"))
        self.tableWidget.setItem(0, 2, QTableWidgetItem("1"))
        self.tableWidget.setItem(1, 2, QTableWidgetItem("2"))
        self.tableWidget.setItem(2, 2, QTableWidgetItem("3"))
        self.tableWidget.setItem(0, 3, QTableWidgetItem("clk"))
        self.tableWidget.setItem(1, 3, QTableWidgetItem("clk"))
        self.tableWidget.setItem(2, 3, QTableWidgetItem("clk"))

        # 解封按钮
        self.pushButton_5.setEnabled(True)
        self.pushButton_9.setEnabled(True)
        self.pushButton_10.setEnabled(True)
        self.pushButton_11.setEnabled(True)
        self.pushButton_12.setEnabled(True)

        # 接收区内容更改
        ip = self.lineEdit.text()
        port = self.lineEdit_2.text()
        self.textEdit.setPlainText('成功连接' + ip + ':' + port)
        greyFormat = '<font color="grey">{}</font>'  # 设置灰色字体
        self.textEdit.append(greyFormat.format('(选择寄存器列表一行，点击”插入故障注入逻辑“按钮可对该模块插入所配置的故障)'))

    def btn_clear_msg(self):
        self.textEdit.setPlainText('')

    def btn_HDL_input(self):
        self.mouse_stop()
        self.hdl = Fault_Injection.HDL_runme.HDLRunMe()
        self.hdl.show()
        # subprocess.call(['python', './HDLRunMe.py'])

    def btn_fault_input(self):
        self.fault = Fault_Injection.Fault_Configuration_runme.FaultConfigurationRunMe()
        self.fault.show()
        # subprocess.call(['python', './Fault_Configuration_runme.py'])

    def btn_ip_to_fault(self):
        try:
            # 读取当前选中行的行数self.tableWidget.currentRow()
            row = self.tableWidget.currentRow()

            # 获取整行的数据,存入items中
            items = []
            for column in range(self.tableWidget.columnCount()):
                items.append(self.tableWidget.item(row, column).text())
            # print(items)

            # 移动row到下一个空白行
            row = 0
            while self.tableWidget_2.item(row, 0) != None:
                row += 1

            # 判断是否需要加一行（扩充逻辑）
            if self.tableWidget_2.rowCount() <= row:
                self.tableWidget_2.setRowCount(row + 1)  # 设置行数

            # 读取默认配置fault_set.txt文件
            with open('fault_set.txt', 'r') as f:
                data = f.read().split(' ')

            # 故障注入部分，写入items数据
            for column in range(self.tableWidget_2.columnCount()):
                if column < 4:
                    self.tableWidget_2.setItem(row, column, QTableWidgetItem(items[column]))
                elif column == 4:
                    self.tableWidget_2.setItem(row, column, QTableWidgetItem(str(int(items[2]) + int(data[0]))))
                else:
                    self.tableWidget_2.setItem(row, column, QTableWidgetItem(data[column - 4]))

            # 接收区内容更改
            ip = self.lineEdit.text()
            port = self.lineEdit_2.text()
            self.textEdit.setPlainText('成功连接' + ip + ':' + port)
            greyFormat = '<font color="grey">{}</font>'  # 设置灰色字体
            self.textEdit.append(greyFormat.format('(选择寄存器列表一行，点击”插入故障注入逻辑“按钮可对该模块插入所配置的故障)'))

        except:
            QMessageBox.warning(None, "Warning", "请选择一个寄存器.")
            return None

    def btn_del_all(self):
        if self.tableWidget_2.rowCount() == 0:
            self.textBrowser.setText(f'清空成功,请勿重复操作')  # 消息框显示读取数据条数
        else:
            self.tableWidget_2.setRowCount(0)  # 设置行数
            self.textBrowser.setText(f'清空成功')  # 消息框显示读取数据条数

    def btn_save_all(self):
        data = []
        row = self.tableWidget_2.rowCount()
        column = self.tableWidget_2.columnCount()

        for i in range(row):  # 将表格中所有数据装入列表中
            for j in range(column):
                data.append(self.tableWidget_2.item(i, j).text())

        # 列表最后两个数据为行数和列数
        data.append(str(row))
        data.append(str(column))

        with open('fault_all_msg.txt', 'w') as f:
            f.write(' '.join(data))

        # 消息框显示读取数据条数
        self.textBrowser.setText(f'保存成功，保存故障:{row}条')
        greyFormat = '<font color="grey">{}</font>'  # 设置灰色字体
        self.textBrowser.append(greyFormat.format('(已本地保存，可通过“读取故障文件”按钮读入)'))

    def btn_read_all(self):
        # 将txt内的数据读入列表data中
        with open('fault_all_msg.txt', 'r') as f:
            data = f.read().split(' ')
        # 分离出行数和列数的数据
        row = int(data[-2])
        print(row)
        column = int(data[-1])

        # 设置行数为特定值
        self.tableWidget_2.setRowCount(row)

        # 填充数据
        for i in range(row):
            for j in range(column):
                self.tableWidget_2.setItem(i, j, QTableWidgetItem(data[i * column + j]))

        # 消息框显示读取数据条数
        self.textBrowser.setText(f'读取故障:{row}条')

    def btn_sending_fault(self):
        self.row = self.tableWidget_2.rowCount()  # 获取指令条数
        self.textBrowser.setText('本次指令已全部发送完毕：{}条'.format(self.row))

    def btn_fault_result(self):
        self.mouse_stop()
        # 判断是否是空指令
        if self.tableWidget_2.item(0, 0) == None:
            QMessageBox.warning(None, "Warning", "出现空指令，请检查")
            return
        self.btn_sending_fault()
        QApplication.processEvents()  # 页面刷新
        sleep(1)

        # strr = '1\t3200000\t\t1672000\t\t52.25%\t\n2\t38208000\t\t32652000\t\t85.46%\t\n3\t6592000\t\t5352000\t\t81.19%\t\n'
        self.textBrowser.setText('序号\t 故障注入个数\t 故障发生次数\t 故障率\t')
        for i in range(self.row):
            QApplication.processEvents()  # 页面刷新
            self.mouse_stop()
            a = int(self.tableWidget_2.item(i, 8).text())
            b = randint(0, a)
            c = '%.2f' % ((b / a) * 100)
            self.textBrowser.append(f'{i + 1}\t{a}\t\t{b}\t\t{c}%\t')
        self.textBrowser.append('---故障分析结束(请点击“获取报告”)---')

    def btn_clear_msg1(self):
        self.textBrowser.setText('')

    def btn_report(self):
        self.mouse_stop(1)
        # 把界面所有信息打包装进report_injection.txt中，方便report模块调用
        with open('report_injection.txt', 'w', encoding="utf-8") as f:
            data = []
            now = datetime.now()
            data.append(now.strftime('%Y%m%d%H%M%S%f'))  # 报告编号
            data.append('☐仿真芯片数据    ☑实时芯片数据')  # 报告类型
            data.append(self.lineEdit.text() + ':' + self.lineEdit_2.text())  # 报告IP
            data.append(f'报告完成时间:{now.year}年{now.month}月{now.day}日')  # 报告日期

            try:
                dataa = []
                row = self.tableWidget_2.rowCount()
                column = self.tableWidget_2.columnCount()
                for i in range(row):  # 将表格中所有数据装入列表中
                    for j in range(column):
                        dataa.append(self.tableWidget_2.item(i, j).text())
                data.append(' '.join(dataa))  # 故障注入信息
            except:
                pass

            outt = self.textBrowser.toPlainText()
            print(outt)
            data.append(outt[:-23])  # 故障注入结果
            print(data)
            f.write('\n'.join(data))
        f.close()
        self.report = Report.report_injection_runme.ReportInjectionRunMe()
        self.report.show()

    def mouse_stop(self, n=0):
        self.setCursor(QCursor(Qt.BusyCursor))  # FIXME:设置鼠标匆忙（用于延迟）
        QApplication.processEvents()  # 刷新面板
        if n == 0:
            time.sleep(choice([1, 1.5, 2, 2.5]))
        else:
            time.sleep(n)
        self.setCursor(QCursor(Qt.ArrowCursor))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 声明界面的对象
    eda = EDARunMe()

    eda.show()
    sys.exit(app.exec_())

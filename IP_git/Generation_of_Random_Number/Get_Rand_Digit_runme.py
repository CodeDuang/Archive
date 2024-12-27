import sys
from random import choice, randint

from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog

from Generation_of_Random_Number import Get_Rand_Digit


class GetRandDigitRunMe(QMainWindow, Get_Rand_Digit.Ui_MainWindow):
    def __init__(self):
        super(GetRandDigitRunMe, self).__init__()
        self.setupUi(self)
        self.initt()
        self.setWindowTitle('随机数生成')
        self.thread = None  # 初始化线程

        # # 禁止放大缩小窗口
        # self.setFixedSize(self.width(), self.height())  # 设置窗口固定大小
        # self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)  # 禁用放大按钮
        # self.setWindowFlags(self.windowFlags() & ~Qt.WindowMinimizeButtonHint)  # 禁用缩小按钮

    def initt(self):
        self.pushButton.clicked.connect(self.btn_output)  # “读出”按钮
        self.pushButton_2.clicked.connect(self.btn_clear)  # "清空"按钮
        self.pushButton_3.clicked.connect(self.btn_save)  # 保存




    def btn_save(self):
        filepath, typee = QFileDialog.getSaveFileName(None, "文件保存", "/",
                                                      'hex(*.hex)')  # 前面是地址，后面是文件类型,得到输入地址的文件名和地址txt(*.txt*.xls);;image(*.png)不同类别
        if filepath != '':
            with open('.tmp', 'r') as f:
                data = f.read()
            f.close()  # 释放文件占用
            with open(filepath, 'w') as ff:
                ff.write(data)
            ff.close()  # 释放文件占用
            self.textBrowser.append('文件保存成功,目录：' + filepath)
            print(filepath)

    def btn_output(self):
        self.btn_clear()  # 先调用清空按钮
        # 1.读取信息，判断格式是否正确
        lon = self.lineEdit.text()
        if lon == '':
            QMessageBox.warning(None, "Warning", "请输入需要读出的字节数.")
            return
        try:
            lon = int(lon)  # 字节长度
        except:
            QMessageBox.warning(None, "Warning", "请输入数字.")
            return

        # 2.以下为根据需要随机数的大小，保存随机数的具体文本()()
        if self.comboBox_2.currentText() == 'K位':
            if lon >= 1024:  # 先把1mb部分解决
                for i in range(lon // 1024):
                    num = randint(1, 20)
                    with open('test/'+str(num) + '.hex', 'r') as f:
                        data = f.read()
                        randd = randint(1, 1000)
                        data = data[randd:] + data[:randd]  # 重组一下字符串，进一步打乱
                        with open('.tmp', 'a') as ff:  # 追加写入文件夹内
                            ff.write(data)
                    f.close()  # 释放文件占用
            lon = lon % 1024  # 获取小于1mb的部分
            lon *= 1024  # 获取有多少个16位
            num = randint(1, 20)
            with open('test/'+str(num) + '.hex', 'r') as f:
                data = f.read()[:lon]
                randd = randint(0, lon - 1)
                data = data[randd:] + data[:randd]
                with open('.tmp', 'a') as ff:  # 追加写入文件夹内
                    ff.write(data)
                ff.close()  # 释放文件占用
            f.close()  # 释放文件占用
        elif self.comboBox_2.currentText() == 'M位':  # 当读取的长度为MB时
            for i in range(lon):  # 遍历lon次1mb文件
                # 1.显示进度动态增长
                self.textBrowser.setText(f'随机数过大，请点击“下载”，在文件中查看\n随机数生成进度：{i * 100 / lon}%')
                QApplication.processEvents()  # 刷新面板
                # 2.生成预备文件
                num = randint(1, 20)
                with open('test/'+str(num) + '.hex', 'r') as f:
                    data = f.read()
                    randd = randint(1, 1000)
                    data = data[randd:] + data[:randd]  # 重组一下字符串，进一步打乱
                    with open('.tmp', 'a') as ff:  # 追加写入文件夹内
                        ff.write(data)
                    ff.close()  # 释放文件占用
                f.close()  # 释放文件占用
        else:  # 当读取长度位个的时候
            if lon >= 1024:
                QMessageBox.warning(None, "Warning", "数字过大，请增加单位.")
                return
            data = []
            for i in range(lon):
                data.append(choice("0123456789abcdef"))
            data = ''.join(data)
            with open('.tmp', 'a') as ff:  # 追加写入文件夹内
                ff.write(data)
            ff.close()  # 释放文件占用

        print("保存成功")

        # 3.显示（判断情况）
        if (self.comboBox_2.currentText() == 'K位' and int(
                self.lineEdit.text()) < 201) or self.comboBox_2.currentText() == '位':  # 当数据量很小，可以直接预览的时候，调用线程动态生成数据
            self.open_log()  # 开启线程

        else:  # 否则，不允许预览，让用户生成文件以查看
            self.textBrowser.setText('随机数过大，请点击生成文件，在文件中查看')
            if self.comboBox_2.currentText() == 'K位':
                self.textBrowser.append('随机数生成进度：100%')
                self.textBrowser.append('——随机数生成结束———')
            else:
                self.textBrowser.setText(f'随机数过大，请点击生成文件，在文件中查看\n随机数生成进度：100%')
                QApplication.processEvents()  # 刷新面板
                self.textBrowser.append('——随机数生成结束———')

        self.pushButton_3.setEnabled(True)
        self.pushButton_2.setEnabled(True)

    def btn_clear(self):
        f = open('.tmp', 'w')
        f.close()
        self.textBrowser.clear()
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(False)

    def open_log(self):
        # 创建线程
        self.thread = RunthreadLog()
        # 连接信号
        self.thread._signal.connect(self.append_line)  # 线程连接回传到GUI的事件
        # 开始线程
        self.thread.start()

    def append_line(self, line):
        self.textBrowser.append(line)
        # print("线程运行中")


# 线程类（用于显示随机生成的数字到textBrowser
class RunthreadLog(QtCore.QThread):
    #  通过类成员对象定义信号对象
    _signal = pyqtSignal(str)

    def __init__(self):
        super(RunthreadLog, self).__init__()

    # 实时加载文件的更新内容并输出到textBrowser
    def run(self):
        f = open('.tmp', 'r', encoding='utf-8')
        while 1:
            where = f.tell()  # 返回文件指针的位置
            line = f.read(1044)  # 每次读取100字节内容
            if not line:
                break
            else:
                self._signal.emit(line)
        f.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    a = GetRandDigitRunMe()
    a.show()
    sys.exit(app.exec_())

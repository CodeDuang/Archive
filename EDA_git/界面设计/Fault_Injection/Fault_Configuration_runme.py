import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QMainWindow
from matplotlib.backends.backend_qt import MainWindow

import Fault_Injection.Fault_Configuration


class FaultConfigurationRunMe(QMainWindow, Fault_Injection.Fault_Configuration.Ui_MainWindow):
    def __init__(self):
        super(FaultConfigurationRunMe, self).__init__()
        self.setupUi(self)
        self.initt()  # 初始化以及按钮绑定
        self.setWindowTitle("故障配置参数")  # 设置标题
        self.setFixedSize(self.width(), self.height())  # 禁止缩放

    def initt(self):
        self.pushButton_3.clicked.connect(self.btn_fault_save)  # 保存故障默认配置到文件夹内
        self.pushButton_4.clicked.connect(self.btn_quit)  # 取消保存退出

        with open('fault_set.txt', 'r') as f:
            data = f.read().split(' ')  # 将默认配置读入data中

        # 默认配置填充到界面
        self.lineEdit.setText(data[0])
        self.lineEdit_3.setText(data[1])
        self.comboBox_2.setCurrentIndex(int(data[-1]))  # data[2]是文字 data[-1]是索引
        self.lineEdit_5.setText(data[3])
        self.lineEdit_6.setText(data[4])
        self.lineEdit_7.setText(data[5])

    def btn_quit(self):
        self.close()
        # QCoreApplication.instance().quit()

    def btn_fault_save(self):
        # 将页面的配置信息全部存入data列表中
        data = []
        data.append(self.lineEdit.text())
        data.append(self.lineEdit_3.text())
        data.append(self.comboBox_2.currentText())
        data.append(self.lineEdit_5.text())
        data.append(self.lineEdit_6.text())
        data.append(self.lineEdit_7.text())
        data.append(str(self.comboBox_2.currentIndex()))
        print(data)

        # 将data列表信息
        with open('fault_set.txt', 'w') as f:
            f.write(' '.join(data))
        f.close()
        self.close()
        # QCoreApplication.instance().quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    f = FaultConfigurationRunMe()
    f.show()
    sys.exit(app.exec_())

import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QMainWindow
from matplotlib.backends.backend_qt import MainWindow

import Trojan_Analysis.InputData


class InputDataRunMe(QMainWindow, Trojan_Analysis.InputData.Ui_MainWindow):
    def __init__(self):
        super(InputDataRunMe, self).__init__()
        self.setupUi(self)
        self.initt()
        self.setWindowTitle("数据输入配置")  # 设置标题
        self.setFixedSize(self.width(), self.height())  # 禁止缩放

    def initt(self):
        self.comboBox.setCurrentIndex(1)

        self.pushButton.clicked.connect(self.btn_save)
        self.pushButton_2.clicked.connect(self.btn_close)

        try:
            with open('data.txt', 'r') as f: #通过读取data.txt读入默认配置
                data = f.read().split('\n')
                self.textEdit.setText(data[1])
                self.textEdit_2.setText(data[3])
                self.textEdit_3.setText(data[5])
                self.textEdit_4.setText(data[7])
                self.textEdit_5.setText(data[9])
        except:
            pass

    def btn_save(self):
        d = []
        d.append(str(self.comboBox.currentText()))
        d.append('\n')
        d.append(self.textEdit.toPlainText())
        d.append('\n')
        d.append(str(self.comboBox_2.currentText()))
        d.append('\n')
        d.append(self.textEdit_2.toPlainText())
        d.append('\n')
        d.append(str(self.comboBox_3.currentText()))
        d.append('\n')
        d.append(self.textEdit_3.toPlainText())
        d.append('\n')
        d.append(str(self.comboBox_4.currentText()))
        d.append('\n')
        d.append(self.textEdit_4.toPlainText())
        d.append('\n')
        d.append(str(self.comboBox_5.currentText()))
        d.append('\n')
        d.append(self.textEdit_5.toPlainText())
        with open("data.txt", 'w') as f:
            f.write(''.join(d))
        # QCoreApplication.instance().quit()
        self.close()

    def btn_close(self):
        # QCoreApplication.instance().quit()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # main = MainWindow()
    # self = InputData.Ui_MainWindow()
    # self.setupUi(main)
    # 
    # # 绑定按钮的点击事件
    # initt()

    # main.show()
    a = InputDataRunMe()
    a.show()
    sys.exit(app.exec_())

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox

import Algorithm_Threshold_Detection


class SettingRunMe(QMainWindow, Algorithm_Threshold_Detection.Setting.Ui_MainWindow):
    def __init__(self):
        super(SettingRunMe, self).__init__()
        self.setupUi(self)
        self.initt()
        self.setWindowTitle("门限设置")
        self.setFixedSize(self.width(), self.height())  # 禁止缩放

    def initt(self):
        self.pushButton_2.clicked.connect(self.btn_file)
        self.pushButton.clicked.connect(self.btn_save)  # 保存

        self.data_load()  # 初始化信息

    def data_load(self):
        try:
            with open('setting.txt', 'r') as f:
                data = f.read().split('\n')
                self.lineEdit.setText(data[0])
                self.lineEdit_2.setText(data[1])
                self.comboBox.setCurrentIndex(int(data[2]))
                self.comboBox_2.setCurrentIndex(int(data[3]))
                self.comboBox_3.setCurrentIndex(int(data[4]))
                self.lineEdit_4.setText(data[5])
                self.lineEdit_5.setText(data[6])
            self.close()
        except:
            return

    def btn_file(self):
        filename = QFileDialog.getOpenFileName(None, "选取攻击模型", "./", "All Files (*)")
        self.lineEdit_3.setText(filename[0])
        # self.textBrowser.setText('文件打开成功,目录：' + filename[0])
        print(filename)

    def btn_save(self):
        with open('setting.txt', 'w') as f:
            try:
                a = int(self.lineEdit.text())
            except:
                QMessageBox.warning(None, "Warning", "密钥长度输入错误.")
                return
            data = []
            if a > 1000:
                QMessageBox.warning(None, "Warning", "密钥长度输入过大，请小于1000.")
                return
            data.append(str(a))
            data.append(self.lineEdit_2.text())
            data.append(str(self.comboBox.currentIndex()))
            data.append(str(self.comboBox_2.currentIndex()))
            data.append(str(self.comboBox_3.currentIndex()))
            data.append(self.lineEdit_4.text())
            data.append(self.lineEdit_5.text())  # FIXME:记得将该页面的信息装入data数组
            f.write('\n'.join(data))
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 定义界面
    sett = SettingRunMe()

    # 展示界面
    sett.show()

    sys.exit(app.exec_())

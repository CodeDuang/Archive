import sys
from random import randint

from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication

from Load import Loading


# 异步类
class WorkerThread(QThread):
    # 自定义信号，用于在任务完成时发射信号
    result_signal = pyqtSignal(int)

    def run(self):
        count = 0
        while count < 13:
            count += 1
            self.result_signal.emit(count)
            a = randint(50, 2000)
            self.msleep(a)  # 休眠1秒，模拟耗时任务


class LoadingRunMe(QMainWindow, Loading.Ui_MainWindow):
    def __init__(self):
        super(LoadingRunMe, self).__init__()
        self.setupUi(self)
        self.initt()
        self.setFixedSize(self.width(), self.height())  # 禁止缩放
        # 隐藏边框
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)  # 隐藏边框并在其他边框之上
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置背景透明

    def initt(self):
        # 创建并启动工作线程
        self.worker_thread = WorkerThread()
        self.worker_thread.result_signal.connect(self.update_ui)
        self.worker_thread.start()

    def update_ui(self, count):
        if count == 1:
            self.label.setText(f"正在加载Algorithm...")
            QApplication.processEvents()  # 刷新面板
        elif count == 2:
            self.label.setText(f"正在加载Threshold...")
            QApplication.processEvents()  # 刷新面板
        elif count == 3:
            self.label.setText(f"正在加载Detection...")
            QApplication.processEvents()  # 刷新面板
        elif count == 4:
            self.label.setText(f"正在加载Analysis...")
            QApplication.processEvents()  # 刷新面板
        elif count == 5:
            self.label.setText(f"正在加载Channel...")
            QApplication.processEvents()  # 刷新面板
        elif count == 6:
            self.label.setText(f"正在加载Leakage...")
            QApplication.processEvents()  # 刷新面板
        elif count == 7:
            self.label.setText(f"正在加载Fault...")
            QApplication.processEvents()  # 刷新面板
        elif count == 8:
            self.label.setText(f"正在加载Injection...")
            QApplication.processEvents()  # 刷新面板
        elif count == 9:
            self.label.setText(f"正在加载Security Check...")
            QApplication.processEvents()  # 刷新面板
        elif count == 10:
            self.label.setText(f"正在进入Layout...")
            QApplication.processEvents()  # 刷新面板
        elif count == 11:
            self.label.setText(f"正在初始化...")
            QApplication.processEvents()  # 刷新面板
        elif count == 12:
            self.time_out()

    def time_out(self):
        pass


if __name__ == "__main__":
    ######使用下面的方式一定程度上可以解决界面模糊问题--解决电脑缩放比例问题
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    # # 适应高DPI设备
    # QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    # 解决图片在不同分辨率显示模糊问题
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)


    app = QApplication(sys.argv)
    # 定义页面对象
    loadd = LoadingRunMe()  # 综合导航栏界面

    loadd.show()
    sys.exit(app.exec_())

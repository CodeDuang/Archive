import sys

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QMainWindow, QApplication

from Generation_of_Random_Number import Get_Rand_Digit_runme
from Help.About_runme import AboutRunMe
from Help.BUG_runme import BUGRunMe
from Help.Help_runme import HelpRunMe
from Help.Know_runme import KnowRunMe
from Large_Number_Operation import Big_Num_View_runme, Big_Num_Logical_Operation_runme, Big_Num_Mod_Operation_runme, \
    Big_Num_Count_runme
from Hash_Operator import Get_Hash_Operator, Get_Hash_Operator_runme

from Elliptic_Operator import Get_Elliptic_Operator, Get_Elliptic_Operator_runme, SM2
from Load.Loading_runme import LoadingRunMe, WorkerThread
import All_start


class AllStartRunMe(QMainWindow, All_start.Ui_MainWindow):
    def __init__(self):
        super(AllStartRunMe, self).__init__()
        self.setupUi(self)
        self.initt()
        self.setWindowTitle("安全加速引擎IP核")  # 设置标题
        self.setStyleSheet("#MainWindow{background-color:#fff}")

        # # 禁止放大缩小窗口
        # self.setFixedSize(self.width(), self.height())  # 设置窗口固定大小
        # # self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)  # 禁用放大按钮
        # self.setWindowFlags(self.windowFlags() & ~Qt.WindowMinimizeButtonHint)  # 禁用缩小按钮

    def initt(self):
        self.pushButton.clicked.connect(self.btn_Big_Num)  # 大数运算
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.pushButton_3.clicked.connect(self.btn_Get_Rand_Digit)  # 侧行道泄露分析
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.pushButton_2.clicked.connect(self.btn_Get_Hash_Operator)  # 哈希函数算子
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.pushButton_4.clicked.connect(self.btn_Get_Elliptic_Operator)  # 椭圆曲线算子
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))

        # 菜单项
        self.actionexit.triggered.connect(self.close)  # 退出
        self.actionMinimize.triggered.connect(self.showMinimized)  # 最小化
        self.actionPreference.triggered.connect(self.menu_action_BUG)  # 提交BUG
        self.action_6.triggered.connect(self.menu_jump_1)  # 哈希函数算子
        self.action_7.triggered.connect(self.menu_jump_2)  # 随机数生成
        self.action_10.triggered.connect(self.menu_jump_3_1)  # 大数逻辑运算
        self.action_11.triggered.connect(self.menu_jump_3_2)  # 大数算数运算
        self.action_12.triggered.connect(self.menu_jump_3_3)  # 大数模运算
        self.action_9.triggered.connect(self.menu_jump_4)  # 椭圆曲线算子
        self.action_IP.triggered.connect(self.menu_jump_about)  # 关于IP核心
        self.action_3.triggered.connect(self.menu_open_know)  # 了解文档
        self.action_4.triggered.connect(self.menu_open_know)  # 了解文档
        self.action_5.triggered.connect(self.menu_open_know)  # 了解文档
        self.action_8.triggered.connect(self.menu_open_know)  # 了解文档
        self.action_13.triggered.connect(self.menu_open_help)  # 帮助文档

    # 设置tabWidget页面向左移动一个
    def btn_Left(self):
        now_num = self.tabWidget.currentIndex()
        if now_num <= 0:
            return
        else:
            now_num -= 1
        self.tabWidget.setCurrentIndex(now_num)

    def btn_Right(self):
        now_num = self.tabWidget.currentIndex()
        if now_num >= 3:
            return
        else:
            now_num += 1
        self.tabWidget.setCurrentIndex(now_num)

    def btn_Big_Num(self):
        bigview.show()
        self.hide()

    def btn_Get_Rand_Digit(self):
        rand.show()
        self.hide()

    def btn_Get_Hash_Operator(self):  # 哈希函数算子界面
        hashh.show()
        self.hide()

    def btn_Get_Elliptic_Operator(self):  # 椭圆曲线算子界面
        ellip.show()
        self.hide()

    def menu_action_BUG(self):  # 提交Bug
        self.bug = BUGRunMe()
        self.bug.show()

    def menu_jump_1(self):  # 哈希函数算子
        hashh.show()
        self.hide()

    def menu_jump_2(self):  # 随机数生成
        rand.show()
        self.hide()

    def menu_jump_3_1(self):  # 大数逻辑运算
        logical.show()
        self.hide()

    def menu_jump_3_2(self):  # 大数算数运算
        countt.show()
        self.hide()

    def menu_jump_3_3(self):  # 大数模运算
        mod.show()
        self.hide()

    def menu_jump_4(self):  # 椭圆曲线算子
        ellip.show()
        self.hide()

    def menu_jump_about(self):  # 关于
        about.show()

    def menu_open_know(self): #了解
        know.show()

    def menu_open_help(self): #帮助
        helpp.show()


# 继承Loading.LoadingRunMe,以方便在该类中设置定时器，消失后调取主页面(复写了time_out())
class Loadd(LoadingRunMe):
    def __init__(self):
        super(Loadd, self).__init__()

    def time_out(self):
        # 创建定时器，设置定时器的超时槽函数为关闭登录窗口和打开主页面的函数
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.close_and_open_main)
        # timee = randint(5000,10000)
        self.timer.start(1)  # 设置定时器的间隔为1毫秒（即一调用该函数就超时）

    def close_and_open_main(self):
        self.timer.stop()  # 停止定时器
        self.close()  # 关闭登录窗口
        # all_start = AllStartRunMe()  # 综合导航栏界面
        all_start.show()


# 重绘椭圆曲线算子界面
class GetEllipticOperator(Get_Elliptic_Operator_runme.GetEllipticOperatorRunMe):
    def __init__(self):
        super(GetEllipticOperator, self).__init__()

        # 菜单项
        self.action_4.triggered.connect(self.close)  # 退出
        self.action_3.triggered.connect(self.showMinimized)  # 最小化
        self.action_5.triggered.connect(self.showMaximized)  # 最大化
        self.action_6.triggered.connect(self.showNormal)  # 还原
        self.actionBug_submit.triggered.connect(self.menu_action_BUG)  # 提交BUG
        self.action_7.triggered.connect(self.menu_jump_1)  # 哈希函数算子
        self.action_8.triggered.connect(self.menu_jump_2)  # 随机数生成
        self.action_10.triggered.connect(self.menu_jump_3_1)  # 大数逻辑运算
        self.action_11.triggered.connect(self.menu_jump_3_2)  # 大数算数运算
        self.action_12.triggered.connect(self.menu_jump_3_3)  # 大数模运算
        # self.action_13.triggered.connect(self.menu_jump_4)  # 椭圆曲线算子
        self.action_14.triggered.connect(self.home)  # 导航
        self.action_9.triggered.connect(self.menu_open_help) #帮助文档

    # 点击右上角叉叉触发事件
    def closeEvent(self, event):  # 函数名固定不可变
        self.hide()
        all_start.show()

    def menu_action_BUG(self):  # 提交Bug
        self.bug = BUGRunMe()
        self.bug.show()

    def menu_jump_1(self):  # 哈希函数算子
        hashh.show()
        self.hide()

    def menu_jump_2(self):  # 随机数生成
        rand.show()
        self.hide()

    def menu_jump_3_1(self):  # 大数逻辑运算
        logical.show()
        self.hide()

    def menu_jump_3_2(self):  # 大数算数运算
        countt.show()
        self.hide()

    def menu_jump_3_3(self):  # 大数模运算
        mod.show()
        self.hide()

    def menu_jump_4(self):  # 椭圆曲线算子
        ellip.show()
        self.hide()

    def home(self):  # 导航页面
        all_start.show()
        self.hide()

    def menu_open_help(self): #帮助
        helpp.show()


# 重绘获取随机数界面
class GetRandDigit(Get_Rand_Digit_runme.GetRandDigitRunMe):
    def __init__(self):
        super(GetRandDigit, self).__init__()

        # 菜单项
        self.action.triggered.connect(self.close)  # 退出
        self.action_3.triggered.connect(self.showMinimized)  # 最小化
        self.action_4.triggered.connect(self.showMaximized)  # 最大化
        self.action_5.triggered.connect(self.showNormal)  # 还原
        self.actionBug_submit.triggered.connect(self.menu_action_BUG)  # 提交BUG
        self.action_6.triggered.connect(self.menu_jump_1)  # 哈希函数算子
        self.action_7.triggered.connect(self.menu_jump_2)  # 随机数生成
        self.action_9.triggered.connect(self.menu_jump_3_1)  # 大数逻辑运算
        self.action_10.triggered.connect(self.menu_jump_3_2)  # 大数算数运算
        self.action_11.triggered.connect(self.menu_jump_3_3)  # 大数模运算
        self.action_12.triggered.connect(self.menu_jump_4)  # 椭圆曲线算子
        self.action_13.triggered.connect(self.home)  # 导航
        self.action_2.triggered.connect(self.menu_open_help)  # 帮助文档

        # 点击右上角叉叉触发事件

    def closeEvent(self, event):  # 函数名固定不可变
        self.hide()
        all_start.show()

    def menu_action_BUG(self):  # 提交Bug
        self.bug = BUGRunMe()
        self.bug.show()

    def menu_jump_1(self):  # 哈希函数算子
        hashh.show()
        self.hide()

    def menu_jump_2(self):  # 随机数生成
        rand.show()
        self.hide()

    def menu_jump_3_1(self):  # 大数逻辑运算
        logical.show()
        self.hide()

    def menu_jump_3_2(self):  # 大数算数运算
        countt.show()
        self.hide()

    def menu_jump_3_3(self):  # 大数模运算
        mod.show()
        self.hide()

    def menu_jump_4(self):  # 椭圆曲线算子
        ellip.show()
        self.hide()

    def home(self):  # 导航页面
        all_start.show()
        self.hide()
    def menu_open_help(self): #帮助
        helpp.show()


# 重绘哈希函数算子界面
class GetHashOperator(Get_Hash_Operator_runme.GetHashOperatorRunMe):
    def __init__(self):
        super(GetHashOperator, self).__init__()

        # 菜单项
        self.action.triggered.connect(self.close)  # 退出
        self.action_3.triggered.connect(self.showMinimized)  # 最小化
        self.action_4.triggered.connect(self.showMaximized)  # 最大化
        self.action_5.triggered.connect(self.showNormal)  # 还原
        self.actionBug_submit.triggered.connect(self.menu_action_BUG)  # 提交BUG
        self.action_6.triggered.connect(self.menu_jump_1)  # 哈希函数算子
        self.action_7.triggered.connect(self.menu_jump_2)  # 随机数生成
        self.action_9.triggered.connect(self.menu_jump_3_1)  # 大数逻辑运算
        self.action_10.triggered.connect(self.menu_jump_3_2)  # 大数算数运算
        self.action_11.triggered.connect(self.menu_jump_3_3)  # 大数模运算
        self.action_12.triggered.connect(self.menu_jump_4)  # 椭圆曲线算子
        self.action_13.triggered.connect(self.home)  # 导航
        self.action_2.triggered.connect(self.menu_open_help)  # 帮助文档

        # 点击右上角叉叉触发事件

    def closeEvent(self, event):  # 函数名固定不可变
        self.hide()
        all_start.show()

    def menu_action_BUG(self):  # 提交Bug
        self.bug = BUGRunMe()
        self.bug.show()

    def menu_jump_1(self):  # 哈希函数算子
        hashh.show()
        self.hide()

    def menu_jump_2(self):  # 随机数生成
        rand.show()
        self.hide()

    def menu_jump_3_1(self):  # 大数逻辑运算
        logical.show()
        self.hide()

    def menu_jump_3_2(self):  # 大数算数运算
        countt.show()
        self.hide()

    def menu_jump_3_3(self):  # 大数模运算
        mod.show()
        self.hide()

    def menu_jump_4(self):  # 椭圆曲线算子
        ellip.show()
        self.hide()

    def home(self):  # 导航页面
        all_start.show()
        self.hide()
    def menu_open_help(self): #帮助
        helpp.show()


# 重写大数运算导航页面
class BigView(Big_Num_View_runme.Big_Num_View_runme):
    def __init__(self):
        super(BigView, self).__init__()

    def btn_logical_lgorithm(self):
        logical.show()
        self.close()

    def btn_arithmetic_algorithm(self):
        countt.show()
        self.close()

    def btn_modular_operation(self):
        mod.show()
        self.close()



# 重绘算数运算
class BigNumCount(Big_Num_Count_runme.BigNumCountRunMe):
    def __init__(self):
        super(BigNumCount, self).__init__()

        # 菜单项
        self.action.triggered.connect(self.close)  # 退出
        self.action_3.triggered.connect(self.showMinimized)  # 最小化
        self.action_4.triggered.connect(self.showMaximized)  # 最大化
        self.action_5.triggered.connect(self.showNormal)  # 还原
        self.actionBug_submit.triggered.connect(self.menu_action_BUG)  # 提交BUG
        self.action_6.triggered.connect(self.menu_jump_1)  # 哈希函数算子
        self.action_7.triggered.connect(self.menu_jump_2)  # 随机数生成
        self.action_9.triggered.connect(self.menu_jump_3_1)  # 大数逻辑运算
        self.action_10.triggered.connect(self.menu_jump_3_2)  # 大数算数运算
        self.action_11.triggered.connect(self.menu_jump_3_3)  # 大数模运算
        self.action_12.triggered.connect(self.menu_jump_4)  # 椭圆曲线算子
        self.action_13.triggered.connect(self.home)  # 导航
        self.action_2.triggered.connect(self.menu_open_help)  # 帮助文档

        # 点击右上角叉叉触发事件

    def closeEvent(self, event):  # 函数名固定不可变
        self.hide()
        all_start.show()

    def menu_action_BUG(self):  # 提交Bug
        self.bug = BUGRunMe()
        self.bug.show()

    def menu_jump_1(self):  # 哈希函数算子
        hashh.show()
        self.hide()

    def menu_jump_2(self):  # 随机数生成
        rand.show()
        self.hide()

    def menu_jump_3_1(self):  # 大数逻辑运算
        logical.show()
        self.hide()

    def menu_jump_3_2(self):  # 大数算数运算
        countt.show()
        self.hide()

    def menu_jump_3_3(self):  # 大数模运算
        mod.show()
        self.hide()

    def menu_jump_4(self):  # 椭圆曲线算子
        ellip.show()
        self.hide()

    def home(self):  # 导航页面
        all_start.show()
        self.hide()
    def menu_open_help(self): #帮助
        helpp.show()


# 重绘逻辑运算
class BigNumLogicalOperation(Big_Num_Logical_Operation_runme.Big_Num_Logical_Operation_runme):
    def __init__(self):
        super(BigNumLogicalOperation, self).__init__()

        # 菜单项
        self.action.triggered.connect(self.close)  # 退出
        self.action_3.triggered.connect(self.showMinimized)  # 最小化
        self.action_4.triggered.connect(self.showMaximized)  # 最大化
        self.action_5.triggered.connect(self.showNormal)  # 还原
        self.actionBug_submit.triggered.connect(self.menu_action_BUG)  # 提交BUG
        self.action_6.triggered.connect(self.menu_jump_1)  # 哈希函数算子
        self.action_7.triggered.connect(self.menu_jump_2)  # 随机数生成
        self.action_9.triggered.connect(self.menu_jump_3_1)  # 大数逻辑运算
        self.action_10.triggered.connect(self.menu_jump_3_2)  # 大数算数运算
        self.action_11.triggered.connect(self.menu_jump_3_3)  # 大数模运算
        self.action_12.triggered.connect(self.menu_jump_4)  # 椭圆曲线算子
        self.action_13.triggered.connect(self.home)  # 导航
        self.action_2.triggered.connect(self.menu_open_help)  # 帮助文档

        # 点击右上角叉叉触发事件

    def closeEvent(self, event):  # 函数名固定不可变
        self.hide()
        all_start.show()

    def menu_action_BUG(self):  # 提交Bug
        self.bug = BUGRunMe()
        self.bug.show()

    def menu_jump_1(self):  # 哈希函数算子
        hashh.show()
        self.hide()

    def menu_jump_2(self):  # 随机数生成
        rand.show()
        self.hide()

    def menu_jump_3_1(self):  # 大数逻辑运算
        logical.show()
        self.hide()

    def menu_jump_3_2(self):  # 大数算数运算
        countt.show()
        self.hide()

    def menu_jump_3_3(self):  # 大数模运算
        mod.show()
        self.hide()

    def menu_jump_4(self):  # 椭圆曲线算子
        ellip.show()
        self.hide()

    def home(self):  # 导航页面
        all_start.show()
        self.hide()
    def menu_open_help(self): #帮助
        helpp.show()


# 重绘模运算
class BigNumModOperation(Big_Num_Mod_Operation_runme.Big_Num_Mod_Operation_runme):
    def __init__(self):
        super(BigNumModOperation, self).__init__()

        # 菜单项
        self.action.triggered.connect(self.close)  # 退出
        self.action_3.triggered.connect(self.showMinimized)  # 最小化
        self.action_4.triggered.connect(self.showMaximized)  # 最大化
        self.action_5.triggered.connect(self.showNormal)  # 还原
        self.actionBug_submit.triggered.connect(self.menu_action_BUG)  # 提交BUG
        self.action_6.triggered.connect(self.menu_jump_1)  # 哈希函数算子
        self.action_7.triggered.connect(self.menu_jump_2)  # 随机数生成
        self.action_9.triggered.connect(self.menu_jump_3_1)  # 大数逻辑运算
        self.action_10.triggered.connect(self.menu_jump_3_2)  # 大数算数运算
        self.action_11.triggered.connect(self.menu_jump_3_3)  # 大数模运算
        self.action_12.triggered.connect(self.menu_jump_4)  # 椭圆曲线算子
        self.action_13.triggered.connect(self.home)  # 导航
        self.action_2.triggered.connect(self.menu_open_help)  # 帮助文档

        # 点击右上角叉叉触发事件

    def closeEvent(self, event):  # 函数名固定不可变
        self.hide()
        all_start.show()

    def menu_action_BUG(self):  # 提交Bug
        self.bug = BUGRunMe()
        self.bug.show()

    def menu_jump_1(self):  # 哈希函数算子
        hashh.show()
        self.hide()

    def menu_jump_2(self):  # 随机数生成
        rand.show()
        self.hide()

    def menu_jump_3_1(self):  # 大数逻辑运算
        logical.show()
        self.hide()

    def menu_jump_3_2(self):  # 大数算数运算
        countt.show()
        self.hide()

    def menu_jump_3_3(self):  # 大数模运算
        mod.show()
        self.hide()

    def menu_jump_4(self):  # 椭圆曲线算子
        ellip.show()
        self.hide()

    def home(self):  # 导航页面
        all_start.show()
        self.hide()
    def menu_open_help(self): #帮助
        helpp.show()


if __name__ == "__main__":
    ######使用下面的方式一定程度上可以解决界面模糊问题--解决电脑缩放比例问题
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    # # 适应高DPI设备
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    # 解决图片在不同分辨率显示模糊问题
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)

    # 定义页面
    ellip = GetEllipticOperator()  # 椭圆曲线算子界面
    rand = GetRandDigit()  # 获取随机数界面
    hashh = GetHashOperator()  # 哈希函数算子界面
    countt = BigNumCount()  # 算术运算
    logical = BigNumLogicalOperation()  # 逻辑运算
    mod = BigNumModOperation()  # 模运算
    bigview = BigView()  # 大数运算导航
    about = AboutRunMe()  # 关于IP核心
    know = KnowRunMe()  # 了解文档
    helpp = HelpRunMe() #帮助文档

    all_start = AllStartRunMe()  # 综合导航栏界面
    loadd = Loadd()

    loadd.show()
    sys.exit(app.exec_())

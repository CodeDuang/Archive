# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'report.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 993)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.f1 = QtWidgets.QFrame(self.centralwidget)
        self.f1.setGeometry(QtCore.QRect(90, 40, 651, 80))
        self.f1.setObjectName("f1")
        self.formLayout = QtWidgets.QFormLayout(self.f1)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.f1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label)
        self.f2 = QtWidgets.QFrame(self.centralwidget)
        self.f2.setGeometry(QtCore.QRect(740, 40, 231, 80))
        self.f2.setObjectName("f2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.f2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.f2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.f3 = QtWidgets.QFrame(self.centralwidget)
        self.f3.setGeometry(QtCore.QRect(540, 120, 431, 80))
        self.f3.setObjectName("f3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.f3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.f3)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.f3)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.f4 = QtWidgets.QFrame(self.centralwidget)
        self.f4.setGeometry(QtCore.QRect(90, 120, 451, 82))
        self.f4.setObjectName("f4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.f4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.f4)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.checkBox = QtWidgets.QCheckBox(self.f4)
        self.checkBox.setEnabled(False)
        self.checkBox.setCheckable(True)
        self.checkBox.setChecked(False)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.f4)
        self.checkBox_2.setEnabled(False)
        self.checkBox_2.setCheckable(True)
        self.checkBox_2.setChecked(False)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_2.addWidget(self.checkBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.f4)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.f4)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.f5 = QtWidgets.QFrame(self.centralwidget)
        self.f5.setGeometry(QtCore.QRect(90, 200, 341, 31))
        self.f5.setObjectName("f5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.f5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.f5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QtCore.QSize(0, 20))
        self.label_8.setStyleSheet("")
        self.label_8.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.f6 = QtWidgets.QFrame(self.centralwidget)
        self.f6.setGeometry(QtCore.QRect(430, 200, 541, 31))
        self.f6.setObjectName("f6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.f6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_9 = QtWidgets.QLabel(self.f6)
        self.label_9.setMinimumSize(QtCore.QSize(0, 20))
        self.label_9.setStyleSheet("")
        self.label_9.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.f7 = QtWidgets.QFrame(self.centralwidget)
        self.f7.setGeometry(QtCore.QRect(90, 230, 341, 161))
        self.f7.setObjectName("f7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.f7)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_10 = QtWidgets.QLabel(self.f7)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.f8 = QtWidgets.QFrame(self.centralwidget)
        self.f8.setGeometry(QtCore.QRect(90, 390, 341, 161))
        self.f8.setObjectName("f8")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.f8)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_11 = QtWidgets.QLabel(self.f8)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_4.addWidget(self.label_11)
        self.f9 = QtWidgets.QFrame(self.centralwidget)
        self.f9.setGeometry(QtCore.QRect(90, 550, 341, 161))
        self.f9.setObjectName("f9")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.f9)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_12 = QtWidgets.QLabel(self.f9)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_5.addWidget(self.label_12)
        self.f10 = QtWidgets.QFrame(self.centralwidget)
        self.f10.setGeometry(QtCore.QRect(90, 710, 341, 161))
        self.f10.setObjectName("f10")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.f10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_13 = QtWidgets.QLabel(self.f10)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_6.addWidget(self.label_13)
        self.f11 = QtWidgets.QFrame(self.centralwidget)
        self.f11.setGeometry(QtCore.QRect(430, 230, 541, 161))
        self.f11.setObjectName("f11")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.f11)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_15 = QtWidgets.QLabel(self.f11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_15.setWordWrap(True)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_7.addWidget(self.label_15)
        self.f12 = QtWidgets.QFrame(self.centralwidget)
        self.f12.setGeometry(QtCore.QRect(430, 390, 541, 161))
        self.f12.setObjectName("f12")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.f12)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_17 = QtWidgets.QLabel(self.f12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_17.setWordWrap(True)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_8.addWidget(self.label_17)
        self.f13 = QtWidgets.QFrame(self.centralwidget)
        self.f13.setGeometry(QtCore.QRect(430, 550, 541, 161))
        self.f13.setObjectName("f13")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.f13)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_19 = QtWidgets.QLabel(self.f13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_9.addWidget(self.label_19)
        self.f14 = QtWidgets.QFrame(self.centralwidget)
        self.f14.setGeometry(QtCore.QRect(430, 710, 541, 161))
        self.f14.setObjectName("f14")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.f14)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_21 = QtWidgets.QLabel(self.f14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_21.setWordWrap(True)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_10.addWidget(self.label_21)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(880, 880, 93, 28))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "泄露分析报告"))
        self.label_2.setText(_translate("MainWindow", "这里时报告模板的编号"))
        self.label_6.setText(_translate("MainWindow", "报告完成时间："))
        self.label_7.setText(_translate("MainWindow", "2000年1月1日"))
        self.label_3.setText(_translate("MainWindow", "    报告类型："))
        self.checkBox.setText(_translate("MainWindow", "仿真芯片数据"))
        self.checkBox_2.setText(_translate("MainWindow", "实时芯片数据"))
        self.label_4.setText(_translate("MainWindow", "    实时芯片ip端口："))
        self.label_5.setText(_translate("MainWindow", "无                     "))
        self.label_8.setText(_translate("MainWindow", "侧行道分析方法"))
        self.label_9.setText(_translate("MainWindow", "结论"))
        self.label_10.setText(_translate("MainWindow", "DPA(差分功耗分析)"))
        self.label_11.setText(_translate("MainWindow", "TA(模板分析)"))
        self.label_12.setText(_translate("MainWindow", "CPA(相关性功耗分析)"))
        self.label_13.setText(_translate("MainWindow", "SPA(简单功耗分析)"))
        self.label_15.setText(_translate("MainWindow", "  分析原理：使用统计方法分析测量集，以识别数据的相关性\n"
"  分析结果：LSB=1时AES S-box输出见曲线（上），LSB=0时AES S-box输出见曲线（下）"))
        self.label_17.setText(_translate("MainWindow", "  分析原理：利用设备复制品上创建的\"profile\"快速恢复目标设备的密钥\n"
"  分析结果：7647966b7343c29048673252e490f736"))
        self.label_19.setText(_translate("MainWindow", "  分析原理：创建设备的功率模型(汉明权重模型),幂模型越准确，相关性越强\n"
"  分析结果(汉明权重)：0b10000001，0b11111010, 0b111000"))
        self.label_21.setText(_translate("MainWindow", "  分析原理：运行RSA模块化幂运算环路\n"
"  分析结果：1__ 1__ 1__ 0 0 0 1__ 1__ 0 1__ 1__ 0 1__ 1__ 0 0 1__ 1__ 1__ 1__ "))
        self.pushButton.setText(_translate("MainWindow", "生成word"))

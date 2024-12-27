import subprocess
import sys
from random import randint

from PyQt5.QtCore import pyqtSlot, QCoreApplication
from PyQt5.QtWidgets import QApplication, QMainWindow
from matplotlib.backends.backend_qt import MainWindow

import Fault_Injection.HDL


class HDLRunMe(QMainWindow, Fault_Injection.HDL.Ui_MainWindow):
    # data用于存放HDL模型代码，以遍历多个情况
    data = [
        '﻿//flop.v\nmodule flop(data,clock,clear,q,qb);\n		input data,clock,clear;\n		output q,qb;\n \n        nand  #10   nd1(a,data,clock,clear),    //  注意结束时用逗号，最后才用分号\n                    nd2(b,ndata,clock),         // 表示nd1 到nd8 都是nand(与非门)\n                    nd4(d,c,b,clear),\n                    nd5(e,c,nclock),\n                    nd6(f,d,nclock),\n                    nd8(qb,q,f,clear);\n        nand  #9    nd3(c,a,d),\n                    nd7(q,e,qb);\n        not #10     iv1(ndata,data),\n                    iv2(nclock,clock);\nendmodule'
        ,
        '﻿//hardreg.v\n//` include  " flop.v"\nmodule	hardreg(d,clk,clrb,q);\ninput		clk,clrb;\ninput[3:0]	d;\noutput[3:0]	q;\n \nflop	  f1(d[0],clk,clrb,q[0],),   // 注意结束时用逗号，最后才用分号\n          f2(d[1],clk,clrb,q[1],),   // 表示f1 到f4 都是flop\n          f3(d[2],clk,clrb,q[2],),\nf4(d[3],clk,clrb,q[3],);\n \nendmodule'
        ,
        '﻿//hardreg_top.v\n//`include "flop.v"\n//`include " hardreg.v"      //仿真时需要包含文件"hardreg.v" 和 "flop.v" \nmodule  hardreg_top;         //顶层模块，没有输入和输出的端口\nreg clock, clearb;           //为产生测试用的时钟和清零信号需要寄存器 \nreg [3:0] data;           //为产生测试用数据需要用寄存器\nwire [3:0] qout;            //为观察输出信号需要从模块实例端口中引出线\n \n `define  stim  #100 data=4\'b	        //宏定义 stim,可使源程序简洁\n  event  end_first_pass;		        //定义事件end_first_pass\n \nhardreg  reg_4bit (.d(data), .clk(clock), .clrb(clearb), .q(qout));\ninitial\n	begin\n	 clock = 0;\n	 clearb = 1;\n	end	\n	\n	always #50 clock = ~clock;\n	always @(end_first_pass)\n	clearb = ~clearb;\n	always @(posedge clock)\n           $display("at time %0d clearb= %b data= %d qout= %d",\n                      $time, clearb, data, qout);\n/*****************************************************\n    类似于C语言的 printf 语句，可打印不同时刻的信号值\n******************************************************/\ninitial\n	begin\n	repeat(4)		//重复四次产生下面的data变化\n		begin\n			data=4\'b0000;\n			`stim 0001;\n/***************************************************************\n			  宏定义stim引用,等同于 #100 data=4\'b0001；。注意引用时要用 `符号。\n******************************************************/\n			`stim 0010;\n			`stim 0011;\n			`stim 0100;\n			`stim 0101;\n			`stim 0110;\n			`stim 0111;\n			`stim 1000;\n			`stim 1001;\n			`stim 1010;\n			`stim 1011;\n			`stim 1100;\n			`stim 1101;\n			`stim 1110;\n			`stim 1111;\n			#200 -> end_first_pass;\n		 end\n/***********************************************\n延迟200个单位时间，触发事件end_first_pass\n************************************************/\n		$finish;		//结束仿真\n	end\nendmodule'
        ,
        '﻿module add_4( X, Y, sum, C);\ninput [3 : 0] X, Y;\noutput [3: 0] sum;\noutput C;\nassign {C, Sum } = X + Y;//位拼接，c代表高位\nmodule add_16( X, Y, sum, C);\ninput [15 : 0] X, Y;\noutput [15 : 0] sum;\noutput C;\nassign {C, Sum } = X + Y;\nendmodule\n'
        ,
        '﻿module compare_n ( X, Y, XGY, XSY, XEY);\ninput [width-1:0] X, Y;\noutput XGY, XSY, XEY;\nreg XGY, XSY, XEY;\nparameter width = 8;\n\nalways @ ( X or Y ) // 每当X 或Y 变化时\n	begin\n		if ( X = = Y )\n			XEY = 1; // 设置X 等于Y 的信号为1\n		else XEY = 0;\n		if (X > Y)\n			XGY = 1; // 设置X 大于Y 的信号为1\n		else XGY = 0;\n		if (X < Y)\n			XSY = 1; // 设置X 小于Y 的信号为1\n		else XSY = 0;\n	end\nendmodule\n'
        ,
        '﻿module Count8 ( Clk， Reset，Load， Din，Dout)\n        input Clk， Reset，Load;\n        input [7:0] Din;\n        output [7:0] Dout;reg [7:0] Dout;\n        always @ ( posedge Clk or posedge Reset)\n        if( Reset )        \n                Dout<=0;\n        else begin\n                if( Load )        \n                        Dout<=Din;\n                else\n                        Dout<=Dout+1;\n        end\nendmodule\n'
        ,
        '﻿module CombModule ( DataIn，Y1，Y2,Y3);\n        input [3:0] DataIn;\n        output Y1，Y2,Y3;\n        function[ 1:0]CountOnes;ll该函数计算输入变量中1的个数\n        input [3:0] A;\n        integer K;\n        begin\n          CountOnes=O;\n          for ( K=O; K<=3;K++)\n                lf ( A[K] )CountOnes=CountOnes+1;\n        end\n        endfunction\n        assign Y1=DataIn[0]&DataIn[1]&Dataln[2]&Dataln[3];\n        assign Y2=CountOnes ( DataIn)<2;\n        always @ (DataIn)\n         if (DataIn==O) Y3=O;\n         else Y3=1;\nendmodule\n'
        ,
        '﻿module manchester encoding （ enc data，enc ready，clk，reset，data load，data） ； \n        parameter BYT E WIDT H＝8；／／定义一次变 换的字节长为8位； output enc data；／／编码输出； \n        output enc ready；／／编码允许信号，当它为真 时表示前一码序列已经完成；\n        input clk；\n        input reset；／／重起信号； \n        input data load；／／读取数据允许信号； \n        input ［BYT E WIDT H－1：0］ data；／／编码数 据，宽度为8位； \n        reg phase； reg busy；／／忙标志，说明此时不能进入新的编 码过程； \n        wire enc data；\nendmodule'
        ,
        '﻿module parameter(data,clock,clear,q,qb);\n        reg ［2：0］ bit count；／／已完成的 bit 位； \n        reg ［BYT E WIDT H－1：0］ reg data； ／／产生一个（ 相位） 脉冲序列，判断在该周期内 数据变换的策略； \n        always ＠ （ posedge clk） ；／／循环条件：脉冲沿 触发； \n        begin \n         if （ reset） \n                 begin phase＜＝0；／／初始相位信号 \n        end \n        else \n                begin \n                 phase＜＝～phase；／／相位脉冲序列 \n                end \n        end ／／上一个数据编码完成后，当标志 data load 为真，则从存储器中读取数据（ 从第1个相位开始） ， 否则失败；\nendmodule'
        ,
        '﻿module load(clock,qb);\n        always ＠ （ posedge clk） \n        begin \n         if （ phase ＆data load ＆！busy） begin \n                 reg data＜＝data； \n         end \n        end ／／对标志位进行设置：当编码没有完成时设置 busy，当完成时则设置\n ready； \n        always ＠ （ posedge clk） \n        begin \n         if （ reset） begin \n                busy＜＝0；／／busy 的初始化； \n         end \n         else if （ data load ＆phase） begin \n                 busy＜＝1；／／正在处理编码，busy 为真； \n         end \n         else if （ （ bit count ＝＝ BYT E WIDT H－ 1） ＆＆phase） \n                 begin busy＜＝0；／／根据编码 bit 位计数器，编 码完成，busy 为假，ready 为真； \n                 end \n        end\nendmodule'
        ,
        '﻿module load(clock,qb);\n        assign enc ready＝！busy； ／／计算已编码的 bit 位； \n        always ＠ （ posedge clk） \n        begin\n         if （ reset） begin \n                bit count＜＝0；／／初始化； \n         end \n         else if （ phase ＆busy） begin \n                  bit_count ＜＝bit_count ＋1；／／正在编 码，计数； \n         end \n        end ／／根据编码原理，在相位信号为1时编码为原 码，当相位信号为零时对原码取非； \n        always＠ （ posedge clk） \n        begin \n         if （ phase ＆busy） begin \n                 reg data＞＞1；／／reg data［7：0］＜＝ ｛1’b0，reg data［7：1］｝； \n         end \n        end \n        assign enc data ＝ reg data ［0］ ＾ ～ phase；／／输出编码后的数据；\nendmodule'

    ]
    # idx用于定位data数组中的下标
    idx = randint(0, len(data) - 1)

    def __init__(self):
        super(HDLRunMe, self).__init__()
        self.setupUi(self)
        self.initt()
        self.setWindowTitle("HDL模型故障模块")  # 设置标题
        self.setFixedSize(self.width(), self.height())  # 禁止缩放

    def initt(self):
        # 往textEdit装入HDL代码
        # self.textEdit.setPlainText('import sys\nfrom PyQt5.QtWidgets import QApplication\nfrom matplotlib.backends.backend_qt import MainWindow\n\nif __name__ == \"__main__\":\n    app = QApplication(sys.argv)    main = MainWindow()\n    self = HDL模型源码修改.Ui_MainWindow()\n    self.setupUi(main)\n    # 绑定按钮的点击事件\n    initt()\n    main.show()\n    sys.exit(app.exec_())')
        # try:
        #     with open('HDL.txt', 'r') as f:
        #         data = f.read()
        #         self.textEdit.setPlainText(data)
        # except:
        #     pass
        self.textEdit.setPlainText(self.data[self.idx])

        # 更改代码行数显示,其中通过self.textEdit.document().lineCount()读取textEdit代码行数
        self.label_4.setText(str(self.textEdit.document().lineCount()))
        # print(self.textEdit.toPlainText()) #显示textEdit内容

        self.pushButton.clicked.connect(self.btn_save)  # 保存按钮
        self.pushButton_2.clicked.connect(self.btn_quit)  # 关闭按钮

    def btn_save(self):
        # 现在实现的内容是“下一个”按钮
        self.idx += 1
        if self.idx >= len(self.data):
            self.idx = 0
        self.textEdit.setPlainText(self.data[self.idx])
        self.label_4.setText(str(self.textEdit.document().lineCount()))

    # print(self.textEdit.toPlainText())  # 显示textEdit内容
    # 这个只是方便收集文本内容，注意注销这段代码
    # strr = []
    # for i in self.textEdit.toPlainText():
    #     if i == '\n':
    #         # print("\\n", end='')
    #         strr.append("\\n")
    #     elif i == '\'':
    #         strr.append("\\'")
    #     else:
    #         strr.append(i)
    #         # print(i, end='')
    # subprocess.run(['clip.exe'], input=''.join(strr).strip().encode('utf-16'), check=True)  # 将字符串保存到剪切板中（实现复制功能）
    # 保存代码到文本内
    # text = self.textEdit.toPlainText()  # 读取textEdit的内容到text变量中
    # with open('HDL.txt', 'w') as f:
    #     f.write(text)
    # self.pushButton.setEnabled(False)

    def btn_quit(self):
        # QCoreApplication.instance().quit()
        self.close()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     main = MainWindow()
#     HDLui = HDL.Ui_MainWindow()
#     HDLui.setupUi(main)
#     main.setWindowTitle("HDL模型编辑")  # 设置标题
#
#     # 绑定按钮的点击事件（或者初始事件）
#     initt()
#
#     main.show()
#     sys.exit(app.exec_())

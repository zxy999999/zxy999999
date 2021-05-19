# -*- coding: UTF-8 -*- #声明python代码的文本格式是utf-8编码的，也即告诉python解释器要按照utf-8编码的方式来读取程序。
#coding=utf-8

import matplotlib.pyplot as plt #添加依赖
import numpy as np 
# linspace 第一个参数序列起始值, 第二个参数序列结束值,第三个参数为样本数默认50
x = np.linspace(0, 3 * np.pi, 100) #生成一个序列，从0到3π，一共100个点
y = np.sin(x) #根据序x序列的值，生成对应sin的y序列

plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.subplot(1,2,1) #表示将整个图像窗口分为1行2列, 当前位置为1
plt.title(r'$f(x)=sin(x)$') #设置第一个子图的title,f(x)=sin(x),前缀r,R表示自然字符串
#一般用于转义字符l，$作用是将文本加粗斜体
plt.plot(x, y) #在子图中画图 x表示横轴 y表示纵轴
#plt.show()

x1 = [t*0.375*np.pi for t in x] #依据x序列的值，生成对应sin的y1序列
y1 = np.sin(x1) #根据序列的值生成对应sin的y1的序列
plt.subplot(1,2,2) #此处为切成两个横轴的子图，第二个子图中画图1行2列, 当前位置为2
# plt.title(u"测试2") #注意：在前面加一个u
plt.title(r'$f(x)=sin(\omega x), \omega = \frac{3}{8} \pi$') #设置title,\omega表示w,\frac表示分数，\pi表示π
plt.plot(x1, y1) #根据x1,y1画图
plt.show()#显示

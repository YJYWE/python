# coding=utf-8
from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib import font_manager


#x=range(2,26,2)
#y=[15,13,14.5,17,20,25,26,26,27,22,18,15]

#设置中文字体
my_font=font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")
x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]

plt.figure(figsize=(20, 8), dpi=80)

plt.plot(x, y)
_x = list(x)[::5]
_xtick_labels = ["10点{}分 ".format(i) for i in range(60)]
_xtick_labels += ["11点{}分 ".format(i-60) for i in range(60, 120)]
# print(_xtick_labels)
# print(len(_xtick_labels))
# print(_x)
# print(len(_x))
plt.xticks(_x, _xtick_labels[::5], rotation= 45, fontproperties=my_font)

plt.show()

#plt.plot(x,y)
#_xticks_labels=[i/2 for i in range(4,49)]
#plt.xticks(_xticks_labels[::3])
#plt.savefig("./sig_size.png")

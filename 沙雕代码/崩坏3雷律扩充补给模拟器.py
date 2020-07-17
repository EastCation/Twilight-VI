import random
import time
print (time.strftime("现在是%Y年%m月%d日 %H点%M分%S秒", time.localtime()))
print ("欢迎使用雷律扩充补给模拟程序！")
print ("作者：東暘离子(崩坏3ID：星瞳)")
m = input ("请输入你想要的次数，输入完回车....")
#print("m类型是",type(m))
b = random.randint(1,int (m))
#a = [1,2,3,4,5,6,7,8,9,10]
print ("正在抽卡，请稍候")
#b = random.choice([1,2,3,4,5,6,7,8,9,10])
print("恭喜你，在", m, "连中，你的第", b, "次出了雷律！")
print ("感谢游玩本程序，祝你单抽出奇迹，十连直接毕业，再见！！！")

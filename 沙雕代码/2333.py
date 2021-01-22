from random import random

def 爻():
    """占爻，返回YANG或者YIN"""
    a = random()
    if a < 0.5:
        return "YANG"
    else:
        return "YIN"

def 八卦(卦):
    """将三个爻转化为一个八卦"""
    r = 0
    for i,x in enumerate(卦):
        if x == "YANG":
            r += 2**i
    BaGua = ['地', '山', '水', '风', '雷', '火', '泽', '天']
    return BaGua[r]

def 解(卦):
    """解卦，根据所占的六十四卦，在guaci.txt中寻找对应的卦辞并输出。
    卦辞来源百度"""
    下 = 八卦(卦[0:3])
    上 = 八卦(卦[3:])
    dic = {'地': '坤', '山': '艮', '水': '坎', '风': '巽',
           '雷': '震', '火': '离', '泽': '兑', '天': '乾'}
    if 上 == 下:
        卦名 = dic[下] + '为' + 下
    else:
        卦名 = 上 + 下
    filename = 'guaci.txt'
    with open(filename,'r', encoding='utf-8') as f:
        for i in range(256):
            s = f.readline()
            if 卦名 in s:
                return s

def main():
    卦 = []
    with open('wen.txt','r', encoding='utf-8') as f:
        wen = f.readlines()
    for i in range(6):
        input(wen[i])
        y = 爻()
        卦.append(y)
        print(y)
    for i in range(6):
        if 卦[-i-1] == "YANG":
            print("------------")
        else:
            print("----    ----")
    print(解(卦))

main()

# === 电视机模块演示 ===
# 请将本文件拷贝到本机
# 本文件需要安装以下模块：
# * pygame

import turtle
from time import sleep
from pygame import mixer

class TVSet:
    def playChannel(self):
        colors=['black', 'red', 'orange', 'yellow', 'green',
                'cyan', 'blue', 'purple', 'black', 'brown',
                'gray', 'pink']
        self.t.penup()
        self.t.home()
        self.t.pendown()
        self.t.showturtle()
        self.t.shape("turtle")
        self.t.pensize(self.chan + 2)
        self.t.pencolor(colors[self.chan])
        for n in range(15):
            self.t.forward((self.chan + n) * 5)
            self.t.left(360 / self.chan)
        self.t.hideturtle()
        sleep(1.5)

        
    def showScreen(self):
        self.t.reset()
        self.t.hideturtle()
        self.t.penup()
        self.t.goto(-300, 180)
        self.t.pendown()
        self.t.write("节目源：%s\n频道：%d\n音量：%d" %
                     (self.src, self.chan, self.vol),
                     font=("Arial", 16, "normal"))
        
    def showMsg(self, msg):
        self.t.penup()
        self.t.home()
        self.t.pendown()
        self.t.pencolor("black")
        self.t.write(msg, align="center", font=("Arial", 32, "normal"))
        sleep(1.5)
        
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.hideturtle()
        turtle.title("电视机模块演示")
        turtle.setup(width=640, height=480)
        mixer.init()
        mixer.music.load("snd.wav")
        mixer.music.set_volume(0.5)
        self.showMsg("电视机模块演示")
        self.src = "TV"  # 缺省节目源
        self.chan = 1  # 缺省频道
        self.vol = 5  # 缺省音量
        
    def powerOn(self):
        self.showScreen()
        mixer.music.play(loops=-1)
        self.showMsg("电视已开机，欢迎收看！")
        
    def powerOff(self):
        self.showScreen()
        self.showMsg("电视关机中，谢谢收看！")
        mixer.music.fadeout(1000)
        self.t.reset()
        
    def shift(self, source):
        if source not in ("TV", "AV", "HDMI", "USB"):
            self.showMsg("错误！不存在的节目源。")
            return
        self.src = source
        self.showScreen()
        self.showMsg("当前节目源："+self.src)

    def channel(self, n):
        self.chan = n
        self.showScreen()
        self.showMsg("当前频道：%d" % self.chan)
        self.playChannel()
        
    def channelUp(self):
        self.chan += 1
        self.channel(self.chan)
    
    def channelDown(self):
        self.chan -= 1
        self.channel(self.chan)
    
    def volumeUp(self):
        self.vol += 1
        mixer.music.set_volume(self.vol / 10)
        self.showScreen()
        self.showMsg("音量增强到：%d" % self.vol)
    
    def volumeDown(self):
        self.vol -= 1
        mixer.music.set_volume(self.vol / 10)
        self.showScreen()
        self.showMsg("音量减弱到：%d" % self.vol)        


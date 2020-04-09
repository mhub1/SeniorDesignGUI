from tkinter import *
import tkinter as tk
from tkinter.font import Font
from tkinter import messagebox
import time
import random
import gaugelib

class Fullscreen_Example:
    def __init__(self):
        self.window = tk.Tk()
        self.window.attributes('-fullscreen', True)  
        self.fullScreenState = False
        self.window.bind("<F11>", self.toggleFullScreen)
        self.window.bind("<Escape>", self.quitFullScreen)
        a5 = PhotoImage(file="g1.png")
        self.window.tk.call('wm', 'iconphoto', self.window._w, a5)
        self.window.title("Pi-HUD")
        self.window.configure(bg='black')
        self.rpm = 1000
        self.speed = 0
        self.p1 = gaugelib.DrawGauge3(
            self.window,
            max_value=100,
            min_value=0,
            size=600,
            bg_col='black',
            unit = "Speed",bg_sel = 2)
        self.p1.pack(side=tk.LEFT)
        self.p2 = gaugelib.DrawGauge2(
            self.window,
            max_value=10000,
            min_value=0,
            size=600,
            bg_col='black',
            unit = "RPM",bg_sel = 2)
        self.p2.pack(side=tk.RIGHT)
        

        self.read_every_second()
        self.window.mainloop()

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)

    def read_every_second(self):
        self.speed = random.randint(0,120)
        self.p1.set_value(int(self.speed))
        self.rpm = random.randint(0,6000)
        self.p2.set_value(int(self.rpm))
        self.window.after(100, self.read_every_second)

if __name__ == '__main__':
    app = Fullscreen_Example()
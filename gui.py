# -*- coding:utf_8 -*-
import Tkinter as tk
from datetime import date
import webbrowser
import sys

class GUIApp:
    HelloMessage = u"""

****************************************************

Whoami 的中国视频网站动画番剧列表
GUI 版

Author: Whoami
Version: v0.3
Github: https://github.com/MrWhoami/WhoamiBangumi

****************************************************

今天是 {0}
""".format(date.today().strftime('%A'))

    def __init__(self, master):
        # For Chinese printing orz
        self.charset = sys.getfilesystemencoding()
        # Set window
        master.title("Whoami Bangumi")
        master.minsize(480, 360)
        # Menu bar
        menubar = tk.Menu(master)
        sourceMenu = tk.Menu(menubar, tearoff=0)
        sourceMenu.add_command(label="Acfun")
        sourceMenu.add_command(label="BiliBili")
        sourceMenu.add_command(label="PPTV")
        sourceMenu.add_command(label="Iqiyi")
        sourceMenu.add_command(label="Youku")
        sourceMenu.add_separator()
        sourceMenu.add_command(label="Clear", command=self.clearMainFrame)
        menubar.add_cascade(label="Sources", menu=sourceMenu)
        menubar.add_command(label='Search', command=self.callSearchFrame)
        menubar.add_command(label='About', command=self.openAboutLink)
        master.config(menu=menubar)
        # Main Frame
        self.frame = tk.Frame()
        self.frame.pack()
        self.msg = tk.StringVar()
        tk.Label(self.frame,
            textvariable=self.msg,
            wraplength=460,
            justify=tk.CENTER).pack()
        self.clearMainFrame()

    def clearMainFrame(self):
        self.msg.set(self.HelloMessage)

    def callSearchFrame(self):
        # Create a top level widget
        self.searchFrame = tk.Toplevel()
        self.searchFrame.title("Search for bangumi")
        self.searchEntry = tk.Entry(self.searchFrame, width=33)
        self.searchEntry.pack()
        b = tk.Button(self.searchFrame, text="Search", command=self.searchAction)
        b.pack()

    def searchAction(self):
        # Do the searching
        keywords = self.searchEntry.get()
        self.searchFrame.destroy()
        print keywords

    def openAboutLink(self):
        webbrowser.open('https://github.com/MrWhoami/WhoamiBangumi')

    def say_hi(self):
        print "hi there, everyone!"

root = tk.Tk()

app = GUIApp(root)

root.mainloop()

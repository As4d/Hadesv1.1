from tkinter import *
from tkinter import ttk
from Fileinfector import Infector
from UserInfo import UserInfo
import time
import random

class Window:

    def __init__(self, root, title, geometry):
        #root.iconbitmap('hades.ico')

        self.root = root
        self.root.title(title)
        self.root.geometry(geometry)

        self.count = Infector().getNumberOfFiles()

        self.button = Button(root, text="Run", command=self.startProgress)
        self.button.pack()

        #self.displayUserInfo()

        self.root.mainloop()
    
    def displayUserInfo(self):
        FH = open("User.txt", "r")
        info = FH.readlines()
        for line in info:
            info = Label(self.root, text= str(line))
            info.pack()
    
    def startProgress(self):
        progressBar = ttk.Progressbar(self.root, orient=HORIZONTAL, length=300, mode="determinate")
        progressBar.pack()
        increment = 100/self.count
        for i in range(self.count):
            progressBar['value'] += increment
            self.root.update_idletasks()
        Files = Label(self.root, text=str(self.count) + " Files")
        Files.pack()
        time.sleep(1)
        progressBar.destroy()
        UserInfo().updateLastScan()
        
    def outputTips(self):
        lines = open('Tips.txt').read().splitlines()
        label = Label(self.root, text= random.choice(lines))
        label.pack()

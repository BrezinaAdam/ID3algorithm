import tkinter as tk
from tkinter.filedialog import askopenfilename

from parser import *
from id3 import *

class App:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        self.canvas = tk.Canvas(self.frame, width=700, height=500, bg="black")
        self.canvas.pack()

        self.button1 = tk.Button(self.frame, text='open train data', width=10, command=self.openFile)
        self.button1.pack(side="left")

        self.button2 = tk.Button(self.frame, width=10, text='quit', command=self.quit)
        self.button2.pack(side="right")

        self.button3 = tk.Button(self.frame, text='start', width=10, command=self.startTree)
        self.button3.pack()

        self.frame.pack()

        self.filename = None

    def openFile(self):
        self.filename = askopenfilename()
        print self.filename

    def startTree(self):
        if self.filename == None:
            return

        parser = Parser(self.filename)
        parsedFile = parser.getList()

        A = parsedFile[0]
        CL = parsedFile[1]

        id3 = Id3(A, CL)
        nodes = id3.getNodes()

        self.drawNodes(nodes)

    def drawNodes(self, nodeList):
        pass

    def quit(self):
        exit()
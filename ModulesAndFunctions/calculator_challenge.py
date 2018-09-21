#! /usr/local/bin/python3
__author__="tom"
__date__ ="$Apr 9, 2018 5:26:17 AM$"

import tkinter

mainWindow = tkinter.Tk()
mainWindow.title("Calculator")
mainWindow.geometry('200x200-20-20')
mainWindow['padx'] = 10
mainWindow['pady'] = 10

mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1)
mainWindow.columnconfigure(3, weight=1)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=1)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=1)
mainWindow.rowconfigure(4, weight=1)
mainWindow.rowconfigure(5, weight=1)

result = tkinter.Entry(mainWindow)
result.grid(row=0, column=0, columnspan=4, sticky='ew')

clearButton = tkinter.Button(mainWindow, text="C")
clearButton.grid(row=1, column=0, sticky='ew')
clearEntireButton = tkinter.Button(mainWindow, text="CE")
clearEntireButton.grid(row=1, column=1, sticky='ew')

sevenButton = tkinter.Button(mainWindow, text="7")
sevenButton.grid(row=2, column=0, sticky='ew')
eightButton = tkinter.Button(mainWindow, text="8")
eightButton.grid(row=2, column=1, sticky='ew')
nineButton = tkinter.Button(mainWindow, text="9")
nineButton.grid(row=2, column=2, sticky='ew')
plusButton = tkinter.Button(mainWindow, text="+")
plusButton.grid(row=2, column=3, sticky='ew')

fourButton = tkinter.Button(mainWindow, text="4")
fourButton.grid(row=3, column=0, sticky='ew')
fiveButton = tkinter.Button(mainWindow, text="5")
fiveButton.grid(row=3, column=1, sticky='ew')
sixButton = tkinter.Button(mainWindow, text="6")
sixButton.grid(row=3, column=2, sticky='ew')
minusButton = tkinter.Button(mainWindow, text="-")
minusButton.grid(row=3, column=3, sticky='ew')

oneButton = tkinter.Button(mainWindow, text="1")
oneButton.grid(row=4, column=0, sticky='ew')
twoButton = tkinter.Button(mainWindow, text="2")
twoButton.grid(row=4, column=1, sticky='ew')
threeButton = tkinter.Button(mainWindow, text="3")
threeButton.grid(row=4, column=2, sticky='ew')
multButton = tkinter.Button(mainWindow, text="*")
multButton.grid(row=4, column=3, sticky='ew')

zeroButton = tkinter.Button(mainWindow, text="0")
zeroButton.grid(row=5, column=0, sticky='ew')
equalsButton = tkinter.Button(mainWindow, text="=")
equalsButton.grid(row=5, column=1, columnspan=2, sticky='ew')
divButton = tkinter.Button(mainWindow, text="/")
divButton.grid(row=5,column=3, sticky='ew')

mainWindow.update()
mainWindow.minsize(mainWindow.winfo_width(), mainWindow.winfo_height())
mainWindow.mainloop()
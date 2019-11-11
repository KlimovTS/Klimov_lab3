from random import randrange as rnd,choice
import random
from tkinter import*
import math
import time

root=Tk()
fr=Frame(root)
root.geometry('800x600')
canv=Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)

import controls

def o1(a=0):
    global state
    root.bind('<Key-1>', '')
    root.bind('<Key-2>', '')
    state = 1
    gun.answer=1
def o2(a=0):
    global state
    root.bind('<Key-1>', '')
    root.bind('<Key-2>', '')
    state = 2
    controls.answer = 2
    controls.state = 0
def setState(a):
    global state
    state = a

class Menu():
    def __init__(self):
        self.closed=0
    def draw(self):
        canv.delete(ALL)
        txt=''
        txt+='Играть(1)\n'
        txt+='Настройки(2)'
        canv.create_text(400,300,text=txt,font='Verdana 50')
    def Open(self):
        self.closed=0
        root.bind('<Key-1>', o1)
        root.bind('<Key-2>', o2)
    def Close(self):
        self.closed=1

import gun
gun.init(root, canv)
controls.init(root, canv)

i = 0
def Pause(a):
    global i
    if i:
        gun.stop()
    else:
        gun.start()
    i=1-i

state = 0
windows = []
menu = Menu()
windows.append(menu)
windows.append(gun)
windows.append(controls)

def CloseOpen():
    global state, windows
    for i in windows:
        i.Close()
    windows[state].Open()

def window():
    global state
    CloseOpen()
    if state==0:
        menu.draw()
    if state==1:
        gun.game()
        state = gun.answer
    if state==2:
        controls.window()
        state = controls.answer
    root.bind('<Key-'+controls.pauseChar+'>',Pause)
    root.after(16, window)

def sta(a):
    global state
    state = 1-state

root.bind('<Key-space>',sta)

window()
mainloop()
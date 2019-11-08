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

import gun

gun.init(root, canv)
gun.stop()

def Escape():
    gun.stop()

canv.bind('<space>',Escape)

mainloop()
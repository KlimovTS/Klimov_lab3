from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')
width = 800
heigth = 600

canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)

colors = ['red','orange','yellow','green','blue']

i=0
n=0
I="0"
#[Тип, [параметры]]
#0 - круг
#1 - квадрат
Objects=[]

def randCircle():
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    color = choice(colors)
    vx = randint(1, 8)
    vy = randint(1, 8)
    return [0, [x, y, r, color, vx, vy]]

def randSquare():
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    color = choice(colors)
    vx = randint(9, 16)
    vy = randint(9, 16)
    return [1, [x, y, r, color, vx, vy]]

#круги
for j in range(0, 3, 1):
    Objects.append(randCircle())
#квадраты    
for j in range(0, 2, 1):
    Objects.append(randSquare())


def circle(a):
    global width, heigth
    x = a[0]
    y = a[1]
    r = a[2]
    c = a[3]
    vx = a[4]
    vy = a[5]
    canv.create_oval(x-r,y-r,x+r,y+r,fill = c , width=0)
    if x+r>width:
        a[4]=-randint(1, 8)
    if x-r<0:
        a[4]=randint(1, 8)
    if y+r>heigth:
        a[5]=-randint(1, 8)
    if y-r<0:
        a[5]=randint(1, 8)
    a[0]=x+vx
    a[1]=y+vy

def square(a):
    global width, heigth
    x = a[0]
    y = a[1]
    r = a[2]
    c = a[3]
    canv.create_rectangle(x+r, y+r, x-r, y-r, fill=c, width=0)
    if x+r>width:
        a[4]=-randint(9, 16)
    if x-r<0:
        a[4]=randint(9, 16)
    if y+r>heigth:
        a[5]=-randint(9, 16)
    if y-r<0:
        a[5]=randint(9, 16)
    vx = a[4]
    vy = a[5]
    a[0]=x+vx
    a[1]=y+vy

def draw():
    global I, Objects
    canv.delete(ALL)
    canv.create_text(10, 10, text=I, justify=CENTER, font="Verdana 14", anchor=NW)
    for j in Objects:
        if j[0]==0:
            circle(j[1])
        if j[0]==1:
            square(j[1])
    root.after(16,draw)


def click(event):
    global i, n, I, Objects
    print(i, n)
    for j in Objects:
        if j[0]==0:
            if (event.x-j[1][0])*(event.x-j[1][0])+(event.y-j[1][1])*(event.y-j[1][1])<(j[1][2]*j[1][2]):
                Objects.remove(j)
                i+=1
                Objects.append(randCircle())
        if j[0]==1:
            if (((event.x>j[1][0]-j[1][2]) and (event.x<j[1][0]+j[1][2])) and ((event.y>j[1][1]-j[1][2]) and (event.y<j[1][1]+j[1][2]))):
                Objects.remove(j)
                i+=2
                Objects.append(randSquare())
    I=str(i)
    n+=1
    


draw()
canv.bind('<Button-1>', click)
mainloop()
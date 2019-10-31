from tkinter import *
import random
import time
import math

root = Tk()
width = 800
heigth = 600
WH =  str(width)+'x'+str(heigth)
root.geometry(WH)

canv = Canvas(root, width=width, height=heigth, bg='white')
canv.pack()

x=400
y=300
R=50
W=0
A=0
S=0
D=0
vx=0
vy=0
Points = []
Bullets = []
n = 48
for i in range(0, n+2, 1):
    tmpx = R*math.cos(2*math.pi/n*i)
    tmpy = R*math.sin(2*math.pi/n*i)
    Points.append((tmpx, tmpy))
r=R-10
for i in range(0, n+2, 1):
    tmpx = r*math.cos(2*math.pi/n*(n+1-i))
    tmpy = r*math.sin(2*math.pi/n*(n+1-i))
    Points.append((tmpx, tmpy))

def movePoly(points, dx, dy):
    P = []
    for i in points:
        P.append((i[0]+dx, i[1]+dy))
    return P

def circle(x, y, r):
    canv.create_oval(x+r, y+r, x-r, y-r, fill = "red", width=0)

def randBulet():
    global Bullets
    x = random.randint(0, 799)
    x = 400
    y = 0
    r = 5
    n = 1000
    vx = random.randint(-1*n, 1*n)/n
    vy = random.randint(1*n, 15*n)/n
    obj = canv.create_oval(x+r, y+r, x-r, y-r, fill = "red", width=0)
    Bullets.append([x, y, r, vx, vy, obj])
    root.after(1, randBulet)

def bullet(a):
    a[0] += a[3]
    a[1] += a[4]
    x = a[0]
    y = a[1]
    r = a[2]

def circleCircle(x, y):
    global Points
    P = movePoly(Points, x, y)
    canv.create_polygon(P, fill="black", width=0)

def F1(a):
    return a*a

def draw():
    global x, y, r, W, A, S, D, vx, vy, Bullets
    canv.delete(ALL)
    TmpBullets = []
    for i in Bullets:
        bullet(i)
        if i[1]>600:
            i[1] = 0
        if i[0]>800:
            i[0] = 0
        if i[0]<0:
            i[0] = 800
        if (i[0]-x)**2+(i[1]-y)**2<(r+10)**2:
            a=1
        else:
            TmpBullets.append(i)
    Bullets = TmpBullets
    k=0.5
    t1=0.2
    t2=0.99447
    vx+=k*(D-A)
    vy+=k*(S-W)
    vx-=min([math.copysign(t1*math.sqrt((vx**2)/(vx**2+vy**2+0.000001)), vx), vx], key=F1)
    vy-=min([math.copysign(t1*math.sqrt((vy**2)/(vx**2+vy**2+0.000001)), vy), vy], key=F1)
    vx=vx*t2
    vy=vy*t2
    x+=vx
    y+=vy
    circleCircle(x, y)
    circleCircle(x+800, y)
    circleCircle(x-800, y)
    circleCircle(x, y+600)
    circleCircle(x, y-600)
    circleCircle(x+800, y+600)
    circleCircle(x-800, y-600)
    circleCircle(x-800, y+600)
    circleCircle(x+800, y-600)
    if x>800:
        x-=800
    if x<0:
        x+=800
    if y>600:
        y-=600
    if y<0:
        y+=600
    root.after(16, draw)

def clickW(a):
    global W
    W=1

def clickA(a):
    global A
    A=1

def clickS(a):
    global S
    S=1

def clickD(a):
    global D
    D=1

def clickW1(a):
    global W
    W=0

def clickA1(a):
    global A
    A=0

def clickS1(a):
    global S
    S=0
def clickD1(a):
    global D
    D=0

randBulet()
draw()
root.bind('<KeyPress-w>', clickW)
root.bind('<KeyPress-a>', clickA)
root.bind('<KeyPress-s>', clickS)
root.bind('<KeyPress-d>', clickD)
root.bind('<KeyRelease-w>', clickW1)
root.bind('<KeyRelease-a>', clickA1)
root.bind('<KeyRelease-s>', clickS1)
root.bind('<KeyRelease-d>', clickD1)
mainloop()
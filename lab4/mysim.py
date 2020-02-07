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

v=15
K=0.1 # электрическая константа
eForceParticles = []
scale = 30
Particles = []
curId = 0
Perfect  = []

class eForce:
    def __init__(self, x, y, e, r, ownerID):
        global v, scale
        self.owner = ownerID
        n=1000000
        a = random.randint(0, n)
        sin=math.sin(2*math.pi*a/n)
        cos=math.cos(2*math.pi*a/n)
        self.e = e
        self.vx = cos*v
        self.vy = -sin*v
        self.x = x
        self.y = y
        self.range=math.sqrt(self.vx*self.vx+self.vy*self.vy)
    def move(self):
        self.x+=self.vx
        self.y+=self.vy
        self.range+=math.sqrt(self.vx*self.vx+self.vy*self.vy)
    def draw(self):
        global scale
        canv.create_oval(self.x+self.e*scale*0.1, self.y+self.e*scale*0.1, self.x-self.e*scale*0.1, self.y-self.e*scale*0.1, fill = "orange", width=0)
    def checkDelete(self):
        global width, heigth
        if self.x<0 or self.x>width or self.y<0 or self.y>heigth:
            return 1
        else:
            return 0

class Particle:
    def __init__(self, x, y, m, e, vx, vy):
        global  curId
        self.id = curId
        curId+=1
        self.x = x
        self.y = y
        self.m = m
        self.e = e
        self.vx = vx
        self.vy = vy
    def enterract(self, p):
        global K
#        self.vx+=(math.copysign(1, (self.x-p.x))*self.e*p.e*p.vx*K)/self.m
#        self.vy+=(math.copysign(1, (self.y-p.y))*self.e*p.e*p.vy*K)/self.m
        self.vx+=(self.e*p.e*p.vx*K)/(self.m*p.range)
        self.vy+=(self.e*p.e*p.vy*K)/(self.m*p.range)
    def move(self):
        self.x+=self.vx
        self.y+=self.vy
    def illuminate(self):
        global eForceParticles
        n=200
        n=n*math.copysign(self.e, 1)
        n=int(n)
        for i in range(0, n, 1):
            eForceParticles.append(eForce(self.x, self.y, math.copysign(1, self.e), math.copysign(self.e, 1),  self.id))
    def draw(self):
        global scale
        canv.create_oval(self.x+self.e*scale, self.y+self.e*scale, self.x-self.e*scale, self.y-self.e*scale, fill = "red", width=0)
def draw():
    global eForceParticles, Particles, scale, Perfect
    canv.delete(ALL)
    tmpEForceParticles  = []
    for i in eForceParticles:
        a=1
        if i.checkDelete():
            a=0
        for j in Particles:
            if i.owner!=j.id:
                if (i.x-j.x)**2+(i.y-j.y)**2<(j.e*scale)**2:
                    j.enterract(i)
                    a=0
        if a:
            tmpEForceParticles.append(i)
        i.move()
#        i.draw()
    eForceParticles = tmpEForceParticles
    for i in Particles:
        i.illuminate()
        i.move()
        i.draw()
    canv.create_text(20, 20, text=str(int(math.sqrt((Particles[0].x-Particles[1].x)**2+(Particles[0].y-Particles[1].y)**2))))
    root.after(16, draw)

Particles.append(Particle(300, 300-26*0.1, 1000, 1, 0, 0.1))
#Particles.append(Particle(10, 300-26*0.1, 1000, 1, 25, 0))
Particles.append(Particle(500, 300+26*0.1, 1000, -1, 0, -0.1))
Perfect.append(Particle(200, 274, 1000, 1, 0, 1))
Perfect.append(Particle(600, 326, 1000, -1, 0, -1))

draw()
mainloop()

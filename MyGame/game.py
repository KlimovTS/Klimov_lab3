import  MyKeyboard
import tkinter
import math
import random


idCounter = 0
FrameTime = 16

def F1(a):
    return a*a

def mstr(a):
    a=a*100
    b=int(a)
    if (a-b)>=0.5:
        b=b+1
    b=b/100
    return str(b)

def movePoly(points, dx, dy):
    P = []
    for i in points:
        P.append((i[0]+dx, i[1]+dy))
    return P

def rotate(p, a, x, y):
    P = []
    sin = math.sin(a)
    cos = math.cos(a)
    for i in p:
        tmpx=i[0]-x
        tmpy=i[1]-y
        P.append((cos*tmpx+sin*tmpy+x, -sin*tmpx+cos*tmpy+y))
    return P

class Circle():
    def __init__(self, x, y, r, c):
        self.x = x
        self.y = y
        self.r = r
        self.c = c
    def draw(self):
        canv.create_oval(self.x+self.r, self.y+self.r, self.x-self.r, self.y-self.r, fill = self.c, width=0)

class Bullet():
    def __init__(self, owner):
        global idCounter
        self.id = idCounter
        idCounter += 1
        self.owner = owner
        self.circle = Circle(owner.owner.x+rotate([self.owner.position], self.owner.owner.angle, 0, 0)[0][0]*self.owner.owner.extraSize, owner.owner.y+rotate([self.owner.position], self.owner.owner.angle, 0, 0)[0][1]*self.owner.owner.extraSize, owner.bulletRadius*self.owner.owner.extraSize, owner.owner.color)
        n=1000000000
        tmp3 = random.randint(-owner.bulletSpeedY*n, owner.bulletSpeedY*n)/n
        tmp4 = random.randint(0, n)/n
        tmp = math.cos(tmp4*2*math.pi)*tmp3
        tmp2 = math.sin(tmp4*2*math.pi)*tmp3
        self.vx = (math.cos(owner.position[2]+owner.owner.angle)*(owner.bulletSpeedX+tmp2)+math.sin(owner.position[2]+owner.owner.angle)*tmp)*self.owner.owner.extraSize+self.owner.owner.vx
        self.vy = (-math.sin(owner.position[2]+owner.owner.angle)*(owner.bulletSpeedX+tmp2)+math.cos(owner.position[2]+owner.owner.angle)*tmp)*self.owner.owner.extraSize+self.owner.owner.vy
    def move(self):
        self.circle.x+=self.vx
        self.circle.y+=self.vy
    def draw(self):
        self.circle.draw()
    def outside(self):
        global width, heigth
        n = -50
        if self.circle.x<0+n or self.circle.x>width-n or self.circle.y<0+n or self.circle.y>heigth-n:
            return True
        else:
            return False
    def checkHit(self, st2):
        if (self.circle.x-st2.x)**2+(self.circle.y-st2.y)**2<=(self.circle.r+st2.collisionR*st2.extraSize)**2:
            return True
        else:
            return False

class Gun():
    def __init__(self, owner, position):
        global idCounter
        self.id = idCounter
        idCounter += 1
        self.owner = owner
        self.position = position
        self.name = 'Simple Gun'
        self.ReloadingTime = 250
        self.Reloading = 0
        self.bulletSpeedX = 50
        self.bulletSpeedY = 1
        self.bulletDamage = 10
        self.bulletRadius = 5*self.owner.extraSize
        self.bulletCount = 150
        self.bullets = []
    def tick(self):
        global FrameTime, keyboard
        self.Reloading += FrameTime
        if self.Reloading > self.ReloadingTime:
            self.Reloading = self.ReloadingTime
        txt = 'if keyboard.key'+self.owner.controls[4]+'''==1:
            self.shoot()'''
        exec(txt)
        self.targeting()
        for i in self.bullets:
            i.move()
            if i.outside():
                self.bullets.remove(i)
        self.drawBullets()
    def shoot(self):
        if self.Reloading==self.ReloadingTime:
            for i in range(0, self.bulletCount):
                self.bullets.append(Bullet(self))
            self.Reloading=0
    def draw(self):
        canv.create_oval(self.owner.x+rotate([self.position], self.owner.angle, 0, 0)[0][0]*self.owner.extraSize+10*self.owner.extraSize, self.owner.y+rotate([self.position], self.owner.angle, 0, 0)[0][1]*self.owner.extraSize+10*self.owner.extraSize, self.owner.x+rotate([self.position], self.owner.angle, 0, 0)[0][0]*self.owner.extraSize-10*self.owner.extraSize, self.owner.y+rotate([self.position], self.owner.angle, 0, 0)[0][1]*self.owner.extraSize-10*self.owner.extraSize, fill = 'black', width=0)
    def drawBullets(self):
        for i in self.bullets:
            i.draw()
    def targeting(self):
        a=0
        a+=1
    def checkHit(self, st2):
        for i in self.bullets:
            a=i.checkHit(st2)
            if a:
                self.bullets.remove(i)
                if st2.shield >= self.bulletDamage:
                    st2.shield-=self.bulletDamage
                else:
                    tmp = self.bulletDamage-st2.shield
                    st2.shield=0
                    st2.hp-=tmp

class Starship():
    def __init__(self, color = 'grey', controls = ['w', 'a', 's', 'd', 'space']):
        global idCounter, width, heigth
        self.id = idCounter
        idCounter += 1
        self.hullPoly = [(-30, -30), (-30, 30), (60, 0)]
        self.thrustPoly = [(-30, -10), (-30, 10)]
        self.collisionR = 60
        self.color = color
        self.x = random.randint(0, width-1)
        self.y = random.randint(0, heigth-1)
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0
        self.angle = 0
        self.extraSize = 0.5
        self.maxShield = 100
        self.shield = self.maxShield
        self.maxHp = 100
        self.hp =self.maxHp
        self.shieldRegeneration = 0.1
        self.hpRegeneration = 0.01
        self.engineForceAcseleration = 0.1
        self.maxForce = 10
        self.control =  0.5
        self.controls = controls
        self.force = 0
        self.mass = 50
        gunsPositions = [[-20, -30, 0], [-20, 30, 0]]
        self.guns = []
        for i in gunsPositions:
            self.guns.append(Gun(self, i))
    def tick(self):
        self.shield+=self.shieldRegeneration
        if self.shield>self.maxShield:
            self.shield=self.maxShield
        self.hp+=self.hpRegeneration
        if self.hp>self.maxHp:
            self.hp=self.maxHp
        self.move()
        self.draw()
        for i in self.guns:
            i.draw()
        for i in self.guns:
            i.tick()
    def draw(self):
        #canv.create_oval(self.x+self.collisionR*self.extraSize, self.y+self.collisionR*self.extraSize, self.x-self.collisionR*self.extraSize, self.y-self.collisionR*self.extraSize, fill = 'grey', width=0)
        tmp = []
        for  i in self.thrustPoly:
            tmp.append((i[0]*self.extraSize, i[1]*self.extraSize))
        tmp.append(((-30-10*(self.force+1))*self.extraSize, random.randint(-5, 5)*self.extraSize))
        tmp2 = []
        for  i in self.hullPoly:
            tmp2.append((i[0]*self.extraSize, i[1]*self.extraSize))
        canv.create_polygon(rotate(movePoly(tmp2, self.x, self.y), self.angle, self.x, self.y), fill = 'grey', width=0)
        canv.create_polygon(rotate(movePoly(tmp, self.x, self.y), self.angle, self.x, self.y), fill = 'orange', width=0)
    def move(self):
        global width, heigth
#        if keyboard.key9==1:
#            self.extraSize*=0.99
#        if keyboard.key0==1:
#            self.extraSize/=0.99
        txt = 'if keyboard.key'+self.controls[0]+'''==1:
            self.force+=self.engineForceAcseleration
            if self.force > self.maxForce:
                self.force = self.maxForce'''
        exec(txt)
        txt = 'if keyboard.key'+self.controls[2]+'''==1:
            self.force-=3*self.engineForceAcseleration
            if self.force < 0:
                self.force = 0'''
        exec(txt)
        txt = 'if keyboard.key'+self.controls[1]+'''==1:
            da = (0.5+self.control/2)/5/math.sqrt(1+math.sqrt(((self.vx)**2+(self.vy)**2)))
            self.angle += da
            tmpvx = self.vx
            tmpvy = self.vy
            self.vx = math.cos(da*(0.5+self.control/2))*tmpvx + math.sin(da*(0.5+self.control/2))*tmpvy
            self.vy = -math.sin(da*(0.5+self.control/2))*tmpvx + math.cos(da*(0.5+self.control/2))*tmpvy'''
        exec(txt)
        txt = 'if keyboard.key'+self.controls[3]+'''==1:
            da = (0.5+self.control/2)/5/math.sqrt(1+math.sqrt(((self.vx)**2+(self.vy)**2)))
            self.angle -= da
            tmpvx = self.vx
            tmpvy = self.vy
            self.vx = math.cos(-da*(0.5+self.control/2))*tmpvx + math.sin(-da*(0.5+self.control/2))*tmpvy
            self.vy = -math.sin(-da*(0.5+self.control/2))*tmpvx + math.cos(-da*(0.5+self.control/2))*tmpvy'''
        exec(txt)
        #canv.create_text(width/2-1, 60, text = mstr(math.sqrt((self.vx)**2+(self.vy)**2)), font = 'Verdana 30')
        self.ax = self.force/self.mass*math.cos(self.angle)*self.extraSize
        self.ay = -self.force/self.mass*math.sin(self.angle)*self.extraSize
        self.vx+=self.ax
        self.vy+=self.ay
        t1 = 0.025*self.extraSize
        #t2 = 0.99447
        t2 = 0.99
        self.vx-=min([math.copysign(t1*math.sqrt((self.vx**2)/(self.vx**2+self.vy**2+0.000000001)), self.vx), self.vx], key=F1)
        self.vy-=min([math.copysign(t1*math.sqrt((self.vy**2)/(self.vx**2+self.vy**2+0.000000001)), self.vy), self.vy], key=F1)
        self.vx=self.vx*t2
        self.vy=self.vy*t2
        self.x+=self.vx
        self.y+=self.vy
        if self.x>width-1:
            self.x=0
        if self.x<0:
            self.x=width-1
        if self.y>heigth-1:
            self.y=0
        if self.y<0:
            self.y=heigth-1
    def checkHit(self, obj):
        for i in self.guns:
            i.checkHit(obj)
        
        

if __name__=='__main__':
    root = tkinter.Tk()
    width = 1600
    heigth = 800
    WH =  str(width)+'x'+str(heigth)
    root.geometry(WH)
    canv = tkinter.Canvas(root, width=width, height=heigth, bg='white')
    canv.pack()
    keyboard = MyKeyboard.Keyboard(root)
    x=400
    y=300
    r=100
    Starship001 = Starship(color = 'red', controls = ['9', 'i', 'o', 'p', 'l'])
    Starship002 = Starship(color = 'blue')
    def draw():
        global x, y, r, FrameTime
        canv.delete(tkinter.ALL)
        Starship001.checkHit(Starship002)
        Starship002.checkHit(Starship001)
        Starship001.tick()
        Starship002.tick()
        #canv.create_oval(x+r, y+r, x-r, y-r, fill = "red", width=0)
#        if keyboard.keyw==1:
#            y-=1
#        if keyboard.keya==1:
#            x-=1
#        if keyboard.keys==1:
#            y+=1
#        if keyboard.keyd==1:
#            x+=1
        root.after(FrameTime, draw)
    draw()
    tkinter.mainloop()
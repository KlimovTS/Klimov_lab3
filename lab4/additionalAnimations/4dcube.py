# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 01:02:35 2019

@author: Тимофей
"""





from graph import *
import math
import random



class Point:
    
    def __init__(self):
        self.x=0
        self.y=0
        self.z=0
        self.w=0
        
    def __init__(self, x, y, z, w):
        self.x=x
        self.y=y
        self.z=z
        self.w=w
    
    
    
    def set_coords(self, x, y, z, w):
        self.x=x
        self.y=y
        self.z=z
        self.w=w
    
    def get_coords(self):
        x=self.x
        y=self.y
        z=self.z
        w=self.w
        return [x, y, z, w]
        
    def move(self, dx, dy, dz, dw):
        self.x+=dx
        self.y+=dy
        self.z+=dz
        self.w+=dw
    
    def projection(self, x0, y0, z0, w0, K):
        global X0
        global Y0
        vx = self.x-x0
        vy = self.y-y0
        vz = self.z-z0
        vw = self.w-w0
        k1 = -(w0/vw)*K
        x1 = x0+k1*vx
        y1 = y0+k1*vy
        z1 = z0+k1*vz
        vx1 = x1-x0
        vy1 = y1-y0
        vz1 = z1-z0
        k = -(z0/vz)*K
        x = x1+k*vx1
        y = y1+k*vy1
        k2 = k1*k
        return ((x, y), k2)
    
    def projection2(self, x0, y0, z0, w0, K):
        global X0
        global Y0
        vx = self.x-x0
        vy = self.y-y0
        vz = self.z-z0
        vw = self.w-w0
        k1 = -(w0/vw)*K
        x1 = x0+k1*vx
        y1 = y0+k1*vy
        z1 = z0+k1*vz
        vx1 = x1-x0
        vy1 = y1-y0
        vz1 = z1-z0
        k = -(z0/vz)*K
        x = x1+k*vx1
        y = y1+k*vy1
        k2 = math.sqrt((x0-self.x)*(x0-self.x)+(y0-self.y)*(y0-self.y)+(z0-self.z)*(z0-self.z)+(w0-self.w)*(w0-self.w))
        k2 = 250/k2
        return ((x, y), k2)
    
    def d2(self):
        return (self.x, self.y)

class Parallelepiped4d:
    
    def __init__(self):
        tmp = Point()
        self.points = [tmp, tmp, tmp, tmp, tmp, tmp, tmp, tmp, tmp, tmp, tmp, tmp, tmp, tmp, tmp, tmp]
    
    def __init__(self, p1, p2):
        a = p1.get_coords()
        b = p2.get_coords()
        self.points = [Point(a[0], a[1], a[2], a[3]), Point(a[0], a[1], b[2], a[3]), Point(a[0], b[1], b[2], a[3]), Point(a[0], b[1], a[2], a[3]), Point(b[0], b[1], a[2], a[3]), Point(b[0], b[1], b[2], a[3]), Point(b[0], a[1], b[2], a[3]), Point(b[0], a[1], a[2], a[3]), Point(a[0], a[1], a[2], b[3]), Point(a[0], a[1], b[2], b[3]), Point(a[0], b[1], b[2], b[3]), Point(a[0], b[1], a[2], b[3]), Point(b[0], b[1], a[2], b[3]), Point(b[0], b[1], b[2], b[3]), Point(b[0], a[1], b[2], b[3]), Point(b[0], a[1], a[2], b[3])]
    
    
    
    def set_coords(self, p1, p2):
        a = p1.get_coords()
        b = p2.get_coords()
        self.points[0].set_coords(a[0], a[1], a[2], a[3])
        self.points[1].set_coords(a[0], a[1], b[2], a[3])
        self.points[2].set_coords(a[0], b[1], b[2], a[3])
        self.points[3].set_coords(a[0], b[1], a[2], a[3])
        self.points[4].set_coords(b[0], b[1], a[2], a[3])
        self.points[5].set_coords(b[0], b[1], b[2], a[3])
        self.points[6].set_coords(b[0], a[1], b[2], a[3])
        self.points[7].set_coords(b[0], a[1], a[2], a[3])
        self.points[8].set_coords(a[0], a[1], a[2], b[3])
        self.points[9].set_coords(a[0], a[1], b[2], b[3])
        self.points[10].set_coords(a[0], b[1], b[2], b[3])
        self.points[11].set_coords(a[0], b[1], a[2], b[3])
        self.points[12].set_coords(b[0], b[1], a[2], b[3])
        self.points[13].set_coords(b[0], b[1], b[2], b[3])
        self.points[14].set_coords(b[0], a[1], b[2], b[3])
        self.points[15].set_coords(b[0], a[1], a[2], b[3])
    
    def move(self, dx, dy, dz, dw):
        for i in self.points:
            i.move(dx, dy, dz, dw)
    
    def draw(self):
        a = []
        penSize(20)
        penColor(0, 0, 0)
        brushColor(0, 0, 0)
        
        a.append(polyline([self.points[0].d2(), self.points[1].d2()]))
        a.append(polyline([self.points[0].d2(), self.points[3].d2()]))
        a.append(polyline([self.points[0].d2(), self.points[7].d2()]))
        a.append(polyline([self.points[2].d2(), self.points[1].d2()]))
        a.append(polyline([self.points[2].d2(), self.points[3].d2()]))
        a.append(polyline([self.points[2].d2(), self.points[5].d2()]))
        a.append(polyline([self.points[4].d2(), self.points[3].d2()]))
        a.append(polyline([self.points[4].d2(), self.points[5].d2()]))
        a.append(polyline([self.points[4].d2(), self.points[7].d2()]))
        a.append(polyline([self.points[6].d2(), self.points[1].d2()]))
        a.append(polyline([self.points[6].d2(), self.points[5].d2()]))
        a.append(polyline([self.points[6].d2(), self.points[7].d2()]))
        
        a.append(polyline([self.points[8].d2(), self.points[9].d2()]))
        a.append(polyline([self.points[8].d2(), self.points[11].d2()]))
        a.append(polyline([self.points[8].d2(), self.points[15].d2()]))
        a.append(polyline([self.points[10].d2(), self.points[9].d2()]))
        a.append(polyline([self.points[10].d2(), self.points[11].d2()]))
        a.append(polyline([self.points[10].d2(), self.points[13].d2()]))
        a.append(polyline([self.points[12].d2(), self.points[11].d2()]))
        a.append(polyline([self.points[12].d2(), self.points[13].d2()]))
        a.append(polyline([self.points[12].d2(), self.points[15].d2()]))
        a.append(polyline([self.points[14].d2(), self.points[9].d2()]))
        a.append(polyline([self.points[14].d2(), self.points[13].d2()]))
        a.append(polyline([self.points[14].d2(), self.points[15].d2()]))
        
        a.append(polyline([self.points[0].d2(), self.points[8].d2()]))
        a.append(polyline([self.points[1].d2(), self.points[9].d2()]))
        a.append(polyline([self.points[2].d2(), self.points[10].d2()]))
        a.append(polyline([self.points[3].d2(), self.points[11].d2()]))
        a.append(polyline([self.points[4].d2(), self.points[12].d2()]))
        a.append(polyline([self.points[5].d2(), self.points[13].d2()]))
        a.append(polyline([self.points[6].d2(), self.points[14].d2()]))
        a.append(polyline([self.points[7].d2(), self.points[15].d2()]))
        
        penSize(1)
        penColor(255, 0, 0)
        brushColor(255, 0, 0)
        for i in  self.points:
            tmp = i.d2()
            a.append(circle(tmp[0], tmp[1], 15))
        return a
    
    def draw2(self, x0, y0, z0, w0, k):
        a = []
        b = []
        
        for i in self.points:
            b.append(i.projection(x0, y0, z0, w0, k))
        
        penSize(10)
        penColor(0, 0, 0)
        brushColor(0, 0, 0)
        
        a.append(line1(b[0], b[1]))
        a.append(line1(b[0], b[3]))
        a.append(line1(b[0], b[7]))
        a.append(line1(b[2], b[1]))
        a.append(line1(b[2], b[3]))
        a.append(line1(b[2], b[5]))
        a.append(line1(b[4], b[3]))
        a.append(line1(b[4], b[5]))
        a.append(line1(b[4], b[7]))
        a.append(line1(b[6], b[1]))
        a.append(line1(b[6], b[5]))
        a.append(line1(b[6], b[7]))
        
        a.append(line1(b[8], b[9]))
        a.append(line1(b[8], b[11]))
        a.append(line1(b[8], b[15]))
        a.append(line1(b[10], b[9]))
        a.append(line1(b[10], b[11]))
        a.append(line1(b[10], b[13]))
        a.append(line1(b[12], b[11]))
        a.append(line1(b[12], b[13]))
        a.append(line1(b[12], b[15]))
        a.append(line1(b[14], b[9]))
        a.append(line1(b[14], b[13]))
        a.append(line1(b[14], b[15]))
        
        a.append(line1(b[0], b[8]))
        a.append(line1(b[1], b[9]))
        a.append(line1(b[2], b[10]))
        a.append(line1(b[3], b[11]))
        a.append(line1(b[4], b[12]))
        a.append(line1(b[5], b[13]))
        a.append(line1(b[6], b[14]))
        a.append(line1(b[7], b[15]))
        
        penSize(1)
        penColor(255, 0, 0)
        brushColor(255, 0, 0)
        c = []
        for i in  b:
            c.append(circle(i[0][0], i[0][1], i[1]*50))
        a.append(c)
        return a
    
    def draw3(self, x0, y0, z0, w0, k):
        a = []
        b = []
        
        for i in self.points:
            b.append(i.projection2(x0, y0, z0, w0, k))
        
        penSize(10)
        penColor(0, 0, 0)
        brushColor(0, 0, 0)
        
        a.append(line1(b[0], b[1]))
        a.append(line1(b[0], b[3]))
        a.append(line1(b[0], b[7]))
        a.append(line1(b[2], b[1]))
        a.append(line1(b[2], b[3]))
        a.append(line1(b[2], b[5]))
        a.append(line1(b[4], b[3]))
        a.append(line1(b[4], b[5]))
        a.append(line1(b[4], b[7]))
        a.append(line1(b[6], b[1]))
        a.append(line1(b[6], b[5]))
        a.append(line1(b[6], b[7]))
        
        a.append(line1(b[8], b[9]))
        a.append(line1(b[8], b[11]))
        a.append(line1(b[8], b[15]))
        a.append(line1(b[10], b[9]))
        a.append(line1(b[10], b[11]))
        a.append(line1(b[10], b[13]))
        a.append(line1(b[12], b[11]))
        a.append(line1(b[12], b[13]))
        a.append(line1(b[12], b[15]))
        a.append(line1(b[14], b[9]))
        a.append(line1(b[14], b[13]))
        a.append(line1(b[14], b[15]))
        
        a.append(line1(b[0], b[8]))
        a.append(line1(b[1], b[9]))
        a.append(line1(b[2], b[10]))
        a.append(line1(b[3], b[11]))
        a.append(line1(b[4], b[12]))
        a.append(line1(b[5], b[13]))
        a.append(line1(b[6], b[14]))
        a.append(line1(b[7], b[15]))
        
        penSize(1)
        penColor(255, 0, 0)
        brushColor(255, 0, 0)
        c = []
        for i in  b:
            c.append(circle(i[0][0], i[0][1], i[1]*50))
        a.append(c)
        return a
    
    def rotateXY(self, x0, y0, a):
        a = math.radians(a)
        sin = math.sin(a)
        cos = math.cos(a)
        for i in self.points:
            tmp = i.get_coords()
            tmpx = tmp[0]
            tmpy = tmp[1]
            tmpz = tmp[2]
            tmpw = tmp[3]
            x = x0 + cos*(tmpx-x0)-sin*(tmpy-y0)
            y = y0 + sin*(tmpx-x0)+cos*(tmpy-y0)
            z = tmpz
            w = tmpw
            i.set_coords(x, y, z, w)
    
    def rotateYZ(self, y0, z0, a):
        a = math.radians(a)
        sin = math.sin(a)
        cos = math.cos(a)
        for i in self.points:
            tmp = i.get_coords()
            tmpx = tmp[0]
            tmpy = tmp[1]
            tmpz = tmp[2]
            tmpw = tmp[3]
            x = tmpx
            y = y0 + cos*(tmpy-y0)-sin*(tmpz-z0)
            z = z0 + sin*(tmpy-y0)+cos*(tmpz-z0)
            w = tmpw
            i.set_coords(x, y, z, w)
    
    def rotateZW(self, z0, w0, a):
        a = math.radians(a)
        sin = math.sin(a)
        cos = math.cos(a)
        for i in self.points:
            tmp = i.get_coords()
            tmpx = tmp[0]
            tmpy = tmp[1]
            tmpz = tmp[2]
            tmpw = tmp[3]
            x = tmpx
            y = tmpy
            z = z0 + cos*(tmpz-z0)-sin*(tmpw-w0)
            w = w0 + sin*(tmpz-z0)+cos*(tmpw-w0)
            i.set_coords(x, y, z, w)
    
    def rotateWX(self, w0, x0, a):
        a = math.radians(a)
        sin = math.sin(a)
        cos = math.cos(a)
        for i in self.points:
            tmp = i.get_coords()
            tmpx = tmp[0]
            tmpy = tmp[1]
            tmpz = tmp[2]
            tmpw = tmp[3]
            x = x0 + cos*(tmpx-x0)-sin*(tmpw-w0)
            y = tmpy
            z = tmpz
            w = w0 + sin*(tmpx-x0)+cos*(tmpw-w0)
            i.set_coords(x, y, z, w)
    
    def rotateXZ(self, x0, z0, a):
        a = math.radians(a)
        sin = math.sin(a)
        cos = math.cos(a)
        for i in self.points:
            tmp = i.get_coords()
            tmpx = tmp[0]
            tmpy = tmp[1]
            tmpz = tmp[2]
            tmpw = tmp[3]
            x = x0 + cos*(tmpx-x0)-sin*(tmpz-z0)
            y = tmpy
            z = z0 + sin*(tmpx-x0)+cos*(tmpz-z0)
            w = tmpw
            i.set_coords(x, y, z, w)
    
    def rotateYW(self, y0, w0, a):
        a = math.radians(a)
        sin = math.sin(a)
        cos = math.cos(a)
        for i in self.points:
            tmp = i.get_coords()
            tmpx = tmp[0]
            tmpy = tmp[1]
            tmpz = tmp[2]
            tmpw = tmp[3]
            x = tmpx
            y = y0 + cos*(tmpy-y0)-sin*(tmpw-w0)
            z = tmpz
            w = w0 + sin*(tmpy-y0)+cos*(tmpw-w0)
            i.set_coords(x, y, z, w)
    
    def get_center(self):
        x=0
        y=0
        z=0
        w=0
        for i  in  self.points:
            tmp = i.get_coords()
            x+=tmp[0]
            y+=tmp[1]
            z+=tmp[2]
            w+=tmp[3]
        return [x/16, y/16, z/16, w/16]

obj=0

def line1(b1, b2):
    a = []
    n=10
    dx=b2[0][0]-b1[0][0]
    dy=b2[0][1]-b1[0][1]
    dk=b2[1]-b1[1]
    dx=dx/n
    dy=dy/n
    dk=dk/n
    for i in range(0, n, 1):
        k=b1[1]+dk*i
        x1 = b1[0][0]+(i-0.1)*dx
        y1 = b1[0][1]+(i-0.1)*dy
        x2 = b1[0][0]+(i+1+0.1)*dx
        y2 = b1[0][1]+(i+1+0.1)*dy
        penSize(60*k)
        a.append(line(x1, y1, x2, y2))
    return a

#def line1(b1, b2):
#    a = 0
#    dx=b2[0][0]-b1[0][0]
#    dy=b2[0][1]-b1[0][1]
#    dk=b2[1]-b1[1]
#    x1=b1[0][0]+math.copysign(1,dx)*b1[1]*(dy/(dx+dy))
#    y1=b1[0][1]+math.copysign(1,dy)*b1[1]*(dx/(dx+dy))
#    x2=b1[0][0]-math.copysign(1,dx)*b1[1]*(dy/(dx+dy))
#    y2=b1[0][1]-math.copysign(1,dy)*b1[1]*(dx/(dx+dy))
#    x3=b2[0][0]-math.copysign(1,dx)*b2[1]*(dy/(dx+dy))
#    y3=b2[0][1]-math.copysign(1,dy)*b2[1]*(dx/(dx+dy))
#    x4=b2[0][0]+math.copysign(1,dx)*b2[1]*(dy/(dx+dy))
#    y4=b2[0][1]+math.copysign(1,dy)*b2[1]*(dx/(dx+dy))
#    a = polygon([(x1, y1), (x2, y2), (x3, y3), (x4, y4)])
#    return [a]

def F():
    global posXY
    global posXZ
    global posYZ
    global obj
    global cube
    global w1
    global w2
    global w3
    global w4
    global w5
    global w6
    global dw1
    global dw2
    global dw3
    global dw4
    global dw5
    global dw6
    global X0
    global Y0
    global Z0
    global W0
    global ii
    global stage
    dw1 = (dw1 + 0.002*(randint(0, 100)-49.5))/2
    dw2 = (dw2 + 0.002*(randint(0, 100)-49.5))/2
    dw3 = (dw3 + 0.002*(randint(0, 100)-49.5))/2
    dw4 = (dw4 + 0.002*(randint(0, 100)-49.5))/2
    dw5 = (dw5 + 0.002*(randint(0, 100)-49.5))/2
    dw6 = (dw6 + 0.002*(randint(0, 100)-49.5))/2
    w1+=dw1
    w2+=dw2
    w3+=dw3
    w4+=dw4
    w5+=dw5
    w6+=dw6
    w1=w1*0.99449
    w2=w2*0.99449
    w3=w3*0.99449
    w4=w4*0.99449
    w5=w5*0.99449
    w6=w6*0.99449
    w1=0
    w2=0 #-1
    w3=0
    w4=0 #1
    w5=0 #-1
    w6=0 #1
    for i in  obj:
        for j in i:
            deleteObject(j)
#    for i in  obj:
#        deleteObject(i)
    
    tmp0 = cube.get_center()
    cube.rotateXY(tmp0[0], tmp0[1], w1)
    tmp0 = cube.get_center()
    cube.rotateYZ(tmp0[1], tmp0[2], w2)
    tmp0 = cube.get_center()
    cube.rotateZW(tmp0[2], tmp0[3], w3)
    tmp0 = cube.get_center()
    cube.rotateWX(tmp0[3], tmp0[0], w4)
    tmp0 = cube.get_center()
    cube.rotateXZ(tmp0[0], tmp0[2], w5)
    tmp0 = cube.get_center()
    cube.rotateYW(tmp0[1], tmp0[3], w6)
    tmp0 = cube.get_center()
    
    tmp0 = cube.get_center()
    cube.rotateXY(tmp0[0], tmp0[1], -posXY)
    tmp0 = cube.get_center()
    cube.rotateXZ(tmp0[0], tmp0[2], -posXZ)
    tmp0 = cube.get_center()
    cube.rotateYZ(tmp0[1], tmp0[2], -posYZ)
    
    n1=1
    n2=1
    
    if stage==0:
        if ii<90:
            tmp0 = cube.get_center()
            cube.rotateWX(tmp0[3], tmp0[0], n1)
        ii+=1
        if ii==100:
            ii=0
            stage=1
    if stage==1:
        if ii<90:
            tmp0 = cube.get_center()
            cube.rotateXZ(tmp0[0], tmp0[2], n2)
        ii+=1
        if ii==100:
            ii=0
            stage=2
    if stage==2:
        if ii<90:
            tmp0 = cube.get_center()
            cube.rotateYW(tmp0[1], tmp0[3], n1)
        ii+=1
        if ii==100:
            ii=0
            stage=3
    if stage==3:
        if ii<90:
            tmp0 = cube.get_center()
            cube.rotateXZ(tmp0[0], tmp0[2], -n2)
        ii+=1
        if ii==100:
            ii=0
            stage=4
    if stage==4:
        if ii<90:
            tmp0 = cube.get_center()
            cube.rotateZW(tmp0[2], tmp0[3], n1)
        ii+=1
        if ii==100:
            ii=0
            stage=5
    if stage==5:
        if ii<90:
            tmp0 = cube.get_center()
            cube.rotateYZ(tmp0[0], tmp0[2], n2)
        ii+=1
        if ii==100:
            ii=0
            stage=6
    
    if stage==6:
        if ii<90:
            tmp0 = cube.get_center()
            cube.rotateWX(tmp0[3], tmp0[0], -n1)
        ii+=1
        if ii==100:
            ii=0
            stage=7
    if stage==7:
        if ii<90:
            tmp0 = cube.get_center()
            cube.rotateYZ(tmp0[0], tmp0[2], -n2)
        ii+=1
        if ii==100:
            ii=0
            stage=8
    if stage==8:
        if ii<90:
            tmp0 = cube.get_center()
            cube.rotateYW(tmp0[1], tmp0[3], -n1)
        ii+=1
        if ii==100:
            ii=0
            stage=9
    if stage==9:
        if ii<90:
            tmp0 = cube.get_center()
            cube.rotateXY(tmp0[0], tmp0[2], n2)
        ii+=1
        if ii==100:
            ii=0
            stage=10
    if stage==10:
        if ii<90:
            tmp0 = cube.get_center()
            cube.rotateZW(tmp0[2], tmp0[3], -n1)
        ii+=1
        if ii==100:
            ii=0
            stage=11
    if stage==11:
        if ii<90:
            tmp0 = cube.get_center()
            cube.rotateXY(tmp0[0], tmp0[2], -n2)
        ii+=1
        if ii==100:
            ii=0
            stage=0
    
    tmp0 = cube.get_center()
    cube.rotateYZ(tmp0[1], tmp0[2], posYZ)
    tmp0 = cube.get_center()
    cube.rotateXZ(tmp0[0], tmp0[2], posXZ)
    tmp0 = cube.get_center()
    cube.rotateXY(tmp0[0], tmp0[1], posXY)
    
    obj = cube.draw3(X0, Y0, Z0, W0, 0.35)
    #obj = cube.draw2(X0, Y0, Z0, W0, 0.35)
    #obj = cube.draw()


w1=0
w2=0
w3=0
w4=0
w5=0
w6=0
dw1=0
dw2=0
dw3=0
dw4=0
dw5=0
dw6=0

X0=400
Y0=400
Z0=1200
W0=1200

ii=0
stage=0

cx=400
cy=400
cz=400
cw=400

tmpk = 1.5

lx=350*tmpk
ly=275*tmpk
lz=200*tmpk
lw=125*tmpk

#lx=250*tmpk
#ly=250*tmpk
#lz=250*tmpk
#lw=250*tmpk

posXY=10
posXZ=22.5
posYZ=-22.5

p1 =  Point(cx-0.5*lx, cy-0.5*ly, cz-0.5*lz, cw-0.5*lw)
p2 = Point(cx+0.5*lx, cy+0.5*ly, cz+0.5*lz, cw+0.5*lw)
cube = Parallelepiped4d(p1, p2)


tmp0 = cube.get_center()
cube.rotateYZ(tmp0[1], tmp0[2], posYZ)
tmp0 = cube.get_center()
cube.rotateZW(tmp0[2], tmp0[3], 0)
tmp0 = cube.get_center()
cube.rotateWX(tmp0[3], tmp0[0], 0)
tmp0 = cube.get_center()
cube.rotateXZ(tmp0[0], tmp0[2], posXZ)
tmp0 = cube.get_center()
cube.rotateYW(tmp0[1], tmp0[3], 0)
tmp0 = cube.get_center()
cube.rotateXY(tmp0[0], tmp0[1], posXY)

obj = cube.draw3(X0, Y0, Z0, W0, 0.35)
#obj = cube.draw2(X0, Y0, Z0, W0, 0.35)
#obj = cube.draw()

onTimer(F, 16)

run()






# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 01:02:35 2019

@author: Тимофей
"""





from graph import *
import math



#class Point2d:
#    
#    def __init__(self):
#        self.x=0
#        self.y=0
#        
#    def __init__(self, x, y):
#        self.x=x
#        self.y=y
#    
#    
#    
#    def set_coords(self, x, y):
#        self.x=x
#        self.y=y
#    
#    def get_coords(self):
#        x=self.x
#        y=self.y
#        return (x, y)
#        
#    def move(self, dx, dy):
#        self.x+=dx
#        self.y+=dy

class Point:
    
    def __init__(self):
        self.x=0
        self.y=0
        self.z=0
        
    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z
    
    
    
    def set_coords(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z
    
    def get_coords(self):
        x=self.x
        y=self.y
        z=self.z
        return [x, y, z]
        
    def move(self, dx, dy, dz):
        self.x+=dx
        self.y+=dy
        self.z+=dz
    
    def projection(self, x0, y0, z0, K):
        vx = self.x-x0
        vy = self.y-y0
        vz = self.z-z0
        k = -(z0/vz)*K
        x = x0+k*vx
        y = y0+k*vy
        return ((x, y), k)
    
    def d2(self):
        return (self.x, self.y)

class Parallelepiped:
    
    def __init__(self):
        tmp = Point()
        self.points = [tmp, tmp, tmp, tmp, tmp, tmp, tmp, tmp]
        tmp = Point2d()
#        self.projection = [tmp, tmp, tmp, tmp, tmp, tmp, tmp, tmp]
    
    def __init__(self, p1, p2):
        a = p1.get_coords()
        b = p2.get_coords()
        self.points = [Point(a[0], a[1], a[2]), Point(a[0], a[1], b[2]), Point(a[0], b[1], b[2]), Point(a[0], b[1], a[2]), Point(b[0], b[1], a[2]), Point(b[0], b[1], b[2]), Point(b[0], a[1], b[2]), Point(b[0], a[1], a[2])]
#        tmp = Point2d()
#        self.projection = [tmp, tmp, tmp, tmp, tmp, tmp, tmp, tmp]
    
    
    
    def set_coords(self, p1, p2):
        a = p1.get_coords()
        b = p2.get_coords()
        self.points[0].set_coords(a[0], a[1], a[2])
        self.points[1].set_coords(a[0], a[1], b[2])
        self.points[2].set_coords(a[0], b[1], b[2])
        self.points[3].set_coords(a[0], b[1], a[2])
        self.points[4].set_coords(b[0], b[1], a[2])
        self.points[5].set_coords(b[0], b[1], b[2])
        self.points[6].set_coords(b[0], a[1], b[2])
        self.points[7].set_coords(b[0], a[1], a[2])
    
    def move(self, dx, dy, dz):
        for i in self.points:
            i.move(dx, dy, dz)
    
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
        penSize(1)
        penColor(255, 0, 0)
        brushColor(255, 0, 0)
        for i in  self.points:
            tmp = i.d2()
            a.append(circle(tmp[0], tmp[1], 15))
        return a
    
    def draw2(self, x0, y0, z0, k):
        a = []
        b = []
        for i in self.points:
            b.append(i.projection(x0, y0, z0, k))
        penSize(10)
        penColor(0, 0, 0)
        brushColor(0, 0, 0)
        a.append(polyline([b[0][0], b[1][0]]))
        a.append(polyline([b[0][0], b[3][0]]))
        a.append(polyline([b[0][0], b[7][0]]))
        a.append(polyline([b[2][0], b[1][0]]))
        a.append(polyline([b[2][0], b[3][0]]))
        a.append(polyline([b[2][0], b[5][0]]))
        a.append(polyline([b[4][0], b[3][0]]))
        a.append(polyline([b[4][0], b[5][0]]))
        a.append(polyline([b[4][0], b[7][0]]))
        a.append(polyline([b[6][0], b[1][0]]))
        a.append(polyline([b[6][0], b[5][0]]))
        a.append(polyline([b[6][0], b[7][0]]))
        penSize(1)
        penColor(255, 0, 0)
        brushColor(255, 0, 0)
        for i in  b:
            a.append(circle(i[0][0], i[0][1], i[1]*15))
        return a
    
    def rotateX(self, y0, z0, a):
        a = math.radians(a)
        sin = math.sin(a)
        cos = math.cos(a)
        for i in self.points:
            tmp = i.get_coords()
            tmpx = tmp[0]
            tmpy = tmp[1]
            tmpz = tmp[2]
            x = tmpx
            y = y0 + cos*(tmpy-y0)+sin*(tmpz-z0)
            z = z0 -sin*(tmpy-y0)+cos*(tmpz-z0)
            i.set_coords(x, y, z)
    
    def rotateY(self, z0, x0, a):
        a = math.radians(a)
        sin = math.sin(a)
        cos = math.cos(a)
        for i in self.points:
            tmp = i.get_coords()
            tmpx = tmp[0]
            tmpy = tmp[1]
            tmpz = tmp[2]
            x = x0 -sin*(tmpz-z0)+cos*(tmpx-x0)
            y = tmpy
            z = z0 + cos*(tmpz-z0)+sin*(tmpx-x0)
            i.set_coords(x, y, z)
    
    def rotateZ(self, x0, y0, a):
        a = math.radians(a)
        sin = math.sin(a)
        cos = math.cos(a)
        for i in self.points:
            tmp = i.get_coords()
            tmpx = tmp[0]
            tmpy = tmp[1]
            tmpz = tmp[2]
            x = x0 + cos*(tmpx-x0)+sin*(tmpy-y0)
            y = y0 -sin*(tmpx-x0)+cos*(tmpy-y0)
            z = tmpz
            i.set_coords(x, y, z)
    
    def get_center(self):
        x=0
        y=0
        z=0
        for i  in  self.points:
            tmp = i.get_coords()
            x+=tmp[0]
            y+=tmp[1]
            z+=tmp[2]
        return [x/8, y/8, z/8]

obj=0

def F():
    global obj
    global cube
    global a
    global ii
    global di
    global w
#    global ix
#    global iy
    tmp = math.radians(a)
    tmp0 = cube.get_center()
    for i in  obj:
        deleteObject(i)
    dx=-di*math.sin(math.radians(ii))
    dy=di*math.cos(math.radians(ii))
    cube.rotateX(tmp0[1], tmp0[2], 0)
    cube.rotateY(tmp0[2], tmp0[0], w*-1*math.cos(tmp))
    cube.rotateZ(tmp0[0], tmp0[1], w*1*math.sin(tmp))
    cube.move(dx, dy, 0)
#    ii+=di
#    if ii>150 or ii<-200:
#        di=-di
#    ix+=dx
#    iy+=dy
    ii=ii+1
    obj = cube.draw2(400, 400, 1200, 0.6)

ii=0
di=3.4
w = 2
#ix=0
#iy=0
a=15
p1 =  Point(250, 300, 275)
p2 = Point(550, 500, 525)
cube = Parallelepiped(p1, p2)
cube.move(200, 0, 0)
cube.rotateX(400, 400, a)
obj = cube.draw2(400, 400, 1200, 0.6)

onTimer(F, 16)

run()






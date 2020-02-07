import pygame
import math
import random
import time

class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def setLen(self, const):
        tmpdiv = math.sqrt(self.x**2+self.y**2)
        self.x = const*self.x/tmpdiv
        self.y = const*self.y/tmpdiv
    def leng(self):
        return math.sqrt(self.x**2+self.y**2)
    def getLen(self, const):
        tmpdiv = self.leng()
        if tmpdiv==0:
            return Vector(0, 0)
        else:
            tmpx = const*self.x/tmpdiv
            tmpy = const*self.y/tmpdiv
            return Vector(tmpx, tmpy)
    def multiply(self, const):
        tmpx = self.x * const
        tmpy = self.y * const
        return Vector(tmpx, tmpy)
    def add(self, vector):
        tmpx = self.x + vector.x
        tmpy = self.y + vector.y
        return Vector(tmpx, tmpy)
    def sub(self, vector):
        tmpx = self.x - vector.x
        tmpy = self.y - vector.y
        return Vector(tmpx, tmpy)
    def scalar(self, vector):
        a = self.x*vector.x + self.y*vector.y
        return a
    def norm(self):
        tmpx = -self.y
        tmpy = self.x
        return Vector(tmpx, tmpy)
    def decompose(self, e1, e2):
        tmpa = self.y/e2.y
        tmpb = (self.x*e1.y)/(e1.x*e2.y)
        tmpc = (e2.x*e1.y)/(e1.x*e2.y)
        tmpy = (tmpa-tmpb)/(1-tmpc)
        tmpx = (self.x-tmpy*e2.x)/e1.x
        return Vector(tmpx, tmpy)
    def multiplyByBase(self, e1, e2):
        return e1.multiply(self.x).add(e2.multiply(self.y))
    def draw(self, O, screen):
        tmp = self.add(O)
        pygame.draw.lines(screen, (255, 0, 0), False, [[O.x, O.y], [tmp.x, tmp.y]], 1)

def r01():
    n = 1000000000
    return (random.randint(0*n, 1*n)/n)

class Fractal():
    def __init__(self, w, h):
#        self.elem_polyline = [Vector(0, 0), Vector(0.5, -0.5), Vector(1, 0)]
        self.go = True
        k = 1/2**6
        d = 1-k
        tmp = 0
        try:
            tmp = math.sqrt(d**2-(1-2*k)**2)/2
        except:
            tmp = 0.1
#        self.elem_polyline = [Vector(0, 0), Vector(k, tmp), Vector(1-k, -tmp), Vector(1, 0)]
        self.elem_polylines = []
#        self.elem_polyline = [Vector(0, 0), Vector(0.1, -0.1), Vector(0.2, -0.2), Vector(0.3, -0.4), Vector(0.35, -0.6), Vector(0.4, -0.8), Vector(0.4, -1.1), Vector(0.4, -1.2), Vector(0.4, -1.3), Vector(0.4, -1.6), Vector(0.4, -1.7), Vector(0.4, -1.8), Vector(0.4, -1.9), Vector(0.4, -2.1), Vector(0.6, -2.1), Vector(0.6, -1.9), Vector(0.6, -1.8), Vector(0.6, -1.7), Vector(0.6, -1.6), Vector(0.6, -1.3), Vector(0.6, -1.2), Vector(0.6, -1.1), Vector(0.6, -0.8), Vector(0.65, -0.6), Vector(0.7, -0.4), Vector(0.8, -0.2), Vector(0.9, -0.1), Vector(1, 0)]
#        self.elem_polyline = [Vector(0, 0), Vector(1/3, 0), Vector(1/3, 1/3), Vector(2/3, 1/3), Vector(2/3, 0), Vector(1, 0)]
#        self.elem_polyline = [Vector(0, 0), Vector(0.5, 0), Vector(0.5, 0.25), Vector(0.5, -0.25), Vector(0.5, 0), Vector(1, 0)]
#        self.elem_polyline = [Vector(0, 0), Vector(0.2, 0), Vector(0.2, 0.2), Vector(0.4, 0.2), Vector(0.4, -0.2), Vector(0.6, -0.2), Vector(0.6, 0.2), Vector(0.8, 0.2), Vector(0.8, 0), Vector(1, 0)]
#        self.elem_polyline = [Vector(0, 0), Vector(k, k), Vector(1-k, -k), Vector(1, 0)]
        self.elem_polyline = [Vector(0, 0), Vector(0.01, 0.2), Vector(1, 0.15), Vector(1, 0)]
#        self.elem_polyline = [Vector(0, 0), Vector(0.125, 0.125), Vector(0.375, 0.25), Vector(0.625, -0.25), Vector(0.875, -0.125), Vector(1, 0)]
        
#        bad = True
#        nn = 1+round(1/(r01()+0.1))
#        while bad:
#            self.elem_polyline = [Vector(0, 0)]
#            for i in range(1, nn):
#                self.elem_polyline.append(Vector((2*r01())-0.5, r01()-0.5))
#            self.elem_polyline.append(Vector(1, 0))
#            good = True
#            for i in range(0, nn):
#                good = good and ((self.elem_polyline[i].x-self.elem_polyline[i+1].x)**2 + (self.elem_polyline[i].y-self.elem_polyline[i+1].y)**2 < 0.9**2)
#            bad = not good
            
        self.elem_lenghth = len(self.elem_polyline)-1
        self.LastScale = 1
        self.q = 1/100
        self.B = -1
        for i in range(0, self.elem_lenghth):
            tmp = self.elem_polyline[i+1].sub(self.elem_polyline[i]).leng()
            if tmp > self.B:
                self.B = tmp
        self.B
        self.Q = 0
        self.St = 0
#        print(self.B)
#        self.a = True
        self.a = False
        self.not_end = False
        self.mode = 1
        self.lenghth = 1
        self.polyline = [Vector(0, 0), Vector(1, 0)]
#    def getPointPos(self, Point, line_i):
#        e1 = self.elem_polyline[line_i+1].sub(self.elem_polyline[line_i])
#        e2 = e1.norm()
#        return Point.decompose(e1, e2)
    def getQ(self, Q):
        if Q == -1:
            return 1
        else:
            out  = self.B
            for i in range(0, Q):
                out = out*out
            return out
#            return self.B**(2**(Q))
    def Ubisector(self, line_i0, line_i1, baseLi):
        if line_i0 >= 0:
            L1 = self.polyline[line_i0+1].sub(self.polyline[line_i0])
        else:
            L1 = self.polyline[baseLi+1].sub(self.polyline[baseLi])
        if line_i1 < self.lenghth:
            L2 = self.polyline[line_i1+1].sub(self.polyline[line_i1])
        else:
            L2 = self.polyline[baseLi+1].sub(self.polyline[baseLi])
        B = self.polyline[baseLi+1].sub(self.polyline[baseLi])
        if L1.scalar(L2) > L1.leng()*L2.leng()*0.99999:
            tmpBis = B.norm()
        else:
            tmpV = L1.getLen(1).sub(L2.getLen(1))
            if tmpV.leng()==0:
                tmpBis = B.multiply(-1)
            else:
                tmpBis = tmpV.getLen(B.leng())
        if tmpBis.scalar(B.norm())<0:
            return tmpBis.multiply(-1)
        else:
            return tmpBis
    def calcElemLine(self, polyline):
        B = polyline[len(polyline)-1].sub(polyline[0])
        tmp = 1/B.leng()
        ePolyline = []
        for i in polyline:
            ePolyline.append(i.multiply(tmp))
#            print(i.x*tmp, i.y*tmp)
        return ePolyline
    def calcPointPos(self, Pi, baseLi):
        if self.mode == 0:
            pos = self.elem_polyline[Pi]
            e21 = self.Ubisector(baseLi-1, baseLi, baseLi)
            e22 = self.Ubisector(baseLi, baseLi+1, baseLi)
            B = self.polyline[baseLi+1].sub(self.polyline[baseLi])
            e1 = B.add(e22.multiply(pos.y)).sub(e21.multiply(pos.y))
            return pos.multiplyByBase(e1, e21)
        if self.mode == 1:
            pos = self.elem_polyline[Pi]
            B = self.polyline[baseLi+1].sub(self.polyline[baseLi])
            return pos.multiplyByBase(B, B.norm())
    def betterCalcPointPos(self, Li, Pi, baseLi):
        pos = self.elem_polylines[Li][Pi]
        B = self.polyline[baseLi+1].sub(self.polyline[baseLi])
        return pos.multiplyByBase(B, B.norm())
    
    def transmute(self, baseLi):
        B = self.polyline[baseLi+1].sub(self.polyline[baseLi])
        PointsList = []
        if B.leng()*self.LastScale>self.q:
            O = self.polyline[baseLi]
            for i in range(1, self.elem_lenghth+1):
                tmpP = O.add(self.calcPointPos(i, baseLi))
                PointsList.append(tmpP)
        else:
            PointsList.append(self.polyline[baseLi+1])
        return PointsList
    def firstTransmute(self, baseLi):
        B = self.polyline[baseLi+1].sub(self.polyline[baseLi])
        PointsList = []
        L = B.leng()
        if 0.99999*L>self.getQ(self.Q) and L>self.q/self.LastScale:
            O = self.polyline[baseLi]
            for i in range(1, self.elem_lenghth+1):
                tmpP = O.add(self.calcPointPos(i, baseLi))
                PointsList.append(tmpP)
        else:
            PointsList.append(self.polyline[baseLi+1])
        return PointsList
    def betterTransmute(self, baseLi):
        B = self.polyline[baseLi+1].sub(self.polyline[baseLi])
        PointsList = []
        L = B.leng()
        tmp = L/self.q
#        print(tmp)
        if tmp>1:
            for i in range(0, self.Q):
                if 1.000001*L*self.getQ(self.Q-i-1)>self.getQ(self.Q) and 1.000001*L*self.getQ(self.Q-i-1)>self.q:
                    O = self.polyline[baseLi]
                    for j in range(1, len(self.elem_polylines[self.Q-i-1])):
                        tmpP = O.add(self.betterCalcPointPos(self.Q-i-1, j, baseLi))
                        PointsList.append(tmpP)
                    self.not_end = True
                    return PointsList
            if tmp>1/self.B:
                self.not_end = True
            PointsList.append(self.polyline[baseLi+1])
            return PointsList
        else:
            PointsList.append(self.polyline[baseLi+1])
            return PointsList
    def calcStep(self, extraF=0):
        if extraF==0:
            NewPoly = [self.polyline[0]]
            for i in range(0, self.lenghth):
                NewPoly.extend(self.transmute(i))
            self.polyline = NewPoly
            tmp = self.lenghth
            self.lenghth = len(self.polyline)-1
    #        print(self.lenghth)
            if tmp == self.lenghth:
                return True
            else:
                return False
        if extraF==1:
            NewPoly = [self.polyline[0]]
            for i in range(0, self.lenghth):
                NewPoly.extend(self.firstTransmute(i))
            self.polyline = NewPoly
            tmp = self.lenghth
            self.lenghth = len(self.polyline)-1
            if tmp == self.lenghth:
                return True
            else:
                return False
    def betterStep(self, m = 999999999):
        if self.go:
            if self.Q == 0:
                self.calcStep(1)
                self.Q = 1
                self.elem_polylines.append(self.calcElemLine(self.polyline))
            else:
                self.not_end = False
                NewPoly = [self.polyline[0]]
                for i in range(0, self.lenghth):
                    NewPoly.extend(self.betterTransmute(i))
                    if len(NewPoly)>m:
                        return True
                self.polyline = NewPoly
                tmp = self.lenghth
                self.lenghth = len(self.polyline)-1
                if tmp == self.lenghth:
                    if self.not_end:
                        self.St = 0
                        self.Q += 1
                        self.elem_polylines.append(self.calcElemLine(self.polyline))
                    else:
                        self.go = False
                        return True
                else:
                    self.St += 1
                    return False
    def draw(self, screen, w, h):
        Ox = w//2
        Oy = h//2
        Points = []
        MX = -99999
        mX = 99999
        MY = -99999
        mY = 99999
        for i in range(0, self.lenghth+1):
            if self.polyline[i].x>MX:
                MX = self.polyline[i].x
            if self.polyline[i].x<mX:
                mX = self.polyline[i].x
            if self.polyline[i].y>MY:
                MY = self.polyline[i].y
            if self.polyline[i].y<mY:
                mY = self.polyline[i].y
        Cx = (MX+mX)/2
        Cy = (MY+mY)/2
        Scale = 0.95*min(1/(abs(MX-mX)/w+0.000001), 1/(abs(MY-mY)/h+0.000001))
        self.LastScale = Scale
#        print(Scale)
        for i in range(0, self.lenghth+1):
            tmpx = self.polyline[i].x-Cx
            tmpy = self.polyline[i].y-Cy
            tmpx = Ox+tmpx*Scale
            tmpy = Oy+tmpy*Scale
            Points.append([tmpx, tmpy])
#        print(Points)
        
        if self.a:
            pygame.draw.aalines(screen, (255, 255, 255), False, Points, 1)
        else:
            pygame.draw.lines(screen, (255, 255, 255), False, Points, 1)



FPS = 60
WIDTH = 1593
HEIGHT = 828
pygame.init()
runGame = True
clock = pygame.time.Clock()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fraktal")

Fractal01 = Fractal(WIDTH, HEIGHT)
#Fractal01.calcStep()
#Fractal01.calcStep()
COUNTER = 0
C2 = 0
C3 = 0
С4 = 0
END = ""

def draw():
    win.fill((0, 0, 0))
    Fractal01.draw(win, WIDTH, HEIGHT)
#    for i in range(0, Fractal01.lenghth):
#        Fractal01.Ubisector(i-1, i, i).draw(Fractal01.polyline[i], win)
#    Fractal01.Ubisector(Fractal01.lenghth-1, Fractal01.lenghth, Fractal01.lenghth-1).draw(Fractal01.polyline[Fractal01.lenghth], win)
    cap_txt =  "Fraktal     Q = " + str(Fractal01.Q) + "/" + str(Fractal01.St) + "     l = " + str(Fractal01.lenghth) + "     " + END
    pygame.display.set_caption(cap_txt)
    pygame.display.update()

while runGame:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runGame = False
    COUNTER += 1
    if COUNTER > 0:
        cap_txt =  "Fraktal     Q = " + str(Fractal01.Q) + "/" + str(Fractal01.St) + "     l = " + str(Fractal01.lenghth) + "     " + END
        pygame.display.set_caption(cap_txt)
#        round(100-Fractal01.lenghth/10000)
        COUNTER = 0
        C2 += 1
#        C3 += Fractal01.lenghth
        С4 += 1
        if Fractal01.betterStep():
            C2 += 500
            END =  "Ended"
#        if Fractal01.lenghth>20000:
#            C2 += 500
        if С4 > 0:
            С4 = 0
    if C2 > 500:
        draw()
        time.sleep(5)
        C2 = 0
        C3 = 0
#        Fractal01 = Fractal(WIDTH, HEIGHT)
#        END = ""
#    draw()
pygame.quit()
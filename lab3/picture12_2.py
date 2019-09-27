from graph import *


K=1.5

xSize=400
ySize=565
windowSize(xSize*K,ySize*K)





def animalLeg(k, r, x0, y0):
    ellyps(x0-13*k*r, y0+0*k, x0+13*k*r, y0+60*k)
    ellyps(x0-13*k*r, y0+55*k, x0+13*k*r, y0+115*k)
    ellyps(x0-5*k*r, y0+110*k, x0+25*k*r, y0+130*k)

def animal(k, r, x0, y0):
    xmid=97
    ymid=371
    penColor(255,255,255)
    brushColor(255,255,255)
    ellyps(x0+100*k*r, y0+40*k, x0-100*k*r, y0-40*k)
    ellyps(x0+75*k*r, y0-5*k, x0+115*k*r, y0-120*k)
    ellyps(x0+85*k*r, y0-145*k, x0+135*k*r, y0-115*k)
    penColor(229,128,255)
    brushColor(229,128,255)
    circle(x0+105*k*r, y0-132*k, 10*k)
    penColor(0,0,0)
    brushColor(0,0,0)
    circle(x0+108*k*r, y0-132*k, 5*k)
    penColor(255,255,255)
    brushColor(255,255,255)
    ellyps(x0+98*k*r, y0-140*k, x0+108*k*r, y0-136*k)
    penSize(6*k)
    line(x0+90*k*r, y0-130*k, x0+70*k*r, y0-153*k)
    line(x0+95*k*r, y0-135*k, x0+78*k*r, y0-158*k)
    penSize(1)
    penColor(255,255,255)
    brushColor(255,255,255)
    animalLeg(k, r, x0+80*k*r, y0+20*k)
    animalLeg(k, r, x0+50*k*r, y0-10*k)
    animalLeg(k, r, x0-40*k*r, y0+20*k)
    animalLeg(k, r, x0-80*k*r, y0-10*k)



def flower(k, r, x0, y0):
    penColor(200,200,200)
    brushColor(255,255,255)
    tmpx=-1
    tmpy=-7
    ellyps(x0+(10+tmpx)*k*r, y0+(5+tmpy)*k, x0-(10-tmpx)*k*r, y0-(5-tmpy)*k)
    tmpx=-10
    tmpy=-4
    ellyps(x0+(10+tmpx)*k*r, y0+(5+tmpy)*k, x0-(10-tmpx)*k*r, y0-(5-tmpy)*k)
    tmpx=10
    tmpy=-5
    ellyps(x0+(10+tmpx)*k*r, y0+(5+tmpy)*k, x0-(10-tmpx)*k*r, y0-(5-tmpy)*k)
    penColor(255,255,0)
    brushColor(255,255,0)
    tmpx=0
    tmpy=0
    ellyps(x0+(10+tmpx)*k*r, y0+(5+tmpy)*k, x0-(10-tmpx)*k*r, y0-(5-tmpy)*k)
    penColor(200,200,200)
    brushColor(255,255,255)
    tmpx=13
    tmpy=0
    ellyps(x0+(10+tmpx)*k*r, y0+(5+tmpy)*k, x0-(10-tmpx)*k*r, y0-(5-tmpy)*k)
    tmpx=-15
    tmpy=2
    ellyps(x0+(10+tmpx)*k*r, y0+(5+tmpy)*k, x0-(10-tmpx)*k*r, y0-(5-tmpy)*k)
    tmpx=-7
    tmpy=5
    ellyps(x0+(10+tmpx)*k*r, y0+(5+tmpy)*k, x0-(10-tmpx)*k*r, y0-(5-tmpy)*k)
    tmpx=7
    tmpy=6
    ellyps(x0+(10+tmpx)*k*r, y0+(5+tmpy)*k, x0-(10-tmpx)*k*r, y0-(5-tmpy)*k)

def kustik(k, r, x0, y0):
    penColor(113,200,55)
    brushColor(113,200,55)
    circle(x0, y0, 75*k)
    c1=3/6
    c2=4/6
    c3=5/6
    flower(k*c2, r, x0+5*k*r, y0-55*k)
    flower(k*c1, -r, x0-40*k*r, y0-43*k)
    flower(k*c2, -r, x0-28*k*r, y0-14*k)
    flower(k*c3, r, x0+40*k*r, y0-26*k)
    flower(k*c3, r, x0+6*k*r, y0+19*k)
    flower(k*c2, r, x0+50*k*r, y0+16*k)



def mountains(K):
    penColor(175,221,233)
    brushColor(175,221,233)
    rectangle(0*K, 0*K, xSize*K, ySize*K)
    
    penColor(0,0,0)
    brushColor(179,179,179)
    polygon([(0*K,174*K), (49*K,58*K), (83*K,138*K), (137*K,75*K), (238*K,226*K), (311*K,70*K), (335*K,98*K), (400*K,21*K), (xSize*K,ySize*K), (0*K,ySize*K)])
    
    penColor(0,0,0)
    brushColor(170,222,135)
    polygon([(0*K,300*K), (20*K,290*K), (35*K,289*K), (49*K,289*K), (86*K,283*K), (210*K,283*K), (212*K,284*K), (217*K,284*K), (221*K,290*K), (221*K,300*K), (224*K,302*K), (224*K,330*K), (233*K,333*K), (xSize*K,333*K), (xSize*K,ySize*K), (0*K,ySize*K)])





mountains(K)

kustik(0.24*K, 1, 13*K, 308*K)
kustik(0.24*K, 1, 300*K, 352*K)
kustik(0.6*K, 1, 304*K, 496*K)
kustik(0.367*K, -1, 374*K, 332*K)
kustik(0.6*K, -1, 385*K, 414*K)
kustik(0.333*K, -1, 407*K, 545*K)

animal(0.22*K, 1, 162*K, 275*K)
animal(0.22*K, 1, 107*K, 334*K)
animal(1.5*K, 1, -90*K, 610*K)
animal(0.22*K, -1, 191*K, 363*K)
animal(0.682*K, -1, 428*K, 408*K)





run()
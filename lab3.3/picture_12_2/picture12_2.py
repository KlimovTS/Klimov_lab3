from graph import *


K=1.5
#K=0.5
#K=2

xSize=400
ySize=565
windowSize(xSize*K,ySize*K)



global_ii=0
global_i=-6*K
global_i1=-6*K
global_i2=-6*K
global_v1=1*K
global_v2=-2*K
global_r1=100*K
global_r2=150*K
global_x1=1
global_x2=1
global_R1=-1
global_R2=1



def animalLeg(k, r, x0, y0):
    obj=[]
    obj.append(ellyps(x0-13*k*r, y0+0*k, x0+13*k*r, y0+60*k))
    obj.append(ellyps(x0-13*k*r, y0+55*k, x0+13*k*r, y0+115*k))
    obj.append(ellyps(x0-5*k*r, y0+110*k, x0+25*k*r, y0+130*k))
    return obj

def animal(k, r, x0, y0):
    obj=[]
    xmid=97
    ymid=371
    penColor(255,255,255)
    brushColor(255,255,255)
    obj.append(ellyps(x0+100*k*r, y0+40*k, x0-100*k*r, y0-40*k))
    obj.append(ellyps(x0+75*k*r, y0-5*k, x0+115*k*r, y0-120*k))
    obj.append(ellyps(x0+85*k*r, y0-145*k, x0+135*k*r, y0-115*k))
    penColor(229,128,255)
    brushColor(229,128,255)
    obj.append(circle(x0+105*k*r, y0-132*k, 10*k))
    penColor(0,0,0)
    brushColor(0,0,0)
    obj.append(circle(x0+108*k*r, y0-132*k, 5*k))
    penColor(255,255,255)
    brushColor(255,255,255)
    obj.append(ellyps(x0+98*k*r, y0-140*k, x0+108*k*r, y0-136*k))
    penSize(6*k)
    obj.append(line(x0+90*k*r, y0-130*k, x0+70*k*r, y0-153*k))
    obj.append(line(x0+95*k*r, y0-135*k, x0+78*k*r, y0-158*k))
    penSize(1)
    penColor(255,255,255)
    brushColor(255,255,255)
    obj1=animalLeg(k, r, x0+80*k*r, y0+20*k)
    obj2=animalLeg(k, r, x0+50*k*r, y0-10*k)
    obj3=animalLeg(k, r, x0-40*k*r, y0+20*k)
    obj4=animalLeg(k, r, x0-80*k*r, y0-10*k)
    for i in obj1:
        obj.append(i)
    for i in obj2:
        obj.append(i)
    for i in obj3:
        obj.append(i)
    for i in obj4:
        obj.append(i)
    return obj



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



def moveMultiObj(obj, dx, dy):
    for i in obj:
        moveObjectBy(i, dx, dy)
        
def deleteMultiObj(obj):
    for i in obj:
        deleteObject(i)



def action():
    global global_i1
    global global_i2
    global global_i
    global global_v1
    global global_v2
    global global_r1
    global global_r2
    global global_animal1
    global global_animal2
    global global_animal3
    global global_animal4
    global global_animal5
    global global_x1
    global global_x2
    global global_R1
    global global_R2
    global global_ii
    global K
    if global_x1<=0 or global_x1>=global_r1:
        global_v1=-global_v1
        deleteMultiObj(global_animal1)
        global_animal1=animal(0.22*K, global_R1, 107*K+global_x1, 334*K)
        global_R1=-global_R1
        global_i1=-global_i1
    moveMultiObj(global_animal1, global_v1, 0)
    global_x1=global_x1+global_v1
    if global_x2<=0 or global_x2>=global_r2:
        global_v2=-global_v2
        deleteMultiObj(global_animal2)
        global_animal2=animal(0.22*K, global_R2, 191*K-global_x2, 363*K)
        global_R2=-global_R2
        global_i2=-global_i2
    moveMultiObj(global_animal2, global_v2, 0)
    global_x2=global_x2-global_v2
    if global_ii==50:
        moveObjectBy(global_animal1[4], global_i1*0.22, 0)
        moveObjectBy(global_animal2[4], global_i2*-0.22, 0)
        moveObjectBy(global_animal3[4], global_i*0.22, 0)
        moveObjectBy(global_animal4[4], global_i*1.5, 0)
        moveObjectBy(global_animal5[4], global_i*-0.682, 0)
        global_i=-global_i
        global_i1=-global_i1
        global_i2=-global_i2
        global_ii=0
    global_ii+=1





mountains(K)

kustik(0.24*K, 1, 13*K, 308*K)
kustik(0.24*K, 1, 300*K, 352*K)
kustik(0.6*K, 1, 304*K, 496*K)
kustik(0.367*K, -1, 374*K, 332*K)
kustik(0.6*K, -1, 385*K, 414*K)
kustik(0.333*K, -1, 407*K, 545*K)

global_animal3=animal(0.22*K, 1, 162*K, 275*K)
global_animal1=animal(0.22*K, 1, 107*K, 334*K) ###
global_animal4=animal(1.5*K, 1, -90*K, 610*K)
global_animal2=animal(0.22*K, -1, 191*K, 363*K) ###
global_animal5=animal(0.682*K, -1, 428*K, 408*K)


onTimer(action, 16)


run()
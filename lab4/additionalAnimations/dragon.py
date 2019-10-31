from graph import  *
import copy
import math
import time





new_Points=[[0, 0], [0, -1]]
global_polyline=0
new_Counter=0
quality = 100
timePerStage = 2000
global_max_stage  = 15
global_cur_stage  = 1





def maxAndMinXY(P):
    maX=-2222222222
    maY=-2222222222
    miX=2222222222
    miY=2222222222
    for i in P:
        if i[0]>maX:
            maX=i[0]
        if i[1]>maY:
            maY=i[1]
        if i[0]<miX:
            miX=i[0]
        if i[1]<miY:
            miY=i[1]
    return(maX, maY, miX, miY)

def draw(maX, maY, miX, miY, p):
    global global_polyline
    deleteObject(global_polyline)
    k=1
    dx=maX-miX
    dy=maY-miY
    tmp=max((dx, dy))
    k=700/tmp 
    x0=maX-dx/2
    y0=maY-dy/2
    points = copy.deepcopy(p)
    for i in points:
        i[0]=400+(i[0]-x0)*k
        i[1]=400+(i[1]-y0)*k
    penSize(k/10)
    penColor(0, 0, 0)
    brushColor(0, 0, 0)
    global_polyline=polyline(points)
    
def rotate(p, a):
    a = math.radians(a)
    sin = math.sin(a)
    cos = math.cos(a)
    for i in p:
        tmpx=i[0]
        tmpy=i[1]
        i[0]=cos*tmpx+sin*tmpy
        i[1]=-sin*tmpx+cos*tmpy
    return p

def rotate90(p):
    for i in p:
        tmpx=i[0]
        i[0]=i[1]
        i[1]=-tmpx
    return p

def movePolyLine(x0, y0, p):
    for i in p:
        i[0]=i[0]+x0
        i[1]=i[1]+y0
    return p

def reverse(p):
    l = len(p)
    p2 = []
    for i in range(0, l, 1):
        p2.append(p[l-1-i])
    return p2

def step(p):
    global new_Counter
    global quality
    p1 = copy.deepcopy(p)
    p1 = reverse(p1)
    if new_Counter%quality==0:
        p1 = rotate90(p1)
    else:
        p1 = rotate(p1, new_Counter%quality*(90/quality))
    tmp1 = len(p)-1
    x1=p[tmp1][0]
    y1=p[tmp1][1]
    x2=p1[0][0]
    y2=p1[0][1]
    p1 = movePolyLine(x1-x2, y1-y2, p1)
    P=[]
    for i in p:
        P.append(i)
    for i in range(1, len(p1), 1):
        P.append(p1[i])
    return P

def F(): 
    global new_Points
    global new_Counter
    global quality
    global global_cur_stage
    global global_max_stage
    if global_cur_stage < global_max_stage:
        if new_Counter==0:
            A=maxAndMinXY(new_Points)
            draw(A[0], A[1], A[2], A[3], new_Points)
        else:
            tmp = step(new_Points)
            A=maxAndMinXY(tmp)
            draw(A[0], A[1], A[2], A[3], tmp)
            if new_Counter%quality==0:
                new_Points = tmp
                global_cur_stage = global_cur_stage+1
        new_Counter=new_Counter+1
    return

onTimer(F, int(timePerStage*1000/quality))


from graph import  *
import copy
import math





new_Points=[[0, 0], [0, -1]]
global_polyline=0
new_Counter=0
quality = 10
timePerStage = 1
global_max_stage  = 15
global_cur_stage  = 1





def maxAndMinXY(P):
    maX=-2222222222
    maY=-2222222222
    miX=2222222222
    miY=2222222222
    for i in P:
        if i[0]>maX:
            maX=i[0]
        if i[1]>maY:
            maY=i[1]
        if i[0]<miX:
            miX=i[0]
        if i[1]<miY:
            miY=i[1]
    return(maX, maY, miX, miY)

def draw(maX, maY, miX, miY, p):
    deleteObject(global_polyline)
    global global_polyline
    k=1
    dx=maX-miX
    dy=maY-miY
    tmp=max((dx, dy))
    k=700/tmp 
    x0=maX-dx/2
    y0=maY-dy/2
    points = copy.deepcopy(p)
    for i in points:
        i[0]=400+(i[0]-x0)*k
        i[1]=400+(i[1]-y0)*k
    penSize(k/10)
    penColor(0, 0, 0)
    brushColor(0, 0, 0)
    global_polyline=polyline(points)
    
def rotate(p, a):
    a = math.radians(a)
    sin = math.sin(a)
    cos = math.cos(a)
    for i in p:
        tmpx=i[0]
        tmpy=i[1]
        i[0]=cos*tmpx+sin*tmpy
        i[1]=-sin*tmpx+cos*tmpy
    return p

def rotate90(p):
    for i in p:
        tmpx=i[0]
        i[0]=i[1]
        i[1]=-tmpx
    return p

def movePolyLine(x0, y0, p):
    for i in p:
        i[0]=i[0]+x0
        i[1]=i[1]+y0
    return p

def reverse(p):
    l = len(p)
    p2 = []
    for i in range(0, l, 1):
        p2.append(p[l-1-i])
    return p2

def step(p):
    global new_Counter
    global quality
    p1 = copy.deepcopy(p)
    p1 = reverse(p1)
    if new_Counter%quality==0:
        p1 = rotate90(p1)
    else:
        p1 = rotate(p1, new_Counter%quality*(90/quality))
    tmp1 = len(p)-1
    x1=p[tmp1][0]
    y1=p[tmp1][1]
    x2=p1[0][0]
    y2=p1[0][1]
    p1 = movePolyLine(x1-x2, y1-y2, p1)
    P=[]
    for i in p:
        P.append(i)
    for i in range(1, len(p1), 1):
        P.append(p1[i])
    return P

def F(): 
    global new_Points
    global new_Counter
    global quality
    global global_cur_stage
    global global_max_stage
    if global_cur_stage < global_max_stage:
        if new_Counter==0:
            A=maxAndMinXY(new_Points)
            draw(A[0], A[1], A[2], A[3], new_Points)
        else:
            tmp = step(new_Points)
            A=maxAndMinXY(tmp)
            draw(A[0], A[1], A[2], A[3], tmp)
            if new_Counter%quality==0:
                new_Points = tmp
                global_cur_stage = global_cur_stage+1
        new_Counter=new_Counter+1
    return

time.sleep(1)

onTimer(F, int(timePerStage*1000/quality))

run()
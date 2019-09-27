from graph import*
from math import*

def distance(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def ellipse(x1, y1, x2, y2, a, color_name):
    for i in range( ceil( (x1+x2)*0.5 - a*0.5  ), ceil( (x1+x2)*0.5 + a*0.5 ) ):
        for j in range( ceil( (y1+y2)*0.5 - a*0.5 ), ceil( (y1+y2)*0.5 + a*0.5 ) ):
            if ( (distance(x1, y1, i, j) + distance(x2, y2, i, j)) <= a ):
                point(i, j, color_name)

def framed_ellipse(x1, y1, x2, y2, a, color_name_1, d, color_name_2):
    penSize(d)
    for i in range( ceil( (x1+x2)*0.5 - a*0.5  ), ceil( (x1+x2)*0.5 + a*0.5 ) ):
        for j in range( ceil( (y1+y2)*0.5 - a*0.5 ), ceil( (y1+y2)*0.5 + a*0.5 ) ):
            if ( (distance(x1, y1, i, j) + distance(x2, y2, i, j)) <= a ):
                point(i, j, color_name_1)
            elif (abs((distance(x1, y1, i, j) + distance(x2, y2, i, j)) - a) <= d):
                point(i, j, color_name_2)

def right_wing(x1, y1, k):
    x2 = x1 + 5*k
    y2 = y1 + 4*k
    x3 = x2 + 4*k
    y3 = y2 + 2*k
    x4 = x3 + 7*k
    y4 = y3 + 1*k
    x5 = x4 + 8*k
    y5 = y4 - 2*k
    x6 = x5 + 5*k
    y6 = y5 + 4*k
    x7 = x6 + 3*k
    y7 = y6 + 7*k
    x8 = x7 - 8*k
    y8 = y7 + 5*k
    x9 = x8 - 4*k
    y9 = y8 - 2*k
    x10 = x9 - 2*k
    y10 = y9 - 5*k
    x11 = x10 - 12*k
    y11 = y10 - 4*k
    points = [[x1, y1], [x2, y2], [x3, y3], [x4, y4], [x5, y5], [x6, y6], [x7, y7], [x8, y8], [x9, y9], [x10, y10], [x11, y11]]
    polygon(points)

def left_wing(x1, y1, k):
    x2 = x1 + 1*k
    y2 = y1 + 5*k
    x3 = x2 + 3*k
    y3 = y2 + 4*k
    x4 = x3 + 6*k
    y4 = y3 + 4*k
    x5 = x4 + 8*k
    y5 = y4 + 2*k
    x6 = x5 + 3*k
    y6 = y5 + 5*k
    x7 = x6 - 1*k
    y7 = y6 + 8*k
    x8 = x7 - 9*k
    y8 = y7 + 0*k
    x9 = x8 - 3*k
    y9 = y8 - 3*k
    x10 = x9 - 0*k
    y10 = y9 - 5*k
    x11 = x10 - 9*k
    y11 = y10 - 9*k
    points = [[x1, y1], [x2, y2], [x3, y3], [x4, y4], [x5, y5], [x6, y6], [x7, y7], [x8, y8], [x9, y9], [x10, y10], [x11, y11]]
    polygon(points)

def tail(x1, y1, k):
    points = [[x1+14*k, y1+15*k], [x1+25*k, y1+25*k], [x1+10*k, y1+23*k]]
    polygon(points)

def leg(x1, y1, k):
    brushColor(255, 215, 0)
    points = [[x1+14*k, y1+9*k], [x1+20*k, y1+8*k], [x1+16*k, y1+10*k], [x1+21*k, y1+11*k], [x1+15*k, y1+11*k], [x1+19*k, y1+13*k], [x1+14*k, y1+11*k], [x1+12*k, y1+15*k], [x1+13*k, y1+11*k], [x1+10*k, y1+13*k], [x1+14*k, y1+9*k]]
    polygon(points)
    brushColor(255, 0, 0)
    ellipse(x1, y1, x1+5*k, y1+8*k, 1.2*distance(x1, y1, x1+5*k, y1+8*k), (255, 0, 0))
    ellipse(x1+5*k, y1+8*k, x1+3*k+11*k, y1+6*k+3*k, 1.1*distance(x1+5*k, y1+8*k, x1+14*k, y1+9*k), (255, 0, 0))

def beak(x1, y1, k):
    brushColor('gold')
    points = [[x1, y1], [x1+9*k, y1-2*k], [x1+13*k, y1+1*k]]
    polygon(points)
    points = [[x1, y1], [x1, y1+2*k],  [x1+10*k, y1+3*k], [x1+13*k, y1]]
    polygon(points)

def albatros_suka(x1, y1, k):
    brushColor(255, 0, 0)
    left_wing(x1 + 17 * k, y1 - 9 * k, k)
    right_wing(x1, y1, k)
    tail(x1, y1, k)
    leg(x1 + 25 * k, y1 + 26 * k, k)
    leg(x1 + 30 * k, y1 + 22 * k, k)
    ellipse(x1+22*k, y1+22*k, x1+48*k, y1+22*k, 29*k, (255, 0, 0))
    ellipse(x1+46*k, y1+22*k, x1+56*k, y1+22*k, 11.5*k, (255, 0, 0))
    beak(x1 + 63 * k, y1 + 19 * k, 0.8 * k)
    ellipse(x1 + 55 * k, y1 + 19 * k, x1 + 63 * k, y1 + 19 * k, 10 * k, (255, 0, 0))
    ellipse(x1 + 60 * k, y1 + 18 * k, x1 + 62 * k, y1 + 18 * k, 2.5 * k, 'black')

#(255, 201, 14)
#(255, 128, 0)

def fish(x1, y1, k, r):
    brushColor(255, 201, 14)
    penSize(1)
    points = [[x1 + k*r, y1], [x1 - 7 * k*r, y1 - 3 * k], [x1 - 7 * k*r, y1 + 3 * k]]
    polygon(points)
    brushColor(255, 128, 0)
    points = [[x1 + k*r, y1 + k], [x1 + 3 * k*r, y1 + k], [x1 + 3 * k*r, y1 + 5 * k], [x1 - 2 * k*r, y1 + 4 * k]]
    polygon(points)
    points = [[x1 + 10 * k*r, y1 - 2 * k], [x1 + 11 * k*r, y1 - 5 * k], [x1 + 5 * k*r, y1 - 6 * k], [x1 + 8 * k*r, y1 - 3 * k]]
    polygon(points)
    points = [[x1 + 10 * k*r, y1 + 2 * k], [x1 + 14 * k*r, y1 + 5 * k], [x1 + 10 * k*r, y1 + 6 * k], [x1 + 9 * k*r, y1 + 2 * k]]
    polygon(points)
    brushColor(95, 158, 160)
    framed_ellipse(x1, y1, x1 + 15 * k*r, y1, 16.5 * k, (255, 201, 14), 1, 'black')
    brushColor('blue')
    circle(x1 + 12.5 * k*r, y1, k)
    brushColor('grey')
    circle(x1 + 12.5 * k*r + 3, y1, 0.5*k)

def perehod(x1, y1, x2, y2, r1,g1,b1, r2,g2,b2):
    n=100
    dy=(y2-y1)/n
    dr=(r2-r1)/(n-1)
    dg=(g2-g1)/(n-1)
    db=(b2-b1)/(n-1)
    for i in range(0, n, 1):
        brushColor(int(r1+i*dr), int(g1+i*dg), int(b1+i*db))
        penColor(int(r1+i*dr), int(g1+i*dg), int(b1+i*db))
        rectangle(x1, y1+(i)*dy, x2, y1+(i+1)*dy)

windowSize(500, 600)

penSize(0)
#Фон рисунка
 
#brushColor(25, 25, 112)
#rectangle(0, 0, 500, 90)
#brushColor(123, 104, 238)
#rectangle(0, 0+90, 500, 90+40)
#brushColor(221, 160, 221)
#rectangle(0, 0+90+40, 500, 90+40+70)
#brushColor(238, 130, 238)
#rectangle(0, 0+90+40+70, 500, 90+40+70+100)
#brushColor(255, 160, 122)
#rectangle(0, 0+90+40+70+100, 500, 90+40+70+100+50)

#    brushColor(25, 25, 112)
#    brushColor(123, 104, 238)
#    brushColor(221, 160, 221)
#    brushColor(238, 130, 238)
#    brushColor(255, 160, 122)

perehod(0, 0, 500, 90, 25, 25, 112, 123, 104, 238)
perehod(0, 0+90, 500, 90+40, 123, 104, 238, 221, 160, 221)
perehod(0, 0+90+40, 500, 90+40+70, 221, 160, 221, 238, 130, 238)
perehod(0, 0+90+40+70, 500, 90+40+70+100+50, 238, 130, 238, 255, 160, 122)
#perehod(0, 0+90+40+70+100, 500, 90+40+70+100+50, 255, 160, 122, 255, 160, 122)
    
    

brushColor(70, 130, 180)
rectangle(0, 0+90+40+70+100+50, 500, 90+40+70+100+50+250)

albatros_suka(40, 350, 5)

albatros_suka(150, 200, 2)

fish(340, 540, 2, 1)
fish(300, 500, 1, 1)
fish(380, 500, 3, -1)
fish(420, 580, 4, -1)
fish(300, 580, 2, 1)

run()
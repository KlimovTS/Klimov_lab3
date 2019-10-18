from tkinter import *
import random
import time
import math

# создание окон
root = Tk()
width = 800
heigth = 600
heigth2 = 153
WH =  str(width)+'x'+str(heigth+heigth2)
root.geometry(WH)

# основной экран
canv = Canvas(root, width=width, height=heigth, bg='white')
canv.pack()
# полоса для счёта
c = Canvas(root, width=width, height=20, bg='lightgrey')
c.pack()
# окно с кнопками
d = Canvas(root, width=width, height=170, bg='white')
d.pack()



class Circle:
    
    def __init__(self):
        global time1x, timeMultiplier
        self.x = random.randint(100,700)
        self.y = random.randint(100,500)
        self.r = random.randint(10,40)
        self.c = randColor()
        self.vx = randSign()*random.randint(1, 8)
        self.vy = randSign()*random.randint(1, 8)
        self.lifeTime = 4000*timeMultiplier
        self.k=time1x/self.lifeTime
    
    def draw(self):
        canv.create_oval(self.x-self.r,self.y-self.r,self.x+self.r,self.y+self.r,fill = self.c , width=0)
    
    def drawAndMove(self):
        global width, heigth
        self.x += self.vx
        self.y += self.vy
        canv.create_oval(self.x-self.r,self.y-self.r,self.x+self.r,self.y+self.r,fill = self.c , width=0)
        if self.x+self.r>width:
            self.vx=-random.randint(1, 64)/8
        if self.x-self.r<0:
            self.vx=random.randint(1, 64)/8
        if self.y+self.r>heigth:
            self.vy=-random.randint(1, 64)/8
        if self.y-self.r<0:
            self.vy=random.randint(1, 64)/8
    
    def checkHit(self, x, y, r, obj, s):
        global counter
        if ((x-self.x)*(x-self.x)+(y-self.y)*(y-self.y)<(self.r+r)*(self.r+r)):
            counter+=1
            k1=(16+self.vx*self.vx+self.vy*self.vy)/16
            k2=20*20/self.r/self.r
            s.append(math.pi/4*k1*k2*self.k)
            tmp2=random.randint(0,11)
            if tmp2>=6:
                obj.append(Circle())
                obj.append(Circle())
            if tmp2==4 or tmp2==5:
                obj.append(Circle())
                obj.append(Square())
            if tmp2==2 or tmp2==3:
                obj.append(Circle())
                obj.append(CircleCircle())
            if tmp2==1:
                obj.append(Square())
                obj.append(Square())
            if tmp2==0:
                obj.append(CircleCircle())
                obj.append(CircleCircle())
            return [0, obj, s]
        else:
            return [1]
    
    def checkLifeTime(self, dt):
        self.lifeTime -= dt
        if self.lifeTime<0:
            return 0
        else:
            return 1

class Square:
    
    def __init__(self):
        global time1x, timeMultiplier
        self.x = random.randint(100,700)
        self.y = random.randint(100,500)
        self.r = random.randint(10,40)
        self.c = randColor()
        self.vx = randSign()*random.randint(9, 16)
        self.vy = randSign()*random.randint(9, 16)
        self.lifeTime = 9000*timeMultiplier
        self.k=time1x/self.lifeTime
    
    def draw(self):
        canv.create_rectangle(self.x+self.r, self.y+self.r, self.x-self.r, self.y-self.r, fill=self.c, width=0)
    
    def drawAndMove(self):
        global width, heigth
        self.x += self.vx
        self.y += self.vy
        canv.create_rectangle(self.x+self.r, self.y+self.r, self.x-self.r, self.y-self.r, fill=self.c, width=0)
        if self.x+self.r>width:
            self.vx=-random.randint(1, 128)/8
        if self.x-self.r<0:
            self.vx=random.randint(1, 128)/8
        if self.y+self.r>heigth:
            self.vy=-random.randint(1, 128)/8
        if self.y-self.r<0:
            self.vy=random.randint(1, 128)/8
    
    def checkHit(self, x, y, r, obj, s):
        global counter
        if (((x>self.x-self.r-r) and (x<self.x+self.r+r)) and ((y>self.y-self.r-r) and (y<self.y+self.r+r))):
            counter+=1
            k1=(16+self.vx*self.vx+self.vy*self.vy)/16
            k2=20*20/self.r/self.r
            s.append(1*k1*k2*self.k)
            tmp2=random.randint(0,11)
            if tmp2>=6:
                obj.append(Square())
                obj.append(Square())
            if tmp2==4 or tmp2==5:
                obj.append(Circle())
                obj.append(Square())
            if tmp2==2 or tmp2==3:
                obj.append(Square())
                obj.append(CircleCircle())
            if tmp2==1:
                obj.append(Circle())
                obj.append(Circle())
            if tmp2==0:
                obj.append(CircleCircle())
                obj.append(CircleCircle())
            return [0, obj, s]
        else:
            return [1]
    
    def checkLifeTime(self, dt):
        self.lifeTime -= dt
        if self.lifeTime<0:
            return 0
        else:
            return 1

class CircleCircle:
    
    def __init__(self):
        global time1x, timeMultiplier
        self.x = random.randint(100,700)
        self.y = random.randint(100,500)
        self.R = random.randint(20,60)
        self.r = random.randint(10,self.R-10)
        self.c = randColor()
        self.vx = randSign()*random.randint(1, 8)
        self.vy = randSign()*random.randint(1, 8)
        self.ax = randSign()*random.randint(1, 8)/8
        self.ay = randSign()*random.randint(1, 8)/8
        self.lifeTime = 6000*timeMultiplier
        self.k=time1x/self.lifeTime
        self.Points = []
        n = 90
        for i in range(0, n+2, 1):
            tmpx = self.R*math.cos(2*math.pi/n*i)
            tmpy = self.R*math.sin(2*math.pi/n*i)
            self.Points.append((tmpx, tmpy))
        for i in range(0, n+2, 1):
            tmpx = self.r*math.cos(2*math.pi/n*(n+1-i))
            tmpy = self.r*math.sin(2*math.pi/n*(n+1-i))
            self.Points.append((tmpx, tmpy))
    
    def draw(self):
        P = movePoly(self.Points, self.x, self.y)
        canv.create_polygon(P, fill=self.c, width=0)
    
    def drawAndMove(self):
        global width, heigth
        self.vx += self.ax
        self.vy += self.ay
        self.x += self.vx
        self.y += self.vy
        P = movePoly(self.Points, self.x, self.y)
        canv.create_polygon(P, fill=self.c, width=0)
        if self.x+self.R>width:
            self.vx=-random.randint(1, 8)
            self.ax=randSign()*random.randint(1, 8)/32
            self.ay=randSign()*random.randint(1, 8)/32
        if self.x-self.R<0:
            self.vx=random.randint(1, 8)
            self.ax=randSign()*random.randint(1, 8)/32
            self.ay=randSign()*random.randint(1, 8)/32
        if self.y+self.R>heigth:
            self.vy=-random.randint(1, 8)
            self.ax=randSign()*random.randint(1, 8)/32
            self.ay=randSign()*random.randint(1, 8)/32
        if self.y-self.R<0:
            self.vy=random.randint(1, 8)
            self.ax=randSign()*random.randint(1, 8)/32
            self.ay=randSign()*random.randint(1, 8)/32
    
    def checkHit(self, x, y, r, obj, s):
        global counter
        if (x-self.x)*(x-self.x)+(y-self.y)*(y-self.y)<((self.R+r)*(self.R+r)) and ((x-self.x)*(x-self.x)+(y-self.y)*(y-self.y))**0.5>(self.r-r):
            counter+=1
            k1=(16+self.vx*self.vx+self.vy*self.vy)/16
            k2=20*20/(self.R*self.R-self.r*self.r)
            s.append(math.pi/4*k1*k2*self.k*2)
            tmp2=random.randint(0,11)
            if tmp2>=6:
                obj.append(CircleCircle())
                obj.append(CircleCircle())
            if tmp2==4 or tmp2==5:
                obj.append(CircleCircle())
                obj.append(Square())
            if tmp2==2 or tmp2==3:
                obj.append(Circle())
                obj.append(CircleCircle())
            if tmp2==1:
                obj.append(Square())
                obj.append(Square())
            if tmp2==0:
                obj.append(Circle())
                obj.append(Circle())
            return [0, obj, s]
        else:
            return [1]
    
    def checkLifeTime(self, dt):
        self.lifeTime -= dt
        if self.lifeTime<0:
            return 0
        else:
            return 1
    
# КНОПКИ:

# функция кнопки():
#      что - то
# кнопка
            
# перезапуск игры
def Freset():
    global lock1, lock2, lock3, lock4, pause, startbool, playername, leaderboard, rules, prevpause
    if not (lock1 or lock2 or lock3 or lock4) and playername!='' and leaderboard==0 and rules==0:
        if startbool:
            pause = 0
            Bpause.configure(text = "pause")
            reset.configure(text = "reset")
        startbool=0
        start()
        lock1 = 1
        lock2 = 1
        lock3 = 1
        lock4 = 1
        BLock1.configure(text = "locked")
        BLock2.configure(text = "locked")
        BLock3.configure(text = "locked")
        BLock4.configure(text = "locked")
        canv.delete(ALL)
        if len(Objects)==0:
            if startbool==0:
                canv.delete(ALL)
                canv.create_text(width/2, heigth/2, text="Game over!", justify=CENTER, font="Verdana 70")
        else:
            canv.delete(ALL)
            for j in Objects:
                j.draw()
reset = Button(d, text="start", command=Freset, font="Verdana 25")
reset.grid(column=4, row=5)
# кнопка паузы
def Fpause():
    global pause, active
    if active==1:
        pause = 1-pause
        if pause:
            Bpause.configure(text = "unpause")
        else:
            Bpause.configure(text = "pause")
Bpause = Button(d, text="pause", command=Fpause, font="Verdana 25")
Bpause.grid(column=5, row=5)
# кнопка открытия таблицы лидеров
def Fleaderboard():
    global leaderboard, pause, prevpause, rules
    leaderboard = 1-leaderboard
    if leaderboard:
        prevpause = pause
        pause=0
        Fpause()
        rules=1
        Frules()
        Bleaderboard.configure(text = "close leaderboard")
    else:
        pause = 1-prevpause
        Fpause()
        if rules==0:
            canv.delete(ALL)
            if len(Objects)==0:
                if startbool==0:
                    canv.delete(ALL)
                    canv.create_text(width/2, heigth/2, text="Game over!", justify=CENTER, font="Verdana 70")
            else:
                canv.delete(ALL)
                for j in Objects:
                    j.draw()
        Bleaderboard.configure(text = "open leaderboard")
Bleaderboard = Button(d, text="open leaderboard", command=Fleaderboard, font="Verdana 25")
Bleaderboard.grid(column=6, row=5)
# кнопка открытия правил
def Frules():
    global  leaderboard, pause, prevpause, rules
    rules = 1-rules
    if rules:
        prevpause = pause
        pause=0
        Fpause()
        leaderboard=1
        Fleaderboard()
    else:
        pause = 1-prevpause
        Fpause()
        if leaderboard==0:
            canv.delete(ALL)
            if len(Objects)==0:
                if startbool==0:
                    canv.delete(ALL)
                    canv.create_text(width/2, heigth/2, text="Game over!", justify=CENTER, font="Verdana 70")
            else:
                canv.delete(ALL)
                for j in Objects:
                    j.draw()
Brules = Button(d, text="?!", command=Frules, font="Verdana 25")
Brules.grid(column=7, row=5)
# предохранитель перезапуска
def Flock1():
    global lock1
    lock1 = 1-lock1
    if lock1:
        BLock1.configure(text = "locked")
    else:
        BLock1.configure(text = "unlocked")
BLock1 = Button(d, text="locked", command=Flock1)
BLock1.grid(column=0, row=0)
# предохранитель перезапуска
def Flock2():
    global lock2
    lock2 = 1-lock2
    if lock2:
        BLock2.configure(text = "locked")
    else:
        BLock2.configure(text = "unlocked")
BLock2 = Button(d, text="locked", command=Flock2)
BLock2.grid(column=0, row=10)
# предохранитель перезапуска
def Flock3():
    global lock3
    lock3 = 1-lock3
    if lock3:
        BLock3.configure(text = "locked")
    else:
        BLock3.configure(text = "unlocked")
BLock3 = Button(d, text="locked", command=Flock3)
BLock3.grid(column=10, row=0)
# предохранитель перезапуска
def Flock4():
    global lock4
    lock4 = 1-lock4
    if lock4:
        BLock4.configure(text = "locked")
    else:
        BLock4.configure(text = "unlocked")
BLock4 = Button(d, text="locked", command=Flock4)
BLock4.grid(column=10, row=10)
# установка имени игрока
def Fsetname():
    global playername
    a = e.get()
    e.delete(first=0, last=END)
    if a!='':
        playername = a
    d.delete(ALL)
    txt='Player name: '+playername
    d.create_text(360, 110, text=txt, justify=CENTER, font="Verdana 14", anchor=W)
Bsetname = Button(d, text="SET NAME   ------>", command=Fsetname)
Bsetname.grid(column=4, row=10)

# поле ввода имени игрока
e = Entry(d, width=29)
e.grid(column=5, row=10)

# создание необходимых переменных
playername=''
startbool=1
lock1=1
lock2=1
lock3=1
lock4=1
Score=0
pause=0
prevpause=0
leaderboard=0
rules=0
active=1
I="0"
dI = 0
Difficulty="1"
#[Тип, [параметры]]
#0 - круг
#1 - квадрат
Objects=[]
frameTime=0
frameTime0=1600
time1x=6000
counter=0
timeMultiplier=2
LeaderBoardText = []
clickStreak = 0
MouseRadius = 0
for i  in range(0, 10, 1):
    LeaderBoardText.append(['0\n', 0])

# расставляет параметры для начала игры
def start():
    global Score, I, dI, Objects, frameTime, time1x, counter, timeMultiplier, Difficulty, active, clickStreak, MouseRadius
    active = 1
    MouseRadius=50
    clickStreak=0
    Score=0
    I="0"
    dI = 0
    Objects=[]
    frameTime=frameTime0
    time1x=6000
    counter=0
    timeMultiplier=2
    Difficulty='difficulty='+mstr(2/timeMultiplier)+'   radius bonus='+str(clickStreak)
    #круги
    for j in range(0, random.randint(2,6), 1):
        Objects.append(Circle())
    #квадраты    
    for j in range(0, random.randint(2,6), 1):
        Objects.append(Square())
    #бублики
    for j in range(0, random.randint(2,6), 1):
        Objects.append(CircleCircle())
        
# расставляет параметры для запуска игры
def start0():
    global Score, I, dI, Objects, frameTime, time1x, counter, timeMultiplier, Difficulty, active, startbool, MouseRadius
    startbool=1
    clickStreak=0
    MouseRadius=50
    loadLeaderBoardText()
    Fsetname()
    Score=0
    I="0"
    dI = 0
    Objects=[]
    frameTime=frameTime0
    time1x=6000
    counter=0
    timeMultiplier=2
    Difficulty='difficulty='+mstr(2/timeMultiplier)+'   radius bonus='+str(clickStreak)
    Fpause()
    lock1=1
    lock2=1
    lock3=1
    lock4=1
    Flock1()
    Flock2()
    Flock3()
    Flock4()
    active = 0

# сохраняет таблицу лидеров
def saveresult():
    global LeaderBoardText
    f1 = open('leaderboardNames.txt', 'w')
    f2 = open('leaderboardScores.txt', 'w')
    for i in LeaderBoardText:
        f1.write(i[0])
        f2.write(str(i[1])+'\n')
    f1.close()
    f2.close()

# загружает таблицу лидеров
def loadLeaderBoardText():
    global LeaderBoardText
    try:
        f1 = open('leaderboardNames.txt', 'r')
    except FileNotFoundError:
        f1 = open('leaderboardNames.txt', 'w')
    try:
        f2 = open('leaderboardScores.txt', 'r')
    except FileNotFoundError:
        f2 = open('leaderboardScores.txt', 'w')
    f1 = open('leaderboardNames.txt', 'r')
    f2 = open('leaderboardScores.txt', 'r')
    a1 = []
    a2 = []
    for i  in f1:
        a1.append(i)
    for i  in f2:
        a2.append(i)
    for i in range(0, len(a1), 1):
        LeaderBoardText.append([a1[i], float(a2[i])])
    LeaderBoardText.sort(key=mySort, reverse=True)
    A = []
    for i in range(0, 10, 1):
        A.append(LeaderBoardText[i])
    LeaderBoardText = A
    f1.close()
    f2.close()

# выдаёт либо 1 либо -1
def randSign():
    a = random.randint(0, 1)
    a = a*2
    a = a-1
    return a

# смещение полигона
def movePoly(points, dx, dy):
    P = []
    for i in points:
        P.append((i[0]+dx, i[1]+dy))
    return P

# выдаёт случайный цвет
def randColor():
    r = 255
    g = 255
    b = 255
    while r+g+b>675:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
    col = "#%02X%02X%02X" % (r, g, b)
    return col

# преобразует float в str округляя до 2 знаков после запятой
def mstr(a):
    a=a*100
    b=int(a)
    if (a-b)>=0.5:
        b=b+1
    b=b/100
    return str(b)

# функция  для сортировки
def mySort(a):
    return a[1]

# отрисовка всего нужного
def draw():
    global I, Objects, frameTime, width, heigth, pause, lock1, lock2, lock3,  lock4, active, leaderboard, LeaderBoardText, playername, Score, rules
    if rules: # отрисовка  правил
        canv.delete(ALL)
        rule1  = 'Правила игры' + '\n'
        rule  = '1) Чтобы начать игру нужно задать имя.' + '\n'
        rule  += '2) Защита от  рестарта, чтобы перезапустить игру не' + '\n'
        rule  += 'проиграв, нужно разблокировать  4 кнопки по углам.' + '\n'
        rule  += '3) Сохраняются только 10 лучших результатов.' + '\n'
        rule  += '4) Подсчёт очков: количество очков за фигуру' + '\n'
        rule  += 'зависит от площади фигуры, квадрата скорости и' + '\n'
        rule  += 'времени жизни фигуры.' + '\n'
        rule  += '5) Параметр COMBO показывает сколько за  раз было' + '\n'
        rule  += 'задето фигур, все бонусы умножаются на этот параметр.' + '\n'
        rule  += '6) Параметр DIFFICULTY отражает во сколько раз' + '\n'
        rule  += 'меньше чем в начале живут фигурки (в начале квадрат -' + '\n'
        rule  += 'примерно 18 сек, бублик - 12 сек, круг - 8 сек).' + '\n'
        rule  += '7)Параметр RADIUS BONUS показывает какой будет радиус' + '\n'
        rule  += 'курсора, это упрощает попадание, за промах' + '\n'
        rule  += 'снимается 4 очка, за попаданет добавляется 1 очко.' + '\n'
        rule  += 'При RADIUS BONUS  --> бесконечность - радиус курсора' + '\n'
        rule  += 'примерно равен максимально возможному кругу' + '\n'
        rule  += '(R ~ 1 - 0,99^RADIUS BONUS).' + '\n'
        rule  += '8) Игра кончаеся когда не остаётся фигур, при' + '\n'
        rule  += 'попадании  появляется 2 фигуры.' + '\n'
        canv.create_text(400, 60, text=rule1, justify=CENTER, font="Verdana 30")
        canv.create_text(400, 330, text=rule, justify=CENTER, font="Verdana 15")
    elif leaderboard: # отрисовка таблицы лидеров
        canv.delete(ALL)
        for i in range(0, 10, 1):
            txt = str(i+1) + '     ' + LeaderBoardText[i][0][:-1] + ' = ' + mstr(LeaderBoardText[i][1]) + ' Points'
            canv.create_text(30, 30+60*i, text=txt, justify=CENTER, font="Verdana 30", anchor=W)
    else:
        if pause==0:
            if len(Objects)==0: # условие конца игры
                if active: # условие для однократного срабатывания конца игры
                    canv.delete(ALL)
                    canv.create_text(width/2, heigth/2, text="Game over!", justify=CENTER, font="Verdana 70")
                    lock1=1
                    lock2=1
                    lock3=1
                    lock4=1
                    Flock1()
                    Flock2()
                    Flock3()
                    Flock4()
                    LeaderBoardText.append([playername+'\n', Score])
                    LeaderBoardText.sort(key=mySort, reverse=True)
                    A = []
                    for i in range(0, 10, 1):
                        A.append(LeaderBoardText[i])
                    LeaderBoardText = A
                    saveresult()
                    active = 0
            else: # отрисовка  игры
                canv.delete(ALL)
                c.delete(ALL)
                c.create_text(30, 10, text=I, justify=CENTER, font="Verdana 14", anchor=W)
                c.create_text(770, 10, text=Difficulty, justify=CENTER, font="Verdana 14", anchor=E)
                # обработка времени жизни объектов
                tmpObj = []
                for j in Objects: 
                    if j.checkLifeTime(frameTime):
                        tmpObj.append(j)
                # обработка движения
                Objects = tmpObj
                for j in Objects:
                    j.drawAndMove()
                        
    
    
    
    root.after(frameTime, draw)

# обработка кликов
def click(event):
    global Score, I, Objects, dI, counter, timeMultiplier,  Difficulty, pause, clickStreak, rules, leaderboard, MouseRadius, active
    if pause==0 and active==1:
        obj = []
        s = []
        d = []
        combo = 0
        tmpR=50-MouseRadius
        tmpR=tmpR*(timeMultiplier)**0.5
        for j in Objects:
            a = j.checkHit(event.x, event.y, tmpR, obj, s)
            if a[0]: # оставляет объекты по которым небыло попадания
                obj.append(j)
            else: # усложнение при попадании
                timeMultiplier = timeMultiplier*0.9931
        Objects=obj
        ss = 0
        for i in s:
            ss+=i
        dI = ss*len(s)
        combo = len(s)
        if rules==0 and leaderboard==0:
            if len(s)==0:
                clickStreak=clickStreak-4
                if clickStreak<0:
                    clickStreak=0
                tmpR=50-MouseRadius
                tmpR=tmpR*(timeMultiplier)**0.5
                MouseRadius=MouseRadius/(0.99**4)
                if MouseRadius>50:
                    MouseRadius=50
                canv.create_oval(event.x+tmpR, event.y+tmpR, event.x-tmpR, event.y-tmpR, fill = "red" , width=0)
            else:
                clickStreak+=len(s)*combo
                tmpR=50-MouseRadius
                tmpR=tmpR*(timeMultiplier)**0.5
                MouseRadius=MouseRadius*(0.99**(len(s)*combo))
                canv.create_oval(event.x+tmpR, event.y+tmpR, event.x-tmpR, event.y-tmpR, fill = "black" , width=0)
        Score+=dI
        # изменение выводимого текста счётчиков
        Difficulty='difficulty='+mstr(2/timeMultiplier)+'   radius bonus='+str(clickStreak)
        if combo>0:
            if combo>1:
                I=mstr(Score)+' +'+mstr(dI)+'   '+str(combo)+'x combo'
            else:
                I=mstr(Score)+' +'+mstr(dI)
        else:
            I = mstr(Score)


start0()
draw()
canv.bind('<Button-1>', click)
mainloop()
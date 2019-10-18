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
                if j[0]==0:
                    circle0t(j[1])
                if j[0]==1:
                    square0t(j[1])
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
                    if j[0]==0:
                        circle0t(j[1])
                    if j[0]==1:
                        square0t(j[1])
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
                    if j[0]==0:
                        circle0t(j[1])
                    if j[0]==1:
                        square0t(j[1])
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
frameTime0=16
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
    for j in range(0, 5, 1):
        Objects.append(randCircle())
    #квадраты    
    for j in range(0, 5, 1):
        Objects.append(randSquare())
        
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

# выдаёт либо 1 либо -1
def randSign():
    a = random.randint(0, 1)
    a = a*2
    a = a-1
    return a

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

# создаёт случайный круг
def randCircle():
    global time1x, timeMultiplier
    x = random.randint(100,700)
    y = random.randint(100,500)
    r = random.randint(10,40)
    color = randColor()
    vx = randSign()*random.randint(1, 8)
    vy = randSign()*random.randint(1, 8)
    lifeTime = 4000*timeMultiplier
    k=time1x/lifeTime
    return [0, [x, y, r, color, vx, vy, lifeTime, k]]

# создааёт случайный квадрат
def randSquare():
    global time1x, timeMultiplier
    x = random.randint(100,700)
    y = random.randint(100,500)
    r = random.randint(10,40)
    color = randColor()
    vx = randSign()*random.randint(9, 16)
    vy = randSign()*random.randint(9, 16)
    lifeTime = 9000*timeMultiplier
    k=time1x/lifeTime
    return [1, [x, y, r, color, vx, vy, lifeTime, k]]

# обрабатывает движение и столкновения круга, рисует его
def circle(a):
    global width, heigth
    vx = a[4]
    vy = a[5]
    a[0]=a[0]+vx
    a[1]=a[1]+vy
    x = a[0]
    y = a[1]
    r = a[2]
    c = a[3]
    canv.create_oval(x-r,y-r,x+r,y+r,fill = c , width=0)
    if x+r>width:
        a[4]=-random.randint(1, 64)/8
    if x-r<0:
        a[4]=random.randint(1, 64)/8
    if y+r>heigth:
        a[5]=-random.randint(1, 64)/8
    if y-r<0:
        a[5]=random.randint(1, 64)/8

# рисует круг
def circle0t(a):
    global width, heigth
    x = a[0]
    y = a[1]
    r = a[2]
    c = a[3]
    canv.create_oval(x-r,y-r,x+r,y+r,fill = c , width=0)
    
# обрабатывает движение и столкновения квадрата, рисует его
def square(a):
    global width, heigth
    vx = a[4]
    vy = a[5]
    a[0]=a[0]+vx
    a[1]=a[1]+vy
    x = a[0]
    y = a[1]
    r = a[2]
    c = a[3]
    canv.create_rectangle(x+r, y+r, x-r, y-r, fill=c, width=0)
    if x+r>width:
        a[4]=-random.randint(1, 128)/8
    if x-r<0:
        a[4]=random.randint(1, 128)/8
    if y+r>heigth:
        a[5]=-random.randint(1, 128)/8
    if y-r<0:
        a[5]=random.randint(1, 128)/8

# рисует квадрат
def square0t(a):
    global width, heigth
    x = a[0]
    y = a[1]
    r = a[2]
    c = a[3]
    canv.create_rectangle(x+r, y+r, x-r, y-r, fill=c, width=0)

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
        rule  += 'примерно 18 сек, круг - 12 сек).' + '\n'
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
                # обработка движения
                for j in Objects:
                    if j[0]==0:
                        circle(j[1])
                    if j[0]==1:
                        square(j[1])
                # обработка времени жизни объектов
                for j in Objects: 
                    j[1][6]=j[1][6]-frameTime
                    if j[1][6]<0:
                        Objects.remove(j)
                        
    
    
    
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
        tmpR=tmpR/(2/timeMultiplier)**0.5
        for j in Objects:
            tmp = 1
            if j[0]==0:  # обработка объекта если это круг
                if (event.x-j[1][0])*(event.x-j[1][0])+(event.y-j[1][1])*(event.y-j[1][1])<((j[1][2]+tmpR)*(j[1][2]+tmpR)):
                    counter+=1
                    k1=(16+j[1][4]*j[1][4]+j[1][5]*j[1][5])/16
                    k2=20*20/j[1][2]/j[1][2]
                    s.append(math.pi/4*k1*k2*j[1][7])
                    tmp2=random.randint(0,5)
                    if tmp2==0:
                        obj.append(randCircle())
                        obj.append(randCircle())
                    if tmp2==1:
                        obj.append(randCircle())
                        obj.append(randCircle())
                    if tmp2==2:
                        obj.append(randCircle())
                        obj.append(randCircle())
                    if tmp2==3:
                        obj.append(randCircle())
                        obj.append(randSquare())
                    if tmp2==4:
                        obj.append(randCircle())
                        obj.append(randSquare())
                    if tmp2==5:
                        obj.append(randSquare())
                        obj.append(randSquare())
                    tmp = 0
            if j[0]==1: # обработка объекта если это квадрат
                if (((event.x>j[1][0]-j[1][2]-tmpR) and (event.x<j[1][0]+j[1][2]+tmpR)) and ((event.y>j[1][1]-j[1][2]-tmpR) and (event.y<j[1][1]+j[1][2]+tmpR))):
                    counter+=1
                    k1=(16+j[1][4]*j[1][4]+j[1][5]*j[1][5])/16
                    k2=20*20/j[1][2]/j[1][2]
                    s.append(1*k1*k2*j[1][7])
                    tmp2=random.randint(0,5)
                    if tmp2==0:
                        obj.append(randSquare())
                        obj.append(randSquare())
                    if tmp2==1:
                        obj.append(randSquare())
                        obj.append(randSquare())
                    if tmp2==2:
                        obj.append(randSquare())
                        obj.append(randSquare())
                    if tmp2==3:
                        obj.append(randSquare())
                        obj.append(randCircle())
                    if tmp2==4:
                        obj.append(randSquare())
                        obj.append(randCircle())
                    if tmp2==5:
                        obj.append(randCircle())
                        obj.append(randCircle())
                    tmp = 0
            if tmp: # оставляет объекты по которым небыло попадания
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
                tmpR=tmpR/(2/timeMultiplier)**0.5
                MouseRadius=MouseRadius/(0.99**4)
                if MouseRadius>50:
                    MouseRadius=50
                canv.create_oval(event.x+tmpR, event.y+tmpR, event.x-tmpR, event.y-tmpR, fill = "red" , width=0)
            else:
                clickStreak+=len(s)*combo
                tmpR=50-MouseRadius
                tmpR=tmpR/(2/timeMultiplier)**0.5
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
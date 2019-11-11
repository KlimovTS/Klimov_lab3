import tkinter

closed=1
answer=2
root=0
canv=0

def KeyboardKeys():
    keys = []
    for i in range(97, 123):
        keys.append(chr(i))
    return keys

def init(roote, canva):
    global root, canv
    root = roote
    canv = canva

def Close():
    global closed
    closed=1

def o1(a=0):
    global answer
    root.bind('<Key-1>', '')
    root.bind('<Key-2>', '')
    root.bind('<Key-3>', '')
    answer = 0
def o2(a=0):
    global state
    state=1
def o3(a=0):
    global state
    state=2-state

def Open():
    global closed
    root.bind('<Key-1>', o1)
    root.bind('<Key-2>', o2)
    root.bind('<Key-3>', o3)
    closed=0

state=0
pauseChar='p'

for i in KeyboardKeys():
    txt='def f'+i+'''(a=0):
        global pauseChar, state
        pauseChar=\''''+i+'\''+'''
        for i in KeyboardKeys():
            root.bind('<Key-'+i+'>', '')
        state=0'''
    exec(txt)

def window():
    global state, pauseChar
    if state==0:
        txt=''
        txt+='Выйти в меню(1)\n'
        txt+=pauseChar+' - пауза(2)\n'
        txt+='Об игре(3)'
        canv.delete(tkinter.ALL)
        canv.create_text(400,300,text=txt,font='Verdana 50')
    if state==1:
        canv.delete(tkinter.ALL)
        canv.create_text(400,300,text='Нажмите кнопку для паузы',font='Verdana 25')
        root.bind('<Key-'+pauseChar+'>','')
        if pauseChar!='':
            for i in KeyboardKeys():
                txt = 'root.bind(\'<Key-'+i+'>\', f'+i+')'
                exec(txt)
        pauseChar=''
    if state==2:
        canv.delete(tkinter.ALL)
        txt=''
        txt+='Цель - уничтожать шарики из пушки.\n'
        txt+='Выход обычно на кнопку 1.\n'
        txt+='Кнопку паузы можно настроить.\n'
        txt+='Выйти(3)'
        canv.create_text(400,300,text=txt,font='Verdana 25')
        
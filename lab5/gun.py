from random import randrange as rnd,choice
import random
from tkinter import*
import math
import time
root=Tk()
fr=Frame(root)
root.geometry('800x600')
canv=Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)
class ball():
 def __init__(self,x=40,y=450):
  self.x=x
  self.y=y
  self.r=10
  self.vx=0
  self.vy=0
  self.color=choice(['blue','green','red','brown'])
  self.id=canv.create_oval(self.x-self.r,self.y-self.r,self.x+self.r,self.y+self.r,fill=self.color)
  self.live=30
 def set_coords(self):
  canv.coords(self.id,self.x-self.r,self.y-self.r,self.x+self.r,self.y+self.r)
 def move(self):
  if self.y<=550:
   self.vy-=1.2
   self.y-=self.vy
   self.x+=self.vx
   self.vx*=0.99
   self.set_coords()
  else:
   if self.vx**2+self.vy**2>10:
    self.vy=-self.vy/2
    self.vx=self.vx/2
    self.y=549
   if self.live<0:
    balls.pop(balls.index(self))
    canv.delete(self.id)
   else:
    self.live-=1
  if self.x>780:
   self.vx=-self.vx/2
   self.x=779
 def hittest(self,ob):
  if abs(ob.x-self.x)**2+abs(ob.y-self.y)**2<=(self.r+ob.r)**2:
   return True
  else:
   return False
"""
xd0x9axd0xbbxd0xb0xd1x81xd1x81 gun xd0xbexd0xbfxd0xb8xd1x81xd1x8bxd0xb2xd0xb0xd0xb5xd1x82 xd0xbfxd1x83xd1x88xd0xbaxd1x83. 
"""
class gun():
 def __init__(self):
  self.f2_power=10
  self.f2_on=0
  self.an=1
  self.id=canv.create_line(20,450,50,420,width=7)
 def fire2_start(self,event):
  self.f2_on=1
 def fire2_end(self,event):
  global balls,bullet
  bullet+=1
  new_ball=ball()
  new_ball.r+=5
  self.an=math.atan((event.y-new_ball.y)/(event.x-new_ball.x))
  new_ball.vx=self.f2_power*math.cos(self.an)
  new_ball.vy=-self.f2_power*math.sin(self.an)
  balls+=[new_ball]
  self.f2_on=0
  self.f2_power=10
 def targetting(self,event=0):
  if event:
   self.an=math.atan((event.y-450)/(event.x-20)) 
  if self.f2_on:
   canv.itemconfig(self.id,fill='orange')
  else:
   canv.itemconfig(self.id,fill='black')
  canv.coords(self.id,20,450,20+max(self.f2_power,20)*math.cos(self.an),450+max(self.f2_power,20)*math.sin(self.an))
 def power_up(self):
  if self.f2_on:
   if self.f2_power<100:
    self.f2_power+=1
   canv.itemconfig(self.id,fill='orange')
  else:
   canv.itemconfig(self.id,fill='black')
"""
xd0x9axd0xbbxd0xb0xd1x81xd1x81 target xd0xbexd0xbfxd0xb8xd1x81xd1x8bxd0xb2xd0xb0xd0xb5xd1x82 xd1x86xd0xb5xd0xbbxd1x8c. 
"""
class target():
 def __init__(self):
  self.points=0
  self.id=canv.create_oval(0,0,0,0)
  #self.id_points=canv.create_text(30,30,text=self.points,font='28')
  self.new_target()
  self.live=1
  self.vx=0
  self.vy=0
 def move(self):
  self.x+=self.vx
  self.y+=self.vy
  x=self.x
  y=self.y
  r=self.r
  if x<300+r:
   self.vx=abs(self.vx)
  if x>800-r:
   self.vx=-abs(self.vx)
  if y<50+r:
   self.vy=abs(self.vx)
  if y>550-r:
   self.vy=-abs(self.vx)
  canv.coords(self.id,x-r,y-r,x+r,y+r)
 def new_target(self):
  x=self.x=rnd(600,780)
  y=self.y=rnd(300,550)
  r=self.r=rnd(2,50)
  color=self.color='red'
  canv.coords(self.id,x-r,y-r,x+r,y+r)
  canv.itemconfig(self.id,fill=color)
  self.vx=rnd(-5,5)
  self.vy=rnd(-5,5)
 def hit(self,points=1):
  canv.coords(self.id,-10,-10,-10,-10)
  self.points+=points
  #canv.itemconfig(self.id_points,text=self.points)
t1=target()
t2=target()
t3=target()
id_points=canv.create_text(30,30,text=t1.points+t2.points+t3.points,font='28')
screen1=canv.create_text(400,300,text='',font='28')
g1=gun()
bullet=0
balls=[]
def new_game(event=''):
 global gun,t1,t2,t3,id_points,screen1,balls,bullet
 t1.new_target()
 t2.new_target()
 t3.new_target()
 bullet=0
 balls=[]
 canv.bind('<Button-1>',g1.fire2_start)
 canv.bind('<ButtonRelease-1>',g1.fire2_end)
 canv.bind('<Motion>',g1.targetting)
 z=0.03
 t1.live=1
 t2.live=1
 t3.live=1
 while t1.live or t2.live or t3.live or balls:
  for b in balls:
   b.move()
   if b.hittest(t1)and t1.live:
    t1.live=0
    t1.hit()
   if b.hittest(t2)and t2.live:
    t2.live=0
    t2.hit()
   if b.hittest(t3)and t3.live:
    t3.live=0
    t3.hit()
   if t1.live==0 and t2.live==0 and t3.live==0:
    canv.bind('<Button-1>','')
    canv.bind('<ButtonRelease-1>','')
    canv.itemconfig(screen1,text='Вы уничтожили цели за '+str(bullet)+' выстрелов')
   canv.itemconfig(id_points,text=t1.points+t2.points+t3.points)
  if t1.live==1:
   t1.move()
  if t2.live==1:
   t2.move()
  if t3.live==1:
   t3.move()
  canv.update()
  time.sleep(0.03)
  g1.targetting()
  g1.power_up()
 canv.itemconfig(screen1,text='')
 canv.delete(gun)
 root.after(750,new_game)
new_game() 
mainloop()
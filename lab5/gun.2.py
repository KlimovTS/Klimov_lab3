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
idCounter=0
class ball():
 def __init__(self,x=40,y=450, owner=0):
  self.owner=owner
  if owner.owner!=0:
      x=owner.owner.x
      y=owner.owner.y
  self.idC=int(self.owner.owner.idC)
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
  if ((abs(ob.x-self.x)**2+abs(ob.y-self.y)**2<=(self.r+ob.r)**2) and (not self.idC==ob.idC)):
   return True
  else:
   return False
"""
xd0x9axd0xbbxd0xb0xd1x81xd1x81 gun xd0xbexd0xbfxd0xb8xd1x81xd1x8bxd0xb2xd0xb0xd0xb5xd1x82 xd0xbfxd1x83xd1x88xd0xbaxd1x83. 
"""
class gun():
 def __init__(self, owner=0):
  self.owner=owner
  self.f2_power=10
  self.f2_on=0
  self.an=1
  if owner==0:
      self.id=canv.create_line(20,450,50,420,width=7)
  else:
      self.id=canv.create_line(owner.x,owner.y,owner.x+30,owner.y-30,width=7)
 def fire2_start(self,event):
  self.f2_on=1
 def fire2_end(self,event):
  global balls,bullet,counter
  bullet+=1
  new_ball=ball(owner=self)
  new_ball.r+=5
  if self.owner==0:
   if event.x-20<0:
       self.an=math.atan((event.y-450)/(event.x-20))+math.pi
   else:
       self.an=math.atan((event.y-450)/(event.x-20))
  else:
   if event.x-self.owner.x<0:
       self.an=math.atan((event.y-self.owner.y)/(event.x-self.owner.x))+math.pi
   else:
       self.an=math.atan((event.y-self.owner.y)/(event.x-self.owner.x))
  new_ball.vx=self.f2_power*math.cos(self.an)
  new_ball.vy=-self.f2_power*math.sin(self.an)
  if self.owner!=0:
      new_ball.vx+=self.owner.vx
      new_ball.vy-=self.owner.vy
  balls+=[new_ball]
  self.f2_on=0
  self.f2_power=10
  counter+=1
 def targetting(self,event=0):
  if event:
   if self.owner==0:
       if event.x-20<0:
           self.an=math.atan((event.y-450)/(event.x-20))+math.pi
       else:
           self.an=math.atan((event.y-450)/(event.x-20))
   else:
       if event.x-self.owner.x<0:
           self.an=math.atan((event.y-self.owner.y)/(event.x-self.owner.x))+math.pi
       else:
           self.an=math.atan((event.y-self.owner.y)/(event.x-self.owner.x))
  if self.f2_on:
   canv.itemconfig(self.id,fill='orange')
  else:
   canv.itemconfig(self.id,fill='black')
  if self.owner==0:
      canv.coords(self.id,20,450,20+max(self.f2_power,20)*math.cos(self.an),450+max(self.f2_power,20)*math.sin(self.an))
  else:
      canv.coords(self.id,self.owner.x,self.owner.y,self.owner.x+max(self.f2_power,20)*math.cos(self.an),self.owner.y+max(self.f2_power,20)*math.sin(self.an))
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
 def __init__(self, color='red'):
  global idCounter
  self.color=color
  self.idC=idCounter
  idCounter+=1
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
  if x<0+r:
   self.vx=abs(self.vx)
  if x>800-r:
   self.vx=-abs(self.vx)
  if y<0+r:
   self.vy=abs(self.vx)
  if y>550-r:
   self.vy=-abs(self.vx)
  canv.coords(self.id,x-r,y-r,x+r,y+r)
 def new_target(self):
  x=self.x=rnd(600,780)
  y=self.y=rnd(300,550)
  r=self.r=rnd(2,50)
  canv.coords(self.id,x-r,y-r,x+r,y+r)
  canv.itemconfig(self.id,fill=self.color)
  self.vx=rnd(-5,5)
  self.vy=rnd(-5,5)
 def hit(self,points=1):
  canv.coords(self.id,-10,-10,-10,-10)
  self.points+=points
  #canv.itemconfig(self.id_points,text=self.points)
t1=target(color='red')
t2=target(color='green')
t3=target(color='blue')
id_points1=canv.create_text(30,30,text='1 = '+str(t1.points),font='28')
id_points2=canv.create_text(30,60,text='2 = '+str(t2.points),font='28')
id_points3=canv.create_text(30,90,text='3 = '+str(t3.points),font='28')
screen1=canv.create_text(400,300,text='',font='Verdana 48')
g1=gun()
bullet=0
balls=[]
counter=0
def new_game(event=''):
 global g1,t1,t2,t3,id_points,screen1,balls,bullet,counter
 canv.itemconfig(screen1,text='')
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
 g1.owner=t1
 live=1
 while live:
  for b in balls:
   b.move()
   if b.hittest(t1)and t1.live:
    t1.live=0
    for i in [t1, t2, t3]:
        if i.live:
            i.points+=1
    canv.coords(t1.id,-10,-10,-10,-10)
    #txt = 't'+str(b.idC+1)+'.points+=1'
    #exec(txt)
   if b.hittest(t2)and t2.live:
    t2.live=0
    for i in [t1, t2, t3]:
        if i.live:
            i.points+=1
    canv.coords(t2.id,-10,-10,-10,-10)
    #txt = 't'+str(b.idC+1)+'.points+=1'
    #exec(txt)
   if b.hittest(t3)and t3.live:
    t3.live=0
    for i in [t1, t2, t3]:
        if i.live:
            i.points+=1
    canv.coords(t3.id,-10,-10,-10,-10)
    #txt = 't'+str(b.idC+1)+'.points+=1'
    #exec(txt)
   canv.itemconfig(id_points1,text='1 = '+str(t1.points))
   canv.itemconfig(id_points2,text='2 = '+str(t2.points))
   canv.itemconfig(id_points3,text='3 = '+str(t3.points))
  if t1.live==1:
   t1.move()
  if t2.live==1:
   t2.move()
  if t3.live==1:
   t3.move()
  canv.update()
  time.sleep(z)
  g1.power_up()
  g1.targetting()
  live=t1.live+t2.live+t3.live
  live=(live>1 or len(balls)>0)
  if counter==3:
      counter=0
  if counter==0:
      if t1.live:
          g1.owner=t1
      else:
          counter+=1
  if counter==1:
      if t2.live:
          g1.owner=t2
      else:
          counter+=1
  if counter==2:
      if t3.live:
          g1.owner=t3
      else:
          counter+=1
 canv.bind('<Button-1>','')
 canv.bind('<ButtonRelease-1>','')
 if not live:
  if t1.live:
   canv.itemconfig(screen1,text='Победил 1 игрок')
  if t2.live:
   canv.itemconfig(screen1,text='Победил 2 игрок')
  if t3.live:
   canv.itemconfig(screen1,text='Победил 3 игрок')
 counter+=1
 root.after(2500,new_game)
new_game() 
mainloop()
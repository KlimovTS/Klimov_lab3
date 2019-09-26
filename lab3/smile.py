from graph import *

k=2.5

penColor("yellow")
brushColor("yellow")
circle(100*k, 100*k, 75*k)

penColor("red")
brushColor("red")
circle(70*k, 70*k, 10*k)
circle(130*k, 70*k, 15*k)
penColor("black")
brushColor("black")
circle(70*k, 70*k, 5*k)
circle(130*k, 70*k, 5*k)

polygon([(70*k, 130*k), (70*k,120*k), (130*k,120*k), (130*k,130*k)])
polygon([(90*k, 70*k), (95*k,65*k), (55*k,45*k), (60*k,50*k)])
polygon([((200-90)*k, 70*k), ((200-95)*k,65*k), ((200-55)*k,45*k), ((200-60)*k,50*k)])

run()

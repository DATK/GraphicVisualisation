from src.Engine import GrpahicEngine
from src.Graphic import Grpahic
from src.Interactive.Button import Button
from src.Interactive.Lable import Label

import sys
import math as m


def gen_array(a,b):
    array=[]
    for i in range(a,b):
        for j in range(10):
           #for iji in range(10):
                array.append(i+j/10)#+iji/100)
    return array
            
def sinX(x):
    return m.sin(x)

def CosX(x):
    return m.cos(x)

def Linefunc(x):
    return x


def parab(x):
    return x**2

def tg(x):
    return m.tan(x)


eng=GrpahicEngine(1)
eng.SCALE=100
eng.STEP=50
eng.change_Font_Size(22)


XLIST=gen_array(-1000,1000)

CustomGraphic=Grpahic("My graphic")


SinXGraphic=Grpahic("Sin(x)")
SinXGraphic.set_func(sinX)
SinXGraphic.set_graphic_parms((255,0,0),3,3,2)
SinXGraphic.set_limits((-2000,2000),(-1000,1000))
SinXGraphic.get_x(XLIST)
SinXGraphic.lines=True

CosXGraphic=Grpahic("Cos(x)")
CosXGraphic.set_func(CosX)
CosXGraphic.set_graphic_parms((0,255,0),3,3,2)
CosXGraphic.set_limits((-2000,2000),(-1000,1000))
CosXGraphic.get_x(XLIST)
CosXGraphic.lines=True


TanXGraphic=Grpahic("Tan(x)")
TanXGraphic.set_func(tg)
TanXGraphic.set_graphic_parms((0,0,255),3,3,2)
TanXGraphic.set_limits((-2000,2000),(-1000,1000))
TanXGraphic.get_x(XLIST)
TanXGraphic.lines=True


ParabGraphic=Grpahic("Parabola")
ParabGraphic.set_func(parab)
ParabGraphic.set_graphic_parms((255,80,80),3,3,2)
ParabGraphic.set_limits((-2000,2000),(-1000,1000))
ParabGraphic.get_x(XLIST)
ParabGraphic.lines=True

def stop():
    eng.runing=False

exitButton=Button(eng.RESOLUTION[0]*0.8,0,200,60,(),"Exit",stop)
exitButton.set_parms(30,aligin=(25,5),color_backgroud=((180,180,180),(100,100,100)))
drwButton=Button(eng.RESOLUTION[0]*0.6,0,200,60,(),"Drawing",CustomGraphic.drawmode)
drwButton.set_parms(30,aligin=(25,5),color_backgroud=((180,180,180),(100,100,100)))
clear=Button(eng.RESOLUTION[0]*0.4,0,200,60,(),"Clear",CustomGraphic.clear)
clear.set_parms(30,aligin=(25,5),color_backgroud=((180,180,180),(100,100,100)))


eng.load_graphic(SinXGraphic)
eng.load_graphic(CustomGraphic)
eng.load_graphic(CosXGraphic)
# eng.load_graphic(ParabGraphic)
eng.load_graphic(TanXGraphic)
eng.addButton(exitButton)
eng.addButton(drwButton)   
eng.addButton(clear)

eng.optimisation=1

eng.run(1)
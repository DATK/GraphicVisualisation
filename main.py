import pygame as pg
import sys
import math

from src.Interactive.Lable import Label
from src.Interactive.Button import Button
pg.init()

FULLSCREEN=1
RESOLUTION=(800,800)
FRAMERATE=144
SCALE=100
PAUSE=50
FONT_SIZE=22
START_FROM=(-700,-400)
POINT_RADIUS=4
LINE_WIDTH=4
GRAPHICS={}
NAME_GRAPHICS_CORD=[(0,100)]
DRAWING_REALTIME=True
GRAPH_WINDOW_KOEFS=(0.15,0.15,0.85,0.85)

Window=pg.display.set_mode((0,0),pg.FULLSCREEN) if FULLSCREEN else pg.display.set_mode(RESOLUTION)
pg.display.set_caption("Визуализация Графика по функции f(x)")

RESOLUTION=Window.get_size()

Clock=pg.time.Clock()
Graph_Widnow=pg.Surface((RESOLUTION[0]*GRAPH_WINDOW_KOEFS[2],RESOLUTION[1]*GRAPH_WINDOW_KOEFS[3]))
rc=pg.Rect(RESOLUTION[0]*GRAPH_WINDOW_KOEFS[0],RESOLUTION[1]*GRAPH_WINDOW_KOEFS[1],RESOLUTION[0]*GRAPH_WINDOW_KOEFS[2],RESOLUTION[1]*GRAPH_WINDOW_KOEFS[3])

Font = pg.font.SysFont('Comic Sans MS', FONT_SIZE)

def to_pygame(x,y,resy=RESOLUTION[1]):
    return (x-START_FROM[0],resy-y+START_FROM[1])

def to_graph_winodw(pos):
    res=Window.get_size()
    a=res[0]*GRAPH_WINDOW_KOEFS[0]
    b=res[1]*GRAPH_WINDOW_KOEFS[1]
    #c2=a**2+b**2
    #c=math.sqrt(c2)
    return (pos[0]-a,pos[1]-b)

def numbers_gen(start_x=START_FROM[0],start_y=START_FROM[1],width=Graph_Widnow.get_width(),height=Graph_Widnow.get_height(),pause=5):
    points_x=[]
    points_y=[]
    for i in range(start_x,width+abs(start_x)):
        if i % pause==0:
            points_x.append(i)
    for j in range(start_y,height+abs(start_y)):
        if j % pause==0:
            points_y.append(j)
            
    return (points_x,points_y)

def get_graphic_points(func,x=[],x_limits=[0,500],lines=True,name="Graphic1",settings=((0,0,0),POINT_RADIUS,LINE_WIDTH)):
    cords=[]
    if x==[]:
        for i in range(x_limits[0],x_limits[1]+1):
            cords.append(to_pygame(i*SCALE,func(i)*SCALE,Graph_Widnow.get_height()))
    else:
        for i in x:
            if x_limits[0]<i<x_limits[1]:
                cords.append(to_pygame(i*SCALE,func(i)*SCALE,Graph_Widnow.get_height()))
            else:
                continue
    return (cords,lines,settings,name)

def mouseFuncDrawing(graphic,event):
    pos=pg.mouse.get_pos()
    if event.type==pg.MOUSEBUTTONUP:
        if rc.collidepoint(pos):
            graphic[0].append(to_graph_winodw(pos))
    return graphic
       
        
def custom_func_points(lines=True,name="Graphic1",settings=((0,0,0),POINT_RADIUS,LINE_WIDTH)):
    cords=[]
    return (cords,lines,settings,name)
    

def draw_graphic(scr,graphic_cords,lines=True,settings=((0,0,0),POINT_RADIUS,LINE_WIDTH)):
    for cord in graphic_cords:
        pg.draw.circle(scr,settings[0],cord,settings[1],settings[1])
    if lines:
        for cord in range(len(graphic_cords)-1):
            pg.draw.line(scr,settings[0],graphic_cords[cord],graphic_cords[cord+1],settings[2])

def onoffdrw():
    global DRAWING_REALTIME
    DRAWING_REALTIME = False if DRAWING_REALTIME else True

def clear():
    global GRAPHICS
    graphicCustom=custom_func_points(lines=True,settings=((0,200,0),7,6),name="Custom")
    GRAPHICS["CUSTOM"]=graphicCustom
    
def test(x):
    return math.sin(x)

def test2(x):
    return math.cos(x)

xs=[]

for i in range(-7,11):
    for j in range(10):
        for ij in range(10):
                xs.append(float(i+j/10+ij/100))

graphic1=get_graphic_points(test,x=xs,x_limits=[START_FROM[0],RESOLUTION[0]],name="Sin(x)")
graphic2=get_graphic_points(test2,x=xs,x_limits=[START_FROM[0],RESOLUTION[0]],lines=True,settings=((200,0,0),POINT_RADIUS,LINE_WIDTH),name="Cos(x)")
graphicCustom=custom_func_points(lines=True,settings=((0,200,0),7,6),name="Custom")
#graphic=get_graphic_points(test,x=[],x_limits=[0,RESOLUTION[0]])
points_x,points_y=numbers_gen(pause=PAUSE)
GRAPHICS["SinX"]=graphic1
GRAPHICS["CosX"]=graphic2
GRAPHICS["CUSTOM"]=graphicCustom
#print(graphic)
total_points=0



points_label=Label(0,0,360,60,)
fps=Label(361,0,200,60)
exitButton=Button(RESOLUTION[0]*0.95,0,100,60,(),"Выход",sys.exit)
exitButton.set_parms(25,aligin=(25,25),color=(0,0,0),color_backgroud=((255,255,255),(220,220,220)))

OnOffdrawing=Button(RESOLUTION[0]*0.85,0,200,60,(),"Вкл\Выкл рисование",onoffdrw)
OnOffdrawing.set_parms(25,aligin=(25,25),color=(0,0,0),color_backgroud=((255,255,255),(220,220,220)))

DrawingClear=Button(RESOLUTION[0]*0.7,0,250,60,(),"Удалить рис. точки",clear)
DrawingClear.set_parms(25,aligin=(25,25),color=(0,0,0),color_backgroud=((255,255,255),(220,220,220)))

while True:
    Window.fill((200,200,200))
    Window.blit(Graph_Widnow,(RESOLUTION[0]*GRAPH_WINDOW_KOEFS[0],RESOLUTION[1]*GRAPH_WINDOW_KOEFS[1]))
    Graph_Widnow.fill((255,255,255))
    
    for graphic in GRAPHICS:
       # try:
        draw_graphic(Graph_Widnow,GRAPHICS[graphic][0],lines=GRAPHICS[graphic][1],settings=GRAPHICS[graphic][2])
        text=Font.render(GRAPHICS[graphic][3],True,GRAPHICS[graphic][2][0])
        Window.blit(text,NAME_GRAPHICS_CORD[-1])
        NAME_GRAPHICS_CORD.append((NAME_GRAPHICS_CORD[-1][0],NAME_GRAPHICS_CORD[-1][1]+40))
        #except:
          #  continue
    NAME_GRAPHICS_CORD=[(0,100)]
        
    for point in points_x:
        text=Font.render(str(point/SCALE),True,(0,0,0))
        Graph_Widnow.blit(text,to_pygame(point,text.get_height()+1,Graph_Widnow.get_height()))
        pg.draw.line(Graph_Widnow,(0,0,0),to_pygame(point,START_FROM[1],Graph_Widnow.get_height()),to_pygame(point,Graph_Widnow.get_height(),Graph_Widnow.get_height()))
        
    for point in points_y:
        text=Font.render(str(point/SCALE),True,(0,0,0))
        Graph_Widnow.blit(text,to_pygame(0,point,Graph_Widnow.get_height()))
        pg.draw.line(Graph_Widnow,(0,0,0),to_pygame(START_FROM[0],point+1,Graph_Widnow.get_height()),to_pygame(Graph_Widnow.get_width(),point+1,Graph_Widnow.get_height()))
    
    for pnt in GRAPHICS:
        total_points+=len(GRAPHICS[pnt][0])   
    points_label.show(Window,f"Total point: {total_points}",isbackground=False,size=40,aligin=(25,25),color=(10,10,10))
    fps.show(Window,f"FPS: {int(Clock.get_fps())}",isbackground=False,size=40,aligin=(25,25),color=(10,10,10))
    total_points=0
    
    exitButton.show(Window)
    OnOffdrawing.show(Window)
    DrawingClear.show(Window)
    for event in pg.event.get():
        if event.type==pg.QUIT:
            sys.exit()
        if DRAWING_REALTIME: GRAPHICS["CUSTOM"]=mouseFuncDrawing(GRAPHICS["CUSTOM"],event)
        exitButton.do_func(event)
        OnOffdrawing.do_func(event)
        DrawingClear.do_func(event)
    pg.display.flip()
    Clock.tick(FRAMERATE)
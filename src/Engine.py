import pygame as pg
import sys


class GrpahicEngine:
    
    def __init__(self,fullscreen=False):
        pg.init()
        self.FULLSCREEN=fullscreen
        self.FRAMERATE=144
        self.SCALE=100
        self.fpsnow=self.FRAMERATE
        self.STEP=50
        self.FONT_SIZE=22
        self.START_FROM=(-700,-300)
        self.POINT_RADIUS=4
        self.CUSTOMFUNC={}
        self.BUTTONS=[]
        self.LABLES=[]
        self.LINE_WIDTH=4
        self.GRAPHICS=[]
        self.NAME_GRAPHICS_CORD=[(0,100)]
        self.GRAPH_WINDOW_KOEFS=(0.15,0.15,0.85,0.7)
        self.RESOLUTION=(640,480)
        self.total_points=0
        self.showTotalPoints=True
        self.showFps=True
        self.showGraphicNames=True
        self.optimisation=False
        self.display=pg.display.set_mode((0,0),pg.FULLSCREEN) if self.FULLSCREEN else pg.display.set_mode(self.RESOLUTION)
        pg.display.set_caption("Визуализация Графика по функции f(x)")
        self.RESOLUTION=self.display.get_size()
        self.Clock=pg.time.Clock()
        self.Graph_Widnow=pg.Surface((self.RESOLUTION[0]*self.GRAPH_WINDOW_KOEFS[2],self.RESOLUTION[1]*self.GRAPH_WINDOW_KOEFS[3]))
        self.rc=pg.Rect(self.RESOLUTION[0]*self.GRAPH_WINDOW_KOEFS[0],self.RESOLUTION[1]*self.GRAPH_WINDOW_KOEFS[1],self.RESOLUTION[0]*self.GRAPH_WINDOW_KOEFS[2],self.RESOLUTION[1]*self.GRAPH_WINDOW_KOEFS[3])
        self.Font = pg.font.SysFont('Comic Sans MS', self.FONT_SIZE)
        self.Font_gr_name = pg.font.SysFont('Comic Sans MS', 30)
        
    def normalize_cords(self,x,y):
        return (x-self.START_FROM[0],self.Graph_Widnow.get_height()-y+self.START_FROM[1])

    
    def change_Font_Size(self,size):
        self.FONT_SIZE=size
        self.Font = pg.font.SysFont('Comic Sans MS', self.FONT_SIZE)
    
    def normalise_mousepos(self,pos):
        res=self.display.get_size()
        a=res[0]*self.GRAPH_WINDOW_KOEFS[0]
        b=res[1]*self.GRAPH_WINDOW_KOEFS[1]
        return (pos[0]-a,pos[1]-b)
    
    def customFunctions(self):
        for funcs in self.CUSTOMFUNC:
            if self.CUSTOMFUNC[funcs]["work"]:
                    self.CUSTOMFUNC[funcs]["function"]()

    def addCustomFunc(self,name_func,func,work=False):
        self.CUSTOMFUNC[name_func]={"function":func,"work":work}
        
    def set_work_func(self,name_func,work):
        self.CUSTOMFUNC[name_func]["work"]=work
        
    def change_work_func(self,name_func):
        self.CUSTOMFUNC[name_func]["work"]=False if self.CUSTOMFUNC[name_func]["work"] else True
    
    def numbers_gen(self,width,height):
        points_x=[]
        points_y=[]
        for i in range(self.START_FROM[0],width+abs(self.START_FROM[0])):
            if i % self.STEP==0:
                points_x.append(i)
        for j in range(self.START_FROM[1],height+abs(self.START_FROM[1])):
            if j % self.STEP==0:
                points_y.append(j)         
        return (points_x,points_y)
    
    def load_graphic(self,graphic):
        self.GRAPHICS.append(graphic)

    def draw_graphic(self,graphic,res :tuple):
        graphic.generate_cords()
        if not graphic.mouse_drawing:
            normalcords=[]

            if self.optimisation:
                for cord in graphic.cords:
                    tmp=self.normalize_cords(cord[0]*self.SCALE,cord[1]*self.SCALE) 
                    if 0<=tmp[0]<=res[0] and 0<=tmp[1]<=res[1]:
                        normalcords.append(tmp)
            else:
                normalcords=[self.normalize_cords(cord[0]*self.SCALE,cord[1]*self.SCALE) for cord in graphic.cords]
        else:
            normalcords=graphic.cords

        for cord in normalcords:
            pg.draw.circle(self.Graph_Widnow,graphic.color,cord,graphic.PointRadius,graphic.PointWidth)
        if graphic.lines:
            for cord in range(len(normalcords)-1):
                pg.draw.line(self.Graph_Widnow,graphic.color,normalcords[cord],normalcords[cord+1],graphic.LineWIdth)
    
    def addButton(self,button):
        self.BUTTONS.append(button)
             
    def run(self):
        while True:
            self.display.fill((200,200,200))
            self.display.blit(self.Graph_Widnow,(self.RESOLUTION[0]*self.GRAPH_WINDOW_KOEFS[0],self.RESOLUTION[1]*self.GRAPH_WINDOW_KOEFS[1]))
            self.Graph_Widnow.fill((255,255,255))

            WindowSizeX,WindowSizeY=self.Graph_Widnow.get_size()
            
            for graphic in self.GRAPHICS:
                self.draw_graphic(graphic,(WindowSizeX,WindowSizeY))
                if self.showGraphicNames:
                    text=self.Font_gr_name.render(graphic.name,True,graphic.color)
                    self.display.blit(text,self.NAME_GRAPHICS_CORD[-1])
                    self.NAME_GRAPHICS_CORD.append((self.NAME_GRAPHICS_CORD[-1][0],self.NAME_GRAPHICS_CORD[-1][1]+40))
                self.total_points+=len(graphic.cords)   
                
            if self.showTotalPoints:    
                text=self.Font_gr_name.render(str(self.total_points),True,(0,0,0))
                self.display.blit(text,(5,5))  
            
            self.NAME_GRAPHICS_CORD=[(0,100)]
            self.total_points=0 
            
            points_x,points_y=self.numbers_gen(WindowSizeX,WindowSizeY)                
            for point in points_x:
                text=self.Font.render(str(point/self.SCALE),True,(0,0,0))
                self.Graph_Widnow.blit(text,self.normalize_cords(point,text.get_height()+1))
                pg.draw.line(self.Graph_Widnow,(0,0,0),self.normalize_cords(point,self.START_FROM[1]),self.normalize_cords(point,WindowSizeY))
                
            for point in points_y:
                text=self.Font.render(str(point/self.SCALE),True,(0,0,0))
                self.Graph_Widnow.blit(text,self.normalize_cords(0,point))
                pg.draw.line(self.Graph_Widnow,(0,0,0),self.normalize_cords(self.START_FROM[0],point+1),self.normalize_cords(WindowSizeX,point+1))
            
            if self.showFps:    
                text=self.Font_gr_name.render(str(int(self.fpsnow)),True,(0,0,0))
                self.display.blit(text,(100,5))
            
            for button in self.BUTTONS:
                button.show(self.display)
            
            self.customFunctions()
            
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    sys.exit()
                for graphic in self.GRAPHICS:
                    if graphic.mouse_drawing:
                        graphic.mouseFuncDrawing(event,self.rc,self.normalise_mousepos(pg.mouse.get_pos()))
                for button in self.BUTTONS:
                    button.do_func(event)
            self.fpsnow=self.Clock.get_fps()
            self.rc=pg.Rect(self.RESOLUTION[0]*self.GRAPH_WINDOW_KOEFS[0],self.RESOLUTION[1]*self.GRAPH_WINDOW_KOEFS[1],self.RESOLUTION[0]*self.GRAPH_WINDOW_KOEFS[2],self.RESOLUTION[1]*self.GRAPH_WINDOW_KOEFS[3])
            pg.display.flip()
            self.Clock.tick(self.FRAMERATE)
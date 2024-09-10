import pygame as pg

class Grpahic:
    
    def __init__(self,name):
        self.name=name
        self.func=self.defaultFunc
        self.listX=[]
        self.cords=[]
        self.lines=True
        self.color=(0,0,0)
        self.limitsX=(-100,1000)
        self.limitsY=(-100,1000)
        self.mouse_drawing=False
        self.PointRadius=5
        self.PointWidth=5
        self.LineWIdth=4
        self.drawme=True

    def clear(self):
        self.cords=[]
        
    def defaultFunc(self,x):
        return x   
    
    def drawme_change(self):
        self.drawme=False if self.drawme else True
    
    def drawmode(self):
        self.mouse_drawing=False if self.mouse_drawing else True
    
    def mouseFuncDrawing(self,event,rc,pos):
        if self.mouse_drawing and self.drawme:
            if event.type==pg.MOUSEBUTTONUP:
                if rc.collidepoint(pg.mouse.get_pos()):
                    self.cords.append((pos))
            if pg.key.get_pressed()[pg.K_z] and event.type==pg.KEYDOWN and self.cords!=[]:
                del self.cords[-1]
                
    def set_func(self,func):
        self.func=func
    
    def set_graphic_parms(self,color,pointradius,pointwidth,linewidth):
        self.PointRadius=pointradius
        self.PointWidth=pointwidth
        self.LineWIdth=linewidth
        self.color=color
        
    def get_x(self,x: list):
        self.listX=x
    
    def set_limits(self,lmX,lmY):
        self.limitsX=lmX
        self.limitsY=lmY
    
    def generate_cords(self):
        if not self.mouse_drawing and self.drawme:
            self.cords=[]
            for x in self.listX:
                y=self.func(x)
                if self.limitsX[0]<x<self.limitsX[1] and self.limitsY[0]<y<self.limitsY[1]:
                    self.cords.append((x,y))


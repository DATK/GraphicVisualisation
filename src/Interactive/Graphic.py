import pygame as pg

class Graphic:
    
    def __init__(self,name="Graphic",drawingMouse=False,converter=None):
        self.name=name
        self.cords=[(0,0)]
        self.point_radius=4
        self.color=(0,0,0)
        self.lineWidth=4
        self.line=True
        self.to_pygame=converter
        
    def set_func(self,func):
        self.func=func
    
    def load_x(self,x=[0]):
        for i in x:
            self.cords.append(self.to_pygame(i*SCALE,func(i)*SCALE,Graph_Widnow.get_height()))
    
    def add_x(self,x):
         self.cords.append((x,self.func(x)))
    
    
    def return_grapic(self):
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
    
import pygame as pg


class Button:

    def __init__(self, x: int, y: int, width: int, height: int, textures=(), text=None, function=None, isPressed=False,formenu=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.function = function
        self.isPressed = isPressed
        self.isdraw=True
        self.forMenu=formenu
        if textures!=():
            self.img1=textures[0]
            self.img1 = pg.transform.scale(
                self.img1, (self.width, self.height))
            self.img2=textures[1]
            self.img2 = pg.transform.scale(
                self.img2, (self.width, self.height))
            self.withtexture=True
        else:
            self.img1=pg.Surface((width,height))
            self.img1 = pg.transform.scale(self.img1, (self.width, self.height))
            self.img2=pg.Surface((width,height))
            self.img2 = pg.transform.scale(self.img2, (self.width, self.height))
            self.withtexture=False
        self.set_parms()

    def show(self, scr):
        if self.isdraw:
            if self.withtexture:
                if self.isPressed:self.curret_img = self.img2
                else: self.curret_img = self.img1
            else:
                if self.isPressed:self.curret_img = self.img2
                else: self.curret_img = self.img1
                self.curret_img.blit(self.text_rnd, self.curret_img.get_rect(topleft=self.aligin))
            scr.blit(self.curret_img,(self.x,self.y))
        self.changing()
            
            
    def set_parms(self,size=15, font="Comic Sans MS", aligin=(0, 0), color=(0, 0, 0), color_backgroud=((255, 255, 255),(0,0,0))):
        self.size=size
        self.font=font
        self.aligin=aligin
        self.color=color
        self.color_backgroud=color_backgroud
        my_font = pg.font.SysFont(self.font, self.size)
        self.text_rnd = my_font.render(self.text, False, self.color)
        self.img1.fill(self.color_backgroud[0])
        self.img2.fill(self.color_backgroud[1])

    def changing(self):
        if self.isdraw:
            self.isPressed = pg.rect.Rect(self.x,self.y,self.width,self.height).collidepoint(pg.mouse.get_pos())

    def do_func(self, event):
        if self.function != None and self.isPressed and event.type == pg.MOUSEBUTTONUP and self.isdraw:
            self.function()
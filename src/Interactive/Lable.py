
import pygame as pg

class Label:

    def __init__(self, x, y, weight, height, text="Label1",formenu=False, img_path=None):
        self.x = x
        self.y = y
        self.weight = weight
        self.height = height
        self.text = text
        self.img_path = img_path
        self.forMenu=formenu
        if img_path != None:
            self.zone = pg.image.load(self.img_path)
            self.zone = pg.transform.scale(
                self.zone, (self.weight, self.height))
            self.zone_rect = self.zone.get_rect()
        else:
            self.zone = pg.Surface((self.x, self.y))
            self.zone = pg.transform.scale(
                self.zone, (self.weight, self.height))
            self.zone_rect = self.zone.get_rect(topleft=(self.x, self.y))

    def show(self, scr, text=None, color_background=(0, 0, 0), isbackground=True, font="Comic Sans MS", size=25, aligin=(0, 0), color=(255, 255, 255)):
        if text != None:
            self.text = text
        my_font = pg.font.SysFont(font, size)
        if not isbackground:
            self.zone.fill((0, 0, 0))
            self.zone.set_colorkey((0, 0, 0))
        else:
            self.zone.fill(color_background)
        text_rnd = my_font.render(self.text, False, color)

        self.zone.blit(text_rnd, self.zone.get_rect(topleft=aligin))
        scr.blit(self.zone, self.zone_rect)
        #scr.blit(text_rnd, self.zone.get_rect())
        #scr.blit(self.zone, self.zone_rect.topleft)
        

import pygame
from constants import *
from .game_object import GameObject


class ObjectArea:
    def __init__(self, posX, posY, width, height):
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
    
    def get_coordinates(self):
        return (self.posX, self.posY, self.width, self.height)

    def is_point_inside(self, point):
        return self.posX+self.width > point[0] > self.posX and self.posY+self.height > point[1] > self.posY

class TextObject(GameObject):
    def __init__(self, text, font, posX, posY, color=black):
        self.text = text
        self.font = font
        self.color = color
        self.posX = posX
        self.posY = posY

    def draw(self, game_display):
        textSurface = self.font.render(self.text, True, self.color)

        rect = textSurface.get_rect()
        rect.center = (self.posX, self.posY)
        game_display.blit(textSurface, rect) 
    
class ButtonObject(GameObject):
    def __init__(self, msg, object_area, inactive_color, active_color, action=None):
        self.object_area = object_area
        self.inactive_color =inactive_color
        self.active_color = active_color
        self.action = action
        self.rect_coordenates = object_area.get_coordinates()
        smallText = pygame.font.SysFont("comicsansms",20)
        pos_text_x = object_area.posX + (object_area.width / 2)
        pos_text_y = object_area.posY + (object_area.height / 2)
        self.text_object = TextObject(msg, smallText, pos_text_x, pos_text_y)
        

    def draw(self, game_display):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if self.object_area.is_point_inside(mouse):
            pygame.draw.rect(game_display, self.active_color,self.object_area.get_coordinates())
            if click[0] == 1 and self.action != None:
                self.action()         
        else:
            pygame.draw.rect(game_display, self.inactive_color,self.object_area.get_coordinates())

        self.text_object.draw(game_display)

 
    
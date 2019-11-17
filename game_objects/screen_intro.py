from constants import *
import pygame
from .game_object import GameObject
from .generic_game_objects import TextObject, ButtonObject, ObjectArea
from .screen_filler import Filler


class IntroScreen(GameObject):
    def __init__(self, game_display, message, change_state_func):
        largeText = pygame.font.SysFont("comicsansms",115)
        pos_text_x = display_width / 2
        pos_text_y = display_height / 2
        main_text = TextObject(message, largeText, pos_text_x, pos_text_y)
        button_OK_pos = ObjectArea(150,450,100,50)
        button_quit_pos = ObjectArea(550,450,100,50)
        buttonOK = ButtonObject("GO",button_OK_pos,green,bright_green, change_state_func("GAME"))
        buttonQuit = ButtonObject("Quit",button_quit_pos,red,bright_red, change_state_func("QUIT"))
        filler = Filler(white)
        self.game_objects = [filler, main_text, buttonOK, buttonQuit]
            
    
    
import pygame
from constants import *
from .game_object import GameObject
from .screen_filler import Filler
from .tilemap_object import TilemapObject
from .player_object import PlayerObject
from .generic_game_objects import ObjectArea, ButtonObject, TextObject

class GameScreen(GameObject):
    def __init__(self, game_display, tilemap, change_state_func):
        

        self.game_display = game_display        
        
        button_endturon_pos = ObjectArea(650,150,100,50)
        button_endturn = ButtonObject("End Turn",button_endturon_pos,green,bright_green, change_state_func("GAME_ENDTURN"))
        
        button_quit_pos = ObjectArea(650,250,100,50)
        button_quit = ButtonObject("Quit",button_quit_pos,red,bright_green, change_state_func("QUIT"))

        filler = Filler(white)
        self.tilemap = tilemap
        self.game_objects = [filler, tilemap, button_quit, button_endturn]        

    def draw(self, game_display):
        mouse_x, mouse_y = pygame.mouse.get_pos()        
        tile = self.tilemap.get_tile_from_pos(mouse_x, mouse_y)
        info = f"({mouse_x},{mouse_y}) - Tile: {tile}"
        smallText = pygame.font.SysFont("comicsansms",15)

        screen_info = [TextObject(info, smallText, 670, 30)]
        
        for obj in self.game_objects + screen_info:
            obj.draw(game_display)

from constants import *
import pygame
from .game_object import GameObject
import random


class TileObject(GameObject):
    def __init__(self, tile_type, x, y):
        
        self.textures = {
            GRASS : green,#pg.image.load("assets/grass.png"),
            WATER : bright_blue, #pg.image.load("assets/water.png")
            MOUNTAIN: light_gray

        }     
        self.tile_type = tile_type
        self.tilesize = 40
        self.coord_x = x
        self.coord_y = y

        self.is_visible = False
    
    def draw(self, game_display):

                        
        coordinates = (
            self.coord_x*self.tilesize, 
            self.coord_y*self.tilesize, 
            self.tilesize -1, 
            self.tilesize-1)

        
        pygame.draw.rect(
            game_display, 
            self.textures[self.tile_type],
            coordinates)

        # for player in self.players:
            # player.draw(game_display)
    
   
    def __repr__(self):
        return f"({self.coord_x,self.coord_y}: {self.tile_type})"

        

                
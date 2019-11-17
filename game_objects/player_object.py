from constants import *
import pygame
from .game_object import GameObject

class PlayerObject(GameObject):
    def __init__(self, color, initial_position, name, is_human_controlled=False):
        self.color = color
        self.position = initial_position
        self.name = name
        self.is_human_controlled = is_human_controlled
        self.is_dead = False

    def die(self):
        self.is_dead = True       
    
    def draw(self, game_display):                
        position_2d = (20 + 40*self.position[0], 20 + 40*self.position[1])
        pygame.draw.circle(game_display, self.color, position_2d, 10)
    
    def __repr__(self):
        return f"{self.name}: {self.position}"
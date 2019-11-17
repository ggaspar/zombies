import pygame
from constants import *
from game_engine import GameEngine, GameState

def game_loop():
    phase = "INTRO"
    
    pygame.init()
    game_state = GameState()
    game_engine = GameEngine(game_state)
    pygame.display.set_caption('A bit Racey')

    print("in game loop")
    clock = pygame.time.Clock()
    close = False
    while not close:   
        game_engine.execute_action()
        print(game_state)
        pygame.display.update()
        clock.tick(15)

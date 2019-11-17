import pygame
from constants import *
from game_objects import IntroScreen, GameScreen,PlayerObject, TilemapObject
from actions import QuitGame, DrawScreen, LostGame, EndTurn
import utils
from ai_controller import StupidAI
from exceptions import IllegalMoveException

class GameState:
    def __init__(self, initial_phase="INTRO"):
        self.phase = initial_phase
        self.game_display = pygame.display.set_mode((display_width,display_height))

        self.players_computer = [
            PlayerObject(black, (13,12), "Rui"),
            PlayerObject(black, (12,12), "Jorge"),
        ]

        self.players_human = [PlayerObject(white, (0,0), "Guilherme", True)]
        
        self.players = self.players_computer + self.players_human 
        self.tilemap = TilemapObject(self.game_display, self.players)
        self.intro_screen = IntroScreen(self.game_display, "United", self.change_state_func)
        self.game_screen = GameScreen(self.game_display, self.tilemap, self.change_state_func)
        
        self.selected_player = self.players_human[0]
        self.players_ai = list()
        for player in self.players_computer:
            self.players_ai.append(StupidAI(player, self.tilemap))

        self.actions ={
            "INTRO" : DrawScreen(self.game_display, self.intro_screen),
            "GAME" : DrawScreen(self.game_display, self.game_screen),
            # "GAME_PLAYER_MOVES": PlayerMoves(self.game_display, game_state=self.game_state, change_state_func=self.change_state_func)
            "GAME_ENDTURN" : EndTurn(self.game_display, self.game_screen, change_state_func=self.change_state_func, players_ai=self.players_ai),
            "LOST" : LostGame(self.game_display, self.intro_screen, self),
            "QUIT" : QuitGame()
        } 


        
    def change_state_func(self, phase):
        def func():
            print("chaging to ",phase)
            self.phase = phase
        return func

    def execute(self):
        self.actions[self.phase].execute()

    def reset(self):
        self.__init__()

    def __repr__(self):
        return self.phase

class GameEngine:

    def __init__(self, game_state):
        self.game_state = game_state
        self.game_display = pygame.display.set_mode((display_width,display_height))
        

    def execute_action(self):
        print(self.game_state.selected_player)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state.phase = "QUIT"


            if self.game_state.phase.startswith("GAME") and event.type == pygame.KEYDOWN:
                moviment_vector = (0,0)
                if event.key == pygame.K_LEFT:
                    moviment_vector = (-1,0)
                if event.key == pygame.K_RIGHT:
                    moviment_vector = (1,0)
                if event.key == pygame.K_DOWN:
                    moviment_vector = (0,1)
                if event.key == pygame.K_UP:
                    moviment_vector = (0,-1)
                new_pos = utils.sum_vectors(self.game_state.selected_player.position, moviment_vector)
                if self.game_state.selected_player.position != new_pos:
                    try:              
                        self.game_state.tilemap.move_player(self.game_state.selected_player, new_pos)
                        self.game_state.phase = "GAME_ENDTURN"
                    except IllegalMoveException:
                        continue
                

        
        for player_computer in self.game_state.players_computer:
            for player_human in self.game_state.players_human:
                if player_computer.position == player_human.position:
                    player_human.die()

        for player in self.game_state.players_human:
            if not player.is_dead:
                break
        else:
            pass
            # self.game_state.phase = "LOST"



            # p.possible_moves()
        self.game_state.execute()

    
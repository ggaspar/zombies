import pygame
import exceptions
class Action:
    def __init__(self, game_display=None, game_object=None, game_state=None, change_state_func=None, players_ai=None):
        self.game_display = game_display
        self.game_object = game_object
        self.game_state = game_state
        self.change_state_func = change_state_func
        self.players_ai = players_ai

class DrawScreen(Action):
    def execute(self):    
        self.game_object.draw(self.game_display)


class QuitGame(Action):
    def execute(self):
        print("executing QUIT")  
        pygame.quit()
        quit()

class PlayerMoves(Action):
    def execute(self):
        try:              
            self.game_state.tilemap.move_player(
                self.game_state.selected_player,
                new_pos)
            self.change_state_func("GAME_ENDTURN")()

                            

        except IllegalMoveException:
            return

class LostGame(Action):
    def execute(self):
        print("executing LOST")  
        self.game_state.reset()
        self.game_object.draw(self.game_display)

class EndTurn(Action):
    def execute(self):
        print("executing END OF TURN")  
        for p in self.players_ai:
            try:
                p.play()
            except exceptions.IllegalMoveException:
                continue

        self.game_object.draw(self.game_display)
        self.change_state_func("GAME")()

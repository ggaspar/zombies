import utils

class AIController:
    def __init__(self, player, tilemap):
        self.player = player
        self.tilemap = tilemap

class StupidAI(AIController):
    def play(self):
        position_enemy = [p.position for p in self.tilemap.players if p.is_human_controlled][0]
        possible_moves = self.tilemap.legal_moves(self.player)
        new_position = utils.get_closest(position_enemy, possible_moves)       
        self.tilemap.move_player(self.player, new_position)

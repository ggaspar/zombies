from .game_object import GameObject


class Filler(GameObject):
    def __init__(self, color):
        self.color = color

    def draw(self, game_display):
        game_display.fill(self.color)
        
            
class GameObject:
    def __init__(self):
        self.game_objects = list()

    def draw(self, game_display):
        # print("drawing objects")
        for obj in self.game_objects:
            obj.draw(game_display)
from constants import *
import pygame
from .game_object import GameObject
from .tile_object import TileObject
from exceptions import IllegalMoveException
import random


class TilemapObject(GameObject):
    def __init__(self, game_display, players):
        
        self.textures = {
            GRASS : green,#pg.image.load("assets/grass.png"),
            WATER : bright_blue, #pg.image.load("assets/water.png")
            MOUNTAIN: light_gray

            }        
        self.x_tiles = 15
        self.y_tiles = 15
        self.tilemap_matrix = list()
        
        for row in range(self.x_tiles):
            for column in range(self.y_tiles):
                if column == 0:
                    self.tilemap_matrix.append(list())
                
                weight_water = 1                
                if row > 0:
                    if self.tilemap_matrix[row-1][column] == WATER:
                        weight_water += 35 
                if column > 0:                    
                    if self.tilemap_matrix[row][column-1] == WATER:
                        weight_water += 10

                weight_mountain = 1                
                if row > 0:
                    if self.tilemap_matrix[row-1][column] == MOUNTAIN:
                        weight_mountain += 20 
                if column > 0:                    
                    if self.tilemap_matrix[row][column-1] == MOUNTAIN:
                        weight_mountain += 20
                tile_type = random.choices(
                    [GRASS, WATER, MOUNTAIN],
                    [35, weight_water, weight_mountain])[0]
                self.tilemap_matrix[row].append(
                    TileObject(tile_type, row, column)
                    )

        self.tilesize = 40
        self.mapwidth = len(self.tilemap_matrix)
        self.mapheight = len(self.tilemap_matrix[0])
        self.players = players
    
    def draw(self, game_display):
        x, y = 0,0
        
        for row in self.tilemap_matrix:
            for tile in row:
                if tile.is_visible:
                    tile.draw(game_display)

        for player in self.players:            
            if player.is_human_controlled:
                surrounding_tiles = self.get_surrounding_tiles(player.position, 2)
                for tile in surrounding_tiles:
                    tile.is_visible = True
            if self.get_tile(*player.position).is_visible:
                player.draw(game_display)
    
    def get_surrounding_tiles(self, coordinates, max_range=1):
        res = list()
        for r in range(-max_range, max_range+1):
            for c in range(-max_range, max_range+1):

                tile = self.get_tile(
                                coordinates[0]+r,
                                coordinates[1]+c)
                if tile and abs(c)+abs(r) <= max_range:
                    res.append(tile)
        return res

                

    def legal_moves(self, player):
        legal_moves = [player.position]
        
        possible_positions = [
            (player.position[0]+1,player.position[1]),
            (player.position[0],player.position[1]+1),
            (player.position[0]-1,player.position[1]),
            (player.position[0],player.position[1]-1)            
        ]

        for position in possible_positions:            
            if self.is_position_legal(player, position):
                legal_moves.append(position)
        
        return legal_moves
        

    def move_player(self, player, new_position):
        if self.is_position_legal(player, new_position):            
            player.position = new_position
        else:
            raise IllegalMoveException(f"Illegal Move from user {player}: {new_position} in map {self.tilemap_matrix}")            

    def is_position_legal(self, player, position):
        print("is legal", position)
        is_within_screen = self.x_tiles > position[0] >= 0 and self.y_tiles > position[1] >= 0
        tile = self.get_tile(*position)
        is_tile_legal =  tile and tile.tile_type != WATER
        return is_within_screen and is_tile_legal

    def get_tile(self, x, y):
        try:
            if x >= self.x_tiles or x < 0 or y >= self.y_tiles or y < 0:
                return None 
            return self.tilemap_matrix[x][y]
        except IndexError:
            return None

    def get_tile_from_pos(self, pos_x, pos_y):
        coord_x = pos_x // 40
        coord_y = pos_y // 40
        return self.get_tile(coord_x, coord_y)
        

    def __repr__(self):
        return self.tilemap_matrix

        

                
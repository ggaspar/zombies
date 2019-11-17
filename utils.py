import math


def sum_vectors(vector1, vector2):
    return vector1[0]+vector2[0], vector1[1]+vector2[1]

def calculate_distance(vector1, vector2):
     dist = math.sqrt((vector1[0] - vector2[0])**2 + (vector1[1] - vector2[1])**2)  
     return dist

def get_closest(position_to_compare, positions):    
    closest_dist = 100000
    for pos in positions:
        dist = calculate_distance(position_to_compare, pos)
        if dist < closest_dist:
            closest_dist = dist
            closest_point = pos
    
    return closest_point

def possible_moves(player, tilemap):
    possible_moves = player.position


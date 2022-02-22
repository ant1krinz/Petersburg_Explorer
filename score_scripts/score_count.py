import math


def count_score(curr_coords, dest_coords):
    distance = math.sqrt((dest_coords[0] - curr_coords[0]) ** 2 + (dest_coords[1] - curr_coords[1]) ** 2)
    score = 10 / distance * 200000
    if score > 1000:
        score = 1000
    return int(score)

import math
import pyglet
import random
import resources


def distance(point_1=(0, 0), point_2=(0, 0)):
    """Return the distance between two points."""
    return math.sqrt((point_1[0]-point_2[0])**2 +(point_1[1]-point_2[1])**2)


def lives(num_lives, player_position):
    lives = []
    for i in range(num_lives):
        rat_x, rat_y = player_position
        while distance((asteroid_x, asteroid_y), player_position) < 100:
            rat_x = random.randint(0, 800)
            rat_y = random.randint(0, 600)
        new_playlist = pyglet.sprite.Sprite(img=resources.cat_image, x=rat_x, y=rat_y)
        new_playlist.rotation = random.randint(0, 360)
        lives.append(new_asteroid)
    return lives


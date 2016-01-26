import pygame
import math
import config

class Ball():
    #cos is for y coordinate
    #sin is for x coordinate

    def __init__(self, pos = (0,0), angle = 0.0, speed = 10):
        self.pos = pos
        self.angle = angle
        self.speed = speed

    def normal_bounce(self, orientation_surface = "horizontal"):
        if orientation_surface == "vertical":
            self.angle = 2*math.pi - self.angle
        elif orientation_surface == "horizontal":
            self.angle = math.pi - self.angle
            if self.angle < 0:
                self.angle += 2*math.pi


    def move(self):
        posx = self.pos[0]
        posy = self.pos[1]
        posx += self.speed * math.sin(self.angle)
        posy += self.speed * math.cos(self.angle)
        self.pos = (posx, posy)

ball = Ball(pos = (300, 300), angle = 0.25 * math.pi, speed = 300/config.fps)
#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import cocos
import cocos.euclid as eu
import cocos.collision_model as cm
from cocos.director import director
from cocos.actions import *
import pyglet

STEP=10
class MainCharacter(cocos.sprite.Sprite):
    def __init__(self, image, center_x, center_y, scale=0.5):
        super(MainCharacter, self).__init__(image, (center_x, center_y), scale=scale)
        self.cshape = cm.CircleShape(eu.Vector2(center_x, center_y), 30)
        self.w, self.h = director.get_window_size()

    def update_position(self):
        self.cshape.center = self.position

    def move_forward(self):
        x,y = self.position
        print "qui", self.position
        self.position = x - STEP if (x - STEP) > 0 else x, y
    def move_backward(self):
        x,y = self.position
        print "qua", self.position
        self.position = x + STEP if (x + STEP) < self.w else x, y

class Enemy(cocos.sprite.Sprite):
    def __init__(self, image, center_x, center_y, scale=0.5):

        self.sfx = pyglet.resource.media('assets/scream.wav', streaming=False)
        self.sfx.volume = 10

        sheet = pyglet.image.load(image)
        self.sequence = pyglet.image.ImageGrid(sheet, 1, 2)
        enemy = self.sequence[0]

        self.cshape = cm.CircleShape(eu.Vector2(center_x, center_y), 30)
        sheet = pyglet.image.load(image)

        super(Enemy, self).__init__(enemy, (center_x, center_y), scale=scale)

    def animate(self):
        self.image = self.sequence[1]
        s = ScaleBy(2,1)
        animation = s
        animation += Reverse(s)
        self.sfx.play()
        self.do(animation)

    def standby(self):
        self.image = self.sequence[0]





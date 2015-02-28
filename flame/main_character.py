#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import cocos
import cocos.euclid as eu
import cocos.collision_model as cm
from cocos.director import director

STEP=10
class MainCharacter(cocos.sprite.Sprite):
    def __init__(self, image, center_x, center_y):
        super(MainCharacter, self).__init__(image, (center_x, center_y), scale=0.5)
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
        




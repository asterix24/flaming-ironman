#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import cocos
from cocos.actions import *
import main_character
import pyglet
from pyglet.gl import *


class GameLayer(cocos.layer.Layer):
    is_event_handler = True
    def __init__(self):
        super(GameLayer, self).__init__()
        uno = cocos.sprite.Sprite('assets/CartmanSPG.png')
        uno.position = 300,300
        uno.scale = 0.5
        self.add(uno)

    def on_key_press(self, key, modifiers):
        print key
        # Space key code.


import random
class BackgroundLayer(cocos.layer.Layer):
    def __init__(self):
        super(BackgroundLayer, self ).__init__()
        self.img = pyglet.resource.image('assets/foresta.png')

        for i in range(3):
            bat = cocos.sprite.Sprite('assets/bat.png')
            bat.position = 10 + i * 10, 100
            bat.scale = 0.5
            self.add(bat, z=1)

            uno = MoveBy((random.randint(0,1000), random.randint(0,700)),2)
            s_uno = ScaleBy(2,1)
            ss_uno = Reverse(s_uno)
            due = MoveTo((random.randint(0,1000), random.randint(0,700)),2)
            tre  = MoveTo((random.randint(0,1000), random.randint(0,700)),2)
            s_tre = ScaleBy(2,1)
            ss_tre  = Reverse(s_tre)
            quattro  = MoveTo((random.randint(0,1000), random.randint(0,700)),2)
            cinque = MoveTo((random.randint(0,1000), random.randint(0,700)),2)

            bat.do(Repeat(uno + s_uno + ss_uno + due + tre + s_tre + ss_tre + quattro + cinque))

    def draw( self ):
        glPushMatrix()
        self.transform()
        self.img.blit(0,0)
        glPopMatrix()



class AnimationLayer(cocos.layer.Layer):
    def __init__(self):
        super(AnimationLayer, self).__init__()

        resources = cocos.tiles.load('assets/level_00.tmx')
        self.tilemap = resources["tiles_1"]
        self.tilemap.set_view(0, 0, 1024, 768)


class RootScene(cocos.scene.Scene):
    def __init__(self, game, game_path, main_character_info, main_character_path):
        super(RootScene, self).__init__()

        resources = cocos.tiles.load('assets/level_00.tmx')
        self.tilemap = resources["tiles_1"]
        self.tilemap.set_view(0, 0, 1024, 768)

        self.add(BackgroundLayer())
        self.add(self.tilemap)
        self.add(GameLayer())


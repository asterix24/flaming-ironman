#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import cocos
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


class BackgroundLayer(cocos.layer.Layer):
    def __init__(self):
        super(BackgroundLayer, self ).__init__()
        self.img = pyglet.resource.image('assets/foresta.png')

        uno = cocos.sprite.Sprite('assets/bat.png')
        uno.position = 200,200
        uno.scale = 0.5
        self.add(uno)

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


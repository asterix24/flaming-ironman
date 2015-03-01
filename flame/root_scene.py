#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import cocos
from cocos.layer import *
from cocos.text import *
from cocos.actions import *
import cocos.collision_model as cm
import cocos.euclid as eu
from cocos.director import director
import main_character
import pyglet
from pyglet.gl import *


class GameLayer(cocos.layer.Layer):
    is_event_handler = True
    def __init__(self):
        super(GameLayer, self).__init__()
        self.w, self.h = director.get_window_size()

        self.actor = main_character.MainCharacter('assets/CartmanSPG.png', 311, 610)
        self.add(self.actor)

        self.actor2 = main_character.MainCharacter('assets/CartmanSPG.png', 411, 610)
        self.add(self.actor2)

        self.actors = [ self.actor, self.actor2 ]
        self.collman = cm.CollisionManagerGrid(0.0, self.w, 0.0, self.h, 50, 50)

        for i in self.actors:
            self.collman.add(i)

        self.schedule(self.update)

    def update(self, dt):
        self.actor.update_position()
        self.collman.clear()
        for i in self.actors:
            self.collman.add(i)

        for other in self.collman.iter_colliding(self.actor):
            print "touch"
            

    def on_key_press(self, key, modifiers):
        print key
        if key == pyglet.window.key.LEFT:
            self.actor.move_forward()
        if key == pyglet.window.key.RIGHT:
            self.actor.move_backward()

    def on_mouse_press(self, x, y, buttons, modifiers):
       print director.get_virtual_coordinates(x,y)

import random
class BackgroundLayer(cocos.layer.Layer):
    def __init__(self):
        super(BackgroundLayer, self ).__init__()
        self.img = pyglet.resource.image('assets/foresta2.png')
        seq  = [6, 0, 3, 1, 4, 0, 8, 5, 2]
        seq2 = [0, 2, 7, 1, 5, 6, 3, 0, 8]

        sheet = pyglet.image.load('assets/flame.png')
        sequence = pyglet.image.ImageGrid(sheet, 3, 3)
        flame = pyglet.image.Animation.from_image_sequence(
                [sequence[seq[i]] for i in range(3*3)],
                0.2)

        self.flame = cocos.sprite.Sprite(flame)
        self.flame.position = 720.0, 560.0
        self.flame.scale = 0.6
        self.add(self.flame)

        flame2 = pyglet.image.Animation.from_image_sequence(
                [sequence[seq2[i]] for i in range(3*3)],
                0.2)
        self.flame2 = cocos.sprite.Sprite(flame2)
        self.flame2.position = 820.0, 560.0
        self.flame2.scale = 0.6
        self.add(self.flame2)
        

        #Bats flying
        w,h = director.get_window_size()
        for i in range(3):
            bat = cocos.sprite.Sprite('assets/bat.png')
            bat.position = 10 + i * 10, 100
            bat.scale = 0.5
            self.add(bat, z=1)

            actions =   MoveBy((random.randint(0, w), random.randint(0, h)), 2)
            sl =  ScaleBy(2,1)
            actions += sl
            actions +=  Reverse(sl)
            actions +=  MoveTo((random.randint(0,w), random.randint(0,h)),2)
            actions +=  MoveTo((random.randint(0,w), random.randint(0,h)),2)
            sl =  ScaleBy(2,1)
            actions += sl
            actions +=  Reverse(sl)
            actions +=  MoveTo((random.randint(0,w), random.randint(0,h)),2)
            actions +=  MoveTo((random.randint(0,w), random.randint(0,h)),2)

            bat.do(Repeat(actions))

    def draw(self):
        glPushMatrix()
        self.transform()
        self.img.blit(0,0)
        glPopMatrix()

class ScoreLayer(cocos.layer.Layer): 
    def __init__(self):
        w,h = director.get_window_size()
        super(ScoreLayer, self).__init__()

        # transparent layer
        self.add(ColorLayer(32,32,32,32, width=w, height=48),z=-1 )
        self.position = (0, h-48)
        self.score=Label('Score:', font_size=36,
                font_name='Edit Undo Line BRK',
                color=(255,255,255,255),
                anchor_x='left',
                anchor_y='bottom')
        self.score.position=(0,0)
        self.add(self.score)

        self.lvl=  Label('Lvl:', font_size=36,
                font_name='Edit Undo Line BRK',
                color=(255,255,255,255),
                anchor_x='left',
                anchor_y='bottom')

        self.lvl.position=(450,0)
        self.add(self.lvl)

    def draw(self):
        super(ScoreLayer, self).draw()
        self.score.element.text = 'Score: 000'
        self.lvl.element.text = 'Level: 000'


class RootScene(cocos.scene.Scene):
    def __init__(self, game, game_path, main_character_info, main_character_path):
        super(RootScene, self).__init__()

        resources = cocos.tiles.load('assets/level_00.tmx')
        self.tilemap = resources["tiles_1"]
        self.tilemap.set_view(0, 0, 1024, 768)

        self.add(BackgroundLayer())
        self.add(self.tilemap)
        self.add(GameLayer())
        self.add(ScoreLayer())


#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import cocos

class RootLayer(cocos.layer.Layer):
    is_event_handler = True

    def on_key_press(self, key, modifiers):
        print key

class RootScene(cocos.scene.Scene):
    def __init__(self, game, path):
        super(RootScene, self).__init__()
        self.add(RootLayer())
        self.game, self.path = game, path

        # load first level
        self.loadLevel(game["levels"][0])

    def loadLevel(self, level):
        resources = cocos.tiles.load(os.path.join(self.path, level["file"]))

        tilemap = resources["tiles_1"]
        tilemap.set_view(0, 0, 1024, 768)
        self.add(tilemap)

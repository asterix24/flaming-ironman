#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import cocos
import main_character

class RootLayer(cocos.layer.Layer):
    is_event_handler = True

    def on_key_press(self, key, modifiers):
        print key
        # Space key code.
        if key == 32:
            RootScene.instance.change_level(1)


class RootScene(cocos.scene.Scene):
    instance = None
    def __init__(self, game, game_path, main_character_info, main_character_path):
        super(RootScene, self).__init__()
        RootScene.instance = self
        self.add(RootLayer())


        self.game, self.game_path = game, game_path
        self.tilemap = None

        # load first level
        self.change_level(0)

        self.add(main_character.MainCharacter(main_character_info, main_character_path))

    def change_level(self, index):
        self.loadLevel(self.game["levels"][index])

    def loadLevel(self, level):
        resources = cocos.tiles.load(os.path.join(self.game_path, level["file"]))

        if self.tilemap is not None:
            self.remove(self.tilemap)

        self.tilemap = resources["tiles_1"]
        self.tilemap.set_view(0, 0, 1024, 768)

        self.add(self.tilemap)

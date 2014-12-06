#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import cocos

class MainCharacter(cocos.sprite.Sprite):
    def __init__(self, player_info, player_path):
        self.player_info = player_info
        self.player_path = player_path
        stop_png = os.path.join(self.player_path, self.player_info["moves"][0]["file"])

        super(MainCharacter, self).__init__(stop_png, (100, 100), scale=0.5)



#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import yaml
from cocos.director import director
from root_scene import RootScene

class GameApp(object):
    DEFAULT_CFG = "./flame.cfg"

    def __init__(self, args):
        try:
            cfgs = yaml.load(open(GameApp.DEFAULT_CFG, "r"))
        except IOError:
            cfgs = {"window": {}}

        # loading the game file
        self.game_path = cfgs["game"]["folder"]
        game_file = os.path.join(self.game_path, cfgs["game"]["entry_file"])
        self.game = yaml.load(open(game_file, "r"))

        director.init(**cfgs["window"])

    def run(self):
        director.run(RootScene(self.game, self.game_path))

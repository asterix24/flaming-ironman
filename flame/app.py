#!/usr/bin/python
#-*- coding: utf-8 -*-

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

        director.init(**cfgs["window"])

    def run(self):
        director.run(RootScene())

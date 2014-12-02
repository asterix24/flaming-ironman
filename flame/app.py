#!/usr/bin/python
#-*- coding: utf-8 -*-

from cocos.director import director
from root_scene import RootScene

class GameApp(object):
    def __init__(self, args):
        director.init()

    def run(self):
        director.run(RootScene())

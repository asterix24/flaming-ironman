#!/usr/bin/python
#-*- coding: utf-8 -*-

import cocos

class RootLayer(cocos.layer.Layer):
    is_event_handler = True

    def on_key_press(self, key, modifiers):
        print key

class RootScene(cocos.scene.Scene):
    def __init__(self):
        super(RootScene, self).__init__()
        self.add(RootLayer())

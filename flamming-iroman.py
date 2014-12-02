#
#

from __future__ import division, print_function, unicode_literals

# This code is so you can run the samples without installing the package
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
#

from cocos.director import director
from cocos.layer import Layer
from cocos.scene import Scene
from cocos.sprite import Sprite
from cocos.text import Label
from cocos.actions import *


class FlammingIroman(Layer):

    def __init__(self):
        super(FlammingIroman, self).__init__()

        label = Label('Flamming Iroman',
                font_name='Times New Roman', font_size=32,
                anchor_x='center', anchor_y='center',
                color=(255,0,0,255))

        label.position = 320, 240
        self.add(label)

        # Animazione di tutta la scena
        scale = ScaleBy(2, duration=1)
        label.do(Repeat(scale + Reverse(scale)))

if __name__ == "__main__":
    director.init(resizable=True, caption='Flamming Iroman!')
    director.run(Scene(FlammingIroman()))

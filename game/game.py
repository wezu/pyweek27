import sys
import os
import random
from panda3d.core import *
from direct.showbase.DirectObject import DirectObject

from direct.interval.IntervalGlobal import *
from direct.gui.OnscreenImage import OnscreenImage
from direct.gui.DirectGui import *


class Game(DirectObject):
    def __init__(self):
        img=loader.load_texture('image/background.png')
        self.background= OnscreenImage(image = img, scale=1.0, pos = (0, 0, 0), parent=render2d)

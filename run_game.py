#import all the things!
# it will make it easy for the deploy tools to find the modules
import sys
import os
import random
import math
from panda3d.core import *
from direct.showbase.DirectObject import DirectObject
load_prc_file_data('','textures-power-2 None')
load_prc_file_data('', 'sync-video 0')
load_prc_file_data('', 'show-frame-rate-meter  1')
load_prc_file_data('', 'win-size  1280 720')
#load_prc_file_data('', 'gl-version 3 2')

from direct.showbase import ShowBase
from direct.interval.IntervalGlobal import *
from direct.gui.DirectGui import *

from game.game import Game #great names... -_-'

wp = WindowProperties.getDefault()
wp.set_title("The Silly Number Song Game - wezu")
wp.set_icon_filename('image/p3d.ico')
WindowProperties.setDefault(wp)

class App(DirectObject):
    def __init__(self):
        base = ShowBase.ShowBase()
        base.set_background_color(0, 0, 0)
        base.disable_mouse()

        self.game=Game()


app=App()
base.run()

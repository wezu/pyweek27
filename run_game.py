#import all the things!
# it will make it easy for the deploy tools to find the modules
import sys
import os
import random
import math
import configparser
from panda3d.core import *
Config = configparser.ConfigParser()
Config.read('config.ini')
#read all options as prc_file_data in case they have p3d meaning
for section in Config.sections():
    for option in Config.options(section):
        load_prc_file_data("", option +' '+Config.get(section, option))
from direct.showbase.DirectObject import DirectObject
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

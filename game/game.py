import sys
import os
import random
from panda3d.core import *
from direct.showbase.DirectObject import DirectObject

from direct.interval.IntervalGlobal import *
from direct.gui.OnscreenImage import OnscreenImage
from direct.gui.DirectGui import *

from game.subtitles import make_song_sequence

class Game(DirectObject):
    def __init__(self):
        img=loader.load_texture('image/title_screen.png')
        self.background= OnscreenImage(image = img, scale=1.0, pos = (0, 0, 0), parent=render2d)
        #self.background.set_scale(1.1)

        font=loader.load_font('font/oh_whale.otf')
        font.set_outline(outline_color=(0,0,0,1),outline_width=1.0,outline_feather=0.5)
        font.setPixelsPerUnit(96)

        self.text_node=TextNode('silly_text_node')
        self.text_node.set_font(font)
        self.text_node.set_text('Press any key to start!')
        self.text_node.set_align(TextNode.A_center)
        self.text_node.set_text_color(0.3, 0.3, 1, 1)
        self.text_node.set_shadow(0.03, 0.03)
        self.text_node.set_shadow_color(0, 0, 0, 0.5)
        #self.text_node.setCardColor(1, 1, 1, 0.7)
        #self.text_node.setCardAsMargin(1, 1, 0.5, 0.5)
        #self.text_node.setCardDecal(True)
        self.text_path = aspect2d.attachNewNode(self.text_node)
        self.text_path.set_scale(0.15)
        self.text_path.set_z(-0.9)
        self.text_path.set_transparency(TransparencyAttrib.M_alpha)

        base.buttonThrowers[0].node().setButtonDownEvent('buttonDown')
        self.accept('buttonDown', self.start)

        self.music=loader.load_music('music/the_silly_number_song.ogg')
        self.beat_count=0
        self.beat_tsk=None

    def beat(self, task):
        self.beat_count+=1
        if self.beat_count%2 == 0:
            self.background.setImage(loader.load_texture('image/background2.png'))
        else:
            self.background.setImage(loader.load_texture('image/background.png'))
        return task.again

    def start(self, event=None):
        self.ignore('buttonDown')
        self.beat_tsk=taskMgr.doMethodLater(0.24, self.beat, 'beat_tsk')
        self.text_node.set_text('Get Ready!')
        seq=make_song_sequence(self.text_node)
        #print(seq)
        seq.start()
        self.music.play()

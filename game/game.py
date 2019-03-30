import sys
import os
import random
from panda3d.core import *
from direct.showbase.DirectObject import DirectObject

from direct.interval.IntervalGlobal import *
from direct.gui.OnscreenImage import OnscreenImage
from direct.gui.DirectGui import *

from game.subtitles import make_song_sequence
from game.buttons import make_button_sequence
from game.images import make_image_sequence

class Game(DirectObject):
    def __init__(self):
        self.background= OnscreenImage(image = 'image/title_screen.png', scale=1.0, pos = (0, 0, 0), parent=render2d)

        self.foreground=OnscreenImage(image = 'image/we_are_number_one.png', scale=(256, 1, 256), pos = (640, 0, -360), parent=pixel2d)
        self.foreground.wrt_reparent_to(aspect2d)
        self.foreground.set_transparency(TransparencyAttrib.M_alpha)
        self.foreground.set_bin("fixed", 10)
        self.foreground.hide()

        font=loader.load_font('font/oh_whale.otf')
        font.set_outline(outline_color=(0,0,0,1),outline_width=1.0,outline_feather=0.5)
        font.setPixelsPerUnit(96)

        font64=font.make_copy()
        font64.setPixelsPerUnit(64)

        self.text_node=TextNode('silly_text_node')
        self.text_node.set_font(font)
        self.text_node.set_text('Press any key to start!')
        self.text_node.set_align(TextNode.A_center)
        self.text_node.set_text_color(0.4, 0.5, 1, 1)
        self.text_node.set_shadow(0.03, 0.03)
        self.text_node.set_shadow_color(0, 0, 0, 0.5)
        self.text_path = aspect2d.attach_new_node(self.text_node)
        self.text_path.set_scale(0.15)
        self.text_path.set_z(-0.9)
        self.text_path.set_transparency(TransparencyAttrib.M_alpha)


        self.score_text_node=TextNode('score_text_node')
        self.score_text_node.set_font(font)
        self.score_text_node.set_text('Score: 0')
        self.score_text_node.set_align(TextNode.A_left)
        self.score_text_node.set_text_color(1.0, 1.0, 1.0, 1)
        self.score_text_node.set_shadow(0.03, 0.03)
        self.score_text_node.set_shadow_color(0, 0, 0, 0.5)
        self.score_text_node_path = base.a2dTopLeft.attach_new_node(self.score_text_node)
        self.score_text_node_path.set_scale(0.15)
        self.score_text_node_path.set_pos(0,0,-0.13)
        self.score_text_node_path.set_transparency(TransparencyAttrib.M_alpha)

        self.button=DirectFrame(frameColor=(1.0, 1.0, 1.0, 1.0),
                                  frameTexture='image/button.png',
                                  frameSize=(0, 128, -128, 0),
                                  text='1',
                                  text_font=font64,
                                  text_scale=64,
                                  text_fg=Vec4(1.0),
                                  text_align=TextNode.A_center,
                                  text_pos=(64, -79),
                                  textMayChange=1,
                                  pos=(-64, 0, 64),
                                  state=DGG.NORMAL,
                                  suppressMouse = True,
                                  parent=pixel2d)
        self.button.flatten_light()
        self.button.bind(DGG.B1PRESS, self.on_button_click)
        self.button.wrt_reparent_to(aspect2d)
        self.button.set_transparency(TransparencyAttrib.M_alpha)
        self.button.set_pos(0,0,0)
        self.button.set_bin("fixed", 11)
        self.button.hide()
        self.last_number=self.button['text']
        self.points=[]

        self.fake_button=DirectFrame(frameColor=(1.0, 1.0, 1.0, 1.0),
                                  frameTexture='image/button.png',
                                  frameSize=(0, 128, -128, 0),
                                  text='1',
                                  text_font=font64,
                                  text_scale=64,
                                  text_fg=Vec4(1.0),
                                  text_align=TextNode.A_center,
                                  text_pos=(64, -79),
                                  textMayChange=1,
                                  pos=(-64, 0, 64),
                                  parent=pixel2d)
        self.fake_button.flatten_light()
        self.fake_button.wrt_reparent_to(aspect2d)
        self.fake_button.set_transparency(TransparencyAttrib.M_alpha)
        self.fake_button.set_pos(0,0,0)
        self.button.set_bin("fixed", 11)
        self.fake_button.hide()

        base.buttonThrowers[0].node().setButtonDownEvent('buttonDown')
        self.accept('buttonDown', self.start)

        self.music=loader.load_music('music/the_silly_number_song.ogg')
        self.beat_count=0
        self.beat_tsk=None

        self.images_seq=make_image_sequence(self.foreground)
        self.buttons_seq=make_button_sequence(self.button, self.fake_button)
        self.stubtitles_seq=make_song_sequence(self.text_node, self.music)

    def hide_button(self, task):
        if self.last_number == self.button['text']:
            self.button.hide()
        return task.done

    def reset_button(self, task):
        self.button['frameTexture']='image/button.png'
        return task.done

    def on_button_click(self, event=None):
        self.button['frameTexture']='image/button_down.png'
        self.last_number=self.button['text']
        if self.last_number not in self.points:
            self.points.append(self.last_number)
            self.fake_button.hide()
            #update displayed score:
            self.score_text_node.set_text('Score: {0}'.format(len(self.points)))
        taskMgr.doMethodLater(0.1, self.reset_button, 'reset_tsk')
        taskMgr.doMethodLater(0.2, self.hide_button, 'hide_tsk')


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



        #p=Parallel(self.stubtitles_seq, self.images_seq, self.buttons_seq)
        #p.start()
        self.buttons_seq.start()
        self.stubtitles_seq.start()
        self.images_seq.start()


        #self.music.play()


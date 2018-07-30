#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 00:42:11 2018

@author: nathan
"""

from classes.dialog import Dialog
import assets

class AskString (Dialog):
    
    def __init__(self, cargo = None, done = None, context = None, title = None):
        Dialog.__init__ (self, cargo, done, context)
        self.text = "name"
        self.title = title
    
    def draw (self, draw):
        draw.rectangle ( (20, 20, self.context.parent.width - 20, self.context.parent.height - 20), fill = assets.dialog)
        draw.text ( (30, 30), self.title, font = assets.bigFont, anchor = "nw" )
        draw.rectangle ( (30, assets.bigFontSize + 40, self.context.parent.width - 30 , 2 * assets.bigFontSize + 40 ) )
        if len (self.text) > 0:
            draw.text ( (40, assets.bigFontSize + 40), self.text, font = assets.bigFont, anchor = "nw")
        else:
            draw.text ( (40, assets.bigFontSize + 40), "nothing", font = assets.bigFont, anchor = "nw", fill = (255,150,0) )
    
    def key (self, key, char):
        if key == "BackSpace" and len (self.text) > 0:
            self.text = self.text[:-1]
        elif key == "Return":
            self.done (self.cargo, self.text)
            self.context.parent.dialog = None
        else:
            self.text += char
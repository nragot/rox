#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 21:12:01 2018

@author: nathan
"""

import assets

class TexFile:
    
    def __init__(self, parentTex = None, context = None):
        self.name = "file"
        self.nbr = 1
        self.alone = True
        self.context = context
        self.parentTex = parentTex
    
    def draw(self, draw):
        pass
        
    def key(self, event, key, char):
        pass
    
    def Command (self, event, key, char):
        pass
    
    def antiCommand (self, event, key, char):
        pass
    
    def mouse(self, event):
        pass
    
    def activateDialog (self, dialog):
        self.context.parent.dialog = dialog
    
    def getReady (self, left, up, right, down):
        self.resize (left, up, right, down)
    
    def resize(self, left, up , right, down):
        self.context.left = left
        self.context.right = right
        self.context.up = up
        self.context.down = down
        
    def changeName (self, cargo, x):
        cargo.name = x
        self.nbr = self.parentTex.checkNameNumber (x)
    
    def write (self, path, join):
        pass
    
    def drawArch (self, draw, x, y):
        draw.text ( (x,y), self.name + "(" + str(self.nbr) + ")", fill = assets.archColor, font = assets.font)
        return (x, y + assets.fontsize)
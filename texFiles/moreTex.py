#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 14:55:26 2018

@author: nathan
"""

import assets
from classes.texFile import TexFile
import os

class MoreTex (TexFile):
    
    def __init__(self, parentTex, context):
        TexFile.__init__ (self, parentTex, context)
        self.texFiles = []
        self.focus = 0
        self.name = "hey"
    
    def drawArch (self, draw, x, y):
        draw.text ((x,y), self.name, fill = assets.archColor, font = assets.font)
        x_ = x + assets.charwidth
        y += assets.fontsize
        for f in self.texFiles:
            (x__,y) = f.drawArch (draw, x_,y)
        return (x,y)
    
    def changeFocus (self, x):
        temp = True
        if isinstance (self.texFiles[self.focus], MoreTex):
            temp = self.texFiles[self.focus].changeFocus(x)
        if temp:
            self.focus += x
        if self.focus < 0:
            self.focus = 0
            return True
        elif self.focus > len (self.texFiles) - 1:
            self.focus = len (self.texFiles) - 1
            return True
        self.context.parent.reloadFocusFile (self.texFiles[self.focus])
        return False
    
    def getFocus (self):
        mt = self
        while isinstance (mt, MoreTex):
            mt = mt.texFiles [mt.focus]
        return mt
    
    def getFocusIndex (self):
        mt = self
        while isinstance (mt.texFiles[mt.focus], MoreTex):
            mt = mt.texFiles [mt.focus]
        return mt.focus
    
    def checkNameNumber (self, x):
        n = 0
        for f in self.texFiles:
            if f.name == x and f.nbr > n:
                n = f.nbr
        return n + 1
    
    def append (self, x, context):
        self.texFiles.append (x (self, context) )
    
    def quickAppend (self, x):
        self.texFiles.append (x)
        
    def write (self, path, join):
        directory = path + "/" + self.name + "_" + str(self.nbr)
        if not os.path.exists(directory):
            os.mkdir (directory)
        for file in self.texFiles:
            file.write (directory, join)
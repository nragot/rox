#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 18:46:21 2018

@author: nathan
"""

from classes.texFile import TexFile
import assets

class Math (TexFile):
    
    def __init__(self, parentTex, context):
        TexFile.__init__(self, parentTex, context)
        self.text = ""
        self.cursor = 0
        self.maxCharPerLine = 1
        self.name = "math"
        self.focus = 0
        self.colors = [(  0,   0,   0),\
                       (255,   0,   0),\
                       (  0, 255,   0),\
                       (  0,   0, 255),\
                       (255, 100, 100)]
    
    def resize(self, left, up, right, down):
        TexFile.resize(self, left, up, right, down)
        self.maxCharPerLine = (self.context.right - self.context.left) // assets.charwidth
    
    def key (self, event, key, char):
        if key == "Left":
            self.moveCursor(-1)
        elif key == "Right":
            self.moveCursor(1)
        elif (char == "\b" and self.cursor > 0):
            self.text = self.text[: self.cursor - 1] + self.text[self.cursor:]
            self.moveCursor(-1)
        elif not char == "":
            self.text = self.text[:self.cursor] + char + self.text[self.cursor:]
            self.moveCursor(1)
    
    def moveCursor (self,i):
        self.cursor += i
        if self.cursor < 0: 
            self.cursor = 0
        elif self.cursor > len (self.text): 
            self.cursor = len (self.text)
    
    def draw (self, draw):
        i = 0
        lastBreaks = 0
        line = 1
        boxColor = None
        textColor = None
        left = 0
        up = 0
        color = 0
        
        for char in self.text:
            if i - lastBreaks == self.maxCharPerLine:
                lastBreaks = i
                line += 1
            if ord(char) == 13:
                lastBreaks = i + 1
                line += 1
                char = " "
            elif char == "{":
                color += 1
            if i == self.cursor:
                boxColor  = assets.cursor
                textColor = assets.background 
            else:
                boxColor  = assets.background
                textColor = self.colors[color]
            left = self.context.left + (i - lastBreaks) * assets.charwidth
            up = assets.fontsize * 1.5 * line
            
            draw.rectangle ((left, up, left + assets.charwidth, up + assets.fontsize + 5),\
                            fill = boxColor)
            draw.text ((left, up), char, fill = textColor, font = assets.font)
            i += 1
        if self.cursor == len (self.text):
            left = self.context.left + (i - lastBreaks) * assets.charwidth
            up = assets.fontsize * 1.5 * line
            draw.rectangle( (left, up - 5, left + assets.charwidth, up + assets.fontsize + 5),\
                           fill = assets.cursor)
        
    def write (self, path, join):
        file = path + "/" + self.name + "_" + str(self.nbr)
        doc = open (file, "w")
        i = 0
        doc.write ("$$\n")
        for char in self.text:
            doc.write (char)
            if char == "{":
                i += 1
                c = self.colors[i]
                doc.write ("\\color[rgb]{" + str(c[0] / 255) + "," +\
                           str(c[1] / 255) + "," + str (c[2] / 255)+ "}")
        doc.write ("\n$$")
        doc.close ()
        join.connect (file)
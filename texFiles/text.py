#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 21:17:00 2018

@author: nathan
"""

from classes.texFile import TexFile
import colors

class Text (TexFile):
    
    def __init__(self):
        TexFile.__init__(self)
        self.text = ""
        self.cursor = 0
        self.maxCharPerLine = 1
        self.charwidth = 1
        self.fontsize = 20
        self.charwidth = self.fontsize * 0.8
        self.name = "text"
    
    def resize(self, event, left, up, right, down):
        TexFile.resize(self, event, left, up, right, down)
        self.maxCharPerLine = (self.right - self.left) // self.charwidth
        
    def key(self, event, key, char):
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
    
    def draw(self, canvas):
        i = 0
        lastBreaks = 0
        line = 1
        boxColor = None
        textColor = None
        left = 0
        up = 0
        
        for char in self.text:
            if i - lastBreaks == self.maxCharPerLine:
                lastBreaks = i
                line += 1
            if ord(char) == 13:
                lastBreaks = i + 1
                line += 1
            if i == self.cursor:
                boxColor  = colors.cursor
                textColor = colors.background 
            else:
                boxColor  = colors.background
                textColor = colors.text
            left = self.left + (i - lastBreaks) * self.charwidth
            up = self.fontsize * 1.5 * line
            
            canvas.create_rectangle( (left, up, left + self.charwidth, up + self.fontsize + 5),
                                         fill = boxColor, outline = colors.background)
            canvas.create_text(left,up,\
                                    text = char, fill = textColor,\
                                    font = ("courier", self.fontsize), anchor = "nw" )
            i += 1
        if self.cursor == len (self.text):
            left = self.left + (i - lastBreaks) * self.charwidth
            up = self.fontsize * 1.5 * line
            canvas.create_rectangle( (left, up, left + self.charwidth, up + self.fontsize + 5),
                                         fill = colors.cursor, outline = colors.background)
        
    def write (self):
        return  "HEY" + self.text
        
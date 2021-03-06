#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 21:17:00 2018

@author: nathan
"""

from classes.texFile import TexFile
from PIL import ImageFont
from dialogs.askString import AskString
import assets

class Text (TexFile):
    
    def __init__(self, parentTex, context):
        TexFile.__init__(self, parentTex, context)
        self.text = ""
        self.cursor = 0
        self.maxCharPerLine = 1
        self.name = "text"
        self.titleFont = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', assets.fontsize)
        self.focus = 0
        #break "\\" ; nothing "" ; new "\n\n"
        self.breakType = "break"
    
    def resize(self, left, up, right, down):
        TexFile.resize(self, left, up, right, down)
        self.maxCharPerLine = (self.context.right - self.context.left) // assets.charwidth
        self.line = self.context.down * 0.1
        self.titleFont = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', int ((self.line * 0.9)))
        
    def key(self, event, key, char):
        if key == "Left":
            self.moveCursor(-1)
        elif key == "Right":
            self.moveCursor(1)
        elif key == "Return":
            x = self.parentTex.getFocusIndex ()
            t = Text (self.parentTex, self.context)
            t.name = self.name
            t.nbr = self.parentTex.checkNameNumber (self.name)
            self.parentTex.texFiles.insert (x + 1, t )
            self.context.root.changeFocus (1)
        elif (char == "\b" and self.cursor > 0):
            self.text = self.text[: self.cursor - 1] + self.text[self.cursor:]
            self.moveCursor(-1)
        elif not char == "":
            self.text = self.text[:self.cursor] + char + self.text[self.cursor:]
            self.moveCursor(1)
    
    def command (self, event, key, char):
        if key == "p":
            self.activateDialog ( AskString (self, self.changeName, self.context, "change title") )
    
    def moveCursor (self,i):
        self.cursor += i
        if self.cursor < 0: 
            self.cursor = 0
        elif self.cursor > len (self.text): 
            self.cursor = len (self.text)
    
    def draw(self, draw):
        TexFile.draw (self, draw)
        
        draw.line ( (self.context.left + 20, self.line, self.context.right - 20, self.line), fill = (0,0,0) )
        draw.text ( (self.context.left + 10, 0), self.name, fill = (0,0,0), font = self.titleFont)
        w, temp = draw.textsize (str (self.nbr), font = self.titleFont )
        draw.text ( (self.context.right - w , 10), str(self.nbr), fill = (255, 0, 150), font = self.titleFont)
        
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
            if i == self.cursor:
                boxColor  = assets.cursor
                textColor = assets.background 
            else:
                boxColor  = assets.background
                textColor = assets.text
            left = self.context.left + (i - lastBreaks) * assets.charwidth
            up = assets.fontsize * 1.5 * line + self.line
            
            draw.rectangle ((left, up, left + assets.charwidth, up + assets.fontsize + 5),\
                            fill = boxColor)
            draw.text ((left, up), char, fill = textColor, font = assets.font)
            i += 1
        if self.cursor == len (self.text):
            left = self.context.left + (i - lastBreaks) * assets.charwidth
            up = assets.fontsize * 1.5 * line + self.line
            draw.rectangle( (left, up - 5, left + assets.charwidth, up + assets.fontsize + 5),\
                           fill = assets.cursor)
        
        
    def write (self, path, join):
        file = path + "/" + self.name + "_" + str(self.nbr)
        doc = open (file, "w")
        if self.breakType == "break":
            doc.write ("\\\\\n")
        if self.breakType == "new":
            doc.write ("\n\n")
        doc.write (self.text)
        doc.close ()
        join.connect (file)
        
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 21:08:51 2018

@author: nathan
"""

import assets
from classes.context import Context
from classes.texFile import TexFile
from dialogs.askString import AskString

class Init (TexFile):
    
    def __init__(self, parentTex, context = None):
        TexFile.__init__ (self, parentTex, context)
        self.name = "init"
        self.title = "title"
        self.author = "author"
        self.alone = True
        self.state = None
    
    def key(self, event, key, char):
        if key == "t":
            self.context.parent.dialog = AskString (self, self.changeTitle, self.context, "change title")
        elif key == "a":
            self.context.parent.dialog = AskString (self, self.changeAuthor, self.context, "change author")
        """
        if key == "t":
            self.state = "title"
        if key == "a":
            self.author = simpledialog.askstring("Input", "document author",parent=self.context.parent)
        """
    
    def changeTitle (self, cargo, x):
        cargo.title  = x
    
    def changeAuthor (self, cargo, x):
        cargo.author = x
    
    def draw(self, draw):
        if not self.context == None:
            draw.text ( (self.context.left + 10, 10), text = "press t to change the title", font = assets.bigFont)
            draw.text ( (self.context.left + 10, assets.bigFontSize + 10), text = "press a to change the title", font = assets.bigFont)
            
    def write (self, path, join):
        file = path + "/" + self.name + "_" + str(self.nbr)
        doc = open (file, "w")
        doc.write ("\\documentclass{article}\n"      +\
                   "\\usepackage[utf8x]{inputenc}\n" +\
                   "\\usepackage[T1]{fontenc}\n"     +\
                   "\\usepackage{xcolor}"            +\
                   "\\author{"+self.author+"}\n"     +\
                   "\\date{\\today}\n"               +\
                   "\\title{"+self.title+"}\n"       +\
                   "\\begin{document}\n"             +\
                   "\\maketitle\n")
        join.connect (file)
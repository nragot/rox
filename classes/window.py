#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 17:02:45 2018

@author: nathan
"""

from tkinter import Tk, Canvas
from classes.document import Document
from texFiles.text import Text
import colors

class Window:
    
    def __init__(self):
        self.left = 1
        self.right = 1
        self.leftRatio = .2 
        self.rightRatio = .55
        self.width = 1 #window width
        self.height = 1#window height
        self.doc = Document()
        self.currentTexFile = self.doc.texFiles[1]
    
    def __resize__(self, event):
        self.width  = event.width
        self.height = event.height
        self.left = self.width * self.leftRatio
        self.right = self.width * self.rightRatio
        
        self.currentTexFile.resize (event, self.left, 0, self.right, self.height)
        
        #print ("RESIZE " + str(w) + " " + str(h))
        
        self.redraw()
        
    def __keyBoardInput__(self, event):
        state = event.state
        char = event.char
        key = event.keysym
        if state == 4: #control modifier
            if key == "s":
                self.doc.write(self.width - self.right)
                print ("saved")
        else:    
            self.currentTexFile.key (event, key, char)
        #print (key + " " + char + " " + str (state))
        self.redraw()
        
    def __mouse1Pressed__ (self, event):
        #print ("MOUSE 1 PRESSED " + str (event.x) + " " + str(event.y) )
        pass
        
    def redraw(self):
       pass
    
    def __redrawDefault__(self):
        self.canvas.delete("all")
        
        self.canvas.create_rectangle((0,0, self.width, self.height), fill = colors.background)
        
        self.currentTexFile.draw(self.canvas)
        
        if not self.doc.render == None:
            x = (self.width + self.right) // 2
            y = self.doc.render[0].height ()
            for img in range (len (self.doc.render )) :
                self.canvas.create_image(x , (y + 10) * img, anchor="n", image = self.doc.render[img])
        
        self.canvas.create_line (self.left, 0, self.left, self.height)
        self.canvas.create_line (self.right, 0, self.right, self.height)
        
    
    def __redrawFileNav__(self):
        pass
    
    def go(self):
        self.frame = Tk()
        self.canvas = Canvas (self.frame, width = None, height = None, bg = 'white')
        self.canvas.bind("<Key>", self.__keyBoardInput__)
        self.canvas.bind("<Button-1>", self.__mouse1Pressed__)
        self.frame.bind("<Configure>", self.__resize__)
        self.canvas.focus_set()
        self.canvas.pack(fill = "both", expand=1)
        self.redraw = self.__redrawDefault__
        self.frame.mainloop()
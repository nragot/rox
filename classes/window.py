#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 17:02:45 2018

@author: nathan

"""
import time
from tkinter import Tk, Canvas
from classes.document import Document
from PIL import Image, ImageDraw, ImageTk
from texFiles.text import Text
from texFiles.moreTex import MoreTex
from dialogs.askString import AskString
import assets

class Window:
    
    def __init__(self):
        self.left = 1
        self.right = 1
        self.leftRatio = .2 
        self.rightRatio = .55
        self.width = 1 #window width
        self.height = 1#window height
        self.dialog = None
    
    def __resize__(self, event):
        self.width  = event.width
        self.height = event.height
        self.left = self.width * self.leftRatio
        self.right = self.width * self.rightRatio
        
        self.currentTexFile.resize (self.left, 0, self.right, self.height)
        self.redraw()
        
        #print ("RESIZE " + str(w) + " " + str(h))
    
    def sendSize (self, file):
        file.resize (self.left, 0, self.right, self.height)
        
    def __keyBoardInput__(self, event):
        state = event.state
        char = event.char
        key = event.keysym
        if self.dialog == None:
            if state == 4: #control modifier
                if key == "s":
                    self.doc.write(self.width - self.right)
                    print ("saved")
                elif key == "Up":
                    self.doc.root.changeFocus (-1)
                    self.reloadFocusFile ()
                elif key == "Down":
                    self.doc.root.changeFocus ( 1)
                    self.reloadFocusFile ()
                else:
                    self.currentTexFile.command (event, key, char)
            elif state == 5:
                self.currentTexFile.antiCommand (event, key, char)
            else:    
                self.currentTexFile.key (event, key, char)
        else:
            self.dialog.key (key, char)
        print (key + " " + char + " " + str (state))
        self.redraw()
        
    def __mouse1Pressed__ (self, event):
        #print ("MOUSE 1 PRESSED " + str (event.x) + " " + str(event.y) )
        pass
        
    def redraw(self):
       pass
    
    def __redrawDefault__(self):
        self.canvas.delete("all")
        start = time.time()
        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()
        
        image = Image.new ('RGB', (w, h))
        draw = ImageDraw.Draw(image)
        draw.rectangle ((0,0,w,h), fill = assets.background )
        
        if self.dialog == None:
            self.currentTexFile.draw (draw)
            
            draw.line ( (self.left, 0, self.left, self.height), fill = (0,0,0))
            draw.line ( (self.right, 0, self.right, self.height), fill = (0,0,0) )
            
            if not self.doc.render == None:
                x = int ((self.width + self.right - self.doc.render[0].width) // 2)
                y = self.doc.render[0].height
                print (x, y)
                for img in range (len (self.doc.render )) :
                    image.paste (self.doc.render[img], (x,y * img))
            
            x = 10
            y = 10
            focusY = 0
            
            mt = self.doc.root
            while isinstance (mt, MoreTex):
                focusY += mt.focus + 1
                mt = mt.texFiles[mt.focus]
            
            draw.rectangle ( (0, focusY * assets.fontsize + y, self.left, (focusY+1) * assets.fontsize + y) )
            
            self.doc.root.drawArch (draw, x, y)
            draw.text ( (10,0), str ( (time.time() - start) * 1000 // 1) + " ms")
        else:
            self.dialog.draw (draw)
        
        del draw
        
        self.im = ImageTk.PhotoImage (image)
        self.canvas.create_image ( 0,0, image = self.im, anchor = "nw")
    
    def __redrawFileNav__(self):
        pass
    
    def reloadFocusFile (self, file = None):
        if file == None:
            file = self.doc.root.getFocus ()
        file.getReady (self.left, 0, self.right, self.height)
        self.currentTexFile = file
            
    def go(self):
        self.frame = Tk()
        self.doc = Document(self)
        self.currentTexFile = self.doc.root.texFiles[0]
        self.canvas = Canvas (self.frame, width = None, height = None, bg = 'white')
        self.canvas.bind("<Key>", self.__keyBoardInput__)
        self.canvas.bind("<Button-1>", self.__mouse1Pressed__)
        self.frame.bind("<Configure>", self.__resize__)
        self.canvas.focus_set()
        self.canvas.pack(fill = "both", expand=1)
        self.redraw = self.__redrawDefault__
        self.frame.mainloop()
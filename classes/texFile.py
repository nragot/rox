#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 21:12:01 2018

@author: nathan
"""

class TexFile:
    
    def __init__(self):
        self.name = "file"
        self.alone = True
    
    def draw(self, canvas, left, right):
        pass
    
    def key(self, event, key, char):
        pass
    
    def mouse(self, event):
        pass
    
    def resize(self, event, left, up , right, down):
        self.left = left
        self.right = right
        self.up = up
        self.down = down
    
    def write (self):
        pass
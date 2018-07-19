#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 21:53:17 2018

@author: nathan
"""
from classes.texFile import TexFile

class End (TexFile):
    
    def __init__(self):
        TexFile.__init__(self)
        self.name = "end"
    
    def write (self):
        return "\\end{document}"
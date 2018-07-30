#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 00:40:12 2018

@author: nathan
"""

class Dialog:
    
    def __init__(self, cargo = None, done = None, context = None):
        self.width = 200
        self.height = 200
        self.cargo = cargo
        self.done = done
        self.context = context
    
    def draw (self, draw):
        pass
    
    def key (self, key, char):
        pass
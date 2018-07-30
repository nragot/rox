#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 17:35:41 2018

@author: nathan
"""

class Context:
    
    def __init__(self, parent = None, root = None):
        self.left = 1
        self.right = 2
        self.up = 3
        self.down = 4
        self.parent = parent
        self.root = root
            
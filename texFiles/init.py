#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 21:08:51 2018

@author: nathan
"""

from classes.texFile import TexFile

class Init (TexFile):
    
    def __init__(self):
        self.name = "init"
        self.alone = True
    
    def write (self):
        return "\\documentclass{article}\n"      +\
               "\\usepackage[utf8x]{inputenc}\n" +\
               "\\usepackage[T1]{fontenc}\n"     +\
               "\\author{nathan}\n"              +\
               "\\date{\\today}\n"               +\
               "\\title{test}\n"                 +\
               "\\begin{document}\n"             +\
               "\\maketitle\n"                   
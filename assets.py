#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 17:44:48 2018

@author: nathan
"""

from PIL import ImageFont

fontsize = 20
bigFontSize = 50

background = (62 , 68 , 65 )
text       = (255, 255, 255)
cursor     = (206, 206, 206)
archColor  = (0,0,0)
dialog     = (150,150,150)
errorBackground = (255, 0, 0)
errorText       = (0, 0, 0)

font = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', fontsize)
bigFont = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', bigFontSize)
charwidth = fontsize * 0.8
bigCharwidth = bigFontSize * 0.8

colors = [(  0,   0,   0),\
          (255,   0,   0),\
          (  0, 255,   0),\
          (  0,   0, 255),\
          (255, 100, 100),\
          (100, 255, 100),\
          (100, 100, 255),\
          (100, 255, 100),\
          (100, 100, 255),\
          (255, 200, 200),\
          (200, 255, 200),\
          (200, 200, 255),\
          (255, 255, 255),\
          (255, 200, 100),\
          (100, 255, 200),\
          (200, 100, 255),\
          (255, 100, 200),\
          (200, 255, 100),\
          (100, 255, 200)]
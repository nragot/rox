#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 19:35:59 2018

@author: nathan
"""
import subprocess
from pdf2image import convert_from_path
from texFiles.text import Text
from texFiles.init import Init
from PIL import ImageTk

class Document:
    
    def __init__(self):
        self.title = "title"
        self.path  = "/home/nathan/Documents/workspace/rox projects"
        self.render = None
        self.texFiles = [Init(), Text()]
        self.ratio = (9, 12)
        
    def write(self, width = None):
        doc = open (self.path + "/document.tex","w")
        
        for tf in self.texFiles:
            if tf.alone:
                filePath = self.path + "/" + tf.name
                file = open (filePath, "w")
                
                file.write (tf.write())
                file.close ()
                doc.write ("\\input{\""+ filePath +"\"}\n")
            else:
                doc.write( tf.write())
        doc.write ("\\end{document}")
        
        doc.close ()
        
        proc = subprocess.Popen (["pdflatex",\
                                  "\"" + self.path + "/document.tex\""],\
                                 stdout=subprocess.PIPE, shell=False)
        (out, err) = proc.communicate()
        print ("output \n" + str(out) + "\n err \n" + str(err) )
        
        if width == None:
            x = 300
        else:
            x = width / self.ratio[0]
        self.render = []
        for img in convert_from_path('document.pdf', x):
            #img = img.resize((100, 100), Image.ANTIALIAS)
            im = ImageTk.PhotoImage (img)
            self.render += [im]
        
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 19:35:59 2018

@author: nathan
"""
import subprocess
from classes.context import Context
from texFiles.moreTex import MoreTex
from pdf2image import convert_from_path
from texFiles.text import Text
from texFiles.init import Init
from texFiles.math import Math
import os

class Document:
    
    def __init__(self, parent):
        self.title = "title"
        self.path  = "/home/nathan/Documents/workspace/rox projects"
        self.render = None
        
        context = Context(parent)
        project = MoreTex (None, context)
        context.root = project
        project.append (Init, context)
        firstText = Text (project, context)
        firstText.breakType = "nothing"
        project.quickAppend (firstText)
        project.append (Math, context)
        hep = MoreTex (project, context)
        hep.append (Text, context)
        project.texFiles.append (hep)
        
        self.root = project
        self.ratio = (9, 12)
        
    def write(self, width = None):
        if not os.path.exists(self.path + "/source"):
            os.mkdir (self.path + "/source")
        if not os.path.exists(self.path + "/render"):
            os.mkdir (self.path + "/render")
        
        self.doc = open (self.path + "/source/document.tex","w")
        
        self.root.write (self.path + "/source", self)
        
        """
        for tf in self.texFiles:
            if tf.alone:
                filePath = self.path + "/source/" + tf.name
                file = open (filePath, "w")
                
                file.write (tf.write())
                file.close ()
                doc.write ("\\input{\""+ filePath +"\"}\n")
            else:
                doc.write( tf.write())
        doc.write ("\\end{document}")
        """
        self.doc.write ("\\end{document}")
        self.doc.close ()
        
        proc = subprocess.Popen (["pdflatex",\
                                  "\"" + self.path + "/source/document.tex\""],\
                                 stdout=subprocess.PIPE, shell=False)
        (out, err) = proc.communicate()
        print ("output \n" + str(out) + "\n err \n" + str(err) )
        
        if width == None:
            x = 300
        else:
            x = width / self.ratio[0]
            
        self.render = convert_from_path('document.pdf', x)
        
        os.rename("./document.pdf","" + self.path + "/render/document.pdf")
        os.rename("./document.aux","" + self.path + "/render/document.aux")
        os.rename("./document.log","" + self.path + "/render/document.log")
        
    def connect (self, path):
        self.doc.write ("\\input{\""+ path +"\"}\n")
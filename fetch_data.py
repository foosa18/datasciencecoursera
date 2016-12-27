# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 02:44:11 2016

@author: Ullas
"""
import urllib

myfilecontent=[]
def read_url_html(link):
    f= urllib.request.urlopen(link)
    myfile=f.readline()
    
    if len(myfilecontent)==0:
        myfilecontent.append(myfile)
    return myfilecontent
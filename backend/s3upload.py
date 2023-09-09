#!/usr/bin/python3

import cgi
import os

import cgitb
cgitb.enable()

form = cgi.FieldStorage()
myfilename=form["filecontent"]

print("content-type: text/html")
print()

fh= myfilename.file

filedata=fh.read()
open("myupload/"+ myfilename.filename,"wb")
fh.write(filedata)
fh.close()


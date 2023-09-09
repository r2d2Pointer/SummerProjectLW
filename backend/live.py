#!/usr/bin/python3

import cgi

print("Content-type:text/html")
print()

form = cgi.FieldStorage()
data=form.getvalue("c")

import subprocess as s
out=s.getoutput(data)
print("<pre>")
print(out)
print("</pre>")

#print()
#print()
#print("<form action= HTTP://'your_ip'/menu.html>")
#print("<input type='submit' value='Back to Main menu'></form>")

#!/usr/bin/python3

import cgi

print("Content-type: text/plain")
print("Access-Control-Allow-Origin: *")  # Replace * with the allowed origin(s)
print()

import subprocess as s
out=s.getoutput("date")
print("<pre>")
print(out)
print("</pre>")


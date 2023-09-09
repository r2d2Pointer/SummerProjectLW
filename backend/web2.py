#!/usr/bin/python3

import cgi
import os  # Import the 'os' module to handle file operations
import subprocess as sp 
import cgitb
cgitb.enable()

form = cgi.FieldStorage()

# Use the "file" attribute to get the uploaded file object
myfilename = form["filecontent"]
port= form['c'].value
print("Content-type: text/html")
print()

# Get the actual file data from the file object
filedata = myfilename.file.read()

# Build the path to save the uploaded file
upload_path = "myupload/x.html"

# Open the file in write binary mode and write the file data
with open(upload_path, "wb") as upload_file:
    upload_file.write(filedata)

print("File uploaded successfully.")


n=myfilename.filename
p=n.split(".")
k=p[0]
print(k)
l=str(k)
zz=str(port)
build_command = ["sudo", "docker", "build", "-t", "{}:v1".format(l), "myupload/"]

result1 = sp.run(build_command, capture_output=True, text=True)

run_command = ["sudo", "docker", "run", "-dit", "-p", "{}:80".format(zz), "{}:v1".format(l)]

result = sp.run(run_command, capture_output=True, text=True)

#out1=sp.getoutput("docker build -t {}:v1 myupload/".format(name))
#out2=sp.getoutput("docker run -dit -p 8085:80 {}:v1".format(name))

#print()
#print()
#print("<form action= HTTP://'your_ip'/cgi-bin/web2.py")
#print("<input type='submit' value='Back'></form>")

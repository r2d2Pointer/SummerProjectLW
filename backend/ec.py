#!/usr/bin/python3
import boto3

print("Content-type:text/html")
print()



import subprocess as s
out=s.getoutput("aws ec2 run-instances --image-id {enter you ami_id}  --instance-type {enter instance type}")
print("<pre>")
print(out)
print("</pre>")

print()
print()
print("<form action= HTTP://'your_ip'/menu.html>")
print("<input type='submit' value='Back to Main menu'></form>")



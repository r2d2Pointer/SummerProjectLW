#!/usr/bin/python3

import cgi

print("Content-type:text/html")
print()

form = cgi.FieldStorage()
data1=form.getvalue("d")
data2=form.getvalue("e")

data3=form.getvalue("f")
#myname="vimal"
#print("i am {} ".format(myname))

import boto3
import botocore.exceptions
mybucket=boto3.client("s3")


try:
    s3_client = boto3.client('s3')
    s3_client.upload_file(data2, data1, data3)
    print(f"File uploaded as {data3} in bucket {data1}.")
except botocore.exceptions.ClientError as e:
    print("Error uploading file")

print()
print()
print("<form action= HTTP://'your_ip'/menu.html>")
print("<input type='submit' value='Back to Main menu'></form>")

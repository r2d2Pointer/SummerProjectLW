#!/usr/bin/python3
import cgi
import os
import boto3
from botocore.exceptions import NoCredentialsError

S3_BUCKET_NAME = 'Bucket_name'

# Directory to store uploaded files temporarily
UPLOAD_DIR = '/tmp/upload/'

# Handle the file upload
form = cgi.FieldStorage()
file_item = form['fileToUpload']

if file_item.filename:
    # Create directory if it doesn't exist
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)

    # Save the uploaded file
    upload_path = os.path.join(UPLOAD_DIR, file_item.filename)
    with open(upload_path, 'wb') as upload_file:
        upload_file.write(file_item.file.read())

    # Connect to S3
    s3 = boto3.client('s3')

    try:
        # Upload file to S3 bucket
        s3.upload_file(upload_path, S3_BUCKET_NAME, file_item.filename)
        print("Content-type: text/html\n\n")
        print("<h2>Upload successful</h2>")
    except NoCredentialsError:
        print("Content-type: text/html\n\n")
        print("<h2>Amazon S3 credentials not available</h2>")
    finally:
        # Clean up: Delete the temporarily saved file
        os.remove(upload_path)
else:
    print("Content-type: text/html\n\n")
    print("<h2>No file selected for upload</h2>")


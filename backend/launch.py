#!/usr/bin/python3

import cgi
import json
import boto3

def launch_ec2_instance(ami_id, instance_type):
    ec2 = boto3.resource('ec2')

    try:
        # Launch the EC2 instance
        instance = ec2.create_instances(
            ImageId=ami_id,
            InstanceType=instance_type,
            MinCount=1,
            MaxCount=1
        )[0]

        return instance.id
    except Exception as e:
        return str(e)

def main():
    # Read the input parameters from the request
    form = cgi.FieldStorage()
    ami_id = form.getvalue('ami_id')
    instance_type = form.getvalue('instance_type')

    # Check if both parameters are provided
    if ami_id and instance_type:
        # Launch the EC2 instance
        instance_id = launch_ec2_instance(ami_id, instance_type)
        response = {
            "instance_id": instance_id
        }
    else:
        response = {
            "error": "Both AMI ID and instance type must be provided."
        }

    # Set the response headers
    print("Content-type: application/json")
    print()

    # Return the response as JSON
    print(json.dumps(response))

# Call the main function
main()



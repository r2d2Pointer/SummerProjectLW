#!/usr/bin/python3
import boto3

print("Content-type:text/html")
print()


# count number of instance
try:
    ec2_client = boto3.client('ec2')
    response = ec2_client.describe_instances()
    instance_count = 0
    print("checking")
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            state = instance['State']['Name']
            if state == 'terminated':
                continue
            else:    
                instance_count += 1
    print(f"Number of EC2 instances launched: {instance_count}")
    
except Exception as e:
    print("Error occurred")


print()
print()
print("<form action= HTTP://'your_ip'/menu.html>")
print("<input type='submit' value='Back to Main menu'></form>")



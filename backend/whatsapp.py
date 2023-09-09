#!/usr/bin/python3

import cgi

print("Content-type:text/html")
print()

form = cgi.FieldStorage()
data2=form.getvalue("q")

from twilio.rest import Client

# Replace these with your actual Account SID and Auth Token from Twilio
account_sid = ""
auth_token = ""

# Replace this with your Twilio WhatsApp sandbox number
twilio_whatsapp_number = "+"

# Replace this with the recipient's WhatsApp number with the country code
recipient_whatsapp_number ="" 

# Create a Twilio client
client = Client(account_sid, auth_token)

# Send the WhatsApp message with GPS coordinates
message = client.messages.create(
    body=f"Hello from Twilio! This is a test {data2}",
    from_=f"whatsapp:{twilio_whatsapp_number}",
    to=f"whatsapp:{recipient_whatsapp_number}"
)

print("WhatsApp message  sent successfully!")


print()
print()
print("<form action= http://3.108.228.1/menu.html>")
print("<input type='submit' value='Back to Main menu'></form>")

#!/usr/bin/python3

import cgi

print("Content-type:text/html")
print()

form = cgi.FieldStorage()
data1=form.getvalue("a")

data2=form.getvalue("b")
import smtplib
sender_email = "senders_mail"
sender_password = "senders_password"
recipient_email = data1
subject = "Test Email from Python" 
body = data2

message = f"Subject: {subject}\n\n{body}"

try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message)
    print("Email sent successfully.")
except Exception as e:
    print("Error sending email")


print()
print()
print("<form action= HTTP://'your_ip'/menu.html>")
print("<input type='submit' value='Back to Main menu'></form>")

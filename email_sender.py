# first thing we want to do is import email message
# This email is already pre installed 
from email.message import EmailMessage
# import password from app2.py file 
from app2 import password
import certifi
import ssl
import smtplib

email_sender = 'fanicita4@gmail.com'
email_password = password

# used a temporary password to check the functionality
email_receiver = 'bahata4298@gawte.com'

subject = "Don't forget about IEEE meeting!"
body = """

Meeting its set for 6:30pm 

Zoom Link : 

"""

# Now we want to actually create an instance of the email messgae library 


em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context(cafile=certifi.where())

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

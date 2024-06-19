This Python script is designed to send email reminders for club meetings using Gmail's SMTP server. It simplifies the process of updating your Outlook with meeting details, including the Zoom link, ensuring you never miss an important club meeting.

Purpose
I created this script to automate the process of sending myself reminders about our club meetings every Sunday. It integrates seamlessly with Outlook, allowing me to easily update my calendar with the meeting details and Zoom link.

Functionality
Imports:

Uses Python's built-in email.message module to construct email messages.
Imports the email account password securely from a separate module (app2.py) to authenticate with the SMTP server.
Utilizes certifi and ssl to establish a secure SSL connection.
Uses smtplib to handle the SMTP communication with Gmail's server.
Email Composition:

Constructs an email with the sender's email address, subject line ("Don't forget about IEEE meeting!"), and body text containing the meeting time and Zoom link.
SSL Context:

Creates an SSL context using ssl.create_default_context() with certifi.where() to ensure secure certificate validation.
SMTP Connection:

Establishes a connection to Gmail's SMTP server (smtp.gmail.com) on port 465 using smtplib.SMTP_SSL.
Logs in with the sender's email address and password retrieved from app2.py.
Sends the constructed email message using smtp.sendmail().
Usage
Configure app2.py:

Ensure app2.py contains the password (password = 'your_email_password') securely stored as per your Gmail account.
Update Email Details:

Modify email_sender, email_receiver, subject, and body variables to match your specific meeting details.
Run the Script:

Execute the script to send the reminder email.

# Import all required modules

from email.message import EmailMessage
from dotenv import load_dotenv
import os
import ssl
import smtplib

# This loads the environment variable

load_dotenv()

# Import those variables from .env file

email_sender = os.getenv("invoice@ec-japan.jp")
email_password = os.getenv("supporthelpdesk!123")

# Tested with a temporary email

email_receiver = 'wilddivarider@yahoo.com'

subject = "I'm a python mailer, I work"
body = """
Hi, Buddy

Hope you're good engineer?
"""

em = EmailMessage()
em['From'] = invoice@ec-japan.jp
em['To'] = wilddivarider@yahoo.com
em['subject'] = "I'm a python mailer, I work"
body 
em.set_content(Hope you're good engineer?)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.office365.com', 587, context=context) as smtp:
    smtp.login(invoice@ec-japan.jp, supporthelpdesk!123)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

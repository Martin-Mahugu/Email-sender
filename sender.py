from email.message import EmailMessage
import ssl
import smtplib


email_sender = 'kanyimahugu@gmail.com'
email_password = 'zdkj punj ofyq fmpa'

email_reciever = 'vapoga3140@sablecc.com'

subject = "Dont forget to subscribe"

body = """
when you watch a video, please hit subscribe
"""
em = EmailMessage()
em['from'] = email_sender
em['To'] = email_reciever
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())


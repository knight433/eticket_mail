#by knight
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

server = smtplib.SMTP('smtp.gmail.com', 587)
user = '1rn21ai047.dhruva@gmail.com'
password = 'wwubsvmtoxsjzvtm'

message = MIMEMultipart()

message['From'] = user
message['Subject'] = 'this is a test mail'
body = 'this is your ticket'
message.attach(MIMEText(body, 'plain'))

def sendMail(receiver,photo_filename):

    message['To'] = receiver
    
    with open(photo_filename, 'rb') as photo_file:
        photo_attachment = MIMEImage(photo_file.read())
        photo_attachment.add_header('Content-Disposition', 'attachment', filename=photo_filename)
        message.attach(photo_attachment)

    server.starttls()
    server.login(user, password)

    try:
        server.send_message(message)
        print(f'mail to {receiver} sent')
    except Exception as e:
        print('Error:', str(e))

    server.quit()
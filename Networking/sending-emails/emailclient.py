import smtplib
from email.mime.text import MIMEText

body = "This is a test email . !!"

msg = MIMEText(body)

msg["From"] = 'from-email@gmail.com'

msg["To"] = 'to-email@gmail.com'

msg['Subject'] = "Hello from the other side."

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('emailhere', 'yourpasswordhere')

server.send_message(msg)

print('Mail Sent')

server.quit()

# Email with attachment

import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

with open(f"D:\\Projects\\data\\gmail_app_password.txt", "r") as f:
    app_password = f.read().strip()

sender_email = "vamandeshmukh@gmail.com"
receiver_email = "dyesmuk@gmail.com"

msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = "Email from IBM batch"

body = "Hello, this is a test email with attachment."
msg.attach(MIMEText(body, "plain"))

# file from disk 
# generate file dynamically 
file_path = f"D:\\Projects\data\\sample.txt"

try:
    with open(file_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename={file_path.split('\\')[-1]}",
    )
    msg.attach(part)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

    print("Email with attachment sent successfully")
except Exception as e:
    print("Error:", e)


# Email without attachment


# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# with open(f"D:\\Projects\\data\\gmail_app_password.txt", "r") as f:
#     app_password = f.read().strip()

# sender_email = "vamandeshmukh@gmail.com"
# receiver_email = "dyesmuk@gmail.com"

# msg = MIMEMultipart()
# msg["From"] = sender_email
# msg["To"] = receiver_email
# msg["Subject"] = "Email from IBM batch"

# body = "Hello, this is a test email sent from Python using Gmail App Password."
# msg.attach(MIMEText(body, "plain"))

# try:
#     server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
#     server.login(sender_email, app_password)

#     server.sendmail(sender_email, receiver_email, msg.as_string())
#     print("Email sent successfully")
#     server.quit()
# except Exception as e:
#     print("Error:", e)

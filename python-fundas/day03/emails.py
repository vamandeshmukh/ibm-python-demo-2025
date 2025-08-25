import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

with open(f"D:\\Projects\\data\\gmail_app_password.txt", "r") as f:
    app_password = f.read().strip()

sender_email = "vamandeshmukh@gmail.com"
receiver_email = "dyesmuk@gmail.com"

msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = "Email from IBM batch"

body = "Hello, this is a test email sent from Python using Gmail App Password."
msg.attach(MIMEText(body, "plain"))

try:
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(sender_email, app_password)

    server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Email sent successfully")
    server.quit()
except Exception as e:
    print("Error:", e)

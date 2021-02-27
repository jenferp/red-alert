import smtplib
from email.message import EmailMessage

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "red.alert.roboticsproject@gmail.com"
    msg['from'] = user
    password = "twopobfmpgcydpae"

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)

    server.quit()

# if __name__ == '__main__':
#     email_alert("red alert test", "some one is dyinggggg help", "9168376779@messaging.sprintpcs.com")

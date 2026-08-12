import smtplib
from email.message import EmailMessage

def Marvellous_send_mail(sender,app_password,receiver,subject,body):

    msg = EmailMessage()

    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject

    msg.set_content(body)

    smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)

    smtp.login(sender,app_password)

    smtp.send_message(msg)
 
    smtp.quit()


def main():
    sender_email = "rutus1329@gmail.com"

    app_password = "qhsz oebk lcfc tpgc"

    receiver_email = "sk5835527@gmail.com"

    subject = "Test mail from python script"

    body = """Jay Ganesh,
    This is a test email sent using Marvellous python.
    Regards,
    Marvellous Infosystems
    """

    Marvellous_send_mail(sender_email,app_password,receiver_email,subject,body)
    
    print("Marvellous Mail sent successfully")



if __name__ == "__main__":
    main()
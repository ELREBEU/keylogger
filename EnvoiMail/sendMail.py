import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def send_mail(receiver_email, subject, body, attachments=[]):
    """
    Envoie un email avec les fichiers joints spécifiés.
    :param receiver_email: Adresse du destinataire
    :param subject: Objet du mail
    :param body: Corps du mail
    :param attachments: Liste des fichiers à joindre
    """
    sender_email = "amazonoussama640@gmail.com"  # Adresse d'envoi
    password = "tdcf hoql nrco flxv"  # Mot de passe de l'expéditeur
    smtp_server = "smtp.gmail.com"
    port = 465

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    for filename in attachments:
        try:
            with open(filename, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", f"attachment; filename={filename}")
            message.attach(part)
        except FileNotFoundError:
            print(f"Fichier non trouvé : {filename}")
            continue

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("Le mail a été envoyé")
    except Exception as e:
        print(f"Erreur lors de l'envoi du mail : {e}")

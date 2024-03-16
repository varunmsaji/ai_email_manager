import os 
import imaplib
import email
import asyncio
import concurrent.futures
from email.utils import parseaddr
import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import yaml
class EmailFetcher:
    def __init__(self):
        self.user = os.getenv("EMAIL_USER")
        self.password = os.getenv("EMAIL_PASSWORD")
        self.host=os.getenv("IMAP_HOST")
        self.smtp_server=os.getenv("SMTP_SERVER")

        with open("whitelist.yaml","r") as file:
            data =yaml.safe_load(file)
            self.whitelist = set(data.get("whitelist",[]))

    #login 

    def login(self):
        mail = imaplib.IMAP4(self.host)
        mail.login(self.user,self.password)
        mail.select("inbox") 
        return mail


test_obj = EmailFetcher()
data =test_obj.login()
print(data)
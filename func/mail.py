#!/usr/bin/env python
# coding: utf-8
"""
@description: Send e-mails via SMTP-Gateway
@author: tkadt
@created: 2017-04-11
"""
from smtplib import SMTP
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.utils import COMMASPACE, formatdate
from email import encoders


SMTP_GATEWAY = "smtp.six-group.net"


def sendEmail(send_from, send_to, subject, text, 
              server=SMTP_GATEWAY, files=None):
    """
    @description: Sends e-mails to the adresses
    @param send_from: an e-mail Adress as Sender
    @param send_to: a string of comma separated e-mail adresses as receiver
    @param subject: the subject for the e-mail
    @param text: a Text to send
    @param server: the SMTP-Gateway
    @param files: list of files  
    """
    smtp = SMTP(SMTP_GATEWAY)
    msg = makeMessage(send_from, send_to, subject, text, files)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()

def makeMessage(send_from, send_to, subject, text, files):
    """
    @description: Creates a message with MIMETypes etc.
    @param send_from: an e-mail Adress as Sender
    @param send_to: a string of comma separated e-mail adresses as receiver
    @param subject: the subject for the e-mail
    @param text: a Text to send
    @param files: list of files 
    @return: a Message as MIMEMultipart Object
    """
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = send_to
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
            part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
            msg.attach(part)         
    return msg


'''

# Sendmail mit File anhang
#    sendEmail("heinz.wuethrich@six-group.com", 'heinz.wuethrich@six-group.com', 
#              "Ein Test", "Ich teste nur mal die smtp lib von Python", files=["U:\\ZZZ\\test.txt"])

# Sendmail ohne File anhang
    sendEmail("heinz.wuethrich@six-group.com", 'heinz.wuethrich@six-group.com', 
        "Ein Test", "Ich teste nur mal die smtp lib von Python", files=[])
    
    
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from config import EMAIL_ACCOUNT, EMAIL_PASSWORD

test_subject = 'Julklappsinfo - ETT TEST!'

test_body = '''Hej {0}!

Svara gärna så snabbt som möjligt på det här mailet!

Om det varit på riktigt skulle du gett en present till {1} på julafton.

Kontrollera att
1. Du inte bor tillsammans med personen du ska ge presenten till
2. Du inte är direkt familj med personen du ska ge presenten till

När vi vet att det funkar kommer tomten få den här algoritmen och köra den på nordpolens stordator.

Vi hörs snart!
Jultomtens IT-avdelning
'''

real_subject = "Julklappsinfo"

real_body = '''Hej {0}!

Tomtens maskinintelligenta robot drog ditt och sedan {1}s namn från julhatten.
Det betyder att du ska ge en present till {1} på julafton!

Det här är alltså inte ett test utan PÅ RIKTIGT!

Du kommer att få en present från en annan person än {1}.
Du vet inte från vem. Vi vet inte från vem. Endast tomtens stordator vet från vem.


God Jul! 
Jultomtens IT-avdelning
Nordpolen 1337'''

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)
print "Successfully logged in to the mail service!"

def create_message(address, username, user_to_give_to):
    msg = MIMEMultipart()
    msg['From'] = "Nordpolens IT-avdelning"
    msg['To'] = address
    msg['Subject'] = test_subject
    
    body = test_body.format(username, user_to_give_to)
    msg.attach(MIMEText(body, 'plain'))
    return msg


def send_mail(address, message):
    text = message.as_string()
    server.sendmail(EMAIL_ACCOUNT, address, text)

def close_mail_server():
    server.quit()

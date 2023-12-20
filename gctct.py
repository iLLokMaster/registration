import random
import string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
def generate_password(length = random.randint(5, 10)):
    letters = string.ascii_lowercase
    digits = string.digits
    punctuations = string.punctuation

    password = ''.join(random.choice(letters + digits + punctuations) for _ in range(length))

    return password
def register():
    mail = input("mail")
    # create message object instance
    msg = MIMEMultipart()
    message = generate_password()
    #setup the parameters of the message
    password = "" #your google password
    msg['From'] = "" #your mail
    msg['To'] = mail
    msg['Subject'] = "password"
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    #create server
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    # Login Credentials for sending the mail
    server.login(msg['From'], password)
    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
    print("successfully sent email to %s:" % (msg['To']))
    if input("check your mail") == password:
        print("successfully")
        user_password = input("password from mail")
print("1 register\n"
      "2 login")
vibor = int(input())
if vibor == 1:
    register()
elif vibor == 2:
    pass
else:
    print("try again")
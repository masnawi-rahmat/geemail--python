print('')
print("++++++++++++++++++++++++++++++++++++++++++++++++")
print("XXXXX  XXXXX  XXXXX  XXXXXXXX  XXXXXX  XX  XX   ")
print("XX     XX     XX     XX XX XX  XX  XX  XX  XX   ")
print("XX     XXXXX  XXXXX  XX XX XX  XXXXXX  XX  XX   ")
print("XX  X  XX     XX     XX XX XX  XX  XX  XX  XX   ")
print("XXXXX  XXXXX  XXXXX  XX XX XX  XX  XX  XX  XXXXX")
print("++++++++++++++++++++++++++++++++++++++++++++++++ v.01")
print('')
print('Important! For this applet to work, please configure your email account to allow for less secure app, if applicable.')
print('')
import smtplib
from email.mime.text import MIMEText
emailaddress = input("What is your gmail address? Please input below:\n ")
while '@' not in emailaddress:
    emailaddress = input("Please input a valid email address below:\n ")
else:
    emailpassword = input("What is your email password? Please input below:\n ")
if '@gmail' in emailaddress:
    server_name = 'smtp.gmail.com'
    server_port = 465
else:
    server_name = input("What is the email server name? Please input below:\n ")
    server_port = input("What is the email server port? Please input below:\n ")
mailto = input("What is the email address that you want to send your email to? Please input below:\n ")
while '@' not in mailto:
    mailto = input("Please input a valid email address below:\n ")
else:        
    subject = input("What is the subject header of your email? Please input below:\n ")
    text = input("What is the content of your email? Please input below:\n ")
    msg = (MIMEText(text + '\n\nThis message is sent from Python.'))
    msg ['Subject'] = subject
print("Hang on... your email is being sent.")
try:
    server = smtplib.SMTP_SSL(server_name, server_port)
    server.login(emailaddress, emailpassword)
    server.sendmail(emailaddress, mailto, msg.as_string())
    server.quit()
    print('Email successfully sent to ' + mailto + '!')
except:
    print('Oops! Something went wrong... Please try again.')
    
#cut & paste job (and a tiny bit of coding) by masnawi rahmat
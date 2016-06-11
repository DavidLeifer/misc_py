import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromaddress = '' #throwaway address
toaddress = '' #throwaway address
text = 'This is my first email from python'
username = '' #throwaway usrname
password ='' #throwaway password
msg = MIMEMultipart()
msg['From'] =fromaddress
msg['To'] = toaddress
msg['Subject'] = text
msg.attach(MIMEText(text))
server = smtplib.SMTP('smtp.googlemail.com')
server.ehlo()
server.starttls()
server.ehlo()
server.login(username,password)
server.sendmail(fromaddress,toaddress,msg.as_string())
server.quit()
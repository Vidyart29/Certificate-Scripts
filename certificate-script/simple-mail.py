# Python code to illustrate Sending mail with attachments 
# from your Gmail account 

# libraries to be imported 
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

fromaddr = "SENDERS EMAIL ID"
toaddr ="RECEIVERS EMAIL ID"

'''
before sending the mail, make sure to TURN OFF- LESS SECURE APPS
'''

# instance of MIMEMultipart 
msg = MIMEMultipart() 

# storing the senders email address 
msg['From'] = fromaddr 

# storing the receivers email address 
msg['To'] = toaddr 

# storing the subject 
msg['Subject'] = "SUBJECT OF MAIL"  #from here change subject of mail

# string to store the body of the mail 
body = "testing mail"  #from here change the body(content) mail

# attach the body with the msg instance 
msg.attach(MIMEText(body, 'plain')) 

# open the file to be sent 
filesname ="Ms.Vidya Rautela"
attachment = open("C:/Users/hp/Desktop/teachmebro_intern/certificate-script/output/Ms.Vidya Rautela.png ", "rb") 

# instance of MIMEBase and named as p 
p = MIMEBase('application', 'octet-stream') 


# To change the payload into encoded form 
p.set_payload((attachment).read()) 

# encode into base64 
encoders.encode_base64(p) 
p.add_header('Content-Disposition', "attachment; filename= %s" % filesname) 

# attach the instance 'p' to instance 'msg' 
msg.attach(p) 

# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 

# start TLS for security 
s.starttls() 

# Authentication 
s.login(fromaddr, "Password_of_senders_mail_will_come_here") 

# Converts the Multipart msg into a string 
text = msg.as_string() 

# sending the mail 
s.sendmail(fromaddr, toaddr, text) 

# terminating the session 
s.quit() 

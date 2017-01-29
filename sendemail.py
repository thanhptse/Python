import smtplib

# Strings
username = 'test@gmail.com'
password = 'xxxxx'

fromaddr = 'test@gmail.com'
toaddr = 'thanhptse@gmail.com'

# Content
msg = 'Happy new year'

# Do job

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)

server.sendmail(fromaddr,toaddr,msg)

server.close()




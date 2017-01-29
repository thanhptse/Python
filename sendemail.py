import smtplib

# Strings
username = 'jvevermight@gmail.com'
password = 'xxxxx'

fromaddr = 'jvevermight@gmail.com'
toaddr = 'thanhptse@gmail.com'

# Content
msg = 'Happy new year'

# Do job

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)

server.sendmail(fromaddr,toaddr,msg)

server.close()




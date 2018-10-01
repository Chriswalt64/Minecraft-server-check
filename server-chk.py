import minestat
import smtplib
import credentials 

ipAdd = '' #Enter in the external IP of your server
ms = minestat.MineStat(ipAdd, 25565) #If you're using a different port, you would change this here

#You can also add email credentials directly if you wish, but importing from a different file adds an extra layer of security
user = credentials.user
passwd = credentials.passwd

print('Minecraft server status of %s on port %d:' % (ms.address, ms.port))
if ms.online:
  print('Server is online running version %s with %s out of %s players.' % (ms.version, ms.current_players, ms.max_players))
  print('Message of the day: %s' % ms.motd)
  
else:
  print('Server is offline!')
  contacts = open('numbers.txt').readlines()
  content = "The Minecraft server is down. "
# setting up auto generated emails when server is down
 # mail = smtplib.SMTP('smtp.gmail.com',587)
  #Accessing the extended smtp stuff
  #mail.ehlo()
  #Encrypt login credentials
  #mail.starttls()
  #login to email
  #mail.login(user,passwd)
  #actual email
  #mail.sendmail('fromemail',contacts,content)
  #closing out the login info
  #mail.close()

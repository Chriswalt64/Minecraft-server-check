# Minecraft-server-check
This code utilizes an already existing project called Minestat (https://github.com/ldilley/minestat), but also allows for notification via email/text message.

# Things to Note

## Adding text message functionality

Cell phone numbers can be used on the notification list, but in order to do so, you have to append the domain name to the end of the cell phone number. This varies from carrier to carrier, here is a list of common ones

- Alltel: phonenumber@message.alltel.com
- AT&T: phonenumber@txt.att.net
- T-Mobile: phonenumber@tmomail.net
- Virgin Mobile: phonenumber@vmobl.com
- Sprint: phonenumber@messaging.sprintpcs.com
- Verizon: phonenumber@vtext.com
- Nextel: phonenumber@messaging.nextel.com
- US Cellular: phonenumber@mms.uscc.net


## Using smtplib

https://docs.python.org/3/library/smtplib.html

I wont go into all of the information on how it works here, but I have included a link to the documentation for the smtplib Module in Python. 

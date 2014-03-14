#!/usr/bin/python

from piglow import PiGlow
import praw
import time


piglow = PiGlow()

# Reddit stuff

username = 'USERNAME'
password = 'PASSWORD'

r = praw.Reddit('/u/'+username+' LED piglow orangered system by /u/balrogath, v 0.1')
r.login(username, password)

# notifications we've already been notified about
already_done = []

# forever!
while True:
	try:
		piglow.led1(0)
		unread = r.get_unread()
		unreadcount = 0
		for message in unread:
			unreadcount = unreadcount + 1
			if message.id not in already_done:
			  #flash to get attention! new message!
				piglow.led3(20)
				time.sleep(.5)
				piglow.led3(0)
				time.sleep(.5)
				piglow.led3(20)
				time.sleep(.5)
				piglow.led3(0)
				time.sleep(.5)
				piglow.led3(20)
				time.sleep(.5)
				piglow.led3(0)
				time.sleep(.5)
			already_done.append(message.id)		
		if unreadcount == 0:
			piglow.led3(0)
		else:
			piglow.led3(20)
		time.sleep(30)
	except Exception as e:
		# Ohnoes! an error!
		piglow.led1(10) 
		time.sleep(120)

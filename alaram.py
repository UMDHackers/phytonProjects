from time import gmtime, strftime
import time
import winsound
from msvcrt import getch
import threading

active_alarm = dict()
Freq = 2500 # Set Frequency To 2500 Hertz
Dur = 500 # Set Duration To 1000 ms == 1 second
alarm = "0"
key = 0
def check_time():
	#print(strftime("%I:%M:%S %p", time.localtime()))
	current = strftime("%I:%M:%S %p", time.localtime())
	for key in active_alarm:
		if current == active_alarm[key]:
			for x in range(0, 3):
				print "WAKE UP"
				print "GET UP"
				winsound.Beep(Freq,Dur)
				del active_alarm[key]

def pick_time():
	alarm = raw_input("Enter time you would like to wake up please! HH:MM:SS AM/PM ")
	
try: 
	threading.Thread(target=check_time, args=())
except:
	print "fail"

pick_time()
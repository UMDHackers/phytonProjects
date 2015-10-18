from time import gmtime, strftime
import time
import winsound
from msvcrt import getch
pick = False
Freq = 2500 # Set Frequency To 2500 Hertz
Dur = 500 # Set Duration To 1000 ms == 1 second
alarm = "0"
key = 0

while True:
    #print(strftime("%I:%M:%S %p", time.localtime()))
    current = strftime("%I:%M:%S %p", time.localtime())
    if current == alarm :
        pick = False
        alarm = "0"
        i = 0
        while i != 6:
            print "WAKE UP"
            print "GET UP"
            winsound.Beep(Freq,Dur)
            i += 1


    if pick != True :
        print("Enter time you would like to wake up please! HH:MM:SS AM/PM")
        alarm = raw_input()
        pick = True

    #time.sleep(1)

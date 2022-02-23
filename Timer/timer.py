#import modules
import time
from playsound import playsound
import msvcrt as m

#define wait for microsoft windows
def wait():
    m.getch()

#define the countdown function
def countdown(t):
    #convert t from mins into seconds
    t = t*60

    while t:
        #split t into mins and secs
        mins, secs = divmod(t, 60)

        #formatted string
        timer = '{:02d}:{:02d}'.format(mins, secs)
        
        #display formatted string
        print(timer, end="\r")

        #wait
        time.sleep(1)

        #decrement
        t -= 1

    #after timer is finished
    try:
        while True:
            print("Time is up! Back to work.")
            playsound('Timer/alarm.wav')
    except KeyboardInterrupt:
        pass

#input time in minutes
t = input("Please enter the time desired in minutes: ")

#call countdown function
countdown(int(t))
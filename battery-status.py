# display the battery status
# when power is below 15 % beep until stopped

import time
from playsound import playsound

# contains battery remaining power
statusf = "/sys/class/power_supply/BAT0/capacity"
with open(statusf) as f:
    while True:
        pow_= f.read()
        print(pow_)
        if float(pow_) < 15.0:
            print("power crisis!!")
            while True:
                # beeps until exited
                playsound('beep.wav')
                time.sleep(2)
        time.sleep(5 * 60)


# display the battery status
# when power is below 15 % beep until stopped

import time
from playsound import playsound

# contains battery remaining power
statusf = "/sys/class/power_supply/BAT0/capacity"
with open(statusf) as f:
    # keep checking the battery power every
    # 5 min
    while True:
        # battery remaining power
        pow_= f.read()
        print(pow_)
        # when battery power less than 15%
        # beep
        if float(pow_) < 15.0:
            print("power crisis!!")
            while True:
                # beeps until killed
                playsound('beep.wav')
                time.sleep(2)
        time.sleep(5 * 60)


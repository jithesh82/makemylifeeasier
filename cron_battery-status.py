#!/usr/bin/env python3

# display the battery status
# when power is below 15 % beep until stopped

import time
from playsound import playsound
from tkinter import *
from PIL import ImageTk, Image


# contains battery remaining power
statusf = "/sys/class/power_supply/BAT0/capacity"
with open(statusf) as f:
    # battery remaining power
    pow_= f.read()
    print(pow_)
    open('/home/jk/jk/python/power-battery.data', 'a').write(pow_)
    # when battery power less than 15%
    # beep
    #pow_ = 12
    if float(pow_) < 20.0:
        print("power crisis!!")
        if open('/sys/class/power_supply/BAT0/status').read() != 'Charging\n':
            playsound('/home/jk/jk/python/beep.wav')
            #Label(root, text="Error!").pack()
            #root = Tk()
            #imageobj = Image.open('power.png')
            #photoimg = ImageTk.PhotoImage(imageobj)
            #Button(image=photoimg, command=root.quit).pack()
            #root.mainloop()
            import os
            #os.environ['DISPLAY'] = ':0'
            #os.environ['XAUTHORITY'] = '/home/jk/.Xauthority'
            os.system('open /home/jk/jk/python/power.png')


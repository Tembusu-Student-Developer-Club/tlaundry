# POWEROFF BUTTON - connecting pins 38 and 40
# Add the following line at the bottom of /etc/profile to enable poweroff button on startup.
#
# sudo python /home/pi/tlaundry/pi/poweroff_btn.py &

import RPi.GPIO as GPIO
import time
import datetime
import os

BTN_PIN = 20 # pin 38
SET_PIN = 21 # pin 40
GPIO.setmode(GPIO.BCM)

# make sure initial output of button pin is not high.
GPIO.setup(BTN_PIN, GPIO.OUT)
GPIO.output(BTN_PIN, 0)

GPIO.setup(SET_PIN, GPIO.OUT)
GPIO.output(SET_PIN, 1)
GPIO.setup(BTN_PIN, GPIO.IN)

# while(True):
#     print(GPIO.input(BTN_PIN))
#     time.sleep(1)

print("Poweroff button enabled. HOLD pins 38 and 40 to poweroff.")

while(True):
    if(GPIO.input(BTN_PIN)):
        print("\nPoweroff Button pressed. HOLD to shutdown.")
        print("Shutting down in 3...")
        time.sleep(1)

        if(GPIO.input(BTN_PIN)):
            print("Shutting down in 2...")
            time.sleep(1)

            if(GPIO.input(BTN_PIN)):
                print("Shutting down in 1...")
                time.sleep(1)

                if(GPIO.input(BTN_PIN)):
                    print("\nShutting down...")
                    os.system("sudo poweroff")

                else:
                    print("\nShutdown aborted.")
            else:
                print("\nShutdown aborted.")
        else:
            print("\nShutdown aborted.")

    time.sleep(1)

GPIO.cleanup()

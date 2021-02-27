import RPi.GPIO as GPIO
import time
import datetime
import os

BTN_PIN = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(BTN_PIN, GPIO.IN, initial=GPIO.LOW)

while(True):
    if not(GPIO.input(BTN_PIN)):
        print("\nPoweroff Button pressed. HOLD to shutdown.")
        print("Shutting down in 3...")
        time.sleep(1)

        if not(GPIO.input(BTN_PIN)):
            print("Shutting down in 2...")
            time.sleep(1)

            if not(GPIO.input(BTN_PIN)):
                print("Shutting down in 1...")
                time.sleep(1)

                if not(GPIO.input(BTN_PIN)):
                    print("\nShutting down...")
                    os.system("sudo poweroff")
                
                else:
                    print("\nShutdown aborted.")
            else:
                print("\nShutdown aborted.")
        else:
            print("\nShutdown aborted.")

    time.sleep(1)
                


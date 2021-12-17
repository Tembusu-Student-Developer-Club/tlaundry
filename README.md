# tLaundry Project (formerly Tembusu Washing Machine Project)

This project was started by Tembusians, for Tembusians.

The project aims to conceptualise and modularise a detection system for the running state of all washing machines and dryers in Tembusu College. The information collected through the detection system can then be passed to users through a Telegram bot or a mobile website.

The script is mainly written in Python.

## Installation

`detect.py` is a Python script written to be run on a Raspberry Pi, and it checks the curent state of all op-amps sending digital signals to its GPIO pins. 

It runs on the Raspberry PI at startup, and will continue to run forever. The script continually checks the state of the LDRs connected to the washing machines / dryer plugged into the Pi's GPIO pins.

## Project Status

The script currently only supports the machines on Tembusu College Level 9. Once the functionality of the system has been verified, we plan to extend the script to cover the machines on Tembusu College Level 17 as well.

## Credits

This project is currently being worked on under the Tembusu Student Developer Club (SDC).

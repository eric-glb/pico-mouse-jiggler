# Script to run a raspberry pi pico with CircuitPython and the
# Adafruit adafruit_hid.keyboard library.
# It simulates a keyboard, and the [F1] key is pressed every 10 sec.
#                                                eric-glb 2023/04/18

import board
import digitalio
import time
import busio
import usb_hid
import usb_hid_map as usb
from adafruit_hid.keyboard import Keyboard

# We'll use the board's LED
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# Define keyboard ^^
kbd = Keyboard(usb_hid.devices)

# [F1] every 15 sec, ad vitam aeternam
while True:
  for i in range(1, 50):
    led.value = True
    time.sleep(1/i)
    led.value = False
    time.sleep(1/i)    
  led.value = True
  kbd.send(usb.F1)
  time.sleep(0.2)
  led.value = False
  time.sleep(5.8)


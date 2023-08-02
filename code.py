# Pi Pico Mouse jiggler
# inspired from https://www.tomshardware.com/how-to/diy-mouse-jiggler-raspberry-pi-pico
#                                                                   eric-glb 2023/08/01

import time
import usb_hid
from adafruit_hid.mouse import Mouse
import board
from digitalio import DigitalInOut, Direction, Pull

# define hardware
mouse = Mouse(usb_hid.devices)
button = DigitalInOut(board.GP11)
button.direction = Direction.INPUT
button.pull = Pull.UP
led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT

# Start as soon as plugged
active = 1

# Other variables
time_interval = 2
time_last_fired = 0

# Visual feedback
def blink():
    for i in range(5):
        led.value = True
        time.sleep(0.1)
        led.value = False
        time.sleep(0.1)

# Main loop
print("Start mouse jiggler")
blink()

while True:
    if button.value == False and active == 0:
        print("Turning on")
        active = 1
        blink()
    elif button.value == False and active == 1:
        print("Turning off")
        active = 0
        blink()
    elif button.value == True and active == 1:
        time_elapsed = time.monotonic() - time_last_fired
        if time_elapsed > time_interval:
            if led.value:
                mouse.move(-2, 0, 0)
            else: 
                mouse.move(2, 0, 0)
            time_last_fired = time.monotonic()
            led.value = not led.value

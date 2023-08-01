import storage
import board
from digitalio import DigitalInOut, Direction, Pull

button = DigitalInOut(board.GP11)
button.direction = Direction.INPUT
button.pull = Pull.UP

# Disable the CIRCUITPY USB drive
storage.disable_usb_drive()

# Check button
value = button.value
print("Read-only:", value)
storage.remount("/", readonly=value)

# To re-enable the CIRCUITPY USB drive manually, in REPL:
# >>> import storage
# >>> storage.remount("/", readonly=False)

print("boot finished OK")

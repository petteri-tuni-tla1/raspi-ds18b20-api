import RPi.GPIO as gpio
import time
import sys


# With the relay board, just gpio signal on-off does not seem to work. This trick seems to work.
# ... by letting the pin to "float" - making it IN instead of OUT, pulls the signal down
# https://forum.allaboutcircuits.com/threads/raspberry-pi-triggers-relay-before-power-is-turned-on.174898/

pin1=int(12)

if len(sys.argv) > 1:
    pin1=int(sys.argv[1])

print("Using GPIO-pin ",pin1)

gpio.setmode(gpio.BCM)

while True:
    gpio.setup(pin1, gpio.IN)
    print("INPUT mode",pin1)
    time.sleep(4)
    gpio.setup(pin1, gpio.OUT)
    gpio.output(pin1, gpio.LOW)
    print("OUTPUT mode - LOW",pin1)
    time.sleep(4)



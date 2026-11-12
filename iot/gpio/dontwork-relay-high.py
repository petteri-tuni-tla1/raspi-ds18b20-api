import RPi.GPIO as gpio
import time

pin1=12

gpio.setmode(gpio.BCM)
gpio.setup(pin1, gpio.OUT)

while True:
    gpio.output(pin1, gpio.HIGH)
#    gpio.output(pin1,False)
    print("HIGH",pin1)
    time.sleep(4)



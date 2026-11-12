import RPi.GPIO as gpio
import time

pin1=19
pin2=26

gpio.setmode(gpio.BCM)
gpio.setup(pin1, gpio.OUT)
gpio.setup(pin2, gpio.OUT)

while True:
    gpio.output(pin1, gpio.HIGH)
    print("HIGH",pin1," ... ",pin2)
    gpio.output(pin2,True)
    time.sleep(4)
    gpio.output(pin1, gpio.LOW)
    gpio.output(pin2,False)
    print("LOW",pin1)
    time.sleep(4)



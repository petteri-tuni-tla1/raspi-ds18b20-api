import RPi.GPIO as gpio
import time

pin1=19
pin2=26
pausetime=3

gpio.setmode(gpio.BCM)
gpio.setup(pin1, gpio.OUT)
gpio.setup(pin2, gpio.OUT)

while True:
    gpio.output(pin1, gpio.HIGH)
    gpio.output(pin2, gpio.LOW)
    print("HIGH",pin1)
    time.sleep(pausetime)
    gpio.output(pin1, gpio.LOW)
    gpio.output(pin2, gpio.HIGH)
    print("HIGH",pin2)
    time.sleep(pausetime)

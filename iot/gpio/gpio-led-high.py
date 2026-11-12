import RPi.GPIO as gpio
import time

pin1=19
pin2=26

gpio.setmode(gpio.BCM)
gpio.setup(pin1, gpio.OUT)
gpio.setup(pin2, gpio.OUT)
gpio.output(pin1, gpio.HIGH)
gpio.output(pin2, gpio.HIGH)
print("HIGH",pin1," - ",pin2)

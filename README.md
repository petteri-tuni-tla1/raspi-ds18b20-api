# Introduction

Funny projects and ideas with raspberry PI

# GPIO - blinking LEDS

## iot/gpio

Short code to blink LEDS.
There are two leds in different GPIO-pins. Blinking alternated between the LEDS with some fixed delay time.

Further development:
* Add relay so that two sets of LEDs could be controlled - 
* Binary temperature "display with leds": 
  * one set of leds for +temperatures 
  * another set of leds for -temperatures
  * 5 GPIO-pins needed for leds (1-63 values)
  * 1 GPIO-pin for for relay.

## Hardware notices

Some resistor needed for the LEDs.
Shared GND for all.
Separate GPIO-pin for each + own resistor.
Example: 330 ohm

+5V -- R_330_Ohm -- LED -- GND

Yleesä ei kannata kytkeä kahta LEDiä rinnan yhden yhteisen vastuksen kanssa
Ongelma on, että LEDit eivät ole täysin samanlaisia. Toinen voi alkaa johtaa enemmän virtaa kuin toinen, jolloin se palaa kirkkaammin ja voi kuormittua liikaa.

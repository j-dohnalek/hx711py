"""Test script

Simple tests to see if the HX711 class is working properly.
Change DOUT and SCK to match the pins on your raspberry pi.
"""

import RPi.GPIO as GPIO
from hx711 import HX711


GPIO.setmode(GPIO.BCM)

print("Initializing HX711")
hx = HX711(2, 3, gain=64)
offset = hx.read_average()
hx.set_offset(offset)
print("Place something with a known weight on the scale.")
r = input("Press enter when ready.")
rawRead = hx.read()
print(rawRead)
weightOnScale = input("Enter weight on scale in grams: ")
scale = rawRead/weightOnScale
hx.set_scale(scale)
adjustedWeight = hx.get_grams()
print("Weight: {}g, verify that the measured weight is correct."
      .format(adjustedWeight))
print("Provided the above result is correct the following can be used"
      " in your main program:")
print("Offset: {}".format(offset))
print("Scale: {}".format(scale))
print("Test complete. Exiting.")
GPIO.cleanup()

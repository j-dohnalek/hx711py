"""
HX711 Load cell amplifier Python Library
Original source: https://gist.github.com/underdoeg/98a38b54f889fce2b237
Documentation source: https://github.com/aguegu/ardulibs/tree/master/hx711
Adapted by 2017 Jiri Dohnalek

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

ATTENTION:
This version runs in python 3.x (using python 2.7 will break it)
"""

import RPi.GPIO as GPIO
import time
import sys
from hx711 import HX711

# Make sure you correct these to the correct pins for DOUT and SCK.
hx = HX711(5, 6)


def cleanAndExit():
    print("Cleaning up...")
    GPIO.cleanup()
    print("Bye!")
    sys.exit()


def setup():
    """
    code run once
    """
    print("Initializing.\n Please ensure that the scale is empty.")
    scale_ready = False
    while not scale_ready:
        if (GPIO.input(hx.DOUT) == 0):
            scale_ready = False
        if (GPIO.input(hx.DOUT) == 1):
            print("Initialization complete!")
            scale_ready = True


def calibrate():
    readyCheck = input("Remove any items from scale. Press any key when ready.")
    offset = hx.read_average()
    print("Value at zero (offset): {}".format(offset))
    hx.set_offset(offset)
    print("Please place an item of known weight on the scale.")

    readyCheck = input("Press any key to continue when ready.")
    measured_weight = hx.read_average()
    item_weight = input("Please enter the item's weight in grams.\n>")
    scale = int(measured_weight)/int(item_weight)
    print("Scale adjusted for grams: {}".format(scale))


def loop():
    """
    code run continuously
    """
    try:
        val = hx.get_grams()
        hx.power_down()
        time.sleep(.001)
        hx.power_up()

        print("Item weighs {} grams.".format(val))
        prompt_handled = False
        while not prompt_handled:
            choice = input("Please choose:\n"
                           "[1] Recalibrate.\n"
                           "[2] Display offset and scale then continue.\n"
                           "[0] Clean and exit.\n>")
            if choice == "1":
                prompt_handled = True
                calibrate()
            if choice == "2":
                prompt_handled = False
                print("Offset: {}\nScale: {}\n".format(hx.get_offset(), hx.get_scale()))
            if choice == "0":
                prompt_handled = True
                cleanAndExit()
            if choice != ("0" or "1" or "2"):
                print("Invalid selection.\n")
                prompt_handled = False
    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()


##################################

if __name__ == "__main__":

    setup()
    calibrate()
    while True:
        loop()

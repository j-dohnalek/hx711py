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


##################
PYTHON 2.7 EXAMPLE

This version of example is python 2.7 compatible
and outputs weight in grams.

Make sure you enter the correct values for offset and scale!
Also, don't forget to set the correct gain, default is 128.
"""

import RPi.GPIO as GPIO
import time
import sys
from hx711 import HX711


hx = HX711(5, 6)


def cleanAndExit():
    print "Cleaning..."
    GPIO.cleanup()
    print "Bye!"
    sys.exit()


def setup():
    """
    code run once
    """
    hx.set_offset(`Place offset here`)
    hx.set_scale(`Place ratio here`)
    hx.tare()
    pass


def loop():
    """
    code run continuosly
    """

    try:
        val = hx.get_grams()
        print val

        hx.power_down()
        time.sleep(.001)
        hx.power_up()

        time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()


##################################

if __name__ == "__main__":

    setup()
    while True:
        loop()

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
    #hx.set_offset(24813)
    #hx.set_scale()
    #hx.tare()
    pass


def loop():
    """
    code run continuosly
    """

    try:
        val = hx.read_average()
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

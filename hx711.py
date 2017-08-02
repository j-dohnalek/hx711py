import RPi.GPIO as GPIO
import time
import sys

def createBoolList(size=8):
    ret = []
    for i in range(8):
        ret.append(False)
    return ret


class HX711:

    def __init__(self, dout, pd_sck, gain=128):
        GPIO.setmode(GPIO.BCM)

        self.PD_SCK = pd_sck
        self.DOUT = dout

        GPIO.setup(self.PD_SCK, GPIO.OUT)
        GPIO.setup(self.DOUT, GPIO.IN)

        self.GAIN = 0
        self.OFFSET = 0
        self.SCALE = 1
        self.lastVal = 0

        GPIO.output(self.PD_SCK, True)
        GPIO.output(self.PD_SCK, False)

        self.set_gain(gain);

    def is_ready(self):
        return GPIO.input(self.DOUT) == 0


    def set_gain(self, gain):
        if gain is 128:
            self.GAIN = 1
        elif gain is 64:
            self.GAIN = 3
        elif gain is 32:
            self.GAIN = 2

        GPIO.output(self.PD_SCK, False)
        

    def read(self):

        while not self.is_ready():
            pass

        count = 0
        for i in range(24):

            GPIO.output(self.PD_SCK, True)
            count = count << 1
            GPIO.output(self.PD_SCK, False)
            if(GPIO.input(self.DOUT)):
                count += 1

        return count ^ 0x800000



    def read_average(self, times=3):
        sum = 0
        for i in range(times):
            sum += self.read()
        return sum / times
        

    def get_value(self, times=3):
        return self.read_average(times) - self.OFFSET


    def get_units(self, times=3):
        return self.get_value(times) / self.SCALE


    def tare(self, times=15):
        sum = self.read_average(times)
        self.set_offset(sum)


    def set_scale(self, scale):
        self.SCALE = scale


    def set_offset(self, offset):
        self.OFFSET = offset


    def power_down(self):
        GPIO.output(self.PD_SCK, False)
        GPIO.output(self.PD_SCK, True)


    def power_up(self):
        GPIO.output(self.PD_SCK, False)


############# EXAMPLE

hx = HX711(5, 6)
hx.set_scale(24813)
hx.tare()

while True:
    try:
        val = hx.read_average()
        print val

        hx.power_down()
        time.sleep(.001)
        hx.power_up()

        time.sleep(2)

    except (KeyboardInterrupt, SystemExit):
        GPIO.cleanup()
        sys.exit()

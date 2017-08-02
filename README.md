# HX711PY
Python library for the HX711 load cell amplifier and Raspberry Pi

## Initial Calibration

1. Place nothing on the scale, run the calibration.py and record the output. That is the **offset**.
2. Place a known weight like 1kg(1000g) on the scale, record the output as **weight**.
3. Calculate the ratio
```
ratio = (w - offset) / 1000
```
*1000 being the 1000 grams or the weight previously placed on scale*

Edit the example.py file with the offset and ratio
```Python
def setup():
    """
    code run once
    """
    hx.set_offset(`Place offset here`)
    hx.set_scale(`Place ratio here`)
    hx.tare()
    pass
```

## Resources

Source code adapted from:<br>
https://gist.github.com/underdoeg/98a38b54f889fce2b237

Documentation adapted from:<br>
https://github.com/aguegu/ardulibs/tree/master/hx711

HX711 Datasheet (EN):<br>
http://image.dfrobot.com/image/data/SEN0160/hx711_english.pdf

"""This example uses the slide switch to control the little red LED."""
from adafruit_circuitplayground.express import cpx

while True:
    if cpx.switch:
        cpx.red_led = True
    else:
        cpx.red_led = False

# Can also be written as:
#    cpx.red_led = cpx.switch

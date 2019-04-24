"""This example shows using the shake_threshold argument with cpx.shake(). It turns on the little
red LED when a shake is detected."""
import time
from adafruit_circuitplayground.express import cpx

while True:
    # Lower shake_threshold means shake detection will trigger more easily!
    if cpx.shake(shake_threshold=20):
        print("Shake detected!")
        cpx.red_led = True
        time.sleep(0.1)
    else:
        cpx.red_led = False

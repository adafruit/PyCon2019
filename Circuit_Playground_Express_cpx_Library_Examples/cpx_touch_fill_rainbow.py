"""This example uses the capacitive touch pads on the CPX. They are located around the outer edge
of the board and are labeled A1-A7. (A0 is not a touch pad.) This example lights up all the
NeoPixels a different color of the rainbow for each pad touched!"""
import time
from adafruit_circuitplayground.express import cpx

cpx.pixels.brightness = 0.3

while True:
    if cpx.touch_A1:
        print("Touched A1!")
        cpx.pixels.fill((255, 0, 0))
    if cpx.touch_A2:
        print("Touched A2!")
        cpx.pixels.fill((210, 45, 0))
    if cpx.touch_A3:
        print("Touched A3!")
        cpx.pixels.fill((155, 100, 0))
    if cpx.touch_A4:
        print("Touched A4!")
        cpx.pixels.fill((0, 255, 0))
    if cpx.touch_A5:
        print("Touched A5!")
        cpx.pixels.fill((0, 135, 125))
    if cpx.touch_A6:
        print("Touched A6!")
        cpx.pixels.fill((0, 0, 255))
    if cpx.touch_A7:
        print("Touched A7!")
        cpx.pixels.fill((100, 0, 155))
    time.sleep(0.1)

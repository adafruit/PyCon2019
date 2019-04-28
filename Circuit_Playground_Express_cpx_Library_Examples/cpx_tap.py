"""This example prints to the serial console when you double-tap the CPX!"""
from adafruit_circuitplayground.express import cpx

# Set this to 1 to detect a single-tap!
cpx.detect_taps = 2

while True:
    if cpx.tapped:
        print("Tapped!")

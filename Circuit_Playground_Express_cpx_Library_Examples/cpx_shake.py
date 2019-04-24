"""This example prints to the serial console when you shake the board!"""
from adafruit_circuitplayground.express import cpx

while True:
    if cpx.shake():
        print("Shake detected!")

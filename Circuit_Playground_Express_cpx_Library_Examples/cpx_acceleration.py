"""This example uses the accelerometer in the center of the CPX. Try moving the board around to see
the values change!"""
import time
from adafruit_circuitplayground.express import cpx

while True:
    x, y, z = cpx.acceleration
    print((x, y, z))
    time.sleep(0.5)

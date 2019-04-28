"""This example requires a potentiometer. Talk to the team to get one!

Connect the blue clip on the potentiometer to pad A0.
Connect the black clip to a GND pad.
Connect the red clip to a 3.3v pad.

THIS EXAMPLE REQUIRES A SEPARATE LIBRARY BE LOADED ONTO YOUR CIRCUITPY DRIVE.
This example requires the simpleio.mpy library.

Rotate the potentiometer knob to see the number of NeoPixels lit up on your CPX change!"""
import time
import board
import analogio
import simpleio
from adafruit_circuitplayground.express import cpx

cpx.pixels.auto_write = False
cpx.pixels.brightness = 0.3
potentiometer = analogio.AnalogIn(board.A0)


def get_voltage(pin):
    return (pin.value * 3.3) / 65536


while True:
    # Potentiometer voltage value remapped to pixel position
    cpx_peak = simpleio.map_range(get_voltage(potentiometer), 0, 3.3, 0, 10)

    for i in range(0, 10, 1):
        if i <= cpx_peak:
            cpx.pixels[i] = (0, 255, 255)
        else:
            cpx.pixels[i] = (0, 0, 0)
    cpx.pixels.show()
    time.sleep(0.05)

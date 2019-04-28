"""This example requires a potentiometer and a NeoPixel strip. Talk to the team to get one of each!

Connect the blue clip on the potentiometer to pad A0.
Connect the black clip to a GND pad.
Connect the red clip to a 3.3v pad.

Connect the white clip on the NeoPixel strip to pad A7.
Connect the black clip on the NeoPixel strip to a GND pad.
Connect the red clip on the NeoPixel strip to the VOUT pad.

THIS EXAMPLE REQUIRES A SEPARATE LIBRARY BE LOADED ONTO YOUR CIRCUITPY DRIVE.
This example requires the simpleio.mpy library.

Rotate the potentiometer knob to watch the number of pixels lit up on the strip change!"""
import time
import board
import simpleio
import analogio
import neopixel

strip = neopixel.NeoPixel(board.A7, 30, auto_write=False)
strip.brightness = 0.3
potentiometer = analogio.AnalogIn(board.A0)


def get_voltage(pin):
    return (pin.value * 3.3) / 65536


while True:
    # Potentiometer voltage value remapped to pixel position
    strip_peak = simpleio.map_range(get_voltage(potentiometer), 0, 3.3, 0, 30)

    for j in range(0, 30, 1):
        if j <= strip_peak:
            strip[j] = (0, 255, 255)
        else:
            strip[j] = (0, 0, 0)

    strip.show()
    time.sleep(0.05)

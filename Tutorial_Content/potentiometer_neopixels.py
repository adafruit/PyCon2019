"""This example uses the potentiometer and the alligator clips from the Adafruit lunchbox kit.

With the potentiometer upright and facing towards you, use the alligator clips to:
Connect the LEFT PIN on the potentiometer to a GND pad on the CPX.
Connect the MIDDLE PIN on the potentiometer to pad A0 on the CPX.
Connect the RIGHT PIN on the potentiometer to a 3.3v pad on the CPX.

Rotate the potentiometer knob to see the number of NeoPixels lit up on your CPX change!"""
import time
import board
import analogio
from adafruit_circuitplayground.express import cpx

cpx.pixels.auto_write = False
cpx.pixels.brightness = 0.3
potentiometer = analogio.AnalogIn(board.A0)


def get_voltage(pin):
    return (pin.value * 3.3) / 65536


while True:
    # Potentiometer voltage value remapped to pixel position
    peak = get_voltage(potentiometer) * 10 / 3.3

    for i in range(0, 10, 1):
        if i <= peak:
            cpx.pixels[i] = (0, 255, 255)
        else:
            cpx.pixels[i] = (0, 0, 0)
    cpx.pixels.show()
    time.sleep(0.05)

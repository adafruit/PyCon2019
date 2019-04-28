"""This example lights up and pulses the NeoPixels on your CPX in Python colours, like the logo!
Thank you to Nicholas Tollervy for this lovely example!"""
from adafruit_circuitplayground.express import cpx

# Set this as a float from 0 to 1 to change the brightness. The decimal represents a percentage.
# So, 0.3 means 30% brightness!
cpx.pixels.brightness = 0.3

# Changes to NeoPixel state will not happen without explicitly calling show()
cpx.pixels.auto_write = False

# Python colours: blue and yellow!
python_colors = ((32, 64, 255), (255, 180, 20))
# Fade offset for Python colours
fade_offset = 0
# Fade flag
fade_out = True

while True:
    for pixel in range(10):
        if pixel < 4 or pixel == 9:  # Blue pixel range
            colour = [max(0, colours - fade_offset) for colours in python_colors[0]]
        else:  # Yellow pixel range
            colour = [max(0, colours - fade_offset) for colours in python_colors[1]]
        cpx.pixels[pixel] = tuple(colour)
    if fade_out:
        fade_offset += 3
    else:
        fade_offset -= 3
    if fade_offset > 100 or fade_offset == 0:
        fade_out = not fade_out
    cpx.pixels.show()

"""For a detailed guide on all the features of the Circuit Playground Express (cpx) library:
https://adafru.it/cp-made-easy-on-cpx"""
import time
import microcontroller
from adafruit_circuitplayground.express import cpx

# Set TONE_PIANO to True to enable a tone piano on the touch pads!
TONE_PIANO = False

# Set this as a float from 0 to 1 to change the brightness. The decimal represents a percentage.
# So, 0.3 means 30% brightness!
cpx.pixels.brightness = 0.3

# Changes to NeoPixel state will not happen without explicitly calling show()
cpx.pixels.auto_write = False

# Startup behavior is based on your board's unique ID!
# uid returns a bytearray. The individual numbers are summed then modulo by 3.
board_id = sum(microcontroller.cpu.uid) % 3


def color_wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition red - green - blue - back to red.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (int(255 - pos*3), int(pos*3), 0)
    if pos < 170:
        pos -= 85
        return (0, int(255 - pos*3), int(pos*3))
    pos -= 170
    return (int(pos * 3), 0, int(255 - (pos*3)))


# Digi-Key colors: red and white!
digi_key_colors = ((255, 0, 0), (180, 180, 150))
# Python colors: blue and yellow!
python_colors = ((32, 64, 255), (255, 180, 20))

color_index = 0
pixel_number = 0
# time.monotonic() allows for non-blocking LED animations!
start = time.monotonic()
while True:
    now = time.monotonic()
    if board_id == 0:
        # Flash Digi-Key colors!
        if now - start > 0.5:
            color_index = (color_index + 1) % len(digi_key_colors)
            cpx.pixels.fill(digi_key_colors[color_index])
            cpx.pixels.show()
            start = now
    elif board_id == 1:
        # Flash Python colors!
        if now - start > 0.5:
            color_index = (color_index + 1) % len(python_colors)
            cpx.pixels.fill(python_colors[color_index])
            cpx.pixels.show()
            start = now
    elif board_id == 2:
        # Red-comet rainbow swirl!
        pixel_number = (pixel_number + 1) % 10
        for p in range(10):
            color = color_wheel(25 * ((pixel_number + p) % 10))
            cpx.pixels[p] = tuple([int(c * (10 - (pixel_number + p) % 10) / 10.0) for c in color])
            cpx.pixels.show()

    # If the switch is to the left, it returns True!
    cpx.red_led = cpx.switch

    # Press the buttons to play sounds!
    if cpx.button_a:
        cpx.play_file("drama.wav")
    elif cpx.button_b:
        cpx.play_file("low_fade.wav")

    # Set TONE_PIANO to True above to enable a tone piano on the touch pads!
    if TONE_PIANO:
        if cpx.touch_A1:
            cpx.start_tone(262)
        elif cpx.touch_A2:
            cpx.start_tone(294)
        elif cpx.touch_A3:
            cpx.start_tone(330)
        elif cpx.touch_A4:
            cpx.start_tone(349)
        elif cpx.touch_A5:
            cpx.start_tone(392)
        elif cpx.touch_A6:
            cpx.start_tone(440)
        elif cpx.touch_A7:
            cpx.start_tone(494)
        else:
            cpx.stop_tone()

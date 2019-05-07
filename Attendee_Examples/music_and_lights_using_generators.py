from random import randrange
from time import monotonic as now
from adafruit_circuitplayground.express import cpx

cpx.detect_taps = 2
cpx.pixels.brightness = 0.01
BLACK = (0, 0, 0)

def sleep(delay):
    start = now()
    while start + delay > now():
        yield

def leds_off():
    for i in range(len(cpx.pixels)):
        cpx.pixels[i] = BLACK

def gated(bool_func, off_func = None, *, switch = False, on = False):
    if switch:
        condition = lambda on: on != bool_func()
    else:
        condition = lambda on: bool_func()

    def outer(generator):
        iterator = generator()
        def inner():
            while True:
                yield
                if condition(on):
                    on = not on
                    if not on:
                        off_func()
                    yield from sleep(0.3)
                if on:
                    next(iterator)
        return inner
    return outer

@gated((lambda: cpx.button_a), leds_off)
def color_pixels():
    while True:
        for i, color in enumerate(cpx.pixels):
            yield from sleep(0.1)
            if color == BLACK:
                color = randrange(256), randrange(256), randrange(256)
                maxval = max(color)
                color = tuple(int((value / maxval) * 255) for value in color)
                cpx.pixels[i] = color
            else:
                cpx.pixels[i] = BLACK

@gated((lambda: cpx.button_b), cpx.stop_tone)
def play_sounds():
    # A Minor Pentatonic
    tones = [587, 523, 440, 392, 330, 294, 262]
    for i in range(1, 8):
        cpx._touch(i)   
    prev = 0
    touched = True

    while True:
        yield
        for i, touch in enumerate(cpx._touches[1:]):
            if touch.value:
                if not (i == prev and touched):
                    prev = i
                    cpx.stop_tone()
                cpx.start_tone(tones[i])
                touched = True
                break
        else:
            touched = False

# shake is too slow, so use tap instead.
def flash_on_double_tap():
    while True:
        if cpx.tapped:
            for _ in range(3):
                cpx.red_led = True
                yield from sleep(0.2)
                cpx.red_led = False
                yield from sleep(0.1)
        yield from sleep(0.2)

def main(*generators):
    iterators = [generator() for generator in generators]
    while True:
        for iterator in iterators:
            next(iterator)

main(play_sounds, color_pixels, flash_on_double_tap)
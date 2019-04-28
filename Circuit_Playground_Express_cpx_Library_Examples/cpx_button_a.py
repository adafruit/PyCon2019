"""This example turns on the little red LED when button A is pressed."""
from adafruit_circuitplayground.express import cpx

while True:
    if cpx.button_a:
        print("Button A pressed!")
        cpx.red_led = True

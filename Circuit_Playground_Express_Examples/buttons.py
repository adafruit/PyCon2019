"""This example turns the little red LED on if you press button A and turns it off if you press
button B!"""
import time
import board
import digitalio

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

button_a = digitalio.DigitalInOut(board.BUTTON_A)
button_a.direction = digitalio.Direction.INPUT
button_a.pull = digitalio.Pull.DOWN

button_b = digitalio.DigitalInOut(board.BUTTON_B)
button_b.direction = digitalio.Direction.INPUT
button_b.pull = digitalio.Pull.DOWN

while True:
    if button_a.value:  # Button A is pressed
        led.value = True
    elif button_b.value:  # Button B is pressed
        led.value = False
    time.sleep(0.01)

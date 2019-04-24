"""This example turns the little red LED on and off as you move the slide switch left and right!"""
import board
import digitalio

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

switch = digitalio.DigitalInOut(board.SLIDE_SWITCH)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

while True:
    if switch.value:
        led.value = True
    else:
        led.value = False

    # Can also be written as:
    # led.value = switch.value

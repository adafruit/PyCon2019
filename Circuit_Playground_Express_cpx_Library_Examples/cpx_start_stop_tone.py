"""This example plays a tone while you're pressing a button! It is a different tone for each button
pressed, and it plays for the duration of the button press."""
from adafruit_circuitplayground.express import cpx

while True:
    if cpx.button_a:
        cpx.start_tone(262)
    elif cpx.button_b:
        cpx.start_tone(294)
    else:
        cpx.stop_tone()

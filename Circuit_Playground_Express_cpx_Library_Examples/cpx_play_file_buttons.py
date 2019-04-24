"""THIS EXAMPLE REQUIRES A WAV FILE FROM THE ADDITIONAL_CONTENT FOLDER IN THE PyCon2019 REPO!
Copy the "dip.wav" and "rise.wav" files to your CIRCUITPY drive.

Once the files are copied, this example plays a different wav file for each button pressed!"""
from adafruit_circuitplayground.express import cpx

while True:
    if cpx.button_a:
        cpx.play_file("dip.wav")
    if cpx.button_b:
        cpx.play_file("rise.wav")

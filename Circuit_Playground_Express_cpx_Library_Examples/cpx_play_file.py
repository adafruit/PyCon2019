"""THIS EXAMPLE REQUIRES A WAV FILE FROM THE ADDITIONAL_CONTENT FOLDER IN THE PyCon2019 REPO!
Copy the "dip.wav" file to your CIRCUITPY drive.

Once the file is copied, this example plays a wav file!"""
from adafruit_circuitplayground.express import cpx

cpx.play_file("dip.wav")

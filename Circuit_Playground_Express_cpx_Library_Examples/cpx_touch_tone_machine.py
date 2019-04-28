"""This example requires seven wav files from the Additional_Content folder on the PyCon2019 GitHub
repo. Download the files and copy them to your CIRCUITPY drive. Once copied, try touching the touch
pads on A1-A7 to hear a funky scale of notes!"""
import time
from adafruit_circuitplayground.express import cpx

while True:
    if cpx.touch_A1:
        print("Touched A1!")
        cpx.play_file("square_Do.wav")
    if cpx.touch_A2:
        print("Touched A2!")
        cpx.play_file("square_Re.wav")
    if cpx.touch_A3:
        print("Touched A3!")
        cpx.play_file("square_Mi.wav")
    if cpx.touch_A4:
        print("Touched A4!")
        cpx.play_file("square_Fa.wav")
    if cpx.touch_A5:
        print("Touched A5!")
        cpx.play_file("square_Sol.wav")
    if cpx.touch_A6:
        print("Touched A6!")
        cpx.play_file("square_La.wav")
    if cpx.touch_A7:
        print("Touched A7!")
        cpx.play_file("square_Ti.wav")
    time.sleep(0.1)

"""This example requires a servo. Talk to the team to get one!

Connect the blue clip (on the yellow wire) on the servo to pad A1.
Connect the black clip (on the brown wire) on the servo to a GND pad.
Connect the red clip (on the red wire) on the servo to a 3.3v pad.

THIS EXAMPLE REQUIRES A SEPARATE LIBRARY BE LOADED ONTO YOUR CIRCUITPY DRIVE.
This example requires the adafruit_motor library.

Press the buttons to watch the servo rotate!"""
import board
import pwmio
from adafruit_motor import servo
from adafruit_circuitplayground.express import cpx

pwm = pwmio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)
servo = servo.Servo(pwm)

while True:
    if cpx.button_a:
        servo.angle = 180
    elif cpx.button_b:
        servo.angle = 0

"""Connect the blue clip (yellow wire) on the servo to A1.
Connect the black clip (brown wire) on the servo to a GND pad.
Connect the red clip (red wire) on the servo to a 3.3v pad.

THIS EXAMPLE REQUIRES A SEPARATE LIBRARY BE LOADED ONTO YOUR CIRCUITPY DRIVE.
This example requires the adafruit_motor.mpy library.

Press the buttons to watch the servo rotate!"""
import board
import pulseio
from adafruit_motor import servo
from adafruit_circuitplayground.express import cpx

pwm = pulseio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)
servo = servo.Servo(pwm)

while True:
    if cpx.button_a:
        servo.angle = 180
    elif cpx.button_b:
        servo.angle = 0

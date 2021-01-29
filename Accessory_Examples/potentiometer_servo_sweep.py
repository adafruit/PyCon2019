"""This example requires a potentiometer and a servo. Talk to the team to get one of each!

Connect the blue clip on the potentiometer to pad A0.
Connect the red clip on the potentiometer to a 3.3v pad.
Connect the black clip on the potentiometer to a GND pad.

Connect the blue clip (on the yellow wire) on the servo to pad A1.
Connect the black clip (on the brown wire) on the servo to a GND pad.
Connect the red clip (on the red wire) on the servo to a 3.3v pad.

THIS EXAMPLE REQUIRES A SEPARATE LIBRARY BE LOADED ONTO YOUR CIRCUITPY DRIVE.
This example requires the simpleio.mpy AND adafruit_motor libraries.

Rotate the potentiometer knob to watch the servo rotate!"""
import board
import simpleio
import analogio
import pwmio
from adafruit_motor import servo

potentiometer = analogio.AnalogIn(board.A0)
pwm = pwmio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)
servo = servo.Servo(pwm)


def get_voltage(pin):
    return (pin.value * 3.3) / 65536


while True:
    # Potentiometer voltage value remapped to servo angle
    servo_sweep = simpleio.map_range(get_voltage(potentiometer), 0, 3.3, 0, 180)
    servo.angle = servo_sweep

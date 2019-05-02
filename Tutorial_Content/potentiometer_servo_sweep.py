"""This example uses, from the Adabox 006 lunchbox kit:
 * the potentiometer
 * the alligator clips (clips on both ends)
 * the servo
 * the alligator-to-jumper-wire clips (clips on one end, a pin on the other end)

With the potentiometer upright and facing towards you, use the alligator clips to:
Connect the LEFT PIN on the potentiometer to a GND pad on the CPX.
Connect the MIDDLE PIN on the potentiometer to pad A0 on the CPX.
Connect the RIGHT PIN on the potentiometer to a 3.3v pad on the CPX.

Using the alligator-to-jumper-wire clips:
Place a clip on the yellow wire on the servo, and connect it to pad A1 on the CPX.
Place a clip on the brown wire on the servo, and connect it to a GND pad on the CPX.
Place a clip on the red wire on the servo, and connect it to a 3.3v pad on the CPX.

THIS EXAMPLE REQUIRES A SEPARATE LIBRARY BE LOADED ONTO YOUR CIRCUITPY DRIVE.
This example requires the adafruit_motor library.

Rotate the potentiometer knob to watch the servo rotate!"""
import board
import analogio
import pulseio
from adafruit_motor import servo

potentiometer = analogio.AnalogIn(board.A0)
pwm = pulseio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)
servo = servo.Servo(pwm)


def get_voltage(pin):
    return (pin.value * 3.3) / 65536


while True:
    # Potentiometer voltage value remapped to servo angle
    servo_sweep = get_voltage(potentiometer) * 180 / 3.3
    servo.angle = servo_sweep

"""This example uses the temperature sensor on the CPX, located next to the image of a thermometer
on the board. It prints the temperature in both C and F to the serial console. Try putting your
finger over the sensor to see the numbers change!"""
import time
from adafruit_circuitplayground.express import cpx

while True:
    print("Temperature C:", cpx.temperature)
    print("Temperature F:", cpx.temperature * 1.8 + 32)
    time.sleep(1)

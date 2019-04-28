"""This example uses the temperature sensor, located next to the picture of a thermometer on the
CPX. It prints the temperature """
import time
import board
import adafruit_thermistor

thermistor = adafruit_thermistor.Thermistor(board.TEMPERATURE, 10000, 10000, 25, 3950)

while True:
    temperature_c = thermistor.temperature
    temperature_f = thermistor.temperature * 9 / 5 + 32
    print("Temperature is: %f C and %f F" % (temperature_c, temperature_f))
    time.sleep(0.25)

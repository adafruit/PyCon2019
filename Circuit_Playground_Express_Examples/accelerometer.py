"""This example uses the accelerometer in the center of the CPX. Try moving the board around to see
the values change!"""
import time
import board
import digitalio
import busio
import adafruit_lis3dh

i2c = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)
int1 = digitalio.DigitalInOut(board.ACCELEROMETER_INTERRUPT)
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, address=0x19, int1=int1)

# Loop forever printing accelerometer values
while True:
    x, y, z = lis3dh.acceleration
    print(x, y, z)
    time.sleep(0.1)

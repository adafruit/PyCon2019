"""This example turns on, or "fills", all the NeoPixels red!"""
from adafruit_circuitplayground.express import cpx

while True:
    cpx.pixels.fill((50, 0, 0))

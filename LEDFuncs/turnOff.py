import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 30)

while True:
    pixels[0] = (0,0,0)

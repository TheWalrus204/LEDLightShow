import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 30)

while True:
    pixels.fill((0, 0, 0))
    pixels.fill((255, 0, 0))


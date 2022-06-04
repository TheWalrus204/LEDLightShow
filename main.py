import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 30)

pixels[0] = (255,0,0)
time.sleep(3)
pixels[0] = (0,0,0)

import board
import neopixel
import time
import random

num_pixels = 10
BRIGHTNESS = 0.5
np = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=BRIGHTNESS, auto_write=False)

def sparkle(color, delay=0.1, loop=4):

    np.fill(color)
    np.show()
    time.sleep(delay)

    color = [255, 60, 0]

    for i in range(loop):
        np[random.randint(0, 9)] = color
    np.show()
    time.sleep(delay)

while True:
    for i in range(10):
        sparkle((255, 115, 0))



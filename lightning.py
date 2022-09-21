import board
import time
import neopixel
import random

num_pixels = 10
np = neopixel.NeoPixel(board.NEOPIXEL, num_pixels, brightness=1.0, auto_write=False)

def constrain(low, high, value):
    if value < low:
        return low
    if value > high:
        return high
    return value

np.fill((255, 127, 0))
np.show()

'''
Function: Fire
Description: Creates a flame effect on a strip of neopixels
Parameters: background: base color for flame, foreground: color used to flash / highlight
return value: none
'''
def fire(background, foreground):
    for j in range(45):
        intensity = random.random() * 0.7 + 0.3
        i_background = [int(i * intensity) for i in background]
        np.fill(i_background)
        for i in range(random.randint(2, int(num_pixels/5))):
            intensity = random.random() * 0.7 + 0.3
            i_foreground = [int(i * intensity) for i in foreground]
            np[random.randint(0, num_pixels-1)] = i_foreground
        np.show()
        time.sleep(0.06)


def light(back, fore):
    ran = random.random()/20
    for j in range(10):
        intense = random.random() * 0.7 + 0.3
        i_back = [int(i * intense) for i in back]
        np.fill(i_back)
        for i in range(random.randint(2, int(num_pixels/5))):
            intense = random.random() * 0.7 + 0.3
            i_fore = [int(i * intense) for i in fore]
            np[random.randint(0, num_pixels-1)] = i_fore
        np.show()
        time.sleep(ran)
while True:
    fire((34, 2, 56), (104, 52, 139))
    light((255, 255, 255), (255, 255, 255))

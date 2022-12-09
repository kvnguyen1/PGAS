import time
import board
import neopixel
import random
import adafruit_hcsr04

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.A7, echo_pin=board.A6)

BRIGHTNESS = .25
num_pixels = 30
np = neopixel.NeoPixel(board.A1, num_pixels, brightness=BRIGHTNESS, auto_write=False)

def sensor():
    np.fill([0, 0, 0])
    the_range = 30 - (sonar.distance/5)
    for i in range(int(the_range)):
        if the_range >= 0 and the_range <= 10:
            np[i] = [255, 10, 60]
        if the_range >= 11 and the_range <= 20:
            np[i] = [255, 10, 60]
        if the_range >= 21 and the_range <= 29:
            np[i] = [255, 10, 60]
    np.show()
    time.sleep(0.01)

while True:
    try:
        sensor()
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)

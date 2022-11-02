#imports libraries
import neopixel
import board
import time
import random
import digitalio as dio
import touchio

# defines neopixel
BRIGHTNESS = 0.25
np = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=BRIGHTNESS, auto_write=False)

# defines the buttons and touch pads
button_a = dio.DigitalInOut(board.BUTTON_A)
button_a.direction = dio.Direction.INPUT
button_a.pull = dio.Pull.DOWN
touch1 = touchio.TouchIn(board.A1)
touch2 = touchio.TouchIn(board.A2)
touch3 = touchio.TouchIn(board.A5)
touch4 = touchio.TouchIn(board.A6)

# defines rgb values
red = [255, 0, 0]
blue = [0, 0, 255]
green = [0, 255, 0]
yellow = [236, 236, 0]
black = [0, 0, 0]

# defines the game list and boolean values
game_list = []
game_stat = False
buttons = False
compare = 0

"""
Function name: flashing
Description: it flashes the input color twice
Parameters: color - tuple(flashes the rgb), delay - floating point (the delay time)
Return value: none
"""
def flashing(color, delay):
  for i in range(2):
      np.fill(color)
      np.show()
      time.sleep(delay)
      np.fill(black)
      np.show()
      time.sleep(delay)

"""
Function name: make_sequence
Description: creates the sequence randomly (uses numbers)
Parameters: list_game - list (the list that holds all the values)
Return value: none
"""
def make_sequence(list_game):
  global starting
  starting = 1
  number = random.randint(0, 3)
  list_game.append(number)

"""
Function name: show_sequence
Description: assigns a rgb color to a number and shows the sequence by flashing the colors in the list
Parameters: num - int (value from list), delay - floating point (delay time)
Return value: none
"""
def show_sequence(num, delay):
  if num == 0:
      np[5] = green
      np[6] = green
      np.show()
      time.sleep(delay)
      np[5] = black
      np[6] = black
      np.show()
      time.sleep(delay)
  if num == 1:
      np[8] = blue
      np[9] = blue
      np.show()
      time.sleep(delay)
      np[8] = black
      np[9] = black
      np.show()
      time.sleep(delay)
  if num == 2:
      np[0] = red
      np[1] = red
      np.show()
      time.sleep(delay)
      np[0] = black
      np[1] = black
      np.show()
      time.sleep(delay)
  if num == 3:
      np[3] = yellow
      np[4] = yellow
      np.show()
      time.sleep(delay)
      np[3] = black
      np[4] = black
      np.show()
      time.sleep(delay)
  time.sleep(delay * 2)

"""
Function name: check_sequence
Description: checks the sequence by checking the compare value to the index
Parameters: comp_val - int (the compare value), index - int (the index from the game list)
Return value: True or False
"""
def check_sequence(comp_val, index):
  if comp_val == index:
      return True
  else:
      return False
  time.sleep(0.25)

"""
Function name: user_input
Description: Takes in user input and flashes the rgb value, sets the compare value, and checks check_sequence. 
Parameters: delay - floating point (delay time)
"""
def user_input(delay):
  global compare
  global value_sent
  for i in range(len(game_list)):
      while (touch1.value or touch2.value or touch3.value or touch4.value) == False:
          pass
      if touch1.value == True:
          np[5] = green
          np[6] = green
          np.show()
          time.sleep(delay)
          np[5] = black
          np[6] = black
          np.show()
          time.sleep(delay)
          compare = 0
      if touch2.value == True:
          np[8] = blue
          np[9] = blue
          np.show()
          time.sleep(delay)
          np[8] = black
          np[9] = black
          np.show()
          time.sleep(delay)
          compare = 1
      if touch3.value == True:
          np[0] = red
          np[1] = red
          np.show()
          time.sleep(delay)
          np[0] = black
          np[1] = black
          np.show()
          time.sleep(delay)
          compare = 2
      if touch4.value == True:
          np[3] = yellow
          np[4] = yellow
          np.show()
          time.sleep(delay)
          np[3] = black
          np[4] = black
          np.show()
          time.sleep(delay)
          compare = 3    
      value_sent = check_sequence(compare, game_list[i])
      if not value_sent == True:
          flashing(red, 0.1)
          reset()
          return

"""
Function name: reset
Description: resets the game by giving it an empty list and setting the status to false
Parameters: none
Return value: none
"""
def reset():
  global game_list, game_stat
  game_list = []
  game_stat = False

"""
Function name: the_game
Description: creates the game by calling the other functions
Parameters: none
Return value: none
"""
def the_game():
  global game_list
  make_sequence(game_list)
  flashing(green, 0.1)
  time.sleep(1)
  for i in range(len(game_list)):
      show_sequence(game_list[i], 0.25)
  user_input(0.40)

# displays the loop of the game
while True:
  time.sleep(0.01)
  if not game_stat:
      if button_a.value:
          buttons = not buttons
          time.sleep(0.05)
          game_stat = True
  else:
      the_game()

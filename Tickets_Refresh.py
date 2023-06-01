#! usr/bin/env/ python3

from pyautogui import *
import pyautogui
import time
import pynput
from pynput.mouse import Button
from pynput.keyboard import Key
import numpy as np
import random



keyboard = pynput.keyboard.Controller()
mouse    = pynput.mouse.Controller()

# Keyboard Functions

def on_press(key):
    print('pressed:', key)
    if str(key) == "'q'":  # it has to be with `' '` inside `" "`
        # Stop listener
        print("exit listener")
        return False  # `False` ends listener
    
# Mouse Functions

def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))



#Main Functions

def Check_for_tickets():
    print(mouse.position)
    #mouse.position = (1224, 445)
    print(mouse.position)
    mouse.press(Button.left)
    time.sleep(.01)
    mouse.release(Button.left)
    
    


def main():
    time.sleep(5)

    #with pynput.keyboard.Listener(on_press=on_press) as keyboard_listener:
        #while keyboard_listener.is_alive():
            #time.sleep(1)
            #print('alive')

    #with pynput.mouse.Listener(on_click=on_click, on_move=on_move, on_scroll=on_scroll) as mouse_listener:
        #while mouse_listener.is_alive():
            #time.sleep(10)
            #print('alive')

    Check_for_tickets()


if __name__ == "__main__":
    main()

    


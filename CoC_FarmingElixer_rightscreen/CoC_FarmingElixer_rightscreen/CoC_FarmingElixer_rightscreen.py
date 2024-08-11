#!usr/bin/env/python3

from ast import If, While
from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api, win32con

time.sleep(5)

def click(x,y):
  win32api.SetCursorPos((x,y))
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
  time.sleep(0.2)
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
 
def click_hold(x,y,sec):
  win32api.SetCursorPos((x,y))
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
  time.sleep(sec)
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
  
def pan_page_up():
  win32api.SetCursorPos((1954,486))
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
  time.sleep(0.1)
  win32api.SetCursorPos((1954,803))
  time.sleep(1)
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
  time.sleep(.5)
  
def elixir_match():
  click(140,1300) #Attack
  time.sleep(1)
  click(1890,945) #Find Now
  time.sleep(4)
  click(953,1312) #Select cannon cart
  time.sleep(1)
  click(1982,1073)#Place cart down
  time.sleep(1)
  click(149,1072) #Surrender
  time.sleep(1)
  click(1511,893) #Confirm Surrender
  time.sleep(1)
  click(1280,1213)#Return Home
  time.sleep(3)
  pan_page_up() #move up
  
def gold_match():
  click(140,1300) #Attack
  time.sleep(1)
  click(1890,945) #Find Now
  time.sleep(4)
  i = 0
  while i < 8: #Deploy troops
    x = (i*170)+430
    click(x,1328)
    click(1982,1073)
    time.sleep(1)
    i += 1
  time.sleep(105)
  if pyautogui.locateOnScreen('return_home.png', grayscale=False, confidence=0.8) == None:
    i = 0
    while i < 8: #Deploy troops
      x = (i*170)+430
      click(x,1328)
      click(1982,1073)
      time.sleep(1)
      i += 1
    time.sleep(60)
  click(149,1072) #Surrender
  time.sleep(1)
  click(1511,893) #Confirm Surrender
  time.sleep(1)
  click(1280,1213)#Return Home
  time.sleep(3)
  pan_page_up() #move up


def run_gold_match():
  gold_match()
  Elixir_cart = pyautogui.locateOnScreen('Elixir_cart.png', grayscale=False, confidence=0.9)
  Elixir_cart2 = pyautogui.locateOnScreen('Elixir_cart2.png', grayscale=False, confidence=0.9)
  if Elixir_cart != None:
    Elixir_cartx, Elixir_carty = pyautogui.center(Elixir_cart)
    time.sleep(0.1)
    click(Elixir_cartx, Elixir_carty)
    time.sleep(1)
    click(1889,1215)
    time.sleep(1)
    click(2143,141)
    time.sleep(1)
  if Elixir_cart2 != None:
    Elixir_cart2x, Elixir_cart2y = pyautogui.center(Elixir_cart2)
    time.sleep(0.1)
    click(Elixir_cart2x, Elixir_cart2y)
    time.sleep(1)
    click(1889,1215)
    time.sleep(1)
    click(2143,141)
    time.sleep(1)
    
def run_elixir_match():
  elixir_match()
  Elixir_cart = pyautogui.locateOnScreen('Elixir_cart.png', grayscale=False, confidence=0.9)
  Elixir_cart2 = pyautogui.locateOnScreen('Elixir_cart2.png', grayscale=False, confidence=0.9)
  if Elixir_cart != None:
    Elixir_cartx, Elixir_carty = pyautogui.center(Elixir_cart)
    time.sleep(0.1)
    click(Elixir_cartx, Elixir_carty)
    time.sleep(1)
    click(1889,1215)
    time.sleep(1)
    click(2143,141)
    time.sleep(1)
  if Elixir_cart2 != None:
    Elixir_cart2x, Elixir_cart2y = pyautogui.center(Elixir_cart2)
    time.sleep(0.1)
    click(Elixir_cart2x, Elixir_cart2y)
    time.sleep(1)
    click(1889,1215)
    time.sleep(1)
    click(2143,141)
    time.sleep(1)

def main():
  while keyboard.is_pressed('q') == False:
    i = 0
    while keyboard.is_pressed('q') == False and i < 1:
      i += 1
      run_gold_match()
    i = 0
    while keyboard.is_pressed('q') == False and i < 4:
      i += 1
      run_elixir_match()
    
 

if __name__ == "__main__":
  main()
    


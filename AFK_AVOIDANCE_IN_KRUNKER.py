import pyautogui as pag 
import random 
import time

while True:
    x_coordinate = random.randint(600,700)
    y_coordinate = random.randint(200,700)
    pag.moveTo(x_coordinate,y_coordinate,0.8)
    pag.click()
    time.sleep(4)

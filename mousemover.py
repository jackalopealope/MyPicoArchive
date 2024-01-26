import os
try:
    import pyautogui
except:
    os.system("pip install pyautogui")
    import pyautogui
try:
    import keyboard
except:
    os.system("pip install keyboard")
    import keyboard
import random
import time

def randmouse():
    # Move the mouse cursor randomly
    x_offset = random.randint(-250, 250)
    y_offset = random.randint(-250, 250)
    pyautogui.moveRel(x_offset, y_offset, duration=0.25)
    time.sleep(0.1)  # 1 second delay

for i in range(10000000):
    if keyboard.is_pressed('e'):
        if keyboard.is_pressed('n'):
            if keyboard.is_pressed('d'):
                break

            else:
                  randmouse()
        else:
              randmouse()
    else:
          randmouse()
            
    

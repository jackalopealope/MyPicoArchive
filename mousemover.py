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
    x_offset = random.randint(-250, 250)
    y_offset = random.randint(-250, 250)

    # Limit the mouse movement within the screen boundaries
    x, y = pyautogui.position()
    new_x = max(0, min(pyautogui.size().width - 1, x + x_offset))
    new_y = max(0, min(pyautogui.size().height - 1, y + y_offset))

    pyautogui.moveTo(new_x, new_y, duration=0.25)
    time.sleep(0.1)


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
            
    

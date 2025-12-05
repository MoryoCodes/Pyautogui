import time
import pyautogui
import keyboard

keyboard.wait("space")
print(pyautogui.pixel(645,500)) 

while True:
    if pyautogui.pixel(645,599) == (75, 219, 106):
        time.sleep(0.001)
        pyautogui.click()
        time.sleep(10 )
        print("green")
    else:
        print("no green")
import pyautogui
import time

x = 1
time.sleep(5)
while x<20:
    pyautogui.write(f'I love youu baby girl!!....', interval=0.1)
    pyautogui.press('enter')
    x+=1

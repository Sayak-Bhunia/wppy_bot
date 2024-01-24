import pyautogui as auto
import time

time.sleep(3)
with open('text.txt', 'r') as file:
    auto.FAILSAFE = False
    for line in file:
        auto.typewrite(line)
        auto.press('enter')


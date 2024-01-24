import pyautogui as auto
import time

time.sleep(3)
with open('text.txt', 'r') as theFile:
    auto.FAILSAFE = False
    for line in theFile:
        auto.typewrite(line)
        auto.press('enter')

import pyautogui
posx = 189
posy = 421
189, 421

while True:
    if not pyautogui.pixelMatchesColor(posx, posy, (32, 33, 36)):
        pyautogui.press('space')
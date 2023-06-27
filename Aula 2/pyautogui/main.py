import pyautogui
import time
largura_tela, altura_tela = pyautogui.size()

print(largura_tela, altura_tela)

# while True:
#     print(pyautogui.position())

# time.sleep(5)
# pyautogui.click()

# pyautogui.moveTo(100,100)


pyautogui.click(400,400)

pyautogui.press('d')
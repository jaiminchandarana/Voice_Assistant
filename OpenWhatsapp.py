import pyautogui
import time

call = True
video_call = False
pyautogui.press('winleft')
time.sleep(2)
pyautogui.click(866, 151)
pyautogui.write('WhatsApp',interval=0.1)
pyautogui.press('enter')
time.sleep(5)
pyautogui.click(489,156)
input = "vivek gohel"
pyautogui.write(f'{input}',interval=0.1)
time.sleep(1)
pyautogui.click(276,236)

if call:
    pyautogui.click(1824,93)
elif video_call:
    pyautogui.click(1761,85)
import pyautogui
import time
from audio import speak
import os

def video_call(name):
    words = name.split()
    if "call" in words:
        index = words.index("call") + 1
        words_after_call = words[index:]
        calling = " ".join(words_after_call)
    speak(f"Calling {calling} sir")
    npath = r"" \\ Your whatsapp.exe path here.
    os.startfile(npath)
    pyautogui.click(489,156)
    pyautogui.click(489,156)
    pyautogui.write(f'{calling}',interval=0.1)
    time.sleep(1)
    pyautogui.click(276,236)
    time.sleep(1)
    pyautogui.click(1765,88)

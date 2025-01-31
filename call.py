import pyautogui
import time
from audio import speak
import os 

def call(name):
    try:
        words = name.split()
        if "call" in words:
            index = words.index("call") + 1
            words_after_call = words[index:]
            calling = " ".join(words_after_call)
        speak(f"Calling {calling} sir")
        npath = r"C:\Program Files\WindowsApps\5319275A.WhatsAppDesktop_2.2445.7.0_x64__cv1g1gvanyjgm\WhatsApp.exe"
        os.startfile(npath)
        pyautogui.click(489,156)
        pyautogui.click(489,156)
        pyautogui.write(f'{calling}',interval=0.1)
        time.sleep(1)
        pyautogui.click(276,236)
        time.sleep(1)
        pyautogui.click(1834,93)
    except Exception as e :
        speak("Call was not possible please try again sir.")
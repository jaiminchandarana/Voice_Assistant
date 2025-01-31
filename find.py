import pyautogui
import time
from audio import (speak,takecommand)
import os

def find():
    speak("In whose chat you want to find sir?")
    chat = takecommand().lower()
    speak("What do you want to find sir?")
    find = takecommand().lower()
    speak(f"Finding {find} in {chat} chat sir.")
    npath = r"C:\Program Files\WindowsApps\5319275A.WhatsAppDesktop_2.2445.7.0_x64__cv1g1gvanyjgm\WhatsApp.exe"
    os.startfile(npath)
    pyautogui.click(489,156)
    pyautogui.click(489,156)
    pyautogui.write(f'{chat}',interval=0.1)
    time.sleep(1)
    pyautogui.click(276,236)
    time.sleep(1)
    pyautogui.click(1891,92)
    time.sleep(1)
    pyautogui.click(1880,174)
    time.sleep(1)
    pyautogui.click(1891,92)
    time.sleep(1)
    pyautogui.click(1546,184)
    pyautogui.click(1546,184)
    pyautogui.write(f'{find}',interval=0.1)
    time.sleep(1)
    pyautogui.click(1755,167)
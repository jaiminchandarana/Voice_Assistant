from audio import(speak,takecommand)
import pyautogui

def click_action(image, action_name):
    location = pyautogui.locateOnScreen(image, confidence=0.8)
    if location is not None:
        pyautogui.click(pyautogui.center(location))
        print(f'Call {action_name}d.')
    elif "Receive" in action_name:
        speak(f"I guess there is no call incoming to receive sir.")
    elif "Decline" in action_name:
        speak(f"I guess there is no call ongoing to decline or end sir.")
    else:
        speak("Please try again sir.")
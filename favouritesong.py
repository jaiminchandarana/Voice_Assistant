from audio import(speak,takecommand)
import webbrowser
import random

def favouritesong():
    speak("Which playlist would you like to play sir?")
    choice = takecommand().lower()
    def firstp():
        webbrowser.open("") # Your favourite song link here.
        speak("Opening your favourite song sir.")
    def secondp():
        webbrowser.open("") # Your favourite song link here.
        speak("Opening your favourite song sir.")
    def thirdp():
        webbrowser.open("") # Your favourite song link here.
        speak("Opening your favourite song sir.")
    def fourth():
        webbrowser.open("") # Your favourite song link here.
        speak("Opening your favourite song sir.")
    if "first" in choice:
        firstp()
    elif "second" in choice:
        secondp()
    elif "third" in choice:     
        thirdp()
    elif "fourth" in choice:
        fourth()
    elif "anyone" in choice or "random" in choice:
        randomn = random.randint(1,4)
        print(randomn)
        if randomn == 1:
            firstp()
        elif randomn == 2:
            secondp()
        elif random == 3:
            thirdp()
        elif random == 4:
            fourth()
    else:
        webbrowser.open("https://www.youtube.com/")

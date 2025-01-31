from audio import(speak,takecommand)
import webbrowser
import random

def favouritesong():
    speak("Which playlist would you like to play sir?")
    choice = takecommand().lower()
    def firstp():
        webbrowser.open("https://www.youtube.com/watch?v=ntLv_697xo8&list=RDGMEMCMFH2exzjBeE_zAHHJOdxg&start_radio=1&rv=XeJtg2hFnhs&ab_channel=PrinceJadon")
        speak("Opening your favourite song sir.")
    def secondp():
        webbrowser.open("https://www.youtube.com/watch?v=1sRaLqtHXQU&list=RD1sRaLqtHXQU&start_radio=1&ab_channel=SanjuLofiEdits")
        speak("Opening your favourite song sir.")
    def thirdp():
        webbrowser.open("https://www.youtube.com/watch?v=PaoeGgJs3Ac&list=RDPaoeGgJs3Ac&start_radio=1&rv=PaoeGgJs3Ac&t=0&ab_channel=T-Series")
        speak("Opening your favourite song sir.")
    def fourth():
        webbrowser.open("https://www.youtube.com/watch?v=BwiaxAos5cg&list=RDBwiaxAos5cg&start_radio=1&ab_channel=SRLofi")
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
import pyautogui
import time
from audio import (speak,takecommand)
import re

def extract(number):
    first_digit = int(str(number)[0])
    return first_digit

def getcoordinate(sentence):
    pattern = r'\b[a-zA-Z][a-zA-Z0-9]*\d[a-zA-Z0-9]*\b'
    matches = re.findall(pattern, sentence)
    return matches

def move():  
    speak("Please tell me your move sir.")
    playmove = takecommand().lower()  
    if "Close" in playmove or "quit" in playmove or "end" in playmove or "finish" in playmove:
        return
    else:
        coordinates = {
            "a1" : (269,891),
            "a2" : (269,802),
            "a3" : (269,712),
            "a4" : (269,630),
            "a5" : (269,538),
            "a6" : (269,449),
            "a7" : (269,369),
            "a8" : (269,280),
            "b1" : (358,891),
            "b2" : (358,802),
            "b3" : (358,712),
            "b4" : (358,630),
            "b5" : (358,538),
            "b6" : (358,449),
            "b7" : (358,369),
            "b8" : (358,280),
            "c1" : (445,891),
            "c2" : (445,802),
            "c3" : (445,712),
            "c4" : (445,630),
            "c5" : (445,538),
            "c6" : (445,449),
            "c7" : (445,369),
            "c8" : (445,280),
            "d1" : (530,891),
            "d2" : (530,802),
            "d3" : (530,712),
            "d4" : (530,630),
            "d5" : (530,538),
            "d6" : (530,449),
            "d7" : (530,369),
            "d8" : (530,280),
            "e1" : (619,891),
            "e2" : (619,802),
            "e3" : (619,712),
            "e4" : (619,630),
            "e5" : (619,538),
            "e6" : (619,449),
            "e7" : (619,369),
            "e8" : (619,280),
            "f1" : (707,891),
            "f2" : (707,802),
            "f3" : (707,712),
            "f4" : (707,630),
            "f5" : (707,538),
            "f6" : (707,449),
            "f7" : (707,369),
            "f8" : (707,280),
            "g1" : (792,891),
            "g2" : (792,802),
            "g3" : (792,712),
            "g4" : (792,630),
            "g5" : (792,538),
            "g6" : (792,449),
            "g7" : (792,369),
            "g8" : (792,280),
            "zee1" : (792,891),
            "zee2" : (792,802),
            "zee3" : (792,712),
            "zee4" : (792,630),
            "zee5" : (792,538),
            "zee6" : (792,449),
            "zee7" : (792,369),
            "zee8" : (792,280),
            "h1" : (880,891),
            "h2" : (880,802),
            "h3" : (880,712),
            "h4" : (880,630),
            "h5" : (880,538),
            "h6" : (880,449),
            "h7" : (880,369),
            "h8" : (880,280),
        }
        try:
            match = getcoordinate(playmove)
            first = match[0]
            second = match[1]
            st_tuple_value = coordinates[first]
            end_tuple_value = coordinates[second]
            stvalue0 = st_tuple_value[0]
            stvalue1 = st_tuple_value[1]
            endvalue0 = end_tuple_value[0]
            endvalue1 = end_tuple_value[1]
            startx = stvalue0
            starty = stvalue1
            endx = endvalue0
            endy = endvalue1
            pyautogui.moveTo(startx, starty)
            pyautogui.mouseDown()
            pyautogui.dragTo(endx, endy, duration=0.5)
            pyautogui.mouseUp()
            time.sleep(3)
            move()
        except Exception as e:
            move()

if __name__ == "__main__":
    move()
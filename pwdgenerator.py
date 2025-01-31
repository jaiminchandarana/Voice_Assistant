from audio import(speak,takecommand)
import string
from word2number import w2n
import random

def pwdgenerator():
    speak("How long your password should be sir?")
    char_values = string.ascii_letters + string.digits + string.punctuation
    def pwd_generator():
        try:
            password = ""
            query = takecommand()
            lenght = w2n.word_to_num(query.split()[0])
        except ValueError:
            speak("Please provide an integer number sir.")
            return pwdgenerator()

        for i in range(lenght):
            Random = random.choice(char_values) 
            password += Random

        speak(f"Your generated password is {password}")

    pwd_generator()
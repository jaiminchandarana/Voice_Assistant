import random
from audio import speak, takecommand
from word2number import w2n

def fetch_first_number(sentence):
    print(sentence)
    words = sentence.split()
    for word in words:
        try:
            number = w2n.word_to_num(word)
            return number
        except ValueError:
            continue
    return None

def play():
    speak("Welcome to the number guessing game sir.")
    speak("What is your top range sir?")
    range_sentence = takecommand()
    top_range = fetch_first_number(range_sentence)

    if top_range is not None and isinstance(top_range, int):
        if top_range <= 0:
            speak("Please enter a number greater than 0 sir.")
            play()
    else:
        speak("Please provide a valid number next time sir.")
        play()

    random_number = random.randrange(1, top_range + 1)
    guess_attempts = 0

    while True:
        guess_attempts += 1
        speak("Please make a guess, sir.")
        guess_sentence = takecommand()
        guess = fetch_first_number(guess_sentence)

        if guess is not None and isinstance(guess, int):
            if guess == random_number:
                speak(f"You got it, sir. You got it in {guess_attempts} guesses sir.")
                break
            elif guess > random_number:
                speak("You are above the number sir.")
            else:
                speak("You are below the number sir.")
        else:
            speak("Please provide a valid number next time sir.")


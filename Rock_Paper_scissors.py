from audio import (speak,takecommand)
def Rock_Paper_scissors():
    from word2number import w2n
    import random
    import re
    option = ["rock", "paper", "scissors"]
    user_win = 0
    computer_win = 0

    while True:
        speak("Do you want to start or quit sir?")
        de = takecommand().lower()
        if "quit" in de:
            break

        speak("How many game should be there in a match sir?")
        round_input = takecommand().lower() 
        def extract_first_number(text):
            words = text.split()   
            for word in words:
                try:
                    return w2n.word_to_num(word)
                except ValueError:
                    if word.isdigit():
                        return int(word)
        round = extract_first_number(round_input)
        if round is None:
            speak("I am not understanding number, so i am assuming number 1")
            round = 1
        
        for i in range(round):
            speak("Please say your input sir.")
            user_guess = takecommand().lower()
            random_number = random.randint(0,2)
            computer_guess = option[random_number]

            if "rock" in user_guess and computer_guess == "scissors":
                speak("You won this game sir.")
                user_win += 1
            elif "paper" in user_guess and computer_guess == "rock":
                speak("You won this game sir.")
                user_win += 1
            elif "scissor" in user_guess and computer_guess == "paper":
                speak("You won this game sir.")
                user_win += 1
            elif "rock" in user_guess and "rock" in computer_guess:
                speak("This game ended in Draw sir.")
            elif "paper" in user_guess and "paper" in computer_guess:
                speak("This game ended in Draw sir.")
            elif "scissor" in user_guess and "scissors" in computer_guess:
                speak("This game ended in Draw sir.")
            elif user_guess not in option:
                speak("Please select from Rock Paper or scissors.")
                continue
            else:
                speak("Computer won this game sir.!")
                computer_win += 1
            speak(f"Computer selected {computer_guess}.")

    speak(f"You won {user_win} games sir.")
    speak(f"Computer won {computer_win} games sir.")
    if user_win > computer_win:
        speak(f"You beat computer by {user_win} - {computer_win} sir.")
    elif computer_win > user_win:
        speak(f"Computer beat you by {computer_win} - {user_win} sir.")
    else:
        speak("Match ended in a draw sir.")
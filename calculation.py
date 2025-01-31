from audio import(speak,takecommand)
import speech_recognition as sr
import operator

def calculation():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=5,phrase_time_limit=10)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said {query}")
    except sr.UnknownValueError:
        speak("I didn't understand that sir.")
        return calculation()
    except sr.RequestError:
        speak("There's an issue with the speech recognition service sir.")
        return calculation()

    def get_operator_fn(op):
        return {
            "+" : operator.add,
            "-" : operator.sub,
            "*" : operator.mul,
            "divided" : operator.truediv,
        }.get(op, None)

    def eval_binary_expr(op1, oper, op2):
        try:
            op1, op2 = int(op1), int(op2)
            operation = get_operator_fn(oper)
            if operation:
                return operation(op1, op2)
            else:
                speak(f"Sorry, I don't recognize the operator '{oper}'")
                return calculation()
        except ZeroDivisionError:
            speak("Division by zero is not allowed.")
            return calculation()
        except ValueError:
            speak("Invalid numbers provided.")
            return calculation()

    tokens = query.split()
    if len(tokens) == 3:
        result = eval_binary_expr(*tokens)
        if result is not None:
            speak(f"Your result is {result}")
    else:
        speak("Sorry, I couldn't understand the calculation request.")
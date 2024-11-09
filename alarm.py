import datetime
import winsound
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=15,phrase_time_limit=100)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said {query}")
    
    except Exception as e:
        speak("Please say that again sir.")
        return takecommand()
    return query

    
def alarm(time):
    alttime = str(datetime.datetime.now().strptime(time,"%I:%M %p"))
    alttime = alttime[11:-3]
    print(alttime)
    horeal = alttime[:2]
    horeal = int(horeal)
    mireal = alttime[3:5]
    mireal = int(mireal)
    speak(f"Done sir, Alarm is set for {time}")

    while True:
        if horeal==datetime.datetime.now().hour:
            if mireal==datetime.datetime.now().minute:
                speak("It's time to wake up sir.")
                winsound.PlaySound(r'C:\Users\Jaimin\Downloads\thoralarm.wav',winsound.SND_LOOP)
            elif mireal<datetime.datetime.now().minute:
                break
                

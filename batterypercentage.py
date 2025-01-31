from audio import speak
import psutil

def batterypercentage():
    battery = psutil.sensors_battery()
    percentage = battery.percent
    speak(f"Our system has {percentage} percent battery sir.")
    if percentage >= 75:
        speak("We have enough battery to work sir.")
    elif percentage < 75 and percentage >= 40:
        speak("We can wait or pluge in charger sir.")
    elif percentage < 40 and percentage >= 15:
        speak("We have low battery, Please pluge in the charger sir.")
    else:
        speak("Please pluge in charger else system will go shut down sir.")

import importlib
import sys
from audio import (speak,takecommand)

def dynamic_import(module_name):
    if module_name not in sys.modules:
        globals()[module_name] = importlib.import_module(module_name)
    return sys.modules[module_name]    

def wakeword():
    sr = dynamic_import("speech_recognition")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        query = r.recognize_google(audio,language='en-in').lower()
        if query == "hey jarvis":
            pass
        else:
            wakeword()
    
    except Exception as e:
        return wakeword()

def wish():
    datetime = dynamic_import("datetime")
    time = dynamic_import("time")
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    if hour >= 0 and hour < 12:
        speak(f"Good morning sir, its {tt}.")
    elif hour >= 12 and hour < 17:
        speak(f"Good afternoon sir, its {tt}.")
    else:
        speak(f"Good evening sir, its {tt}.")

    speak("This is jarvis in your servis sir. How can i help you?")

def main():
    print("Hey jarvis to wake up")
    wakeword()
    wish()
    def mainfun():
        while True:
            query = takecommand().lower()
            if "jai" in query or "jay" in query:
                speak(f"{query} sir.")
            elif "open notepad" in query:
                try:
                    os = dynamic_import("os")
                    npath = "C:\\Program Files\\Notepad++\\notepad++.exe"
                    speak("Do you want to write in file sir?")
                    choice = takecommand().lower()
                    if "yes" in choice or "write" in choice:
                        speak("What is your file name sir?")
                        file_name = takecommand().lower()
                        file_path = f"C:\\Users\\[username]\\OneDrive\\Desktop\\{file_name}.txt" 
                        speak("What do you want to write sir?")
                        writ = takecommand().lower()
                        with open(file_path,'w') as file:
                            file.write(writ)       
                            os.startfile(npath)
                            os.system(f'{npath} "{file_path}"')
                            speak("Content has been written in notepad file sir.")
                    else:
                        os.startfile(npath)
                        speak("Notepad opened sir.")
                except Exception as e:
                    mainfun()
            elif "close notepad" in query:
                try:
                    os = dynamic_import("os")
                    os.system("taskkill /f /im notepad++.exe")
                    speak("Notepad closed sir")
                except Exception as e:
                    mainfun()

            elif "open command prompt" in query or "open cmd" in query:
                os = dynamic_import("os")
                os.system("start cmd")
                speak("Command prompt opened sir.")
            elif "close command prompt" in query or "close cmd" in query:
                os = dynamic_import("os")
                os.system("taskkill /f /im cmd.exe")
                speak("Command prompt closed sir.")

            elif "open visual studio code" in query or "open vs code" in query:
                try:
                    os = dynamic_import("os")
                    npath = "C:\\Users\\[username]\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(npath)
                    speak("Visual studio code opened sir")
                except Exception as e:
                    mainfun()
            elif "close visual studio code" in query or "close vs code" in query:
                try:
                    os = dynamic_import("os")
                    os.system("taskkill /f /im Code.exe") 
                    speak("Visual studio code closed sir.")
                except Exception as e:
                    mainfun()

            elif "open excel" in query:
                try:
                    os = dynamic_import("os")
                    npath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
                    os.startfile(npath)
                    speak("Opened microsoft excel sir.")
                except Exception as e:
                    mainfun()
            elif "close excel" in query:
                try:
                    os = dynamic_import("os")
                    os.system("taskkill /f /im EXCEL.EXE")
                    speak("Closed microsoft excel sir.")
                except Exception as e:
                    mainfun()

            elif "open word" in query:
                try:
                    os = dynamic_import("os")
                    npath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
                    os.startfile(npath)
                    speak("Opened microsoft word sir.")
                except Exception as e:
                    mainfun()
            elif "close word" in query:
                try:
                    os = dynamic_import("os")
                    os.system("taskkill /f /im WINWORD.EXE")
                    speak("Closed microsoft word sir.")
                except Exception as e:
                    mainfun()

            elif "open download" in query:
                try:
                    os = dynamic_import("os")
                    npath = "C:\\Users\\[username]\\Downloads"
                    os.startfile(npath)
                    speak("Downloads folder opened sir")
                except Exception as e:
                    mainfun()
            elif "close download" in query:
                os = dynamic_import("os")
                os.system("taskkill /f /im explorer.exe")
                speak("Downloads folder closed sir")

            elif "open document" in query:
                try:
                    os = dynamic_import("os")
                    npath = "C:\\Users\\[username]\\OneDrive\\Documents"
                    os.startfile(npath)
                    speak("Documents folder opened sir")
                except Exception as e:
                    mainfun()
            elif "close document" in query:
                os = dynamic_import("os")
                os.system("taskkill /f /im explorer.exe")
                speak("Documents folder opened sir")
            elif "minimize document" in query or "minimise document" in query:
                gw = dynamic_import("pygetwindow")
                window = gw.getWindowsWithTitle('Documents')[0]
                window.minimize()
                speak("Documents folder minimized sir.")

            elif "open desktop" in query:
                try:
                    os = dynamic_import("os")
                    npath = "C:\\Users\\[username]\\OneDrive\\D"
                    os.startfile(npath)
                    speak("Desktop opened sir.")
                except Exception as e:
                    mainfun()
            elif "close desktop" in query:
                os = dynamic_import("os")
                os.system("taskkill /f /im explorer.exe")
                speak("Desktop closed sir.")

            elif "open file manager" in query or "open file explorer" in query:
                os = dynamic_import("os")
                os.system("start explorer.exe")
                speak("File explorerd folder opened sir")
            elif "close file manager" in query or "close file explorer" in query:
                os = dynamic_import("os")
                os.system("taskkill /f /im explorer.exe")
                speak("File explorerd folder closed sir")

            elif "open screenshot" in query:
                try:
                    os = dynamic_import("os")
                    npath = "C:\\Users\\[username]\\OneDrive\\Pictures\\Screenshots"
                    os.startfile(npath)
                    speak("Opened screenshots folder sir.")
                except Exception as e:
                    mainfun()
            elif "close screenshot" in query:
                os = dynamic_import("os")
                os.system("taskkill /f /im explorer.exe")
                speak("Closed screenshots folder sir.")

            elif "open setting" in query:
                pyautogui = dynamic_import("pyautogui")
                speak("Opening setting sir.")
                pyautogui.hotkey('winleft', 'i')
            elif "close setting" in query:
                subprocess = dynamic_import("subprocess")
                speak("Closing setting sir.")
                subprocess.run(['taskkill', '/F', '/IM', 'SystemSettings.exe'], shell=True)
                
            elif "open file" in query:
                find_and_open_file = dynamic_import("openfile").find_and_open_file
                filename = dynamic_import("openfile").filename
                os = dynamic_import("os")
                start_directory = "C:\\"
                speak("Please tell me your file name sir.")
                file_name = takecommand().lower()
                file_name = filename(file_name)
                if not os.path.isdir(start_directory):
                    speak(f"The directory '{start_directory}' does not exist.")
                else:
                    find_and_open_file(start_directory, file_name)            

            elif "open whatsapp" in query:
                os = dynamic_import("os")
                npath = r"C:\Program Files\WindowsApps\5319275A.WhatsAppDesktop_2.2445.7.0_x64__cv1g1gvanyjgm\WhatsApp.exe"
                os.startfile(npath)
            elif "call" in query:
                try:
                    call = dynamic_import("call").call
                    call(query)
                except Exception as e:
                    speak("Please try again sir.")
                    mainfun()
            elif "video call" in query:
                try:
                    video_call = dynamic_import("video_call").video_call
                    video_call(query)
                except Exception as e:
                    speak("Please try again sir.")
                    mainfun()
            elif "find" in query or "chat" in query:
                try:
                    find = dynamic_import("find").find
                    find()
                except Exception as e:
                    speak("Please try again sir.")
                    mainfun() 
                                   
            elif "volume up" in query or "increase volume" in query:
                pyautogui = dynamic_import("pyautogui")
                speak("Increasing system volumn sir.")
                pyautogui.press("volumeup")
            elif "volume down" in query or "decrease volume" in query:
                pyautogui = dynamic_import("pyautogui")
                speak("Decreasing system volumn sir.")
                pyautogui.press("volumedown")
            elif "mute" in query:
                pyautogui = dynamic_import("pyautogui")
                speak("Muting system volume sir.")
                pyautogui.press("volumemute")
            elif "set volume to" in query:
                set_volume_level = dynamic_import("set_volume_level").set_volume_level
                volume_level = int(''.join(filter(str.isdigit, query)))
                speak(f"Volume set at {volume_level} sir.")
                set_volume_level(volume_level)
            elif "volume now" in query or "current volume" in query:
                volume_now = dynamic_import("volume_now").volume_now
                volume_now()

            elif "open camera" in query:
                cv2 = dynamic_import("cv2")
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam',img)
                    k = cv2.waitKey(50)
                    close = takecommand()
                    if "close" in close:
                        break
                    else:
                        pass
                    if k==27:
                        break
                cap.release()
                cv2.destroyAllWindows()

            elif "temperature" in query or "weather" in query or "humidity" in query or "wind" in query:
                extract_city = dynamic_import("getcity").extract_city
                extract_city = dynamic_import("getcity").extract_city
                get_weather = dynamic_import("temperature").get_weather
                speak("Checking for temperature sir.")
                city = query
                city_weather = extract_city(city)
                print(city_weather)
                get_weather(city_weather)               

            elif "which song" in query or "what song" in query:
                extract_lyrics = dynamic_import("findsong").extract_lyrics
                song = dynamic_import("findsong").song
                lyrics = extract_lyrics(query)
                song(lyrics)
                
            elif "switch tab" in query:
                pyautogui = dynamic_import("pyautogui")
                pyautogui.hotkey('alt','tab')
            elif "change tab" in query:
                pyautogui = dynamic_import("pyautogui")
                pyautogui.hotkey('ctrl','tab')
            elif "close tab" in query:
                pyautogui = dynamic_import("pyautogui")
                pyautogui.hotkey('ctrl','w')

            elif "wikipedia" in query:
                wikipedia = dynamic_import("wikipedia")
                speak("searching wikipedia")
                query = query.replace("wikipedia","")
                results = wikipedia.summary(query,sentences=10)
                speak("According to wikipedia")
                speak(results)

            elif "search youtube" in query or "search in youtube" in query:
                webbrowser = dynamic_import("webbrowser")
                speak("What do you want to search in youtube sir?")
                search = takecommand().lower()
                webbrowser.open(f"https://www.youtube.com/results?search_query={search}")
                speak("Opening what you searched for in youtube sir.")
            elif "open youtube" in query:
                webbrowser = dynamic_import("webbrowser")
                webbrowser.open("www.youtube.com")
                speak("Opening youtube sir.")
            elif "open chess" in query:
                webbrowser = dynamic_import("webbrowser")
                webbrowser.open("https://www.chess.com/home")
                speak("Opening chess.com sir.")
            elif "open chatgpt" in query or "open chat gpt" in query:
                webbrowser = dynamic_import("webbrowser")
                webbrowser.open("https://chatgpt.com/")
                speak("Opening chatgpt sir.")
            elif "open jio cinema" in query or "open jiocinema" in query:
                webbrowser = dynamic_import("webbrowser")
                webbrowser.open("https://www.jiocinema.com/search")
                speak("Opening jio cinema sir.")
            elif "open gemini" in query:
                webbrowser = dynamic_import("webbrowser")
                webbrowser.open("https://gemini.google.com/app?hl=en-IN")
                speak("Opening gemini ai sir.")
            elif "open google" in query:
                webbrowser = dynamic_import("webbrowser")
                speak("What should i search on google sir?")
                cm = takecommand().lower()  
                webbrowser.open(f"https://www.google.com/search?q={cm}")
            elif "close google" in query or "close chrome" in query:
                pyautogui = dynamic_import("pyautogui")
                speak("Closing google chrome sir.")
                pyautogui.click(x=1886, y=18)
                pyautogui.moveTo(500, 500)

            elif "favourite song" in query:
                try:
                    favouritesong = dynamic_import("favouritesong").favouritesong
                    favouritesong()
                except Exception as e:
                    mainfun()
                    
            elif "play song on youtube" in query or "play a song on youtube" in query:
                kit = dynamic_import("pywhatkit")
                speak("Which song i should play sir?")
                cm = takecommand()
                kit.playonyt(f"{cm}")

            elif "time now" in query:
                datetime = dynamic_import("datetime")
                time = dynamic_import("time")
                hour = int(datetime.datetime.now().hour)
                tt = time.strftime("%I:%M %p")
                speak(f"Its {tt}.")

            elif "set alarm" in query:
                alarm = dynamic_import("alarm")
                def format_time(tt):
                    tt = tt.replace(".", "").strip()                
                    if len(tt) == 5:
                        formatted_time = f"{tt[:2]}:{tt[2:]} {tt[4:]}"
                    elif len(tt) == 6:
                        formatted_time = f"0{tt[0]}:{tt[1:3]} {tt[4:]}"
                    elif len(tt) == 7: 
                        formatted_time = f"{tt[0]}{tt[1]}:{tt[2:4]} {tt[5:]}"
                    elif len(tt) == 4:  
                        formatted_time = f"0{tt[0]}:{tt[1]} {tt[3:]}" 
                    elif len(tt) == 2:  
                        formatted_time = f"0{tt[0]}:00 {tt[2:]}" 
                    elif len(tt) == 3:  
                        formatted_time = f"0{tt[0]}:{tt[1:]} {tt[2:]}"  
                    else:
                        formatted_time = tt  
                    
                    return formatted_time
                speak("Please tell me the time to set alarm sir.")
                tt = takecommand()
                tt = tt.replace("set alarm to ", "").strip()
                formatted_time = format_time(tt.upper())
                alarm.alarm(formatted_time)

            elif "joke" in query:
                pyjokes = dynamic_import("pyjokes")
                joke = pyjokes.get_joke()
                speak(joke)

            elif "pick up" in query or "accept" in query or "receive" in query:
                time = dynamic_import("time")
                click_action = dynamic_import("click_action").click_action
                if "transfer" in query:
                    time.sleep(5) 
                    click_action('transfercall.png', 'Receive')
                    speak("Call transfered sir.")
                else:
                    time.sleep(5) 
                    click_action('acceptcall.png', 'Receive')
                    speak("Call received sir.")
            elif "decline" in query or "reject" in query:
                time = dynamic_import("time")
                click_action = dynamic_import("click_action").click_action
                time.sleep(5) 
                click_action('declinecall.png', 'Decline')
                speak("Call declined sir.")
            elif "end" in query:
                time = dynamic_import("time")
                click_action = dynamic_import("click_action").click_action
                time.sleep(5) 
                click_action('endcall.png', 'Decline')
                speak("Call ended sir.")
                
            elif "where i am" in query or "location" in query:
                requests = dynamic_import("requests")
                speak("Please wait sir, let me check.")
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url = 'https://get.geojs.io//v1//ip//geo//'+ipAdd+'.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    city = geo_data['city']
                    country = geo_data['country']
                    speak(f"I am not sure, but i think we are in {city} city of {country} country sir.")
                except Exception as e:
                    speak("For some reason i am unable to find your location sir.")
                    pass

            elif "instagram profile" in query:
                instaloader = dynamic_import("instaloader")
                webbrowser = dynamic_import("webbrowser")
                speak("Please enter the profile name correctly sir.")
                name = input("Enter username here : ")
                webbrowser.open(f"www.instagram.com/{name}")
                speak(f"Here is the profile of the user {name} sir.")
                time.sleep(5)
                speak(f"Would you like to download profile picture of user {name} sir?")
                condition = takecommand().lower()
                if "download it" in condition:
                    mod = instaloader.Instaloader()
                    mod.download_profile(name,profile_pic_only=True)
                    speak("Profile picture is downloaded in main folder sir.")
                else:
                    pass

            elif "take screenshot" in query:
                try:
                    ImageGrab = dynamic_import("PIL")
                    time = dynamic_import("time")
                    os = dynamic_import("os")
                    speak("Tell me the name of the screenshot file sir.")
                    name = takecommand().lower()
                    speak("Please hold the screen for few seconds sir.")
                    time.sleep(3)
                    screenshot_folder = r"C:\Users\[username]\OneDrive\Pictures\Screenshots"
                    img = ImageGrab.grab()
                    if not os.path.exists(screenshot_folder):
                        os.makedirs(screenshot_folder)
                    img.save(os.path.join(screenshot_folder, f"{name}.png"))
                    speak("Image has been saved to screenshot folder sir.")
                except Exception as e:
                    mainfun()

            elif "hide this folder" in query or "hide all file" in query:
                os = dynamic_import("os")
                os.system("attrib +h /s /d")
                speak("All the fildes are hiden sir.")
            elif "unhide this folder" in query or "unhide all file" in query:
                os = dynamic_import("os")
                os.system("attrib -h /s /d")
                speak("All the files are now visible.")
                
            elif "read pdf" in query:
                pdfreader = dynamic_import("pdfreader").pdfreader
                pdfreader()

            elif "activate how to" in query:
                search_wikihow = dynamic_import("pywikihow").search_wikihow
                speak("How to mod activated sir.")
                how = takecommand()
                max_results = 1
                how_to = search_wikihow(how, max_results)
                assert len(how_to) == 1
                how_to[0].print()
                speak(how_to[0].summary)

            elif "how much power we have" in query or "battery percentage" in query:
                batterypercentage = dynamic_import("batterypercentage").batterypercentage
                batterypercentage()

            elif "shutdown" in query:
                os = dynamic_import("os")
                speak("shutting down the system sir.")
                os.system("shutdown /s /t 1")
            elif "restart" in query:
                os = dynamic_import("os")
                speak("Restarting the system sir.")
                os.system("shutdown /r /t 1")
            elif "sleep" in query:
                os = dynamic_import("os")
                speak("sleeping the system sir.")
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

            elif "do some calculation" in query or "can you calculate" in query:
                calculation = dynamic_import("calculation").calculation
                calculation()
                
            elif "generate a password" in query or "generate password" in query:
                pwdgenerator = dynamic_import("pwdgenerator").pwdgenerator
                pwdgenerator()

            elif "scrap website" in query or "scrape website" in query:
                scrape = dynamic_import("scrapeweb").scrape
                scrape()
            
            elif "play game" in query or "play a game" in query:
                speak("Which game would you like to play sir?")
                choice = takecommand().lower()
                if "rockpaperscissor" in choice or "rock paper scissor" in choice:
                    Rock_Paper_scissors = dynamic_import("rock_paper_scissors").Rock_paper_scissors
                    Rock_Paper_scissors()
                elif "number" in query or "numberguess" in choice:
                    play = dynamic_import("NumberGuesser").play
                    play()
                elif "chess" in choice:
                    move = dynamic_import("playmove").move
                    webbrowser = dynamic_import("webbrowser")
                    webbrowser.open("https://www.chess.com/play/online")   
                    time.sleep(5)
                    pyautogui.click(1256,398)
                    move()
                else:
                    speak("This game is coming soon sir.")

            elif "internet speed" in query:
                speedtest = dynamic_import("speedtest")
                speak("Checking internet speed sir.")
                st = speedtest.Speedtest()
                dl = st.download()
                dl = dl / 8000000
                ul = st.upload()
                ul = ul / 8000000
                speak(f"We have {dl} mb per second download speed and {ul} mb per second upload speed sir.")
                
            elif "download video" in query or "from youtube" in query:
                download = dynamic_import("Youtube_video_Downloader").download
                speak("Please provide me with a link to your video sir.")
                video_url = input("Enter the YouTube URL: ")    
                download(video_url)
            
            elif "extract text" in query:
                pytesseract = dynamic_import("pytesseract")
                Image = dynamic_import("PIL").Image
                pytesseract.pytesseract.tesseract_cmd = r'' # Your tesseract.exe path here.
                speak("Provide me path to your image sir.")
                path = input("Path to your image : ")
                speak("Extracting text from image sir.")
                image = Image.open(path)
                extracted_text = pytesseract.image_to_string(image)
                speak(extracted_text)
  
            elif "data analysis" in query:
                choice = dynamic_import("DataAnalysis").choice
                load_csv = dynamic_import("DataAnalysis").load_csv
                analyze_data = dynamic_import("DataAnalysis").analyze_data 
                file_path = input("Enter the CSV file path: ")
                data = load_csv(file_path)
                speak(f"You have following columns in the data sir.")
                print( {list(data.columns)})  
                user_prompt = choice()  
                result = analyze_data(data, user_prompt)
                speak(result)
                
            elif "gesture" in query:
                main = dynamic_import("gesture").main
                speak("This feature is coming soon sir.")
                # main()

            elif "you can rest" in query or "you can sleep" in query or "wait" in query:
                speak("Thank you for giving me rest.")
                speak("Wake me up when you need me sir.")
                main()
                
            elif "perform task" in query:
                re = dynamic_import("re")
                genai = dynamic_import("google.generativeai")
                speak("Provide me your data sir.")
                data = input("Provide your data : ")
                speak("What you want to perform sir.")
                task = takecommand().lower()
                query = f"{data} {task}give me only thing what is asked for don't explain."
                genai.configure(api_key="") # Add your Google gemini api key here. 
                model = genai.GenerativeModel("gemini-1.5-flash")
                rp = model.generate_content(query)
                cleaned_text = re.sub(r"\*","",rp.text)
                speak(cleaned_text)
                
            elif "what" in query or "write me" in query or "tell me" in query or "where" in query or "which" in query or "when" in query or "who" in query or "may" in query or "can" in query or "how" in query or "should" in query:
                try:
                    execute = dynamic_import("assistant").execute
                    execute(query)
                except Exception as e:
                    mainfun()
                
            else:
                speak("Parden for your inconvenience sir.")
                
    mainfun()
            
if __name__ == "__main__":
    main()

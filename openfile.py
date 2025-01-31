import os
import platform
import re
from audio import speak

def filename(sentence):
    special_characters = {
        "underscore": "_",
        "dot": ".",
        "dash": "-",
        "plus": "+"
    }
    pattern = r"(\s)({})".format("|".join(re.escape(key) for key in special_characters.keys()))
    result = re.sub(pattern, lambda m: special_characters[m.group(2)], sentence)
    return result

def find_and_open_file_in_drive(start_dir, target_file_name):
    found_files = []
    for root, dirs, files in os.walk(start_dir):
        for file in files:
            if os.path.splitext(file)[0].lower() == target_file_name.lower():
                found_files.append(os.path.join(root, file))
    
    if found_files:
        file_to_open = found_files[0]
        speak(f"File found sir.")
        try:
            if platform.system() == "Windows":
                os.startfile(file_to_open)
            elif platform.system() == "Darwin": 
                os.system(f"open {file_to_open}")
            else:
                os.system(f"xdg-open {file_to_open}")
            speak(f"File '{file_to_open}' opened successfully sir.")
        except Exception as e:
            speak(f"Failed to open the file sir.")
        return True
    else:
        return False

def find_and_open_file(target_file_name):
    drives = [f"{chr(65 + i)}:\\" for i in range(26) if os.path.exists(f"{chr(65 + i)}:\\")]
    for drive in drives:
        speak(f"Finding in {drive} drive sir.")
        if find_and_open_file_in_drive(drive, target_file_name):
            return
    speak(f"No file named '{target_file_name}' found in any drive sir.")
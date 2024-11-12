# Voice Assistant

  

Jarvis is a comprehensive voice assistant developed in Python, designed to simplify everyday tasks through the power of voice commands. Built to handle a range of functions, Jarvis combines multiple Python libraries and APIs to create an interactive, hands-free experience that feels responsive and intuitive.

This repository contains a voice assistant program, which you can activate and control using various voice commands. 

**The primary file to execute is `jarvis.py`, **not**  `main.py`.**

  

## Prerequisites

  

1.  **Install Python**:

- Download Python from [Microsoft Store]([https://www.microsoft.com/en-us/store/b/python](https://www.microsoft.com/store/productId/9NCVDN91XZQP?ocid=pdpshare)) or from the [official Python website](https://www.python.org/downloads/).

2.  **Add Python to System Path**:

- Ensure Python is added to your system path. By default, Python is usually located at:

```

C:\Users\[Your Username]\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\Scripts

```

- To add Python to your path:

- Open **Environment Variables** > **System Variables** > **Path** > **Edit**.

- Add the path to your Python directory containing `ipython.exe` (usually in the folder listed above).

- Click **OK** to save.

  

3.  **Install Chrome Driver**:

- A `chromedriver.exe` file is provided in this repository. If it does not work, download the latest version from [Chrome’s website](https://developer.chrome.com/docs/chromedriver/downloads) or [direct download link](https://storage.googleapis.com/chrome-for-testing-public/129.0.6668.58/win64/chromedriver-win64.zip).

- Extract and place `chromedriver.exe` in the same folder as `jarvis.py`.

  

## Running the Voice Assistant

  

1.  **Set Up Your Environment**:

- Create or use an existing folder, and place all files from this repository into it.

- Add `chromedriver.exe` to the same folder.

  

2.  **Install Dependencies**:

- Open Command Prompt in the folder where you saved the files.

- Run:

```bash

pip install -r requirements.txt

```

- This will install the required packages (~300-400 MB of data).

  

3.  **Run `jarvis.py`**:

- Open your IDE and execute `jarvis.py` to start the voice assistant.

  

## Voice Commands

  

### Activation

-  **"Hey Jarvis"**: Activate the voice assistant.

  

### Sample Commands and Their Functions

1.  **"What is the time now"**: Tells the current system time.

2.  **"Open file explorer"**: Opens the file explorer.

3.  **"Close file explorer"**: Closes the file explorer.

4.  **"Open Notepad"**: Opens Notepad. *(Note: specify your own path if necessary)*

-  **"Yes, write in file"**: Write in a file via voice command.

-  **"No, don't write"**: Only opens Notepad.

5.  **"Close Notepad"**: Closes Notepad.

6.  **"Open Command Prompt"**: Opens Command Prompt.

7.  **"Close Command Prompt"**: Closes Command Prompt.

8.  **"Open Visual Studio Code"**: Opens Visual Studio Code. *(Specify your path)*

9.  **"Close Visual Studio Code"**: Closes Visual Studio Code.

10.  **"Volume to [number]"**: Sets system volume to specified level.

11.  **"Mute" / "Unmute"**: Mutes or unmutes system volume.

12.  **"Open [application]"** (like **Excel**, **Word**, **Downloads**, **Documents**, etc.): Opens specified application or folder. *(Specify paths as needed)*

  

### Web-Related Commands

1.  **"Open YouTube"**: Opens YouTube in the browser.

2.  **"Search in Google"**: Initiates a Google search. Jarvis will ask for the search query.

3.  **"Search in YouTube"**: Initiates a YouTube search. Jarvis will ask for the search term.

4.  **"Open ChatGPT"**, **"Open Chess"**, **"Open Gemini"**, **"Open JioCinema"**: Opens specified web applications.

5.  **"[Your query] in/from Wikipedia"**: Searches Wikipedia for the specified query and returns an answer.

  

### System and Utility Commands

1.  **"Set alarm"**: Sets an alarm. Jarvis will ask for the time.

2.  **"Tell me a joke"**: Tells a joke.

3.  **"Pick up/Accept/Receive call"**: Accepts a call if your phone is connected to Microsoft Phone Link.

4.  **"Decline call"**: Declines an incoming call if connected via Microsoft Phone Link.

5.  **"What is my location?"**: Provides current location.

6.  **"Take screenshot"**: Takes a screenshot and saves it to the specified path.

7.  **"Generate password"**: Generates a strong password. Jarvis will ask for the desired length.

8.  **"Let’s play a game"**: Initiates a game (options include **rock paper scissors**, **number guesser**, **chess**).

9.  **"Shut down system"** / **"Restart system"** / **"Sleep system"**: Performs the specified system command.

  

### Productivity and Utility Tools

1.  **"Read PDF"**: Reads a page from a PDF file. *(Place PDF in the same folder as `jarvis.py` and specify the page number)*

2.  **"Activate how-to mode"**: Provides step-by-step guidance on specified topics.

3.  **"What is battery percentage?"**: Tells current system battery percentage.

4.  **"Do some calculations"**: Performs basic math operations, e.g., **"2 + 2"**.

5.  **"Scrape website"**: Scrapes data from a specified website (provide URL).

6.  **"Check internet speed"**: Measures and displays download/upload speeds.

  

### Interaction and Rest Mode

1.  **"[Ask any question]"**: Jarvis responds to general questions, such as coding queries or trivia.

2.  **"[Perform task]"**: Jarvis performs specific task on provided data. *(Provide data).*

3.  **"You can rest"**: Puts Jarvis in idle mode. Activate again by saying **"Hey Jarvis"**.

  

---

  

*Ensure paths and settings are customized as needed for your system. Enjoy using Jarvis, your voice assistant!*

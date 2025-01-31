import yt_dlp
import os
from audio import speak, takecommand

def video_download(url, save_path):
    try:
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        def progress_hook(d):
            if d['status'] == 'downloading':
                print(f"Downloading: {d['_percent_str']} complete")
            elif d['status'] == 'finished':
                print("Download completed!")

        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',  
            'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
            'quiet': False,
            'verbose': True,
            'progress_hooks': [progress_hook],  
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        speak("Video downloaded successfully sir!")
    except Exception as e:
        speak(f"An error occurred: {e}")

def download(video_url):
    save_dir = r"C:\Users\Jaimin\Downloads"

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    if video_url:
        speak(f"Download started... Video will be saved in: {save_dir} folder sir.")
        video_download(video_url, save_dir)
    else:
        speak("Please provide a correct URL sir!")

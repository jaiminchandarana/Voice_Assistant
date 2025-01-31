import requests
from bs4 import BeautifulSoup
import re
from audio import (speak,takecommand)

def search_song_by_lyrics(lyrics):
    query = f"{lyrics} site:genius.com"
    url = f"https://www.google.com/search?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    results = []
    for g in soup.find_all('div', class_='tF2Cxc'):
        title = g.find('h3').text
        link = g.find('a')['href']
        results.append({'title': title, 'url': link})

    return results[:1] if results else None

def song(lyrics):
    results = search_song_by_lyrics(lyrics)
    
    if results:
        print("Found:")
        for i, result in enumerate(results, start=1):
            speak(f"{i}. {result['title']} - {result['url']}")
    else:
        speak("No songs found with the given lyrics.")
        
def extract_lyrics(query):
    patterns = [
        r"which song is this[: ]*(.+)",
        r"what song has these lyrics[: ]*(.+)",
        r"song is this [: ]*(.+)"
        r"song has these lyrics [: ]*(.+)"
        r"(.+) which song is it",
        r"(.+) what song has these lyrics"
    ]
    for pattern in patterns:
        match = re.search(pattern, query, re.IGNORECASE)
        if match:
            return match.group(1).strip()
    return None

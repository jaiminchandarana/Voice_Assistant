from audio import (speak,takecommand)
from scrape import(scrape_website,extract_body_content,clean_body_content,split_dom_content)
import re
import google.generativeai as genai

def scrape():
    genai.configure(api_key="AIzaSyCUv38iXDaLaVKUopLtFHkp9OkF3Zgabgw")
    def main():
        speak("Provide me your URL sir.")
        url = input("Enter your URL : ")
        
        if url:
            speak("Getting data from the website...")
            result = scrape_website(url)
            body_content = extract_body_content(result)
            cleaned_content = clean_body_content(body_content)

            # Store cleaned content for later use
            # dom_content = cleaned_content
            # print("\nDOM content:")
            return cleaned_content.lower()
    content = main()
    print(content)
    speak("Do you want to perform tasks on scraped data sir?")
    de = takecommand().lower()
    if "yes" in de or "perform task" in de:
        speak("What task you want to perform sir?")
        prompt = takecommand().lower()
        datapre = content
        data = f"{datapre} \n {prompt}" 
        model = genai.GenerativeModel("gemini-1.5-flash")
        rp = model.generate_content(data)
        cleaned_text = re.sub(r"\*", "", rp.text)
        speak(cleaned_text)
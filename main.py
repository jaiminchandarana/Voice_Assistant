from scrape import (scrape_website, extract_body_content, clean_body_content, split_dom_content)
from parse import main
from audio import (speak,takecommand)

def main():
    # print("AI Web Scraper")
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
        return cleaned_content

#         if dom_content:
#             speak("\nDescribe what you want to parse: ")
#             parse_description = takecommand().lower()
#             if parse_description:
#                 if parse_description:
#                     speak("Parsing the content.")
#                     dom_chunks = split_dom_content(dom_content)
#                     speak("\nParsed content is : ")
#                     for chunk in dom_chunks:
#                         print(chunk)  # Display each chunk or process it further
#                 else:
#                     spe("Didn't parse your description.")

# if __name__ == "__main__":
#     main()

from audio import(speak,takecommand)
import PyPDF2

def pdfreader():
    book = open('Advertisement.pdf', 'rb')
    pdfReader = PyPDF2.PdfReader(book) 
    pages = len(pdfReader.pages) 
    speak(f"Total number of pages in the PDF is {pages}.")
    speak("Please enter the number of the page I have to read, sir.")
    pg = int(input("Please enter the page number: "))
    if pg < 0 or pg >= pages: 
        speak("Invalid page number.")
        pdfreader()
    else:
        page = pdfReader.pages[pg]-1
        text = page.extract_text()  
        speak(text)

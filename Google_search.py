# google search with automation:
import speech_recognition as sr
import pyttsx3
import webbrowser
import googlesearch

def voice_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Please speak your search query.")
        try:
            audio = recognizer.listen(source)
            query = recognizer.recognize_google(audio)
            print(f"You said: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I did not understand the audio.")
            return None
        except sr.RequestError:
            print("Error with the speech recognition service.")
            return None
        
def google_search(query):
    print(f"Searching Google for: {query}")
    for result in search(query, num_results=5):  # Adjust num_results as needed
        print(result)
    # Open the first result in a web browser
    webbrowser.open(next(search(query, num_results=1)))

def main():
    query = voice_to_text()
    if query:
        google_search(query)

if __name__ == "__main__":
    main()

# for turn on and off automaticaly by using voice command:
import speech_recognition as sr
import pyttsx3
import requests

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for voice commands
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening for your command...")
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return None
        except sr.RequestError:
            speak("Unable to connect to the internet.")
            return None
        except sr.WaitTimeoutError:
            speak("No command received in time.")
            return None

# Function to turn on the lights
def turn_on_lights():
    try:
        # Replace with your smart home API endpoint
        smart_home_api_url = "http://your-smart-home-api/lights/on"
        response = requests.get(smart_home_api_url)
        if response.status_code == 200:
            speak("The lights are now on.")
            print("Lights turned on successfully.")
        else:
            speak("Failed to turn on the lights.")
            print("Error:", response.text)
    except Exception as e:
        speak("An error occurred while turning on the lights.")
        print("Exception:", e)

# Main function
def main():
    while True:
        command = listen()
        if command:
            if "turn on the lights" in command:
                turn_on_lights()
            elif "exit" in command or "stop" in command:
                speak("Goodbye!")
                break
            else:
                speak("I didn't understand that command.")

if __name__ == "__main__":
    main()


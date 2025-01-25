import speech_recognition as sr
import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init()

def speak(text):
    """Speak the given text."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to the user's speech and convert it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust to background noise
        try:
            audio = recognizer.listen(source, timeout=5)
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print(f"You said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            print("Speech was unclear or not understood.")
            speak("Sorry, I could not understand what you said.")
        except sr.RequestError:
            print("Could not request results; check your internet connection.")
            speak("Could not request results; check your internet connection.")
        except Exception as e:
            print(f"An error occurred: {e}")
            speak(f"An error occurred: {e}")
        return None

def main():
    """Main function for the virtual assistant."""
    speak("Hello, how can I assist you today?")
    failure_count = 0
    max_failures = 5  # Limit failures to prevent infinite loop
    while True:
        command = listen()
        if command is None:
            failure_count += 1
            if failure_count >= max_failures:
                speak("Too many failed attempts. Goodbye!")
                break
            continue
        
        if "hello" in command:
            speak("Hello there! How can I help?")
        elif "how are you" in command:
            speak("I'm just a virtual assistant, but I'm doing great! How about you?")
        elif "what is your name" in command:
            speak("I am your virtual assistant. You can call me Helper.")
        elif "exit" in command or "quit" in command or "goodbye" in command:
            speak("Goodbye! Have a great day!")
            break
        else:
            speak("I'm not sure how to respond to that. Can you try something else?")
        failure_count = 0  # Reset failures on successful command

if __name__ == "_main_":
    main()
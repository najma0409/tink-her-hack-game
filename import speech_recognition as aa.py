import speech_recognition as aa
import pyttsx3 
listener = aa.Recognizer()
machine=pyttsx3.init()
def talk(text)
    machine.say(text)
machine.runAndWait()
def input_instruction()

    try:
        with aa.Microphone() as orgin:
            print("Listening")
            speech=listener.listen(orgin)
            instruction=listener.recogonize_goggle(speech)
            instruction=listener.lower()
            if "Anu" in instruction:
                print(instruction)
            print(instruction)
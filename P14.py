import pyttsx3
import speech_recognition as sr

text = "Hello, Welcome to Artificial Intelligence."
engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()

print("Text to Speech:")
print(text)

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("\nSpeak something!")
    audio = recognizer.listen(source)
    try:
        result = recognizer.recognize_google(audio)
        print("Speech to Text:")
        print(result)
    except sr.UnknownValueError:
        print("Could not understand the speech.")
    except sr.RequestError:
        print("Could not connect to the speech recognition service.")
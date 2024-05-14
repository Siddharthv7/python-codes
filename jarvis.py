import speech_recognition as sr
from gtts import gTTS
import os

# Initialize the recognizer
recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        user_input = recognizer.recognize_google(audio)
        print("User: " + user_input)
        return user_input
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return None

def respond(text):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    os.system("start response.mp3")

def main():
    print("Hello, I'm your Jarvis-like AI assistant.")
    while True:
        user_input = listen()
        if user_input:
            if "hello" in user_input.lower():
                respond("Hello! How can I assist you?")
            elif "bye" in user_input.lower():
                respond("Goodbye!")
                break
            else:
                respond("I'm sorry, I can't help with that.")

if __name__ == "__main__":
    main()

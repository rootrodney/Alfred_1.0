'''
    This is ALFRED 1.0 he is a virtual assistant ,he is still undergoing development this what he can currently do
    Play a Song on YouTube

    Retrieve Information from Wikipedia

    Provide the Current Time

    Tell a Joke

'''
#these are his prerequisite libraries they can  be found here "https://pypi.org/project"

import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime
import pyjokes

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Create an instance of the speech recognizer
listener = sr.Recognizer()

# Retrieve the available voices for the text-to-speech engine
voices = engine.getProperty("voices")

# Set the voice for the text-to-speech engine to the first available voice in the list
engine.setProperty("voice", voices[0].id)

# Use the text-to-speech engine to say the greeting
engine.say("Hi, my name is Alfred. What can I assist you with today?")
engine.runAndWait()


def talk(text):
    # Use the text-to-speech engine to speak the provided text
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            # Use the speech recognizer to listen to the user's voice
            voice = listener.listen(source)
            # Recognize the speech using Google Speech Recognition
            command = listener.recognize_google(voice)
            # Convert the recognized speech to lowercase for easier processing
            command = command.lower()
            if "alfred" in command:
                # Remove the trigger word "Alfred" from the recognized command
                command = command.replace("alfred", "")
                print(command)

    except:
        pass
    return command


def run_alfred():
    # Obtain a command from the user
    command = take_command()
    print(command)
    if "play" in command:
        # Extract the song name from the command and play it on YouTube
        song = command.replace("play", "")
        talk("Now playing" + song)
        pywhatkit.playonyt(song)
    elif "who is" in command:
        # Extract the person's name from the command and retrieve information from Wikipedia
        person = command.replace("who is", "")
        info = wikipedia.summary(person, 1)
        print(info)
        talk("Here's what I found: " + info)
    elif "time" in command:
        # Retrieve the current time and provide it as a response
        time = datetime.datetime.now().strftime("%I:%M %p")
        print("It is currently " + time)
        talk("It is currently " + time)
    elif "joke" in command:
        # Retrieve a random joke and tell it
        talk(pyjokes.get_joke())
    else:
        # Ask the user to repeat the command if it cannot be recognized
        talk("Please say that again.")


while True:
    # Continuously run the virtual assistant
    run_alfred()

import pyttsx3
import sys

if len(sys.argv) != 2:
    print("Please provide an input text as a command-line argument.")
    exit()

text = sys.argv[1]

engine = pyttsx3.init()

# Set the read speed
engine.setProperty('rate', 300)

engine.say(text)
engine.runAndWait()

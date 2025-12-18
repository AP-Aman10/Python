import pyjokes as pj
import pyttsx3

joke = pj.get_joke()
print(f"Printing Joke: {joke}")

engine = pyttsx3.init()
engine.say(joke)
engine.runAndWait()

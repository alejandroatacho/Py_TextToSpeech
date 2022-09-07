from cgitb import text
from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from gtts import gTTS

Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
# show an "Open" dialog box and return the path to the selected file
filename = fd.askopenfilename()
with open(filename, 'r') as f:
    text = f.read()


class TextToSpeech:
    def __init__(self, text, language, filename):
        self.text = text
        self.lang = language
        self.filename = filename

    def speak(self):
        tts = gTTS(text=self.text, lang=self.lang, slow=False)
        tts.save(f"{self.filename}.mp3")


person1 = TextToSpeech(text, "en", "hello")
person1.speak()

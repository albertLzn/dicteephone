from gtts import gTTS
import os

class TextToSpeech:
    def convert(self, text, filename="output.mp3", lang='fr'):
        tts = gTTS(text=text, lang=lang)
        tts.save(filename)
        print(f"Texte converti en audio et sauvegardé dans {filename}")

    def play(self, filename="output.mp3"):
        os.system(f"mpg321 {filename}")  # Assurez-vous que mpg321 est installé sur le Raspberry Pi
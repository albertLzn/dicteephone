import speech_recognition as sr

class SpeechToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def convert(self, audio_file):
        with sr.AudioFile(audio_file) as source:
            audio = self.recognizer.record(source)
        try:
            text = self.recognizer.recognize_google(audio, language="fr-FR")
            print("Texte reconnu :", text)
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition n'a pas pu comprendre l'audio")
        except sr.RequestError as e:
            print(f"Impossible d'obtenir les résultats de Google Speech Recognition; {e}")
        return ""
import pyaudio
import wave

class AudioManager:
    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.stream = None

    def record(self, filename, duration=5, sample_rate=44100, chunk=1024):
        self.stream = self.p.open(format=pyaudio.paInt16,
                                  channels=1,
                                  rate=sample_rate,
                                  input=True,
                                  frames_per_buffer=chunk)

        print("Enregistrement...")
        frames = []
        for _ in range(0, int(sample_rate / chunk * duration)):
            data = self.stream.read(chunk)
            frames.append(data)
        print("Enregistrement terminé.")

        self.stream.stop_stream()
        self.stream.close()

        wf = wave.open(filename, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(self.p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))
        wf.close()

    def play(self, filename):
        wf = wave.open(filename, 'rb')
        self.stream = self.p.open(format=self.p.get_format_from_width(wf.getsampwidth()),
                                  channels=wf.getnchannels(),
                                  rate=wf.getframerate(),
                                  output=True)

        print("Lecture...")
        data = wf.readframes(1024)
        while data:
            self.stream.write(data)
            data = wf.readframes(1024)
        print("Lecture terminée.")

        self.stream.stop_stream()
        self.stream.close()
        wf.close()

    def __del__(self):
        self.p.terminate()
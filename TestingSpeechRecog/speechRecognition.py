# Configuración de parámetros
DURATION = 5  # Duración de la grabación en segundos
SAMPLE_RATE = 44100  # Frecuencia de muestreo
import sounddevice as sd
import speech_recognition as sr
from scipy.io.wavfile import write
import os

class AudioRecorder:
    def __init__(self, duration=5, sample_rate=44100, filename="output.wav"):
        self.duration = duration
        self.sample_rate = sample_rate
        self.filename = filename
        self.recognizer = sr.Recognizer()

    def record_audio(self):
        print("Grabando...")
        recording = sd.rec(int(self.duration * self.sample_rate), samplerate=self.sample_rate, channels=1, dtype='int16')
        sd.wait()  # Espera a que termine la grabación
        print("Grabación finalizada.")
        write(self.filename, self.sample_rate, recording)  # Guardar el archivo WAV

        return self.filename

    def recognize_audio(self):
        with sr.AudioFile(self.filename) as source:
            audio = self.recognizer.record(source)  # Lee el archivo de audio

        try:
            # Realiza el reconocimiento de voz
            text = self.recognizer.recognize_google(audio, language='es-ES')  # Cambia 'es-ES' si es necesario
            print("Texto reconocido: " + text)
            return text
        except sr.UnknownValueError:
            print("No se pudo entender el audio")
            return "No se pudo entender el audio"
        except sr.RequestError as e:
            print(f"Error en la solicitud de reconocimiento de voz: {e}")
            return f"Error en la solicitud de reconocimiento de voz: {e}"

# Instancia global para usar en Flask
recorder = AudioRecorder()

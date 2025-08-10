import speech_recognition as sr
from faster_whisper import WhisperModel
whisper = WhisperModel("large-v2", device= "cpu", compute_type="int8")


class VoiceInput:
    def __init__(self):
      self.recognizer=sr.Recognizer()
      self.audio = None
      try:
        with sr.Microphone() as source:
           print("Listening!!......Please speak now?")
           self.audio=self.recognizer.listen(source,timeout=5,phrase_time_limit=100)
      except sr.WaitTimeoutError:
           print("No speech detected — you stayed silent too long.")
      except sr.UnknownValueError:
           print("Could not understand the audio (maybe distortion or unclear speech).")
      except Exception as e:
          print(f"Some other error occurred: {e}")
          return # Exit if recording failed
      self.write_input()
      self.convert_to_text()
    def write_input(self):
      with open("output.wav", "wb") as f:
        f.write(self.audio.get_wav_data())
    def convert_to_text(self):
      whisper.transcribe("output.wav")
      #segments:: a list of segment objects is returned
      segments, info = whisper.transcribe("output.wav")
      print(f"Detected Language: {info.language}")
      print(f"Duration: {info.duration:.2f} seconds")
      self.text = " ".join([segment.text for segment in segments])
      print(f"📝 Full combined transcription: {self.text}")  # <-- ✅ Add this

      for segment in segments:
        print(f"🕒 From {segment.start:.2f}s to {segment.end:.2f}s ➤ You said: {segment.text}")


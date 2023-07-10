import speech_recognition as sr
from app.models.audio import Audio
from app.process.conversions import try_conversion
from mutagen.wave import WAVE


def get_text(file: Audio):
   if file.type == 'audio/x-wav':
      file.text = transcription(file.path)
      file.duration = get_duration(file.path)
   else:
      temp_file = try_conversion(file)
      if temp_file == False:
        file.text = 'Áudio não pode ser transcrito'
        file.duration = 'Duração não pode ser obtida'
      else:
        file.text = transcription(temp_file)
        file.duration = get_duration(temp_file)
   return file

def transcription(path):
    r = sr.Recognizer()
    file_audio = sr.AudioFile(path)
    with file_audio as source:
        audio_text = r.record(source)
        text = r.recognize_google(audio_text,language='pt-BR')
    return text

def get_duration(path):
   metadata = WAVE(path)
   hours, min, seconds = audio_duration (int(metadata.info.length))
   duration = ('{}:{}:{}').format(hours, min, seconds)
   return duration

def audio_duration(length):
    hours = length // 3600
    length %= 3600
    mins = length // 60
    length %= 60
    seconds = length
  
    return hours, mins, seconds
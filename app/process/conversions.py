import moviepy.editor as mp
import speech_recognition as sr
import moviepy.editor as mp
from pydub import AudioSegment
from app.models.audio import Audio 

def try_conversion(file: Audio):
   if file.type == 'video/mp4':
      return mp4_to_wav(file)
   elif file.type == 'audio/mpeg':
      return mpeg_to_wav(file)
   else:
      return False    

def mp4_to_wav(file: Audio):
   temp_path = "./temp_audios/"+file.name+".mp3"

   clip = mp.VideoFileClip(file.path).subclip()
   clip.audio.write_audiofile(temp_path)
   sound = AudioSegment.from_mp3(temp_path)

   temp_path = "./temp_audios/"+file.name+".wav"
   sound.export(temp_path, format="wav")
   sr.AudioFile(temp_path)
   
   return temp_path

def mpeg_to_wav(file: Audio):
   temp_path = "./temp_audios/"+file.name+".wav"
   sound = AudioSegment.from_mp3(file.path)

   sound.export(temp_path, format="wav")
   sr.AudioFile(temp_path)
   
   return temp_path
import speech_recognition as sr
# from gtts import gTTS
import pyaudio
import wave, struct
import os
import re

from scipy.io.wavfile import write
import wavio as wv


CHUNK = 1024
FORMAT = pyaudio.paInt16
SAMPLERATE = 44100.0
DURATION = 1000.0

freq = 48000

get_current_directory = os.getcwd()
change_directory = os.chdir(get_current_directory)

get_enable_command = 'SoundVolumeView.exe /Enable Stereo Mix'
get_enable_recording_device = os.system(get_enable_command)

# microphone_list = list(enumerate(sr.Microphone.list_microphone_names()))
microphone_list = sr.Microphone.list_microphone_names()
# print('microphone_list',microphone_list)

# txt = 'Stereo Mix (Realtek HD Audio Stereo input)'
# re.search("^Stereo Mix.+$",txt)

index_for_stereo_device = microphone_list.index('Stereo Mix (Realtek(R) Audio)')

# au_file = wave.open('test_sound.wav','wb')
# au_file.setnchannels(1)
# au_file.setsampwidth(2)
# au_file.setframerate(SAMPLERATE)

# print('frame rate',au_file.readframes(-1))



recognizer = sr.Recognizer()
microphone = sr.Microphone(device_index=index_for_stereo_device)
with microphone as source:
    print('please start')
    # audio = recognizer.record(source)
    audio = recognizer.listen(source)
    # print('type audio',type(audio))

    # tts = gTTS(audio)
    # tts.save('test_audio.mp3')
    print('ok done')
    # write('r20.wav',freq,audio)
    # wv.write('r3.wav',audio,freq,sampwidth=2)
    # au_file.writeframesraw(audio)
    # au_file.close()
        
    




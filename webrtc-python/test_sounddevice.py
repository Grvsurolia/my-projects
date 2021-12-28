import sounddevice as sd 
from scipy.io.wavfile import write
import wavio as wv
import os

get_current_directory = os.getcwd()
change_directory = os.chdir(get_current_directory)


# freq = 44100
freq = 48000
duration = 10

list_devices = sd.query_devices()
device_name = 'Stereo Mix (Realtek(R) Audio)'

# print('device',list_devices)
count = 0
for i in list(list_devices):
	if i["name"]==device_name:
		index = count
		break
	count += 1
print(index)

sd.default.device = index

recording = sd.rec(int(duration * freq),
	samplerate=freq,channels=2)
sd.wait()
write('test_sound2.wav',freq,recording)

# recording = sd.rec(int(duration * freq),
# 	samplerate=freq,channels=2)
# sd.wait()
# write('test_sound1.wav',freq,recording)




# while True:
# 	duration = 20

# 	get_enable_command = 'SoundVolumeView.exe /Enable Stereo Mix'
# 	get_enable_recording_device = os.system(get_enable_command)

# 	sd.default.device = 'Stereo Mix (Realtek(R) Audio)'
# 	sd.default.device = 3

# 	recording = sd.rec(int(duration * freq),
# 		samplerate=freq,channels=2)
# 	sd.wait()
# 	write('test_sound1.wav',freq,recording)

#wv.write('test_sound2.wav',recording,freq,sampwidth=2)


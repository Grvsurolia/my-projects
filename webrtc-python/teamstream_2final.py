import re
import sys
import time
import os
import requests
import json 


# from google.cloud import speech
import pyaudio
from six.moves import queue



# tsJson = {
#   "type": "service_account",
#   "project_id": "teamstream-299015",
#   "private_key_id": "24f77d2bc9dcc8c1983be75deff97f9f59fb7176",
#   "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDWNMdRxIXiSxEQ\nrioQspjXy8kA6gn2RGlNmdAm1nw6ys1UZXA3vcaoDx0KxZV2gXAMz+xWtCOya7oG\n5P88hRUxuISvEUWPpvBWOodxB1pLoohQOJ4N14SMWkGydyzFvfTmPe22gIsJo/09\n8haLvjej6Pzudoo229ERebYsPRRRUV2EmiaqK5MyUySiwu7HP4c07rWkFkZcDCKs\nlsLd33gb0koDfJT8+PFX8M/l3p1l2N5avY7tDLsQOSOoxRNSw56rcB0qBMquRehe\n5vWzcbXI21rBLDcVYu1rlWWE8pkmVpJ0XgF5oykfvEV0BFoL9KXsnDIc+UI1D65r\nfgIuylt1AgMBAAECggEAIQVGU6PKqsl9Ijfi+qt5dcyvmfE6I2lE3WZQaOhIAs0o\nDXJMs/8QjHA1/ybZxUirVAJKccw3s4W5Sd5LvVHbpExIQe+U7FHk+znvDpy+TeoK\nfulXbhVS1MsGFSObdokzozmZNzjGFjCeNYon8Rdb3uvn77+8yzukFUBQta2dv/IV\nmCOlpkZSKxQefiTCTzTJiOYYWHmWnseXQezwhZ7zoHQr0aIjhVwJpeQkBbfpzSJw\nGaMaIyk6fQkx2Vf+CWGwfErBTN6zRZuzYbTc6QYJ1wOUJ9juYvRGgxtDXGfN2/3c\nE5mMW3h42UN92lHQ6UjDGPcZG29SIoIloqLNf+aXgQKBgQDrt5AJPB9gk0Q7gUuz\nTBjAZoCI9RxZabCZtcg1DjCjwxr3MmIFrHKteYpQpxZ1aNHbHBo9CcvKlPY5h6TK\nqSAb6KZnVjyKZkwmDCtHvO+Kv7UdcBeX6xgkU6rW4DT2F772McleqBPZt0+NVNSa\n8Cn+9qu1X0OnsWZsZp+LOTLg9QKBgQDoo15jJCU1m4w53MuYc/v3Ky7M3cFB5RSg\nn+MMeEsktq47ekWwt/P6rVEHvaI6heswrT8m1DltwQKrOQggIpXcx8lSTX0NWNVg\nwVjbvEq9ub5MYgyw2uyeMkgPsAtdq2nm/Nle8Id3P56HFO0PNgBGG1rRHwcwaK4T\nOoIcZysAgQKBgQCsMhji5iz13B9IaRfoD3s1cqwLYSQonXEJmSZ8u7UErQ8R7ph1\nFJlh6RwF90oM01oa+tigJnvdrhyBwnm8Ivj16mtFqlXntPuD//fOHFPRxGKG8tAJ\nhxDH2OdAueF2tbonGA/HOnnl3mgbExGNbkz/mSuu/7zo0EvGfOGoT0y/0QKBgD1L\n7m7I81Twqz4Dw1FkHhu+MRKhy24FYi4Act6yQ3pk9/uL+BjcH1kJmbQkbz5kUtf8\njgs5F/inRoC/AjkVY89MhOs+p5iAs5hO2Y7sSfU7n7yYiSeAR6BXN02K4TPJGppW\nPSAa2Fa/WJHXHa9IV0Ihqwg22LoUmulOHUJGnLoBAoGBAN/WGha7PRspkVaX4jvY\nhbCwc2/NDy1jcPH8RcKyfs/GULJz7U6z2OM7+dcsocycfjydZA7q6WW374fuc3XI\nJ3do+JkA9Sc+Nxg2YSnD/zfOgJ3u+IASnJb371cX6XHiytXZdYskbLn6dvsHtyYP\nRNRt3gLZ89xOm3YlsLSOScXA\n-----END PRIVATE KEY-----\n",
#   "client_email": "audio-recording@teamstream-299015.iam.gserviceaccount.com",
#   "client_id": "114174020383502549322",
#   "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#   "token_uri": "https://oauth2.googleapis.com/token",
#   "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#   "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/audio-recording%40teamstream-299015.iam.gserviceaccount.com"
# }


# os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r"TeamStream.json"

# get_current_directory = os.getcwd()
# change_directory = os.chdir(get_current_directory)

# Create Folder TeamStream if not exist
if not os.path.exists('C:\\ProgramData\\TeamStream'):
    os.makedirs('C:\\ProgramData\\TeamStream')

#Download soundvolumeview-x64.zip
url = "https://www.nirsoft.net/utils/soundvolumeview-x64.zip"
r = requests.get(url) 
with open("C:\\ProgramData\\TeamStream\\soundvolumeview-x64.zip",'wb') as f: 
	f.write(r.content) 

# Extract soundvolumeview-x64.zip
import zipfile
with zipfile.ZipFile("C:\\ProgramData\\TeamStream\\soundvolumeview-x64.zip", 'r') as zip_ref:
    zip_ref.extractall("C:\\ProgramData\\TeamStream")

# Delete soundvolumeview-x64.zip
os.remove("C:\\ProgramData\\TeamStream\\soundvolumeview-x64.zip")

get_enable_command = 'C:\\ProgramData\\TeamStream\\SoundVolumeView.exe /Enable Stereo Mix'
get_enable_recording_device = os.system(get_enable_command)

# Audio recording parameters

STREAMING_LIMIT = 240000  # 4 min
SAMPLE_RATE = 16000
CHUNK_SIZE = int(SAMPLE_RATE / 10)  # 100ms

RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[0;33m"


def get_current_time():
    """Return Current Time in MS."""

    return int(round(time.time() * 1000))


class ResumableMicrophoneStream:
    """Opens a recording stream as a generator yielding the audio chunks."""

    def __init__(self, rate, chunk_size):
        self._rate = rate
        self.chunk_size = chunk_size
        self._num_channels = 1
        self._buff = queue.Queue()
        self.closed = True
        self.start_time = get_current_time()
        self.restart_counter = 0
        self.audio_input = []
        self.last_audio_input = []
        self.result_end_time = 0
        self.is_final_end_time = 0
        self.final_request_end_time = 0
        self.bridging_offset = 0
        self.last_transcript_was_final = False
        self.new_stream = True
        self._audio_interface = pyaudio.PyAudio()
        self._audio_stream = self._audio_interface.open(
            format=pyaudio.paInt16,
            channels=self._num_channels,
            rate=self._rate,
            input=True,
            frames_per_buffer=self.chunk_size,
            stream_callback=self._fill_buffer,
        )

    def __enter__(self):

        self.closed = False
        return self

    def __exit__(self, type, value, traceback):

        self._audio_stream.stop_stream()
        self._audio_stream.close()
        self.closed = True
        self._buff.put(None)
        self._audio_interface.terminate()

    def _fill_buffer(self, in_data, *args, **kwargs):
        """Continuously collect data from the audio stream, into the buffer."""

        self._buff.put(in_data)
        return None, pyaudio.paContinue

    def generator(self):
        """Stream Audio from microphone to API and to local buffer"""

        while not self.closed:
            data = []

            if self.new_stream and self.last_audio_input:

                chunk_time = STREAMING_LIMIT / len(self.last_audio_input)

                if chunk_time != 0:

                    if self.bridging_offset < 0:
                        self.bridging_offset = 0

                    if self.bridging_offset > self.final_request_end_time:
                        self.bridging_offset = self.final_request_end_time

                    chunks_from_ms = round(
                        (self.final_request_end_time - self.bridging_offset)
                        / chunk_time
                    )

                    self.bridging_offset = round(
                        (len(self.last_audio_input) - chunks_from_ms) * chunk_time
                    )

                    for i in range(chunks_from_ms, len(self.last_audio_input)):
                        data.append(self.last_audio_input[i])

                self.new_stream = False

            # Use a blocking get() to ensure there's at least one chunk of
            # data, and stop iteration if the chunk is None, indicating the
            # end of the audio stream.
            chunk = self._buff.get()
            self.audio_input.append(chunk)

            if chunk is None:
                return
            data.append(chunk)
            # Now consume whatever other data's still buffered.
            while True:
                try:
                    chunk = self._buff.get(block=False)

                    if chunk is None:
                        return
                    data.append(chunk)
                    self.audio_input.append(chunk)

                except queue.Empty:
                    break

            yield b"".join(data)


def listen_print_loop(responses, stream):

    # for response in responses:
    #     print(response)

    for response in responses:

        if get_current_time() - stream.start_time > STREAMING_LIMIT:
            stream.start_time = get_current_time()
            break

    #     if not response.results:
    #         continue

    #     result = response.results[0]

    #     if not result.alternatives:
    #         continue

    #     transcript = result.alternatives[0].transcript

    #     result_seconds = 0
    #     result_micros = 0

    #     if result.result_end_time.seconds:
    #         result_seconds = result.result_end_time.seconds

    #     if result.result_end_time.microseconds:
    #         result_micros = result.result_end_time.microseconds

    #     stream.result_end_time = int((result_seconds * 1000) + (result_micros / 1000))

    #     corrected_time = (
    #         stream.result_end_time
    #         - stream.bridging_offset
    #         + (STREAMING_LIMIT * stream.restart_counter)
    #     )
    #     # Display interim results, but with a carriage return at the end of the
    #     # line, so subsequent lines will overwrite them.

    #     if result.is_final:

    #         # sys.stdout.write(GREEN)
    #         sys.stdout.write("\033[K")
    #         # sys.stdout.write(str(corrected_time) + ": " + transcript + "\n")
    #         sys.stdout.write("==> " + transcript + "\n")

    #         stream.is_final_end_time = stream.result_end_time
    #         stream.last_transcript_was_final = True

    #         # Exit recognition if any of the transcribed phrases could be
    #         # one of our keywords.
    #         if re.search(r"\b(exit|quit)\b", transcript, re.I):
    #             # get_enable_command = 'SoundVolumeView.exe /SetDefault Microphone Array'
    #             # get_enable_recording_device = os.system(get_enable_command)
    #             get_enable_command = 'C:\\ProgramData\\TeamStream\\SoundVolumeView.exe /Disable Stereo Mix'
    #             get_enable_recording_device = os.system(get_enable_command)
    #             # sys.stdout.write(YELLOW)
    #             sys.stdout.write("Exiting...\n")
    #             stream.closed = True

    #             os.remove("TeamStream.json")

    #             break

    #     else:
    #         # sys.stdout.write(RED)
    #         sys.stdout.write("\033[K")
    #         # sys.stdout.write(str(corrected_time) + ": " + transcript + "\r")
    #         sys.stdout.write("==> " + transcript + "\r")

    #         stream.last_transcript_was_final = False


def main():
    """start bidirectional streaming from microphone input to speech API"""

    get_current_directory = os.getcwd()
    change_directory = os.chdir(get_current_directory)

    get_enable_command = 'SoundVolumeView.exe /Enable Stereo Mix'
    get_enable_recording_device = os.system(get_enable_command)



    # client = speech.SpeechClient() #credentials=tsJson
    # config = speech.RecognitionConfig(
    #     encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    #     sample_rate_hertz=SAMPLE_RATE,
    #     language_code="en-US",
    #     max_alternatives=1,
    #     use_enhanced=True,
    # )

    # streaming_config = speech.StreamingRecognitionConfig(
    #     config=config, interim_results=True
    # )

    mic_manager = ResumableMicrophoneStream(SAMPLE_RATE, CHUNK_SIZE)
    # print(mic_manager.chunk_size)
    # sys.stdout.write(YELLOW)
    # sys.stdout.write('\nListening, say "Quit" or "Exit" to stop.\n\n')
    # sys.stdout.write("End (ms)       Transcript Results/Status\n")
    # sys.stdout.write("=====================================================\n")

    with mic_manager as stream:

        while not stream.closed:
            # sys.stdout.write(YELLOW)
            # sys.stdout.write(
            #     "\n" + str(STREAMING_LIMIT * stream.restart_counter) + ": NEW REQUEST\n"
            # )

            stream.audio_input = []
            audio_generator = stream.generator()

            # print(audio_generator)

            # requests = (
            #     speech.StreamingRecognizeRequest(audio_content=content)
            #     for content in audio_generator
            # )

            # responses = client.streaming_recognize(streaming_config, requests)

            # Now, put the transcription responses to use.
            # listen_print_loop(responses, stream)

            # listen_print_loop(audio_generator, stream)

            if stream.result_end_time > 0:
                stream.final_request_end_time = stream.is_final_end_time
            stream.result_end_time = 0
            stream.last_audio_input = []
            stream.last_audio_input = stream.audio_input
            stream.audio_input = []
            stream.restart_counter = stream.restart_counter + 1

            if not stream.last_transcript_was_final:
                sys.stdout.write("\n")
            stream.new_stream = True
    


if __name__ == "__main__":

    main()
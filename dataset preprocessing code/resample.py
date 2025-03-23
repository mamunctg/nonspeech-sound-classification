import os
import pydub
from pydub import AudioSegment
import librosa
import numpy as np


def main():
    """audio_files=os.listdir('/home/mamun/Downloads/test/')
    #Folder is having audio files of both MP3 and WAV formats
    len_audio=len(audio_files)
    print(len_audio)

    for i in range(len_audio):
        if os.path.splitext(audio_files[i])[1]==".mp3":
            mp3_sound =AudioSegment.from_mp3(audio_files[i])
            mp3_sound.export('</~/test/>\\converted.wav', format='wav')"""

    # another example

    path = "/~/audio analysis/current work/man crying/"

    # Change working directory
    os.chdir(path)

    audio_files = os.listdir()


    #example
    for file in audio_files:
        name, ext = os.path.splitext(file)
        if ext == ".wav":
            y, sr=librosa.load(file, sr=32000, mono=True)

            #data=librosa.load(file, sr=32000, mono=True)

            print(y, sr)

            librosa.output.write_wav("{0}.wav".format(name),y, sr)













    # # You dont need the number of files in the folder, just iterate over them directly using:

        # spliting the file into the name and the extension
    # for file in audio_files:
    #     name, ext = os.path.splitext(file)
    #     if ext == ".wav":
    #         y, sr=librosa.load(file)
    #         #print(y.shape)
    #         y_mono = librosa.to_mono(y)
    #
    #         librosa.output.write_wav(y, sr)
    #
    #
    #
    #
    #         orig_sound=pydub.AudioSegment.from_file(file)
    #         # orig_sound1 = orig_sound.set_channels(1)
    #         channel=orig_sound.channels
    #         print(channel)
    #
    #
    #
    #
    #
    #
    #         #mp3_sound = AudioSegment.from_mp3(file)
    #         #aiff_sound =aiff_sound.set_frame_rate(32000)
    #         #aiff_sound=aiff_sound.set_channels(1)
    #
    #         # orig_sound=orig_sound.set_frame_rate(32000)
    #         sample_rate=orig_sound.frame_rate
    #         print(sample_rate)
    #
    #
    #

            #orig_sound.export("{0}.wav".format(name), format="wav")

    # for file in audio_files:
    #     name, ext = os.path.splitext(file)
    #     if ext .endswith !=('.wav' ):  #to convert from ext
    #
    #         sound=AudioSegment.from_file(file)
    #
    #         sound=sound.set_frame_rate(32000)    #to set sample rate
    #
    #         channel_count = sound.channels
    #         print(channel_count)


            #sound.export("{0}.wav".format(name), format="wav")  # rename them using the old name + ".wav"



# Driver code
if __name__ == '__main__':
    # calling main() function
    main()

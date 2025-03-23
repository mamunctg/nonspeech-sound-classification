import glob
import os
import pydub
from pydub import AudioSegment
from pydub.utils import mediainfo

path = '/~/data_FSD50K/exp_with_BG/dev/Yawn/'
# Change working directory
os.chdir(path)

audio_files = os.listdir() #one directory

# Function to convert multiple files
def main():
    """audio_files=os.listdir('/home/mamun/Downloads/test/')
    #Folder is having audio files of both MP3 and WAV formats
    len_audio=len(audio_files)
    print(len_audio)

    for i in range(len_audio):
        if os.path.splitext(audio_files[i])[1]==".mp3":
            mp3_sound =AudioSegment.from_mp3(audio_files[i])
            mp3_sound.export('<~/Downloads/test/>\\converted.wav', format='wav')"""

    # another example

    for file in audio_files:
        name, ext = os.path.splitext(file)
        sound=AudioSegment.from_file(file)
        print(sound)
        sound=sound.set_frame_rate(8000)    #to set sample rate 32KHz
        sound=sound.set_channels(1)
        channel_count = sound.channels
        print(channel_count)
        sound.export("{0}.wav".format(name), format="wav", bitrate="1024k")  # rename them using the old name + ".wav"
#


# # You dont need the number of files in the folder, just iterate over them directly using:

        # spliting the file into the name and the extension
    # for file in audio_files:
    #     name, ext = os.path.splitext(file)
    #     if ext == ".wav":
    #         aiff_sound=AudioSegment.from_file(file)
    #         #mp3_sound = AudioSegment.from_mp3(file)
    #         #aiff_sound =aiff_sound.set_frame_rate(32000)
    #         #aiff_sound=aiff_sound.set_channels(1)
    #
    #         aiff_sound.export("{0}.flac".format(name), format="flac")

    # for file in audio_files:
    #     name, ext = os.path.splitext(file)
    #     print(name, ext)
    #
    #     if ext .endswith !=('.wav' ):  #  to convert .wav from ext
    #         sound=AudioSegment.from_file(file)
    #         print(sound)
    #         sound=sound.set_frame_rate(24000)    #to set sample rate 32KHz
    #         sound=sound.set_channels(1)
    #         channel_count = sound.channels
    #         print(channel_count)
    #
    #
    #
    #         sound.export("{0}.wav".format(name), format="wav", bitrate="1024k")  # rename them using the old name + ".wav"
    #


# Driver code
if __name__ == '__main__':
    # calling main() function
    main()

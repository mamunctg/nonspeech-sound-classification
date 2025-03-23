#http://pydub.com/


import glob
import os
from pydub import AudioSegment
import audiosegment


# Function to convert multiple files
def main():
    """audio_files=os.listdir('/home/mamun/Downloads/test/')
    #Folder is having audio files of both MP3 and WAV formats
    len_audio=len(audio_files)
    print(len_audio)

    for i in range(len_audio):
        if os.path.splitext(audio_files[i])[1]==".mp3":
            mp3_sound =AudioSegment.from_mp3(audio_files[i])
            mp3_sound.export('</home/mamun/Downloads/test/>\\converted.wav', format='wav')"""

    # another example

    path = "/~/final/fold_6_sneeze/"

    # Change working directory
    os.chdir(path)

    audio_files = os.listdir()


    for file in audio_files:
        name, ext = os.path.splitext(file)
        if ext.endswith('.wav'):  # to convert from ext
            global sound
            sound=audiosegment.from_file(file)
            print(sound)
            #sound = AudioSegment.from_file(file)
            sound2=sound.resample(channels=1)


            #sound = sound.set_channels(1)  # to set sample rate

            #sound1.export("{0}.wav".format(name), format="wav")  # rename them using the old name + ".wav"

    # # You dont need the number of files in the folder, just iterate over them directly using:

    #     # spliting the file into the name and the extension
    #     name, ext = os.path.splitext(file)
    #     if ext == ".flac":
    #         aiff_sound=AudioSegment.from_file(file)
    #         #mp3_sound = AudioSegment.from_mp3(file)
    #
    #         aiff_sound.export("{0}.wav".format(name), format="wav")

    # for file in audio_files:
    #     name, ext = os.path.splitext(file)
    #     if ext.endswith('.wav'):  # to convert from ext
    #
    #         sound = AudioSegment.from_file(file)
    #
    #         sound = sound.set_frame_rate(32000)  # to set sample rate
    #
    #         sound.export("{0}.wav".format(name), format="wav")  # rename them using the old name + ".wav"


# Driver code
if __name__ == '__main__':
    # calling main() function
    main()

import glob
import os
import shutil
import pydub
from pydub import AudioSegment

path = '/~/xyz_prac/man yawn/tone2'
destination='/~/Desktop/11'

# Change working directory
os.chdir(path)

audio_files = os.listdir()
# Function to convert multiple files
def main():
    """audio_files=os.listdir('/home/mamun/Downloads/test/')
    #Folder is having audio files of both MP3 and WAV formats
    len_audio=len(audio_files)
    print(len_audio)

    for i in range(len_audio):
        if os.path.splitext(audio_files[i])[1]==".mp3":
            mp3_sound =AudioSegment.from_mp3(audio_files[i])
            mp3_sound.export('</~/Downloads/test/>\\converted.wav', format='wav')"""

    # another example

    for item in audio_files:
        if item.endswith("_0.wav"):
            shutil.move(item, dst=destination)




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









# Driver code
if __name__ == '__main__':
    # calling main() function
    main()

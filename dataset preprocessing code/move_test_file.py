import glob
import os
import shutil
import pydub
from pydub import AudioSegment

#path = 'E:\\ubuntu file\\bridge W&U\\ANonspeech\\test rsl\\aug\\'
#destination='E:\\ubuntu file\\bridge W&U\\ANonspeech\\Atest raw\\'

path='/~/M_DB/sess_25/'
destination='/~/process_DB/sess_25/'
# Change working directory
# os.chdir(path)
#
# audio_files = os.listdir()
# Function to convert multiple files
def main():
    """audio_files=os.listdir('/~/test/')
    #Folder is having audio files of both MP3 and WAV formats
    len_audio=len(audio_files)
    print(len_audio)

    for i in range(len_audio):
        if os.path.splitext(audio_files[i])[1]==".mp3":
            mp3_sound =AudioSegment.from_mp3(audio_files[i])
            mp3_sound.export('<~/Downloads/test/>\\converted.wav', format='wav')"""

    for filename in glob.iglob(path + '**/*.avi', recursive=True):
        print(filename)
        shutil.copy(filename, dst=destination)

    # another example

    # for item in audio_files:
    #     if item.endswith(".wav"):
    #         shutil.move(item, dst=destination)

    # for file in audio_files:
    #     name, ext = os.path.splitext(file)
    #     if ext == ".wav":
    #         filename_base = os.path.basename(file)
    #         filename = os.path.splitext(filename_base)[0]
    #         # data = AudioSegment.from_file(file)
    #         # length = data.duration_seconds
    #         # #print('first:', filename, 'length:', length)
    #         # chunk_lenght = 4  # pydub calcualte in milisec
    #         #
    #         # if length > chunk_lenght:
    #         #     continue
    #         # print(filename, length)
    #         # shutil.move(file, dst=destination)
    #         file_id=filename.split('_')[1]
    #         if file_id !='9':
    #             continue
    #         print(file)
    #         shutil.move(file, dst=destination)












# Driver code
if __name__ == '__main__':
    # calling main() function
    main()

import os
from pydub import AudioSegment
from pydub.utils import make_chunks
import glob



# path = "/~n/Downloads/test/"
#  #Change working directory
# os.chdir(path)
#
# audio_files = os.listdir()




def main(data_path, save_path):
    #path = '/home/mamun/Desktop/xyz1'

    # Change working directory
    #os.chdir(path)
    os.chdir(data_path)

    audio_files = os.listdir()


    print(audio_files)

    # Print the files
    i=0
    for elem in audio_files:
        filename_base = os.path.basename(elem)
        filename = os.path.splitext(filename_base)[0]
        print(filename)
        myaudio=AudioSegment.from_file(elem)
        chunk_lenght_ms=4000  #pydub calcualte in milisec
        chunks=make_chunks(myaudio, chunk_lenght_ms)  #Make chunks of one 4sec

        #export all of the individual chunks as wav file

        for i, chunk in enumerate(chunks):
            chunk_name=os.path.join(save_path, filename+'_' +str(i+1)+'.wav')
            chunk.export(chunk_name, format="wav" )

        i += 1











if __name__ == '__main__':
    data_path = '/~/7 class nonspeech/room/zapslat/laugh'
    save_path = '~/7 class nonspeech/room/zapslat/1/laugh'
    main(data_path, save_path)
import os
from pydub import AudioSegment
from pydub.utils import make_chunks



# path = "/home/mamun/Downloads/test/"
#  #Change working directory
# os.chdir(path)
#
# audio_files = os.listdir()




def main():
    path = '/~/FSD50_prc/exp_with_7class_10s/orig_train/Yawn/'
    out_path='/~/FSD50_prc/exp_with_7class_10s/wav_train/Yawn/'

    # Change working directory
    os.makedirs(out_path, exist_ok=True)
    os.chdir(path)

    audio_files = os.listdir()

    # Print the files
    i=0
    for elem in audio_files:
        filename_base = os.path.basename(elem)
        filename = os.path.splitext(filename_base)[0]
        print(filename)
        myaudio=AudioSegment.from_file(elem)
        chunk_lenght_ms=10000  #pydub calcualte in milisec
        chunks=make_chunks(myaudio, chunk_lenght_ms)  #Make chunks of one 4sec

        #export all of the individual chunks as wav file

        for i, chunk in enumerate(chunks):
            chunk_name=out_path+filename+'_' +str(i)+'.wav'
            chunk.export(chunk_name, format="wav")
        i += 1











if __name__ == '__main__':
    main()
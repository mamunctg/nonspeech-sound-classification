import pydub
from pydub import AudioSegment
from pydub.utils import make_chunks
import os
import glob
import shutil
#import pandas as pd
# path = '/home/mamun/Desktop/lebeling/test data(clips)/woman yawn test'
path = "/~/7 class nonspeech/room/zapslat/Fchunks/yawn"
audio_files=glob.glob(path+'**/*.wav', recursive=True)


#path = "E:\\ubuntu file\\nonspeech\\revised paper\\nonambience\\baby crying"

# Change working directory
# os.chdir(path)
#
# audio_files = os.listdir()

i=0
#for file in glob.glob(path):
for file in audio_files:
    name, ext = os.path.splitext(file)
    if ext == ".wav":
        filename_base=os.path.basename(file)
        filename = os.path.splitext(filename_base)[0]
        #print(filename)
        data=AudioSegment.from_file(file)
        length=data.duration_seconds
        #print('file name:',filename ,'file length:', length)
        chunk_lenght = float(500)  # pydub calcualte in milisec

        # #print(chunk_lenght)
        length_ms=float(length*1000)


        if length_ms < chunk_lenght:
            print(filename, length_ms)
            shutil.move(file, dst='/home/mamun/Desktop/111')
##################################################################################################
        # if length_ms < chunk_lenght:
        #     continue
        # print(filename, length)
        # chunk_lenght_ms=4000
        # chunks = make_chunks(data, chunk_lenght_ms)  # Make chunks of one 4sec
        # filename1=os.path.splitext(filename_base)[0]
        # for i, chunk in enumerate(chunks):
        #     chunk_name= filename +'-' +str(i+1)
        #     chunk.export("{0}.wav".format(chunk_name), format="wav")
        #     i += 1
        #     print(chunk)
        # #print(file)
        # os.remove(file)




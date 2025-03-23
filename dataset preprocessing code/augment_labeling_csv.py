import sys
import pydub
from pydub import AudioSegment
from pathlib import Path
#from pydub.utils import which
#AudioSegment.converter="E:\\important study content\\ffmpeg\\ffmpeg win64-static\\bin\\ffmpeg.exe"
#AudioSegment.converter="E:\\ffmpeg-4.3.1-win64-static\\bin\\ffmpeg.exe"
#from pydub.utils import make_chunks
import os
import shutil
import pandas as pd
path = 'E:\\~\\Atest raw\\'

#path = "E:\\ubuntu file\\nonspeech\\revised paper\\nonambience\\baby crying"

# Change working directory
os.chdir(path)

audio_files = os.listdir()
# print(audio_files)
m=[]
for file in audio_files:
    name, ext = os.path.splitext(file)
    if ext == ".wav":

        filename_base=os.path.basename(file)
        filename = os.path.splitext(filename_base)[0]

        Class_ID = filename.split("_")[1]

        augment_ID = filename.split("_")[2]

        if augment_ID.strip('-'):
            augment_ID1 = augment_ID.split('-')[0]
        else:
            augment_ID1 = augment_ID
        print(augment_ID1)




        # augment_ID1=augment_ID.split('-')[0]

        def CN(Class_ID):
            if Class_ID == '0':
                return "baby crying"
            elif Class_ID == '1':
                return "breath"
            elif Class_ID == '2':
                return "cough"
            elif Class_ID == '3':
                return "laugh"
            elif Class_ID == '4':
                return "man crying"
            elif Class_ID == '5':
                return "man yawn"
            elif Class_ID == '6':
                return "screaming"
            elif Class_ID == '7':
                return "sneeze"
            elif Class_ID == '8':
                return "woman crying"
            else:
                return "woman yawn"


        Class_Name = CN(Class_ID)


        def AI(augment_ID1):
            if augment_ID1 == '0':
                return "original"
            elif augment_ID1 == '1':
                return "median filter"
            elif augment_ID1 == '2':
                return "custom augmentation "
            elif augment_ID1 == '3':
                return "extract loudest"
            elif augment_ID1 == '4':
                return "normalize"
            elif augment_ID1 == '5':
                return "gaussian white noise"
            elif augment_ID == '6':
                return "gain"
            elif augment_ID1 == '7':
                return "cropping"
            elif augment_ID1 == '8':
                return "fade in and out"
            elif augment_ID1 == '9':
                return "slowdown"
            elif augment_ID1 == '10':
                return "speed"
            elif augment_ID1 == '11':
                return "change tone 1"
            elif augment_ID1 == '12':
                return "change tone 2"
            elif augment_ID1 == '13':
                return "shift time left 0.5s"
            elif augment_ID1 == '14':
                return "shift time left 1s"
            elif augment_ID1 == '15':
                return "shift time right 0.5s"
            else:
                return "shift time right 1s"


        Augemnt_Name = AI(augment_ID1)

        #file=os.path.join("C:\\Users\\mmren\\Desktop\\abc", file)
        # print(file)
        try:
            data=AudioSegment.from_file(file)
            Duration = data.duration_seconds
            channel = data.channels
            frame_rate = data.frame_rate
            max_possible_amplitude = data.max_possible_amplitude
        except Exception:
            pass





        m.append([filename_base, Class_ID, Class_Name, augment_ID1, Augemnt_Name, Duration, channel, frame_rate])

        print(m)

        # for i in m:
        #     print(i)

#df = pd.DataFrame(m, columns=['filename_base', 'Class_ID', 'Class_Name', 'augment_ID', 'Augemnt_Name', 'Duration',
#                              'Channel', 'Frame_rate','Max_possible_amplitude'])
df = pd.DataFrame(m, columns=['filename_base', 'Class_ID', 'Class_Name', 'augment_ID', 'Augemnt_Name', 'Duration',
                            'Channel', 'Frame_rate'])

df.to_csv("C:\\~111\\40k_all_test.csv", index=False)  # create csv from df

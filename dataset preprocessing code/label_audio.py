#https://stackoverflow.com/questions/678236/how-to-get-the-filename-without-the-extension-from-a-path-in-python

#how to labelling files

#https://librosa.github.io/librosa/generated/librosa.core.load.html

import os
from os import path
from glob import glob
import pandas as pd
import wave
import librosa
import numpy as np
import contextlib
from pydub import AudioSegment


rootdir="/~/Downloads/final/"


#################################################################################################
m=[]

for subdir, dir, files in os.walk(rootdir):
    for file in files:

        filepath = subdir + os.sep +file
        filename_base = os.path.basename(filepath)
        filename = os.path.splitext(filename_base)[0]
        file_ext = filename_base.split(".")[-1]
        sound=AudioSegment.from_wav(filepath)

        Duration= len(sound)/1000

        FS_ID=filename.split("-")[0]
        Class_ID=filename.split("-")[-2]
        Folder_No=filename.split("-")[-1]


        def CN(Class_ID):
            if Class_ID == '0':
                return "crying_adult"
            elif Class_ID == '1':
                return "crying_infant"
            elif Class_ID == '2':
                return "laugh"
            elif Class_ID == '3':
                return "screeming"
            elif Class_ID == '4':
                return "sigh"
            else:
                return "sneeze"
        Class_Name=CN(Class_ID)

        def FN(Folder_No):
            if Folder_No == '1':
                return "fold_1_crying_adult"
            elif Folder_No== '2':
                return "fold_2_crying_infant"
            elif Folder_No== '3':
                return "fold_3_laugh"
            elif Folder_No == '4':
                return "fold_4_screaming"
            elif Folder_No == '5':
                return "fold_5_sigh"
            else:
                return "fold_6_sneeze"

        Folder_Name=FN(Folder_No)


        m.append([filename, file_ext, Duration,FS_ID,Class_ID,Class_Name,Folder_No, Folder_Name])
        #print(m)




df = pd.DataFrame(m, columns=['Filename', 'File_ext', 'Duration','FS_ID','Class_ID','Class_Name','Folder_No', 'Folder_Name']) # create a dataframe from match list

df.to_csv("expression_audiodataset.csv", index=False) # create csv from df


#################################################################


# Your new sampling rate



#         #if file.endswith('.wav'):   #read all .wav file
#         src=librosa.util.example_audio_file()
#         y, sr=librosa.load(src, sr=41000)  #resample all
#         file_wav=librosa.output.write_wav(src, y, sr)  #conver all files in .wav
#         sample_rate=sr
#
#         clip_duration=librosa.get_duration(y=y, sr=sr)
#         #print(clip_duration)
#
#
#         m.append([filepath, filename, file_ext,label,sample_rate,clip_duration])
#
# df = pd.DataFrame(m, columns=['filename_base', 'filename','file_ext','label','sample_rate', 'clip_duration']) # create a dataframe from match list
# df.to_csv("my_library1111.csv", index=False) # create csv from df



# # Read file
# for subdir, dir, files in os.walk(rootdir):
#     for file in files:
#
#
#         filename=librosa.util.example_audio_file(file)
#         # filepath=subdir + os.sep + file
#         # if filepath.endswith(".wav"):
#         y, sr=librosa.load(filename)
#
#
#         # sampling_rate, data =librosa.
#         # print(sampling_rate)



# # Resample data
# number_of_samples = round(len(data) * float(new_rate) / sampling_rate))
# data = sps.resample(data, number_of_samples)


"""
m=[]

for subdir, dir, files in os.walk(rootdir):
    for file in files:

        # filepath = subdir + os.sep +file
        # filename_base = os.path.basename(filepath)
        # filename = os.path.splitext(filename_base)[0]
        # print(filename)
        # label=filename.split("_")[-1]
        # print(label)
        # file_ext=filename_base.split(".")[-1]
        # print(file_ext)

        #duration=librosa.get_duration(filename=librosa.util.example_audio_file())

        with contextlib.closing(wave.open(file, 'r')) as f:
            frames=f.getnframes()
            rate=f.getframerate()
            duration=frames/float(rate)
            print(duration)
#         m.append([filepath, filename, file_ext,label, duration])
#
#
# df = pd.DataFrame(m, columns=['filename_base', 'filename','file_ext','label', 'duration']) # create a dataframe from match list
# df.to_csv("my_library1111.csv", index=False) # create csv from df"""



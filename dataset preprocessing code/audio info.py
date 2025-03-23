import pydub
from pydub import AudioSegment
import os
import pandas as pd
path = '/~/Desktop/abc/cough'
#path = "/home/mamun/Downloads/current work/all_data"
#path = "E:\\ubuntu file\\nonspeech\\revised paper\\nonambience\\baby crying"

# Change working directory
os.chdir(path)

audio_files = os.listdir()
m=[]
# example
for file in audio_files:
    name, ext = os.path.splitext(file)
    if ext == ".wav":
        filename=os.path.basename(file)
        data=AudioSegment.from_file(file)
        length=data.duration_seconds

        m.append([filename, length])
df=pd.DataFrame(m, columns=['filename', 'length'])

        # channel=data.channels
        # frame_rate=data.frame_rate
        # length=data.duration_seconds
        # f_width=data.frame_width
        # f_dB=data.dBFS
        # f_DB=data.dBFS
        # sample_width=data.sample_width
        # frame_count=data.frame_count(ms=None)
        # highest_dB=data.max_dBFS
        # highest_amplitude=data.max_possible_amplitude
        # value_RMS=data.rms
        # data_maximum=data.max
        # data_type=data.array_type


        #m.append([ filename, channel,frame_rate,length,f_width,f_dB,sample_width,frame_count,highest_amplitude, highest_dB,value_RMS,data_maximum,data_type ])

#df=pd.DataFrame(m, columns=['filename', 'channel','frame_rate','length','f_width','f_dB','sample_width','frame_count','highest_amplitude', 'highest_dB','value_RMS','data_maximum','data_type'])

print(df)
#df.to_csv("woman yawn_info.csv", index=False) # create csv from df

df.to_csv("woman yawn_info.csv", index=False) # create csv from df




        #print(data1, data2, data3, data4, data5,data6, data7, data8, data9,data10, data11, data12)




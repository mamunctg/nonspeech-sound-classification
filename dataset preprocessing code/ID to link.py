import pydub
from pydub import AudioSegment
import os
import pandas as pd
path = '/~/xyz1/xyz2/cough'


# Change working directory
os.chdir(path)

audio_files = os.listdir()
m=[]
# example
for file in audio_files:
    name, ext = os.path.splitext(file)
    if ext == ".wav":
        filename=os.path.basename(file)
        file_ID=filename.split('=')[0]

        #user_name=filename.split('_')[2]
        class_name='cough'
        user_name = filename.split('=')[1]
        file_ID = file_ID + '-'+class_name +'-'+'aigei'


        #link='https://freesound.org/people/' + user_name+ '/sounds/'+file_ID+'/'
        link='http://www.aigei.com/sound/'
        print(link)
        # data=AudioSegment.from_file(file)
        #
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
        m.append([file_ID, class_name, user_name, link ])
#df=pd.DataFrame(m, columns=['filename', 'channel','frame_rate','length','f_width','f_dB','sample_width','frame_count','highest_amplitude', 'highest_dB','value_RMS','data_maximum','data_type'])
df=pd.DataFrame(m, columns=['file_ID', 'class_name', 'user_name', 'link'])
print(df)


df.to_csv("baby crying.csv", index=False) # create csv from df




        #print(data1, data2, data3, data4, data5,data6, data7, data8, data9,data10, data11, data12)




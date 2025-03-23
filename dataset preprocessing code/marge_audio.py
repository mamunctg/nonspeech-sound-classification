#https://stackoverflow.com/questions/61499350/combine-audio-files-in-python

import os

from pydub import AudioSegment

#Change to  current directory
path="/~/xyz_prac/baby crying/noise-car"

os.chdir(path)
audio_files=os.listdir(path)


def main():


    for file in audio_files:
        name, ext = os.path.splitext(file)
        if ext.endswith('.wav'):
            sound1=AudioSegment.from_file(file)
            sound2=AudioSegment.from_file("/~/car_ambience.wav", format="wav")
            # sound1 6 dB louder
            louder = sound1 + 5


            combined = louder.overlay(sound2,position=0)
            combined  = combined.set_frame_rate(32000)   #to set new sampling rate
            combined = combined.set_channels(1)          #to set new channel

            combined.export("{0}.wav".format(name), format="wav")
            print("combining file", name)


if __name__ == '__main__':
    main()








import os

import soundfile


path = '/~/exp_with_7class/nonspeech7K/yawn/'

# Change working directory
os.chdir(path)

audio_files = os.listdir()
# Function to convert multiple files
def main():
    for file in audio_files:
        name, ext = os.path.splitext(file)
        data, samplerate = soundfile.read(file)
        soundfile.write("{0}.wav".format(name), data, samplerate, subtype='PCM_16')
        print('processing------------------')


if __name__ == '__main__':
    # calling main() function
    main()
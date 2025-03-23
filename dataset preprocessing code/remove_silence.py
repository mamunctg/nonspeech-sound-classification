# From https://stackoverflow.com/questions/29547218/
# remove-silence-at-the-beginning-and-at-the-end-of-wave-files-with-pydub



from pydub import AudioSegment
import  os
import glob



path = "~p/7 class nonspeech/room/zapslat/Fchunks/"
audio_files=glob.glob(path+'**/*.wav', recursive=True)
print(audio_files)
# Change working directory
#os.chdir(path)

#audio_files = os.listdir()

    # # You dont need the number of files in the folder, just iterate over them directly using:

        # spliting the file into the name and the extension


def detect_leading_silence(sound, silence_threshold=-60.0, chunk_size=10):
    '''
    sound is a pydub.AudioSegment
    silence_threshold in dB
    chunk_size in ms

    iterate over chunks until you find the first one with sound
    '''
    trim_ms = 0 # ms

    assert chunk_size > 0 # to avoid infinite loop
    while sound[trim_ms:trim_ms+chunk_size].dBFS < silence_threshold and trim_ms < len(sound):
        trim_ms += chunk_size

    return trim_ms

if __name__ == '__main__':
    for file in audio_files:
        name, ext = os.path.splitext(file)
        if ext == ".wav":
            sound=AudioSegment.from_file(file)
            start_trim = detect_leading_silence(sound)
            end_trim = detect_leading_silence(sound.reverse())

            duration = len(sound)
            trimmed_sound = sound[start_trim:duration - end_trim]
            len_trimed = len(trimmed_sound)
            trimmed_sound.export("{0}.wav".format(name), format="wav")
            print(name,"original=", duration, 'current len=== ',len_trimed)
        else:
            print(name)


https://github.com/jiaaro/pydub/



import pydub
from pydub import AudioSegment
from pydub.silence import split_on_silence, detect_silence, detect_nonsilent
from pydub.silence import split_on_silence
import os
from pydub.playback import play


# """path = "/home/mamun/Downloads/test/"
# os.chdir(path)
#
# audio_files = os.listdir()"""
#
# song = AudioSegment.from_wav("408211.wav")
# print(song)
#
# #slice audio
# #pydub does things in milliseconds
# ten_seconds=10*1000
#
# firt_10_seconds=song[:ten_seconds]  #first 10 second of file
#
# last_5_seconds=song[-5000:]     #last 5 seconds
#
# print(len(firt_10_seconds), len(last_5_seconds))
# ##Make begginer lauder and the end quiter
#
# #boost volume by 6dB
#
# beginning =firt_10_seconds + 6
# end =last_5_seconds -3
#
#
# #Concatenate audio(add one file to the end of anoter)
#
# without_the_middle = beginning + end
#
# #How long is it?
#
# without_the_middle.duration_seconds == 15.0
#
# #AudioSegments are immutable
#
# #song is not mofifed
# backeards = song.reverse()
#
# #Crossfade(again , beggining and end are not modified)
#
# #1.5 second crossfade
#
# with_style=beginning.append(end, crossfade=1500)
#
# #repeat the clip twide
#
# do_it_over = with_style*2
#
# #Fade (note that you can chain operations because evrything returns an AudioSegment)
#
# #2 sec fade in, 3 sec fade out
#
# awesome = do_it_over.fade_in(2000).fade_out(3000)
#
# #Save the results(again wahtever ffmpeg supports)
#
# awesome.export("mashup", format="wav")
#
# #save the results with tags(metadata)
#awesome.export("cry.wav", format="wav",  tags={'artist': 'Various artists', 'album':'Best of 2019', 'commments':'This album is awesome!'})

"""
Playback

You can play audio if you have one of these installed (simpleaudio strongly recommended, even if you are installing ffmpeg/libav):

    simpleaudio
    pyaudio
    ffplay (usually bundled with ffmpeg, see the next section)
    avplay (usually bundled with libav, see the next section)



"""

sound= AudioSegment.from_file("cry.wav", format="wav")
play(sound)





# def detect_leading_silence(sound, silence_thresold=50.0, chunk_size=10):
#     '''
#     sound is a pydub.AudionSegment
#     silice_thresold in dB
#     chunk_size in ms
#
#     itereate over chunks until you find the first one with sound
#
#     :param sound:
#     :param silence_thresold:
#     :param chunk_size:
#     :return:
#     '''
#
#     trim_ms = 0  #ms
#     assert chunk_size > 0  #to avoid infinite loop
#     while sound[trim_ms:trim_ms+chunk_size].dBFS< silence_thresold and trim_ms < len(sound):
#         trim_ms +=chunk_size
#
#     return trim_ms
# sound = AudioSegment.from_file("41328-0-0-1.wav", format="wav")
#
# # sample_rate=sound.frame_rate(sound)
# # frameCount=sound.frame_count(sound)
# # frameLength=sound.frame_width(sound)
# #
# # print(sample_rate, frameCount, frameCount)
#
# start_trim = detect_leading_silence(sound)
# end_trim = detect_leading_silence(sound.reverse())
#
# duraion=len(sound)
# print(duraion)
# trimmed_sound=sound[start_trim:duraion-end_trim]
# print(len(trimmed_sound))
# trimmed_sound.export('a111', format='wav')
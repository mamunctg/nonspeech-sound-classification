from pydub import AudioSegment
song = AudioSegment.from_wav("airplane_ambience.wav")
# ten_seconds = 4 * 1000
#
# first_4_seconds = song[:ten_seconds]
#
# first_4_seconds.export("car_ambience.wav", format="wav")
print(song.duration_seconds)
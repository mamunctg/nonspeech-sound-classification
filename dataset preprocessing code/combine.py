from pydub import AudioSegment
sound1 = AudioSegment.from_file("/~11/13802-2_0_0.wav", format="wav")
sound2 = AudioSegment.from_file("/~/11/airplane_ambience.wav", format="wav")

# sound1 6 dB louder
louder = sound1 + 5


# sound1, with sound2 appended (use louder instead of sound1 to append the louder version)
#Overlay sound2 over sound1 at position 0  (use louder instead of sound1 to use the louder version)
overlay = louder.overlay(sound2, position=0)

# simple export
file_handle = overlay.export("/~/final+airp222l.wav", format="wav")
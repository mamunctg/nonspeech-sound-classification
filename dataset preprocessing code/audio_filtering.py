from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_wav("bells001.wav")
new = song.low_pass_filter(10000)

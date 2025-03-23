import nlpaug
import nlpaug.augmenter.audio as naa
from nlpaug.util.audio.visualizer import AudioVisualizer

import librosa
import numpy as np
import scipy.io.wavfile
import scipy.io.wavfile as scipy_io_wavfile

import librosa.display as librosa_display
import matplotlib.pyplot as plt

file_path='xyz/15_9_0.wav'
data, sr = librosa.load(file_path)
print(sr)
print(data.dtype)

##crop Augmenter
# aug=naa.CropAug(sampling_rate=sr)
# augmented_data=aug.augment(data)
# librosa.output.write_wav('file_trim_5s.wav', augmented_data, sr)

# aug = naa.VtlpAug(sampling_rate=sr)
# augmented_data = aug.augment(data)
# librosa.output.write_wav('vltp.wav', augmented_data, sr)

aug = naa.NoiseAug()
augmented_data = aug.augment(data)
librosa.output.write_wav('noise.wav', augmented_data, sr)

# librosa_display.waveplot(augmented_data, sr=sr, alpha=0.5)da
# librosa_display.waveplot(data, sr=sr, color='r', alpha=0.25)
# plt.tight_layout()
# plt.show()
#
 ###Loudness Augmentater
aug=naa.LoudnessAug()
augmented_data=aug.augment(data)
librosa.output.write_wav('xyz/file_trim_loud.wav', augmented_data, sr)
#
# librosa_display.waveplot(augmented_data, sr=sr, alpha=0.25)
# librosa_display.waveplot(data, sr=sr, color='r', alpha=0.5)
#
# plt.tight_layout()
# plt.show()
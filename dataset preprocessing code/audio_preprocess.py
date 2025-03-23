#https://www.kaggle.com/taqanori/trying-mfcc-mel-frequency-cepstral-coefficients
#https://haythamfayek.com/2016/04/21/speech-processing-for-machine-learning.html#fnref:1




# import scipy.io.wavfile
# from scipy.fftpack import dct
# import scipy.io.wavfile as wav
# import pydub
# #from pydub import audio_segment
#
# import glob


from pydub import AudioSegment
import audiosegment
import matplotlib.pyplot as plt
import numpy as np
import librosa
from python_speech_features import mfcc
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
import scipy.io.wavfile as wav
import os

path="~/audio_process/"

os.chdir(path)


import librosa, librosa.display
y, sr=librosa.load('81883-0-5-6.wav')
mfcc =librosa.feature.mfcc(y, sr)
plt.figure(figsize=(20,4))
librosa.display.specshow(mfcc, x_axis='time' )

#plt.pcolormesh(mfcc)
plt.colorbar()





plt.title('sneeze')
#plt.show()
plt.savefig('mfcc6.png')









# (rate,sig) = wav.read("172738-4-0-1.wav")
# from python_speech_features import mfcc
# from python_speech_features import logfbank
# import scipy.io.wavfile as wav
#
# (rate,sig) = wav.read("172738-4-0-1.wav")
# mfcc_feat = mfcc(sig,rate)
# fbank_feat = logfbank(sig,rate)
#
#
# #print(fbank_feat[1:3,:])
# print(mfcc_feat.shape)
# plt.matshow(mfcc_feat)
# plt.show()
# # plt.show()
# print(mfcc_feat)
# #plt.plot(mfcc_feat)
# plt.matshow(mfcc(mfcc_feat))
# plt.show()
##
#MFCC

# x, sr = librosa.load('172738-4-0-1.wav', sr = 8000)
# #n_fft = int(sr * 0.02)   # window length: 0.02 s
# hop_length = n_fft // 2  # usually one specifies the hop length as a fraction of the window length
# mfccs = librosa.feature.mfcc(x, sr=sr, n_mfcc=13, hop_length=hop_length, n_fft=n_fft)
# # check the dimensions
#
# print(mfccs.shape)
# plt.matshow(mfccs)
# plt.show()





#
#
# """
# ##spectrogram
#
# seg= audiosegment.from_file("172738-4-0-1.wav")
# seg = seg.resample(sample_rate_Hz=32000, sample_width=2, channels=1)
# freqs, times, amplitudes = seg.spectrogram(window_length_s=0.03, overlap=0.5)
# amplitudes = 10 * np.log10(amplitudes + 1e-9)
#
# plt.pcolormesh(times, freqs, amplitudes)
# plt.axis('on')
# plt.title('crying_adult')
# plt.xlabel("Time in Seconds")
# plt.ylabel("Frequency in Hz")
# #plt.show()
# plt.savefig('1.png')
# """
#
#
#
#
#
#
# """
#
# MFCC
#
# # from python_speech_features import mfcc
# # import matplotlib.pyplot as plt
# # import numpy as np
# # from matplotlib import cm
# #
# # import numpy as np
# # import matplotlib.pyplot as plt
# # from scipy.io import wavfile
# # from python_speech_features import mfcc, logfbank
# #
# # frequency_sampling, audio_signal = wavfile.read("172738-4-0-1.wav")
# #
# # #audio_signal = audio_signal[:15000]
# #
# # features_mfcc = mfcc(audio_signal, frequency_sampling)
# #
# # print('\nMFCC:\nNumber of windows =', features_mfcc.shape[0])
# # print('Length of each feature =', features_mfcc.shape[1])
# #
# #
# # features_mfcc = features_mfcc.T
#
#
#
#
# plt.matshow(features_mfcc)
#
# #plt.subplot(3,2,1)
# plt.title('crying_adult')
# #plt.axis('off')
# #plt.xlabel('time(s)')
# #plt.ylabel('mfcc coefficient')
# #plt.show()
# plt.savefig('1.png')"""
#
#
#
# """
# filterbank_features = logfbank(audio_signal, frequency_sampling)
#
# print('\nFilter bank:\nNumber of windows =', filterbank_features.shape[0])
# print('Length of each feature =', filterbank_features.shape[1])
#
# filterbank_features = filterbank_features.T
# plt.matshow(filterbank_features)
# plt.title('Filter bank')
# plt.show()
# """
####






# crying_adult
#
# sample_rate, signal = scipy.io.wavfile.read('172738-4-0-1.wav')
# Time=np.linspace(0, len(signal)/sample_rate, num=len(signal))
#
# print(sample_rate)
# plt.subplot(3, 2, 1)
# plt.tight_layout()
# plt.title('Crying_adult')
# plt.plot(Time, signal)
# plt.xlabel('time (s)')
# plt.ylabel('sample rate')
#
# #crying_ infant
#
# sample_rate, signal = scipy.io.wavfile.read('152007-3-1-2.wav')
# Time=np.linspace(0, len(signal)/sample_rate, num=len(signal))
#
# print(sample_rate)
# plt.subplot(3, 2, 2)
# plt.tight_layout()
# plt.title('crying_infant')
# plt.plot(Time, signal)
# plt.xlabel('time (s)')
# plt.ylabel('sample rate')
#
#
# #laugh
#
# sample_rate, signal = scipy.io.wavfile.read('55209-1-2-3.wav')
# Time=np.linspace(0, len(signal)/sample_rate, num=len(signal))
#
# print(sample_rate)
# plt.subplot(3, 2, 3)
# plt.tight_layout()
# plt.title('laugh')
# plt.plot(Time, signal)
# plt.xlabel('time (s)')
# plt.ylabel('sample rate')
#
#
# #screaming
#
# sample_rate, signal = scipy.io.wavfile.read('21742-0-3-4.wav')
# Time=np.linspace(0, len(signal)/sample_rate, num=len(signal))
#
# print(sample_rate)
# plt.subplot(3, 2, 4)
# plt.tight_layout()
# plt.title('screaming')
# plt.plot(Time, signal)
# plt.xlabel('time (s)')
# plt.ylabel('sample rate')
#
# #sigh
# sample_rate, signal = scipy.io.wavfile.read('403936-0-4-5.wav')
# Time=np.linspace(0, len(signal)/sample_rate, num=len(signal))
#
# print(sample_rate)
# plt.subplot(3, 2, 5)
# plt.tight_layout()
# plt.title('sigh')
# plt.plot(Time, signal)
# plt.xlabel('time (s)')
# plt.ylabel('sample rate')
#
#
# #sneeze
# sample_rate, signal = scipy.io.wavfile.read('81883-0-5-6.wav')
# Time=np.linspace(0, len(signal)/sample_rate, num=len(signal))
#
# print(sample_rate)
# plt.subplot(3, 2, 6)
# plt.tight_layout()
#
# plt.title('sneeze')
# plt.plot(Time, signal)
# plt.xlabel('time (s)')
# plt.ylabel('sample rate')
#
#
# #plt.show()
# plt.savefig("wave form of expression.png")



# print(signal)
# plt.figure(1,1,1)
# plt.title('signal wave of screaming ')
#
# plt.xlabel('time in second')
# plt.ylabel('sample rate')
# plt.show()
# plt.savefig('laugh.png')



#
# #emphasized_signal = np.append(signal[0], signal[1:] - pre_emphasis * signal[:-1])
# print(sample_rate, signal)
# plt.figure(1,2,1)
# plt.title('signal wave of screaming ')
# plt.plot(Time, signal)
# plt.xlabel('time in second')
# plt.ylabel('sample rate')
# #plt.show()
# #plt.savefig('sneeze.png')
#
#
# sample_rate, signal = scipy.io.wavfile.read('152007-3-1-2.wav')
# #signal =signal[0:int(sample_rate)]
# Time=np.linspace(0, len(signal)/sample_rate, num=len(signal))
# #print(sample_rate, signal)
# #emphasized_signal = np.append(signal[0], signal[1:] - pre_emphasis * signal[:-1])
# plt.figure(1,2,3)
# plt.title('signal wave of screaming ')
# plt.plot(Time, signal)
# plt.xlabel('time in second')
# plt.ylabel('sample rate')
# #plt.show()
# #plt.savefig('crying_infant.png')
#
# sample_rate, signal = scipy.io.wavfile.read('172738-4-0-1.wav')
# #signal =signal[0:int(sample_rate)]
# # Time=np.linspace(0, len(signal)/sample_rate, num=len(signal))
# # print(sample_rate, signal)
# # emphasized_signal = np.append(signal[0], signal[1:] - pre_emphasis * signal[:-1])
# plt.figure(2,1,1)
# plt.title('signal wave of screaming ')
# plt.plot(Time, signal)
# plt.xlabel('time in second')
# plt.ylabel('sample rate')
# #plt.show()
# #plt.savefig('crying_adult_em.png')
#
# sample_rate, signal = scipy.io.wavfile.read('403936-0-4-5.wav')
# #signal =signal[0:int(sample_rate)]
# Time=np.linspace(0, len(signal)/sample_rate, num=len(signal))
# # print(sample_rate, signal)
# # emphasized_signal = np.append(signal[0], signal[1:] - pre_emphasis * signal[:-1])
# plt.figure(2,2,1)
# plt.title('signal wave of screaming ')
# plt.plot(Time, signal)
# plt.xlabel('time in second')
# plt.ylabel('sample rate')
# #plt.show()
# #plt.savefig('sigh.png')
#
#
#
#
#
#
#
#
#





























#
#
#
#
# pre_emphasis=0.97
#
#
# # #Change working directory
# os.chdir(path)
#
# #
# # for file in glob.glob(path +'**/*', recursive=True):
# #sample_rate, signal=audio_segment.('OSR_us_000_0010_8k.wav')
# sample_rate, signal = scipy.io.wavfile.read('21742-0-3-4.wav')
# #signal =signal[0:int(sample_rate)]
# Time=np.linspace(0, len(signal)/sample_rate, num=len(signal))
# # print(sample_rate, signal)
# # emphasized_signal = np.append(signal[0], signal[1:] - pre_emphasis * signal[:-1])
# # plt.figure(1)
# # plt.title('signal wave of screaming ')
# # plt.plot(Time, signal)
# # plt.xlabel('time in second')
# # plt.ylabel('sample rate')
# # plt.show()
# # plt.savefig('screaming_em.png')
#
#
#
#
#
#
# Time=np.linspace(0, len(signal)/sample_rate, num=len(signal))
# print(sample_rate, signal)
# emphasized_signal = np.append(signal[0], signal[1:] - pre_emphasis * signal[:-1])
#
# ##############framing
# frame_size = 0.025
# frame_stride = 0.01
#
# frame_length, frame_step = frame_size * sample_rate, frame_stride * sample_rate  # Convert from seconds to samples
# signal_length = len(emphasized_signal)
# frame_length = int(round(frame_length))
# # frame_step = int(round(frame_step))
# # num_frames = int(np.ceil(float(np.abs(signal_length - frame_length)) / frame_step))  # Make sure that we have at least 1 frame
# #
# # pad_signal_length = num_frames * frame_step + frame_length
# # z = np.zeros((pad_signal_length - signal_length))
# # pad_signal = np.append(emphasized_signal, z) # Pad Signal to make sure that all frames have equal number of samples without truncating any samples from the original signal
# #
# # indices = np.tile(np.arange(0, frame_length), (num_frames, 1)) + np.tile(np.arange(0, num_frames * frame_step, frame_step), (frame_length, 1)).T
# # frames = pad_signal[indices.astype(np.int32, copy=False)]
#
# frames = np.hamming(frame_length)
# # plt.figure(1)
# # plt.title('Hamming Window from screaming')
# # plt.plot(frames)
# # plt.xlabel('samples')
# # plt.ylabel('amplitude')
# #plt.show()
# #plt.savefig('Hamming_window_screaming.png')
#
#
#
# #Fourier-Transform and Power Spectrum
#
# NFFT=512
#
# mag_frames = np.absolute(np.fft.rfft(frames, NFFT))  # Magnitude of the FFT
# pow_frames = ((1.0 / NFFT) * ((mag_frames) ** 2))  #
#
#
#
#
# ##Filter Banks
#
# nfilt=40
# low_freq_mel = 0
# high_freq_mel = (2595 * np.log10(1 + (sample_rate / 2) / 700))  # Convert Hz to Mel
# mel_points = np.linspace(low_freq_mel, high_freq_mel, nfilt + 2)  # Equally spaced in Mel scale
# hz_points = (700 * (10**(mel_points / 2595) - 1))  # Convert Mel to Hz
# bin = np.floor((NFFT + 1) * hz_points / sample_rate)
#
# fbank = np.zeros((nfilt, int(np.floor(NFFT / 2 + 1))))
# for m in range(1, nfilt + 1):
#     f_m_minus = int(bin[m - 1])   # left
#     f_m = int(bin[m])             # center
#     f_m_plus = int(bin[m + 1])    # right
#
#     for k in range(f_m_minus, f_m):
#         fbank[m - 1, k] = (k - bin[m - 1]) / (bin[m] - bin[m - 1])
#     for k in range(f_m, f_m_plus):
#         fbank[m - 1, k] = (bin[m + 1] - k) / (bin[m + 1] - bin[m])
# filter_banks = np.dot(pow_frames, fbank.T)
# filter_banks = np.where(filter_banks == 0, np.finfo(float).eps, filter_banks)  # Numerical Stability
# filter_banks = 20 * np.log10(filter_banks)  # dB

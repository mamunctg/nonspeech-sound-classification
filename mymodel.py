import keras.backend as K
from keras import regularizers
from keras.layers import Lambda
from keras.layers.convolutional import Conv1D, MaxPooling1D
from keras.layers import Conv1D, GlobalAveragePooling1D, MaxPooling1D,Flatten,Dropout
from keras.layers.core import Activation, Dense
from keras.layers.normalization import BatchNormalization
from keras.models import Sequential

from constants import *


def m3(num_classes=10):
    print('Using Model M3=alexnet')
    m = Sequential()
    # 1st Convolutional Layer
    m.add(Conv1D(96, 3, input_shape=[AUDIO_LENGTH, 1], strides=2, padding='same'))
    m.add(BatchNormalization())
    m.add(Activation('relu'))
    m.add(MaxPooling1D(pool_size=2, strides=None)) #16000
    m.add(Dropout(0.3))

    # m.add(Conv1D(96,
    #              input_shape=[AUDIO_LENGTH, 1],
    #              kernel_size=80,
    #              strides=4,
    #              padding='same',
    #              kernel_initializer='glorot_uniform'))
    #              #kernel_regularizer=regularizers.l2(l=0.0001)))
    # m.add(BatchNormalization())
    # m.add(Dropout(0.2))
    # m.add(Activation('relu'))
    # m.add(MaxPooling1D(pool_size=4, strides=None))

    # 2nd Convolutional Layer
    m.add(Conv1D(256, kernel_size=3, strides=2, padding='same'))
    m.add(BatchNormalization())
    m.add(Activation('relu'))
    m.add(MaxPooling1D(pool_size=4, strides=None))
    m.add(Dropout(0.3))


    # m.add(Conv1D(256,
    #              kernel_size=3,
    #              strides=1,
    #              padding='same',
    #              kernel_initializer='glorot_uniform'))
    #              #kernel_regularizer=regularizers.l2(l=0.0001)))
    # m.add(BatchNormalization())
    # m.add(Dropout(0.2))
    # m.add(Activation('relu'))
    # m.add(MaxPooling1D(pool_size=4, strides=None))

    # # 3rd Convolutional Layer

    m.add(Conv1D(384, kernel_size=3, strides=1, padding='same'))
    m.add(BatchNormalization())
    m.add(Activation('relu'))
    m.add(MaxPooling1D(pool_size=4, strides=None))
    m.add(Dropout(0.3))

    # m.add(Conv1D(384,
    #              kernel_size=3,
    #              strides=1,
    #              padding='same',
    #              kernel_initializer='glorot_uniform'))
    #              #kernel_regularizer=regularizers.l2(l=0.0001)))
    # m.add(BatchNormalization())
    # m.add(Dropout(0.2))
    # m.add(Activation('relu'))
    # m.add(MaxPooling1D(pool_size=4, strides=None))

    # 4th Convolutional Layer
    m.add(Conv1D(384, kernel_size=3, strides=1, padding='same'))
    m.add(BatchNormalization())
    m.add(Activation('relu'))
    m.add(MaxPooling1D(pool_size=4, strides=None))
    m.add(Dropout(0.3))


    # m.add(Conv1D(384,
    #              kernel_size=3,
    #              strides=1,
    #              padding='same',
    #              kernel_initializer='glorot_uniform'))
    #              #kernel_regularizer=regularizers.l2(l=0.0001)))
    # m.add(BatchNormalization())
    # m.add(Dropout(0.2))
    # m.add(Activation('relu'))
    # m.add(MaxPooling1D(pool_size=3, strides=None))

    # 5th Convolutional Layer
    m.add(Conv1D(256, kernel_size=3, strides=1, padding='same'))
    m.add(BatchNormalization())
    m.add(Activation('relu'))
    m.add(MaxPooling1D(pool_size=4, strides=None))
    m.add(Dropout(0.3))

    # m.add(Conv1D(256,
    #              kernel_size=3,
    #              strides=1,
    #              padding='same',
    #              kernel_initializer='glorot_uniform'))
    #              #kernel_regularizer=regularizers.l2(l=0.0001)))
    # m.add(BatchNormalization())
    # m.add(Dropout(0.2))
    # m.add(Activation('relu'))
    # m.add(MaxPooling1D(3))


    #Passing it to a Fully Connected layer
    m.add(Flatten())
    # 1st Fully Connected Layer
    m.add(Dense(4096, activation='relu'))

    # 2nd Fully Connected Layer
    m.add(Dense(4096, activation='relu'))


    #Output Layer
    m.add(Dense(num_classes, activation='softmax'))

    return m

    # print('Using Model M3')
    # m = Sequential()
    # m.add(Conv1D(256,
    #              input_shape=[AUDIO_LENGTH, 1],
    #              kernel_size=80,
    #              strides=4,
    #              padding='same',
    #              kernel_initializer='glorot_uniform',
    #              kernel_regularizer=regularizers.l2(l=0.0001)))
    # m.add(BatchNormalization())
    # m.add(Activation('relu'))
    # m.add(MaxPooling1D(pool_size=4, strides=None))
    # m.add(Conv1D(256,
    #              kernel_size=3,
    #              strides=1,
    #              padding='same',
    #              kernel_initializer='glorot_uniform',
    #              kernel_regularizer=regularizers.l2(l=0.0001)))
    # m.add(BatchNormalization())
    # m.add(Activation('relu'))
    #
    # m.add(MaxPooling1D(pool_size=4, strides=None))
    # m.add(Lambda(lambda x: K.mean(x, axis=1))) # Same as GAP for 1D Conv Layer
    # m.add(Dense(num_classes, activation='softmax'))
    # return m


def m5(num_classes=10):
    print('Using Model M5=mycnn')
    m = Sequential()
    m.add(Conv1D(96,
                 input_shape=[AUDIO_LENGTH, 1],
                 kernel_size=80,
                 strides=4,
                 padding='same',
                 kernel_initializer='glorot_uniform'))
                 #kernel_regularizer=regularizers.l2(l=0.0001)))
    m.add(BatchNormalization())
    m.add(Dropout(0.2))
    m.add(Activation('relu'))

    m.add(MaxPooling1D(pool_size=4, strides=None))

    m.add(Conv1D(96,
                 kernel_size=3,
                 strides=1,
                 padding='same',
                 kernel_initializer='glorot_uniform'))
                 #kernel_regularizer=regularizers.l2(l=0.0001)))
    m.add(BatchNormalization())
    #m.add(Dropout(0.2))
    m.add(Activation('relu'))



    m.add(Conv1D(192,
                 kernel_size=3,
                 strides=1,
                 padding='same',
                 kernel_initializer='glorot_uniform'))
                 #kernel_regularizer=regularizers.l2(l=0.0001)))
    m.add(BatchNormalization())
    m.add(Dropout(0.2))
    m.add(Activation('relu'))



    m.add(Conv1D(192,
                 kernel_size=3,
                 strides=1,
                 padding='same',
                 kernel_initializer='glorot_uniform')),
                 #kernel_regularizer=regularizers.l2(l=0.0001)))
    m.add(BatchNormalization())
    #m.add(Dropout(0.2))
    m.add(Activation('relu'))
    m.add(MaxPooling1D(pool_size=4, strides=None))

    m.add(Conv1D(384,
                 kernel_size=3,
                 strides=1,
                 padding='same',
                 kernel_initializer='glorot_uniform'))
                 #kernel_regularizer=regularizers.l2(l=0.0001)))
    m.add(BatchNormalization())
    m.add(Dropout(0.2))
    m.add(Activation('relu'))



    m.add(Conv1D(384,
                 kernel_size=3,
                 strides=1,
                 padding='same',
                 kernel_initializer='glorot_uniform')),
                 #kernel_regularizer=regularizers.l2(l=0.0001)))
    m.add(BatchNormalization())
    #m.add(Dropout(0.2))
    m.add(Activation('relu'))
    m.add(MaxPooling1D(pool_size=4, strides=None))

    m.add(Conv1D(256,
                 kernel_size=3,
                 strides=1,
                 padding='same',
                 kernel_initializer='glorot_uniform')),
                 #kernel_regularizer=regularizers.l2(l=0.0001)))
    m.add(BatchNormalization())
    m.add(Dropout(0.2))
    m.add(Activation('relu'))



    m.add(Conv1D(256,
                 kernel_size=3,
                 strides=1,
                 padding='same',
                 kernel_initializer='glorot_uniform'))
                 #kernel_regularizer=regularizers.l2(l=0.0001)))
    m.add(BatchNormalization())
    #m.add(Dropout(0.2))
    m.add(Activation('relu'))



    m.add(Conv1D(256,
                 kernel_size=3,
                 strides=1,
                 padding='same',
                 kernel_initializer='glorot_uniform'))
                 #kernel_regularizer=regularizers.l2(l=0.0001)))
    m.add(BatchNormalization())
    #m.add(Dropout(0.2))
    m.add(Activation('relu'))
    m.add(MaxPooling1D(pool_size=4, strides=None))

    m.add(Conv1D(512,
                 kernel_size=3,
                 strides=1,
                 padding='same',
                 kernel_initializer='glorot_uniform')),
                 #kernel_regularizer=regularizers.l2(l=0.0001)))
    m.add(BatchNormalization())
    m.add(Dropout(0.2))
    m.add(Activation('relu'))


    m.add(Conv1D(512,
                 kernel_size=3,
                 strides=1,
                 padding='same',
                 kernel_initializer='glorot_uniform'))
                 #kernel_regularizer=regularizers.l2(l=0.0001)))
    m.add(BatchNormalization())
    m.add(Activation('relu'))


    m.add(Conv1D(512,
                 kernel_size=3,
                 strides=1,
                 padding='same',
                 kernel_initializer='glorot_uniform'))
                 #kernel_regularizer=regularizers.l2(l=0.0001)))
    m.add(BatchNormalization())
    m.add(Dropout(0.2))
    m.add(Activation('relu'))
    m.add(MaxPooling1D())


    m.add(Lambda(lambda x: K.mean(x, axis=1)))  # Same as GAP for 1D Conv Layer
    m.add(Dense(num_classes, activation='softmax'))


    # m.add(Lambda(lambda x: K.mean(x, axis=1))) # Same as GAP for 1D Conv Layer
    # m.add(Dense(num_classes, activation='softmax'))
    #keras.layers.core.Dropout(rate, noise_shape=None, seed=None)
    return m


def m11(num_classes=10):
    print('Using Model M11=VGG16')
    m = Sequential()

    m = Sequential()
    m.add(Conv1D(64, 3, input_shape=[AUDIO_LENGTH, 1], strides=2, padding='same'))
    m.add(BatchNormalization())
    m.add(Activation('relu'))
    m.add(Dropout(0.3))


    #Convolution_ block 1


    # m.add(Conv1D(64,
    #              input_shape=[AUDIO_LENGTH, 1],
    #              kernel_size=80,
    #              strides=4,
    #              padding='same',
    #              kernel_initializer='glorot_uniform'))
    #              #kernel_regularizer=regularizers.l2(l=0.0001)))
    # m.add(BatchNormalization())
    # m.add(Activation('relu'))

    m.add(Conv1D(64, 3, strides=1, padding='same'))
    m.add(BatchNormalization())
    m.add(Activation('relu'))
    m.add(MaxPooling1D(pool_size=4, strides=None))
    m.add(Dropout(0.3))
    # m.add(Conv1D(64,
    #              kernel_size=3,
    #              strides=1,
    #              padding='same',
    #              kernel_initializer='glorot_uniform'))
    #              #kernel_regularizer=regularizers.l2(l=0.0001)))
    # m.add(BatchNormalization())
    # m.add(Dropout(0.2))
    # m.add(Activation('relu'))
    # m.add(MaxPooling1D(pool_size=4, strides=None))




    #convolution_ block 2
    m.add(Conv1D(128, 3, strides=1, padding='same'))
    m.add(BatchNormalization())
    m.add(Activation('relu'))
    m.add(Dropout(0.3))

    #
    # m.add(Conv1D(128,
    #              kernel_size=3,
    #              strides=1,
    #              padding='same',
    #              kernel_initializer='glorot_uniform'))
    #              #kernel_regularizer=regularizers.l2(l=0.0001)))
    # m.add(BatchNormalization())
    # m.add(Activation('relu'))

    m.add(Conv1D(128, 3, strides=1, padding='same'))
    m.add(BatchNormalization())
    m.add(Activation('relu'))
    m.add(MaxPooling1D(pool_size=4, strides=None))
    m.add(Dropout(0.3))
    # m.add(Conv1D(128,
    #              kernel_size=3,
    #              strides=1,
    #              padding='same',
    #              kernel_initializer='glorot_uniform'))
    #              #kernel_regularizer=regularizers.l2(l=0.0001)))
    # m.add(BatchNormalization())
    # m.add(Dropout(0.2))
    # m.add(Activation('relu'))
    # m.add(MaxPooling1D(pool_size=4, strides=None))
    #

    #convolution block 3

    m.add(Conv1D(256, 3, strides=1, padding='same'))
    m.add(BatchNormalization())
    m.add(Activation('relu'))
    m.add(Dropout(0.3))

    # m.add(Conv1D(256,
    #              kernel_size=3,
    #              strides=1,
    #              padding='same',
    #              kernel_initializer='glorot_uniform'))
    #              #kernel_regularizer=regularizers.l2(l=0.0001)))
    # m.add(BatchNormalization())
    # m.add(Activation('relu'))

    m.add(Conv1D(256, 3, strides=1, padding='same'))
    m.add(BatchNormalization())
    m.add(Activation('relu'))
    m.add(Dropout(0.3))


    # m.add(Conv1D(256,
    #              kernel_size=3,
    #              strides=1,
    #              padding='same',
    #              kernel_initializer='glorot_uniform'))
    # # kernel_regularizer=regularizers.l2(l=0.0001)))
    # m.add(BatchNormalization())
    # m.add(Activation('relu'))

    m.add(Conv1D(256, 3, strides=1, padding='same'))
    m.add(BatchNormalization())
    m.add(Activation('relu'))
    m.add(MaxPooling1D(pool_size=4, strides=None))
    m.add(Dropout(0.3))


    # m.add(Conv1D(256,
    #              kernel_size=3,
    #              strides=1,
    #              padding='same',
    #              kernel_initializer='glorot_uniform'))
    # # kernel_regularizer=regularizers.l2(l=0.0001)))
    # m.add(BatchNormalization())
    # m.add(Dropout(0.2))
    # m.add(Activation('relu'))
    # m.add(MaxPooling1D(pool_size=4, strides=None))






    #convolution block 4
    m.add(Conv1D(512, 3, strides=1, padding='same'))
    m.add(BatchNormalization())
    m.add(Activation('relu'))
    m.add(Dropout(0.3))

    #
    # m.add(Conv1D(512,
    #              kernel_size=3,
    #              strides=1,
    #              padding='same',
    #              kernel_initializer='glorot_uniform'))
    #              #kernel_regularizer=regularizers.l2(l=0.0001)))
    # m.add(BatchNormalization())
    # m.add(Activation('relu'))
    #

    m.add(Conv1D(512, 3, strides=1, padding='same'))
    m.add(BatchNormalization())
    m.add(Activation('relu'))
    m.add(Dropout(0.3))


    # m.add(Conv1D(512,
    #              kernel_size=3,
    #              strides=1,
    #              padding='same',
    #              kernel_initializer='glorot_uniform'))
    #              #kernel_regularizer=regularizers.l2(l=0.0001)))
    # m.add(BatchNormalization())
    # m.add(Activation('relu'))

    m.add(Conv1D(512, 3, strides=1, padding='same'))
    m.add(BatchNormalization())
    m.add(Activation('relu'))
    m.add(MaxPooling1D(pool_size=4, strides=None))
    m.add(Dropout(0.3))

    # m.add(Conv1D(512,
    #              kernel_size=3,
    #              strides=1,
    #              padding='same',
    #              kernel_initializer='glorot_uniform'))
    #              #kernel_regularizer=regularizers.l2(l=0.0001)))
    # m.add(BatchNormalization())
    # m.add(Dropout(0.2))
    # m.add(Activation('relu'))
    # m.add(MaxPooling1D(pool_size=4, strides=None))

    m.add(Conv1D(512, 3, strides=1, padding='same'))
    m.add(BatchNormalization())
    m.add(Activation('relu'))
    m.add(Dropout(0.3))

    # m.add(Conv1D(512,
    #              kernel_size=3,
    #              strides=1,
    #              padding='same',
    #              kernel_initializer='glorot_uniform'))
    #              #kernel_regularizer=regularizers.l2(l=0.0001)))
    # m.add(BatchNormalization())
    # m.add(Activation('relu'))

    m.add(Conv1D(512, 3, strides=1, padding='same'))
    m.add(BatchNormalization())
    m.add(Activation('relu'))
    m.add(Dropout(0.3))

    # m.add(Conv1D(512,
    #              kernel_size=3,
    #              strides=1,
    #              padding='same',
    #              kernel_initializer='glorot_uniform'))
    # # kernel_regularizer=regularizers.l2(l=0.0001)))
    # m.add(BatchNormalization())
    # m.add(Activation('relu'))
    #
    m.add(Conv1D(512, 3, strides=1, padding='same'))
    m.add(BatchNormalization())
    m.add(Activation('relu'))
    m.add(MaxPooling1D(pool_size=4, strides=None))
    m.add(Dropout(0.3))
    # m.add(Conv1D(512,
    #              kernel_size=3,
    #              strides=1,
    #              padding='same',
    #              kernel_initializer='glorot_uniform'))
    # # kernel_regularizer=regularizers.l2(l=0.0001)))
    # m.add(BatchNormalization())
    # m.add(Dropout(0.2))
    # m.add(Activation('relu'))
    # m.add(MaxPooling1D(pool_size=2, strides=None))






    m.add(Flatten())
    m.add(Dense(4096, activation='relu'))
    m.add(Dense(4096, activation='relu'))
    m.add(Dense(num_classes, activation='softmax'))



    return m


def m_rec(num_classes=10):
    from keras.layers.recurrent import LSTM
    print('Using Model LSTM 1')
    m = Sequential()
    m.add(Conv1D(64,
                 input_shape=[AUDIO_LENGTH, 1],
                 kernel_size=80,
                 strides=4,
                 padding='same',
                 kernel_initializer='glorot_uniform',
                 kernel_regularizer=regularizers.l2(l=0.0001)))
    m.add(BatchNormalization())
    m.add(Activation('relu'))
    m.add(MaxPooling1D(pool_size=4, strides=None))
    m.add(LSTM(32,
               kernel_regularizer=regularizers.l2(l=0.0001),
               return_sequences=True,
               dropout=0.2))
    m.add(LSTM(32,
               kernel_regularizer=regularizers.l2(l=0.0001),
               return_sequences=False,
               dropout=0.2))
    m.add(Dense(32))
    m.add(Dense(num_classes, activation='softmax'))
    return m

def m18(num_classes=10):
    print('Using Model M18')
    m = Sequential()
    m.add(Conv1D(64, 3, input_shape=[AUDIO_LENGTH, 1], strides=2, padding='same'))
    m.add(BatchNormalization())
    m.add(Activation('relu'))
    m.add(MaxPooling1D(pool_size=4, strides=None))
    m.add(Dropout(0.3))
    # m.add(Conv1D(64,
    #              input_shape=[AUDIO_LENGTH, 1],
    #              kernel_size=80,
    #              strides=4,
    #              padding='same',
    #              kernel_initializer='glorot_uniform',
    #              kernel_regularizer=regularizers.l2(l=0.0001)))
    # m.add(BatchNormalization())
    # m.add(Activation('relu'))
    # m.add(MaxPooling1D(pool_size=4, strides=None))

    for i in range(4):
        m.add(Conv1D(64, 3, strides=1, padding='same'))
        m.add(BatchNormalization())
        m.add(Activation('relu'))
    m.add(MaxPooling1D(pool_size=4, strides=None))
    m.add(Dropout(0.3))
        # m.add(Conv1D(64,
        #              kernel_size=3,
        #              strides=1,
        #              padding='same',
        #              kernel_initializer='glorot_uniform',
        #              kernel_regularizer=regularizers.l2(l=0.0001)))
        # m.add(BatchNormalization())
        # m.add(Activation('relu'))
    # m.add(MaxPooling1D(pool_size=4, strides=None))

    for i in range(4):
        m.add(Conv1D(128, 3, strides=1, padding='same'))
        m.add(BatchNormalization())
        m.add(Activation('relu'))
    m.add(MaxPooling1D(pool_size=4, strides=None))
    m.add(Dropout(0.3))



    #     m.add(Conv1D(128,
    #                  kernel_size=3,
    #                  strides=1,
    #                  padding='same',
    #                  kernel_initializer='glorot_uniform',
    #                  kernel_regularizer=regularizers.l2(l=0.0001)))
    #     m.add(BatchNormalization())
    #     m.add(Activation('relu'))
    # m.add(MaxPooling1D(pool_size=4, strides=None))

    for i in range(4):
        m.add(Conv1D(256, 3, strides=1, padding='same'))
        m.add(BatchNormalization())
        m.add(Activation('relu'))
    m.add(MaxPooling1D(pool_size=4, strides=None))
    m.add(Dropout(0.3))
    #     m.add(Conv1D(256,
    #                  kernel_size=3,
    #                  strides=1,
    #                  padding='same',
    #                  kernel_initializer='glorot_uniform',
    #                  kernel_regularizer=regularizers.l2(l=0.0001)))
    #     m.add(BatchNormalization())
    #     m.add(Activation('relu'))
    # m.add(MaxPooling1D(pool_size=4, strides=None))

    for i in range(4):
        m.add(Conv1D(512, 3, strides=1, padding='same'))
        m.add(BatchNormalization())
        m.add(Activation('relu'))
    m.add(MaxPooling1D(pool_size=4, strides=None))
    m.add(Dropout(0.3))
        # m.add(Conv1D(512,
        #              kernel_size=3,
        #              strides=1,
        #              padding='same',
        #              kernel_initializer='glorot_uniform',
        #              kernel_regularizer=regularizers.l2(l=0.0001)))
        # m.add(BatchNormalization())
        # m.add(Activation('relu'))

    m.add(Lambda(lambda x: K.mean(x, axis=1))) # Same as GAP for 1D Conv Layer
    m.add(Dense(num_classes, activation='softmax'))



    return m
####################################
#ours 1

def ours1(num_classes=10):
    print('Using Model ours1, modified after 17.1.20 ')
    #obained result=61.13  not good


    # m = Sequential()
    # m.add(Conv1D(96, 80, input_shape=[AUDIO_LENGTH, 1], strides=4, activation='relu', padding='same',
    #                  kernel_regularizer=regularizers.l2(l=0.0001)))
    #
    # m.add(Conv1D(128, 2,strides=4, activation='relu', padding='same', kernel_regularizer=regularizers.l2(l=0.0001)))
    #
    # m.add(Conv1D(256, 2, strides=4,activation='relu', padding='same', kernel_regularizer=regularizers.l2(l=0.0001)))
    #
    # m.add(Conv1D(512, 2, strides=4, activation='relu', padding='same', kernel_regularizer=regularizers.l2(l=0.0001)))
    #
    # m.add(MaxPooling1D(9))
    #
    # m.add(Flatten())
    #
    # m.add(Dense(4096, activation='relu'))
    # # model.add(Dropout(0.5))  ####no dropout at 8.20 model
    # m.add(Dense(4096, activation='relu'))
    # # model.add(Dropout(0.5))
    # m.add(Dense(num_classes, activation='softmax'))

    m = Sequential()
    m.add(Conv1D(64, 3, input_shape=[AUDIO_LENGTH, 1],strides=1, padding='same'))  # kernel_initializer='glorot_uniform', kernel_regularizer=regularizers.l2(l=0.001)))
    m.add(BatchNormalization())
    m.add(Activation('relu'))
    #m.add(MaxPooling1D(pool_size=4, strides=None))
    m.add(Dropout(0.3))

    m.add(Conv1D(64, 3,strides=1,
                     padding='same'))  # , kernel_initializer='glorot_uniform',kernel_regularizer=regularizers.l2(l=0.001)))
    m.add(BatchNormalization())
    m.add(Activation('relu'))
    m.add(MaxPooling1D(pool_size=8, strides=None))
    m.add(Dropout(0.3))

    m.add(Conv1D(128, 3,strides=1,
                     padding='same'))  # kernel_initializer='glorot_uniform', kernel_regularizer=regularizers.l2(l=0.001)))
    m.add(BatchNormalization())
    m.add(Activation('relu'))
    # model.add(MaxPooling1D(pool_size=2, strides=None))
    m.add(Dropout(0.3))

    m.add(Conv1D(128, 3,strides=1,
                     padding='same'))  # , kernel_initializer='glorot_uniform', kernel_regularizer=regularizers.l2(l=0.001)))
    m.add(BatchNormalization())
    m.add(Activation('relu'))
    m.add(MaxPooling1D(pool_size=8, strides=None))
    m.add(Dropout(0.3))

    m.add(Conv1D(256, 3,strides=1,
                     padding='same'))  # ,kernel_initializer='glorot_uniform', kernel_regularizer=regularizers.l2(l=0.001)))
    m.add(BatchNormalization())
    m.add(Activation('relu'))
    # model.add(MaxPooling1D(pool_size=2, strides=None))
    m.add(Dropout(0.3))

    m.add(Conv1D(256, 3,strides=1,
                     padding='same'))  # ,kernel_initializer='glorot_uniform', kernel_regularizer=regularizers.l2(l=0.001)))
    m.add(BatchNormalization())
    m.add(Activation('relu'))
    m.add(MaxPooling1D(pool_size=16, strides=None))
    m.add(Dropout(0.3))

    m.add(Lambda(lambda x: K.mean(x, axis=1)))  # Same as GAP for 1D Conv Layer
    m.add(Dense(10, activation='softmax'))

    return m


    # org model
    # m = Sequential()
    # m.add(Conv1D(96, 80, input_shape=[AUDIO_LENGTH, 1], strides=4, activation='relu', padding='same',
    #              kernel_regularizer=regularizers.l2(l=0.0001)))
    #
    # m.add(BatchNormalization())
    # m.add(Conv1D(128, 2, strides=4, activation='relu', padding='same', kernel_regularizer=regularizers.l2(l=0.0001)))
    #
    # m.add(Conv1D(256, 2, strides=4, activation='relu', padding='same', kernel_regularizer=regularizers.l2(l=0.0001)))
    #
    # m.add(Conv1D(512, 2, activation='relu', padding='same', kernel_regularizer=regularizers.l2(l=0.0001)))

    #
    # m.add(MaxPooling1D(4))
    #
    # m.add(Flatten())
    # # model.add(Dense(4096, activation='relu'))
    # m.add(Dense(4096, activation='relu'))
    # m.add(Dropout(0.5))
    # m.add(Dense(4096, activation='relu'))
    # m.add(Dropout(0.5))
    # m.add(Dense(num_classes, activation='softmax'))


#our1 network obtained result=63.20
    # m = Sequential()
    # m.add(Conv1D(96, 80, input_shape=[AUDIO_LENGTH, 1], strides=4, activation='relu', padding='same',
    #              kernel_regularizer=regularizers.l2(l=0.0001)))
    #
    # m.add(BatchNormalization())
    # m.add(Conv1D(128, 2, strides=4, activation='relu', padding='same', kernel_regularizer=regularizers.l2(l=0.0001)))
    # m.add(BatchNormalization())
    #
    # m.add(Conv1D(256, 2, strides=4, activation='relu', padding='same', kernel_regularizer=regularizers.l2(l=0.0001)))
    # m.add(BatchNormalization())
    #
    # m.add(Conv1D(512, 2, strides=4,activation='relu', padding='same', kernel_regularizer=regularizers.l2(l=0.0001)))
    # m.add(BatchNormalization())
    #
    # m.add(MaxPooling1D(4))
    #
    # m.add(Flatten())
    # # model.add(Dense(4096, activation='relu'))
    # m.add(Dense(4096, activation='relu'))
    # m.add(Dropout(0.4))
    # m.add(Dense(4096, activation='relu'))
    # m.add(Dropout(0.4))
    # m.add(Dense(num_classes, activation='softmax'))


    #return m

def ours2(num_classes=10):
    print('Using Model M5=ours-2')
    m = Sequential()
    #conv1
    m.add(Conv1D(96, 3, input_shape=[AUDIO_LENGTH, 1], strides=2, padding='same'))
    m.add(BatchNormalization())
    m.add(Activation('relu'))
    m.add(Dropout(0.3))

    # conv2
    m.add(Conv1D(96, 3, strides=1, padding='same'))
    m.add(BatchNormalization())
    m.add(Activation('relu'))
    m.add(MaxPooling1D(pool_size=4, strides=None))
    m.add(Dropout(0.3))



    #conv3
    m.add(Conv1D(192, kernel_size=3,strides=1, padding='same'))
    m.add(BatchNormalization())
    m.add(Activation('relu'))
    m.add(Dropout(0.3))

    #conv4
    m.add(Conv1D(192, kernel_size=3, strides=1, padding='same'))
    m.add(BatchNormalization())
    m.add(Activation('relu'))
    m.add(MaxPooling1D(pool_size=4, strides=None))
    m.add(Dropout(0.3))

    #conv5
    m.add(Conv1D(384, kernel_size=3, strides=1, padding='same'))
    m.add(BatchNormalization())
    m.add(Activation('relu'))
    m.add(Dropout(0.3))



    #conv6
    m.add(Conv1D(384, kernel_size=3, strides=1, padding='same'))
    m.add(BatchNormalization())
    m.add(Activation('relu'))
    m.add(MaxPooling1D(pool_size=4, strides=None))
    m.add(Dropout(0.3))



    #conv7
    m.add(Conv1D(256, kernel_size=3,strides=1, padding='same'))
    m.add(BatchNormalization())
    m.add(Activation('relu'))
    m.add(Dropout(0.3))


    #conv8
    m.add(Conv1D(256, kernel_size=3, strides=1, padding='same'))
    m.add(BatchNormalization())
    m.add(Activation('relu'))
    m.add(Dropout(0.3))

    #conv9
    m.add(Conv1D(256, kernel_size=3,strides=1,padding='same'))
    m.add(BatchNormalization())
    m.add(Activation('relu'))
    m.add(MaxPooling1D(pool_size=4, strides=None))
    m.add(Dropout(0.3))


    #conv 10
    m.add(Conv1D(512, kernel_size=3, strides=1, padding='same'))
    m.add(BatchNormalization())
    m.add(Activation('relu'))
    m.add(Dropout(0.3))

    #conv11
    m.add(Conv1D(512, kernel_size=3, strides=1, padding='same'))
    m.add(BatchNormalization())
    m.add(Activation('relu'))
    m.add(Dropout(0.3))

    #conv12
    m.add(Conv1D(512, kernel_size=3, strides=1,padding='same'))
    m.add(BatchNormalization())
    m.add(Activation('relu'))
    m.add(MaxPooling1D(pool_size=4, strides=None))
    m.add(Dropout(0.3))


    m.add(Lambda(lambda x: K.mean(x, axis=1)))  # Same as GAP for 1D Conv Layer
    m.add(Dense(num_classes, activation='softmax'))

    #ours 2 with 82.58 acc in raw + nanmabience

    # m.add(Conv1D(96,
    #              input_shape=[AUDIO_LENGTH, 1],
    #              kernel_size=80,
    #              strides=4,
    #              padding='same',
    #              kernel_initializer='glorot_uniform',
    #              kernel_regularizer=regularizers.l2(l=0.0001)))
    # m.add(BatchNormalization())
    # m.add(Dropout(0.2))
    # m.add(Activation('relu'))
    #
    # m.add(MaxPooling1D(4))
    #
    # #conv2
    # m.add(Conv1D(96,
    #              kernel_size=3,
    #              strides=1,
    #              padding='same',
    #              kernel_initializer='glorot_uniform',
    #              kernel_regularizer=regularizers.l2(l=0.0001)))
    # m.add(BatchNormalization())
    # # m.add(Dropout(0.2))
    # m.add(Activation('relu'))
    #
    # #conv3
    # m.add(Conv1D(192,
    #              kernel_size=3,
    #              strides=1,
    #              padding='same',
    #              kernel_initializer='glorot_uniform',
    #              kernel_regularizer=regularizers.l2(l=0.0001)))
    # m.add(BatchNormalization())
    # m.add(Dropout(0.2))
    # m.add(Activation('relu'))
    # #conv4
    # m.add(Conv1D(192,
    #              kernel_size=3,
    #              strides=1,
    #              padding='same',
    #              kernel_initializer='glorot_uniform',
    #              kernel_regularizer=regularizers.l2(l=0.0001)))
    # m.add(BatchNormalization())
    # #m.add(Dropout(0.2))
    # m.add(Activation('relu'))
    # m.add(MaxPooling1D(4))
    #
    # #conv5
    # m.add(Conv1D(384,
    #              kernel_size=3,
    #              strides=1,
    #              padding='same',
    #              kernel_initializer='glorot_uniform',
    #              kernel_regularizer=regularizers.l2(l=0.0001)))
    # m.add(BatchNormalization())
    # m.add(Dropout(0.2))
    # m.add(Activation('relu'))
    #
    # #conv6
    # m.add(Conv1D(384,
    #              kernel_size=3,
    #              strides=1,
    #              padding='same',
    #              kernel_initializer='glorot_uniform',
    #              kernel_regularizer=regularizers.l2(l=0.0001)))
    # m.add(BatchNormalization())
    # # m.add(Dropout(0.2))
    # m.add(Activation('relu'))
    # m.add(MaxPooling1D(4))
    #
    # #conv7
    # m.add(Conv1D(256,
    #              kernel_size=3,
    #              strides=1,
    #              padding='same',
    #              kernel_initializer='glorot_uniform',
    #              kernel_regularizer=regularizers.l2(l=0.0001)))
    # m.add(BatchNormalization())
    # m.add(Dropout(0.2))
    # m.add(Activation('relu'))
    #
    #
    # #conv8
    # m.add(Conv1D(256,
    #              kernel_size=3,
    #              strides=1,
    #              padding='same',
    #              kernel_initializer='glorot_uniform',
    #              kernel_regularizer=regularizers.l2(l=0.0001)))
    # m.add(BatchNormalization())
    # # m.add(Dropout(0.2))
    # m.add(Activation('relu'))
    #
    # #conv9
    # m.add(Conv1D(256,
    #              kernel_size=3,
    #              strides=1,
    #              padding='same',
    #              kernel_initializer='glorot_uniform',
    #              kernel_regularizer=regularizers.l2(l=0.0001)))
    # m.add(BatchNormalization())
    # # m.add(Dropout(0.2))
    # m.add(Activation('relu'))
    # m.add(MaxPooling1D(4))
    #
    # #conv 10
    # m.add(Conv1D(512,
    #              kernel_size=3,
    #              strides=1,
    #              padding='same',
    #              kernel_initializer='glorot_uniform',
    #              kernel_regularizer=regularizers.l2(l=0.0001)))
    # m.add(BatchNormalization())
    # m.add(Dropout(0.2))
    # m.add(Activation('relu'))
    #
    # #conv11
    # m.add(Conv1D(512,
    #              kernel_size=3,
    #              strides=1,
    #              padding='same',
    #              kernel_initializer='glorot_uniform',
    #              kernel_regularizer=regularizers.l2(l=0.0001)))
    # m.add(BatchNormalization())
    # m.add(Activation('relu'))
    #
    # #conv12
    # m.add(Conv1D(512,
    #              kernel_size=3,
    #              strides=1,
    #              padding='same',
    #              kernel_initializer='glorot_uniform',
    #              kernel_regularizer=regularizers.l2(l=0.0001)))
    # m.add(BatchNormalization())
    # m.add(Dropout(0.2))
    # m.add(Activation('relu'))
    # m.add(MaxPooling1D())
    #
    # m.add(Lambda(lambda x: K.mean(x, axis=1)))  # Same as GAP for 1D Conv Layer
    # m.add(Dense(num_classes, activation='softmax'))

    return m
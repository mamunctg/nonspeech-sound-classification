import os
import time
os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"]="0"

import sys

from keras.callbacks import Callback
from keras.callbacks import ReduceLROnPlateau
from keras.utils.np_utils import to_categorical

from file_logger import FileLogger
from model_data import DataReader
from model_resnet import resnet_34
from mymodel import *
#from models import *

from sklearn.metrics import classification_report, confusion_matrix
from sklearn import metrics



class MetricsHistory(Callback):
    def on_epoch_end(self, epoch, logs={}):
        file_logger.write([str(epoch),
                           str(logs['loss']),
                           str(logs['val_loss']),
                           str(logs['accuracy']),
                           str(logs['val_accuracy'])])

class test_out(Callback):
    def on_epoch_end(self, epoch, logs=None):
        Y_pred = model.predict(x_te, 867 // batch_size + 1)
        y_pred = np.argmax(Y_pred, axis=1)
        y_te_max = np.argmax(y_te, axis=1)
        y_classes = y_pred.argmax(axis=-1)
        target_names = ['breath', 'cough', 'crying', 'laugh', 'screaming', 'sneeze','yawn']

        print(confusion_matrix(y_te_max, y_pred))
        print(classification_report(y_te_max, y_pred, target_names=target_names))



if __name__ == '__main__':
    model_name = 'ours2'
    args = sys.argv
    if len(args) == 2:
        model_name = args[1].lower()
    #print('Model selected:', model_name)
    file_logger = FileLogger('out_{}.tsv'.format(model_name), ['step', 'tr_loss', 'te_loss',
                                                               'tr_acc', 'te_acc'])
    # model = None
    model = 'ours2'
    num_classes = 7
    if model_name == 'm3':
        model = m3(num_classes=num_classes)
    elif model_name == 'm5':
        model = m5(num_classes=num_classes)
    elif model_name == 'm11':
        model = m11(num_classes=num_classes)
    elif model_name == 'm18':
        model = m18(num_classes=num_classes)
    elif model_name == 'm34':
        model = resnet_34(num_classes=num_classes)

    elif model_name == 'ours1':
        model = ours1(num_classes=num_classes)

    elif model_name == 'ours2':
        model = ours2(num_classes=num_classes)

    if model is None:
        exit('Please choose a valid model: [m3, m5, m11, m18, m34,ours1,ours2]')

    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    print(model.summary())
    data_reader = DataReader()
    x_tr, y_tr = data_reader.get_all_training_data()
    import numpy as np
    correct_data_index = []
    for i in range(x_tr.shape[0]):
        if not np.isnan(np.max(x_tr[i])):
            correct_data_index.append(i)


    if len(correct_data_index) != x_tr.shape[0]:
        x_tr = x_tr[correct_data_index]
        y_tr = y_tr[correct_data_index]

    y_tr = to_categorical(y_tr, num_classes=num_classes)
    x_te, y_te = data_reader.get_all_testing_data()
    y_te = to_categorical(y_te, num_classes=num_classes)

    # if the accuracy does not increase over 10 epochs, we reduce the learning rate by half.
    reduce_lr = ReduceLROnPlateau(monitor='val_acc', factor=0.5, patience=10, min_lr=0.0001, verbose=2)
    metrics_history = MetricsHistory()
    test_out = test_out()
    batch_size = 64
    start = time.time()
    model.fit(x=x_tr,
              y=y_tr,
              batch_size=batch_size,
              epochs=5, #400
              verbose=2,
              shuffle=True,
              validation_data=(x_te, y_te),
              callbacks=[metrics_history, reduce_lr, test_out])
    print('Training took: %d seconds' % int(time.time() - start))
    print(model.summary())


    file_logger.close()
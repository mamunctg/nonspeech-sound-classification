
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import csv



loss_train = history.history['train_loss']
loss_val = history.history['val_loss']
epochs = range(1,35)
plt.plot(epochs, loss_train, 'g', label='Training loss')
plt.plot(epochs, loss_val, 'b', label='validation loss')
plt.title('Training and Validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()


# x = []
# y=[]
# csv_file = 'E:\\ubuntu file\\current work\\result with ambience sound(items-52067).csv'
# file1 = pd.read_csv(csv_file, delimiter=',')
#
# file1.head()



# loss_training=file1.head('tr_loss')
# loss_val=file1.head('te_loss')
# epochs= range(0,400)
# plt.plot(epochs, loss_training, 'g', label='Training loss')
# plt.plot(epochs, loss_val, 'b', label='validation loss')
# plt.xlabel('Epochs')
# plt.ylabel('Loss')
# plt.legend()
# plt.show()



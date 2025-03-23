import glob
import shutil
from random import shuffle
import os



def split_data(data_path, folder_num, save_path):
    #file_set = glob.glob(data_path + '*.wav')
    file_set = glob.glob(data_path+'**/*.wav')
    shuffle(file_set)
    fold_id = 0
    for i in range(0, folder_num):
        path = save_path + 'fold%d/' % i
        isExists = os.path.exists(path)
        if not isExists:
            os.makedirs(path)

    for file in file_set:
        fold_id %= folder_num
        save_folder = save_path + 'fold%d/' % fold_id
        fold_id += 1
        shutil.copy(file, save_folder)

if __name__ == '__main__':
    data_path = 'E:\\ubuntu file\\current work\\finaldataset\\nonambience\\'
    #data_path = 'E:\\ubuntu file\\current work\\finaldataset\\ambience\\'
    #save_path = 'E:\\ubuntu file\\current work\\finaldataset\\kfolds\\'
    save_path = 'E:\\ubuntu file\\current work\\finaldataset\\kfolds-nonambience\\'
    split_data(data_path, 10, save_path)
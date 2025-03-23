
import os
import shutil

from pydub import AudioSegment

#Change to  current directory
path = '/~h/test norm/test/yawn test/'
#
os.chdir(path)
audio_files=os.listdir(path)

#Example of simple file rename

# source_dir= "/home/mamun/Desktop/xyz_prac/screaming/a-1" ## source path
#
# special_dir= "/home/mamun/Desktop/xyz_prac/screaming/a-11" ## destination path
# os.chdir(source_dir)
# audio_files=os.listdir(source_dir)


def main():
    for file in audio_files:
        fullpath = os.path.join(file)
        filename = os.path.basename(fullpath)
        #print(filename)
        file_id1=filename.split('_')[0]
        class_id = filename.split('_')[1]
        # aug_id = filename.split('_')[2]
        # aug_id1=aug_id.split('-')[0]
        #aug_id='2'
        #aug_id2=aug_id.split('-')[1]
        #print(aug_id1)

        #class_name='woman yawn'
        #class_ID='5'
        aug_id='1'


        #print(file_id2)

        dst=(file_id1 +'_'+class_id+'_'+ aug_id+'.wav')
        #dst = (file_id1 + '_' + class_id + '_' + aug_id1 +'-'+aug_id2 )
        print(fullpath)
        print(dst)
        os.rename(fullpath, dst)


if __name__ == '__main__':
    main()


# # file auto numbering
# def main():
#     for count, filename in enumerate(os.listdir(path)):
#         fullpath = os.path.join(filename)
#         filename = os.path.basename(fullpath)
#         #print(filename)
#         #file_id=filename.split('_')[0]
#         #file_split_id=filename.split('_')[1]
#         #file_class=filename.split('_')[2]
#
#         #dst=(file_id +'_'+file_split_id+'_'+file_class+'_'+'5'+'.wav')
#
#         #dst=(file_id'-'+'cough'+'-' + file_id[-2] +'.wav')
#         #dst = (str(count + 1)+'=' + filename)   #for auto number
#         dst = (str(count + 1) + '='+'zaplet'+ ' yawn')  # for auto number
#         print(dst)
#         os.rename(fullpath, dst)
#
#
# if __name__ == '__main__':
#     main()
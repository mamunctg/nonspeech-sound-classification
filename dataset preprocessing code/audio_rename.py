import os  # glob is unnecessary
from pydub import AudioSegment
from pydub.utils import make_chunks


##########How to rename  file example
#
# def main():
#     path = "/home/mamun/Downloads/test/"
#
#     # Change working directory
#     # os.chdir(path)
#     #
#     # audio_files = os.listdir()
#
#
#
#     for root, dirs, filenames in os.walk(path):
#         for filename in filenames:
#             fullpath = os.path.join(root, filename)
#             filename_split = os.path.splitext(fullpath)  # filename and extension name (extension in [1])
#             filename_zero, fileext = filename_split
#             filename_ID=filename_zero.split("_")[0]
#             filename_chunk_ID=filename_zero.split("_")[-1]
#
#             #filename_ID= audioID, filename_chunk_ID=chunk of original audio, 0 for class 1, 1 for folder 1
#             os.rename(fullpath, filename_ID + "-" + filename_chunk_ID+ "-" +"5"+"-"+ "6" +fileext)
#
#     # for elem in audio_files:
#     #     filename_base = os.path.basename(elem)
#     #     filename = os.path.splitext(filename_base)[0]
#     #     label = filename.split("_")[-1]
#     #     os.rename(label, dst=audio_files)
#
#
#
#         # #export all of the individual chunks as wav file
#         #
#         # for i, chunk in enumerate(chunks):
#         #     chunk_name=filename+'_' +str(i)+'.wav'
#         #     chunk.export(chunk_name, format="wav")
#         # i += 1
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
# if __name__ == '__main__':
#     main()


#another example


#$$$$$Examples
"""
this is used to change spectrogram name with class name



"""
import shutil
def main():

    path = "/~/current work/baby crying/"

    # Change working directory
    os.chdir(path)

    audio_files = os.listdir()

    for file in audio_files:
        fullpath=os.path.join(file)
        filename=os.path.basename(fullpath)  #To get original file name
        filename1=filename.split('-')[0]  ##to print sound ID of file
        file_split_ID=filename.split('-')[1]##To get split file ID
        Class_ID=filename.split('-')[2]  #to get class ID
        file_ext=filename.split('.')[1]  #to get file extention



        print(filename)



        def CN(Class_ID):
            if Class_ID == '0':
                   return "crying-adult"
            elif Class_ID == '1':
                return "crying-infant"
            elif Class_ID == '2':
                return "laugh"
            elif Class_ID == '3':
                return "screeming"
            elif Class_ID == '4':
                return "sigh"
            else:
                return "sneeze"

        class_Name = CN(Class_ID)
            #filename_ID= audioID, filename_chunk_ID=chunk of original audio, 0 for class 1, 1 for folder 1
            #os.rename(fullpath, filename_ID + "-" + filename_chunk_ID+ "-" +"5"+"-"+ "6" +fileext)

        dst=(filename1+"-"+file_split_ID+"_"+class_Name+"."+file_ext)
        print(dst)
        os.rename(fullpath, dst)





if __name__ == '__main__':
    main()
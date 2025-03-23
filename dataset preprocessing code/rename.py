import os  # glob is unnecessary
from pydub import AudioSegment
from pydub.utils import make_chunks


##########How to rename  file example


import os
from os import path
import shutil



#
# def main():
#     for count, filename in enumerate(os.listdir(Source_Path)):
#         fullpath = os.path.join(filename)
#         filename_split = os.path.splitext(fullpath)  # filename and extension name (extension in [1])
#         filename_zero, fileext = filename_split
#         #filename1=filename_zero.split('_')[0]
#         dst =  str(count)+'.' +filename_zero+fileext
#         # rename all the files
#         os.rename(os.path.join(Source_Path, filename),  os.path.join(Destination, dst))
#
#
# # Driver Code
# if __name__ == '__main__':
#     main()



# def main():
#     #path = "/home/mamun/Desktop/aigei/111/"
#
#     # Change working directory
#     # os.chdir(path)
#     #
#     # audio_files = os.listdir()
#
# #Rename multiple files using Python
#
#     for count, filename in enumerate(os.listdir("xyz")):
#         fullpath = os.path.join(filename)
#         filename_split = os.path.splitext(fullpath)  # filename and extension name (extension in [1])
#         filename_zero, fileext = filename_split
#         dst = "Hostel" + str(count) + fileext
#         src = 'xyz' + filename
#         dst = 'xyz' + dst
#
#         # rename() function will
#         # rename all the files
#         os.rename(src, dst)
#
#         # for root, dirs, filenames in os.walk(path):
#     #     for filename in filenames:
#     #         fullpath = os.path.join(root, filename)
#     #         filename_split = os.path.splitext(fullpath)  # filename and extension name (extension in [1])
#     #         filename_zero, fileext = filename_split
#     #         # filename=filename_zero.split("_")[-2]
#     #
#     #         for i in enumerate(path):
#     #             os.rename(fullpath,'cough' +str(i)+fileext)
#     #             i +=1
#     #
#     #         #os.rename(fullpath, filename + "_" + "cough"+" "+fileext)
#     #         print(filename)
#
#
#             # for i, chunk in enumerate(chunks):
#             #     chunk_name=filename+'_' +str(i)+'.wav'
#             #     chunk.export(chunk_name, format="wav")
#             # i += 1
#
#             #filename_ID=filename_zero.split("_")[0]
#             #filename_chunk_ID=filename_zero.split("_")[-1]
#
#             #filename_ID= audioID, filename_chunk_ID=chunk of original audio, 0 for class 1, 1 for folder 1
#             #os.rename(fullpath, filename_ID + "-" + filename_chunk_ID+ "-" +"5"+"-"+ "6" +fileext)
#
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
#
#
# #another example
#
#
# #$$$$$Examples
# # """
# # this is used to change spectrogram name with class name
# #
# #
# #
# # """
# # import shutil
# # def main():
# #     #path = "/home/mamun/Desktop/input/picts/"
# #     path = "/home/mamun/Downloads/current work/baby crying/"
# #
# #     # Change working directory
# #     os.chdir(path)
# #
# #     audio_files = os.listdir()
# #
# #     for file in audio_files:
# #         fullpath=os.path.join(file)
# #         filename=os.path.basename(fullpath)  #To get original file name
# #         filename1=filename.split('-')[0]  ##to print sound ID of file
# #         file_split_ID=filename.split('-')[1]##To get split file ID
# #         Class_ID=filename.split('-')[2]  #to get class ID
# #         file_ext=filename.split('.')[1]  #to get file extention
# #
# #
# #
# #         print(filename)
# #
# #
# #
# #         def CN(Class_ID):
# #             if Class_ID == '0':
# #                    return "crying-adult"
# #             elif Class_ID == '1':
# #                 return "crying-infant"
# #             elif Class_ID == '2':
# #                 return "laugh"
# #             elif Class_ID == '3':
# #                 return "screeming"
# #             elif Class_ID == '4':
# #                 return "sigh"
# #             else:
# #                 return "sneeze"
# #
# #         class_Name = CN(Class_ID)
# #             #filename_ID= audioID, filename_chunk_ID=chunk of original audio, 0 for class 1, 1 for folder 1
# #             #os.rename(fullpath, filename_ID + "-" + filename_chunk_ID+ "-" +"5"+"-"+ "6" +fileext)
# #
# #         dst=(filename1+"-"+file_split_ID+"_"+class_Name+"."+file_ext)
# #         print(dst)
# #         os.rename(fullpath, dst)
# #
# #
# #         os.rename()
# #
# #
# # if __name__ == '__main__':
#     main()
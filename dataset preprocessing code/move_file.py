import os,shutil


source_dir= "/~/bridge W&U/ANonspeech/xyz_prac/cough/a-1" ## source path

special_dir= "/~/cough/a-11" ## destination path



def file_name(file_dir,file_type='.wav'):
  L=[]
  for root, dirs, files in os.walk(file_dir):
    for file in files:
      if os.path.splitext(file)[1] == file_type:
        L.append(os.path.join(root, file))
  return L


os.chdir(source_dir)
audio_files = file_name(source_dir)


for file in audio_files:
    fullpath = os.path.join(file)
    filename=os.path.basename(fullpath)

    file_id1 = filename.split('.')[0]
    class_id =file_id1.split('_')[1]
    aug_id = file_id1.split('_')[2]
    aug_id1=aug_id.split('-')[1]
    print(file_id1)
    print(aug_id1)
    if aug_id1 =='3':

    #if(len(filename.split('_'))!=1):
        continue


    print("Moving...",filename)
    full_path_source_file = os.path.join(source_dir, filename)
    full_path_target_file = os.path.join(special_dir, filename)
    shutil.copy(full_path_source_file, full_path_target_file)









    # if not os.path.isdir(os.path.join(srcDir, fname)):
    #     if not fname.rfind('_'):
    #         if not os.path.isdir(os.path.join(targetDir)):
    #             os.mkdir(os.path.join(targetDir))
    #             shutil.move(os.path.join(srcDir, fname), targetDir)
import os
import glob,shutil

#importing dataset
os.chdir(r"./images")
files= sorted(glob.glob("*.jpg"),key=os.path.getctime)

# print(files)
for index, oldfile in enumerate(files):
    newfile = '{0:04d}.jpg'.format(index+1)
    print(oldfile,newfile)
    # shutil.copy(oldfile,newfile)



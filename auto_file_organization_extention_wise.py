import os
import shutil
import gui

path=gui.source
des=gui.destination
filelist=os.listdir(path)
print("_____________________________\n")
print("F I L E   L I S T  ::: \n ")
for i in filelist:
    print(i)
print("_____________________________\n")


if len(filelist) == 0:
    print("\n\nfolder is empty ....!!!\n\n")
else:
    exlist=[]

    for file in filelist:
        ex = file.split('.')[-1]
        exlist.append(ex)

    exlist=set(exlist)
    print("extension set of list : ",exlist)
    
    try:
        for ex in exlist:
            os.mkdir(des + '\\' + ex)
            for file in filelist:
                if ex == file.split('.')[-1]:
                    if os.path.isfile(file):
                        shutil.move(file , des + '\\' + ex)
    
    except FileExistsError:
        for ex in exlist:
            for file in filelist:
                if ex == file.split('.')[-1]:
                    if os.path.isfile(file):
                        shutil.move(file , des + '\\' + ex)

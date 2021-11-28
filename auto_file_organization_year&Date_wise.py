import os
import os.path
import shutil
import gui
import time

spath=gui.source
destination = gui.destination
filelist=os.listdir(spath)
print("_____________________________\n")
print("F I L E   L I S T  ::: \n ")
for i in filelist:
    print(i)
print("_____________________________\n")
spath += '/'
destination += '/'
for file in filelist:
    t = os.path.getmtime(spath + file)

    time1=time.ctime(t)
    
    print(time1)
    
    year = time1[-4:]
    month = time1[4:7]
    date = time1[8:10]
    
    
    if not(os.path.isdir(destination + year)):
        path=os.path.join(destination, year)
        os.mkdir(path)
    if not(os.path.isdir(destination + year + '/' + month)):
        path1=os.path.join(destination + year , month)
        os.mkdir(path1)
    if not(os.path.isdir(destination + year + '/' + month + '/' + date)):
        path2=os.path.join(destination + year + '/' + month , date)
        os.mkdir(path2)

    s = spath + file
    d = destination + year + '/' + month + '/' + date + '/' + file

    if os.path.exists(d):
        print(file,"------------->>>  already exists")
        continue

    shutil.move(s,d)

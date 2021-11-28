import os
import os.path
import shutil
import gui
import time

s_path=gui.source
destination=gui.destination
choice=gui.choice
filelist=os.listdir(s_path)
print("_____________________________\n")
print("F I L E   L I S T  ::: \n ")
for i in filelist:
    print(i)
print("_____________________________\n")
s_path += '/'
destination += '/'

if choice == 'extension wise':
    os.chdir(s_path)
    print(os.getcwd())
    exlist=[]

    for file in filelist:
        ex = file.split('.')[-1]
        exlist.append(ex)

    exlist=set(exlist)
    print("extension set of list : ",exlist)
    
    try:
        for ex in exlist:
            os.mkdir(destination + '/' + ex)
            for file in filelist:
                if ex == file.split('.')[-1]:
                    if os.path.isfile(file):
                        shutil.move(file , destination + '/' + ex)
    
    except FileExistsError:
        for ex in exlist:
            for file in filelist:
                if ex == file.split('.')[-1]:
                    if os.path.isfile(file):
                        shutil.move(file , destination + '/' + ex)
    
    
        
elif choice == "date & time wise":
    s_path += '/'
    destination += '/'
    for file in filelist:
        t = os.path.getmtime(s_path + file)

        time1=time.ctime(t)

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

        s = s_path + file
        d = destination + year + '/' + month + '/' + date + '/' + file

        if os.path.exists(d):
            print(file," ------------->>>  already exists")
            continue

        shutil.move(s,d)
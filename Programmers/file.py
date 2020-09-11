import os

files=os.listdir()

for f in files:
    if not os.path.isfile(f):
        continue
    
    fp=open(f,'r',encoding='UTF8')
    try:
        level=fp.readline().split()[3]
    except:
        continue
    fp.close()
    
    if level.isdigit():
        path="Level"+level
        if not os.path.isdir(path):
            os.mkdir(path)
        os.rename(f,path+"/"+f)
        print(f,"->",path+"/"+f)


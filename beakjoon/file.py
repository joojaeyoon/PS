# 문제 파일 정리

import os

filelist = os.listdir()

for f in filelist:
    if f[0].isdigit() and os.path.isfile(f):
        name = f.split(".")[0]

        if not os.path.exists(name):
            os.mkdir(name)

        os.rename(f, name+"/"+f)

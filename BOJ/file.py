# 문제 파일 정리

import os

filelist = os.listdir()

for f in filelist:
    if f[0].isdigit() and os.path.isfile(f):
        number = f.split(".")[0]
        min_range = int(number)//1000*1000
        max_range = min_range+1000

        f_name = str(min_range)+"-"+str(max_range)

        path = f_name+"/"+number+"/"+f

        if not os.path.exists(f_name):
            os.mkdir(f_name)

        if not os.path.exists(f_name+"/"+number):
            os.mkdir(f_name+"/"+number)

        os.rename(f, path)

import os
import time
from bs4 import BeautifulSoup
import requests


def get_title(url):
    res = requests.get(url)
    html = res.text

    soup = BeautifulSoup(html, "html.parser")
    title = soup.select_one("#problem_title")

    return title.text


def writeReadme(num, path):
    title = get_title(f"https://www.acmicpc.net/problem/{num}")

    f = open("README.md", "a", encoding="utf-8")
    f.write(f"| {num} | <a href='{path}'>{title}</a> |\n")
    f.close()

    f = open("README.md", "r", encoding="utf-8")
    data = f.readlines()
    header = data[:4]
    data = data[4:]
    f.close()

    data.sort(key=lambda x: int(x.split("|")[1]))

    f = open("README.md", "w", encoding="utf-8")
    f.writelines(header)
    f.writelines(data)
    f.close


def moveFile():
    filelist = os.listdir()

    for f in filelist:
        if f[0].isdigit() and os.path.isfile(f):
            number = f.split(".")[0]
            min_range = int(number)//1000*1000
            max_range = min_range+1000

            f_name = str(min_range)+"-"+str(max_range)
            path = f_name+"/"+number+"/"+f

            writeReadme(number, f"{f_name}/{number}/")

            if not os.path.exists(f_name):
                os.mkdir(f_name)

            if not os.path.exists(f_name+"/"+number):
                os.mkdir(f_name+"/"+number)

            os.rename(f, path)


if __name__ == "__main__":
    moveFile()

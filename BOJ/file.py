import os
import shutil

import requests
from bs4 import BeautifulSoup


def get_title(url):
    res = requests.get(url)
    html = res.text

    soup = BeautifulSoup(html, "html.parser")
    title = soup.select_one("#problem_title")

    return title.text


def writeReadme(num, path):
    title = get_title(f"https://www.acmicpc.net/problem/{num}")

    tier = getTier(num)
    f = open("README.md", "a", encoding="utf-8")
    f.write(f"| {num} | {tier} |<a href='{path}'>{title}</a> |\n")
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
    f.close()


def getAllTiers():
    tiers = {}

    urls = ["https://solved.ac/profile/wow1548/solved",
            "https://solved.ac/profile/wow1548/solved?page=2",
            "https://solved.ac/profile/wow1548/solved?page=3"]

    for url in urls:
        res = requests.get(url)
        html = res.text

        soup = BeautifulSoup(html, "html.parser")
        problems = soup.select(
            "div.StickyTable__Row-akg1ak-2 > div > span > a")

        for i in range(0, len(problems), 2):
            img = problems[i].select_one("img")
            img["class"] = ""
            tiers[int(problems[i].text)] = str(img)

    f = open("README.md", "r", encoding="utf-8")
    data = f.readlines()
    header = data[:4]
    data = data[4:]
    f.close()

    data.sort(key=lambda x: int(x.split("|")[1]))

    for i in range(len(data)):
        tmp = data[i].split("|")
        tier = tiers.get(int(tmp[1]), "?")
        tmp.insert(2, tier)
        data[i] = "|".join(tmp)

    f = open("README.md", "w", encoding="utf-8")
    f.writelines(header)
    f.writelines(data)
    f.close()


def moveFile():
    filelist = os.listdir()

    for f in filelist:
        if f[0].isdigit() and os.path.isfile(f):
            number = f.split(".")[0]
            min_range = int(number)//1000*1000
            max_range = min_range+1000

            f_name = str(min_range)+"-"+str(max_range)
            path = f"{f_name}/{number}/{f}"

            writeReadme(number, f"/BOJ/{f_name}/{number}/")

            if not os.path.exists(f_name):
                os.mkdir(f_name)

            if not os.path.exists(f"{f_name}/{number}"):
                os.mkdir(f"{f_name}/{number}")

            os.rename(f, path)


def getTier(num):
    url = f"https://solved.ac/search?query={num}"

    res = requests.get(url)
    html = res.text

    soup = BeautifulSoup(html, "html.parser")
    tier = soup.select_one(".TierBadge__TierBadgeStyle-bguxxi-0")
    tier["class"]=""

    return str(tier)


if __name__ == "__main__":
    moveFile()

    shutil.copy("README.md", "../")

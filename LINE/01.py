def solution(answer_sheet, sheet):
    answer = -1

    cheets = []

    for i in range(len(sheet)-1):
        for j in range(i+1, len(sheet)):
            cheet = ""
            for k in range(len(answer_sheet)):
                if sheet[i][k] == sheet[j][k] and sheet[i][k] != answer_sheet[k]:
                    cheet += "1"
                else:
                    cheet += "0"
            max_count = len(sorted(cheet.split("0"), reverse=True)[0])
            count = cheet.count("1")

            cheets.append(count+max_count*max_count)

    return max(cheets)


answer = "4132315142"
s = ["3241523133", "4121314445", "3243523133", "4433325251", "2412313253"]


solution(answer, s)

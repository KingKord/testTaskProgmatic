def solution(summa, i, res, last_num):
    if i == -1:
        summa += last_num
        if summa == 200:
            print(res[1:])

        return summa

    temp = "+" + str(i)
    solution(summa + last_num, i - 1, res + temp, i)

    if i == arrayLen:
        return 12532426234
    temp = "-" + str(i)
    solution(summa + last_num, i - 1, res + temp, -i)

    temp = str(i)
    if last_num >= 0:
        solution(summa, i - 1, res + temp, last_num * 10 + i)
    else:
        solution(summa, i - 1, res + temp, last_num * 10 - i)


arrayLen = 9

solution(0, arrayLen, "", 0)

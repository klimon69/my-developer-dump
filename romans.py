romanNum = 0

while romanNum != 'q':
    romanNum = input("Введите римскую цифру от 1 до 39. Для выхода введите 'q'")
    flag = []

    romanNumSplit = list(romanNum)
    if romanNumSplit == ['x', 'c', 'i', 'x']:    # бля за это надо лишать яйца, но....
        romanNumSplit = [99]


    # =========================проверяем все исключения==========================

    # 8 число не может быть длиннее 8 символов
    if len(romanNumSplit) > 8:
        romanNumSplit = ['хуйня']

    # 1. не может быть больше четырех Х

    for i in range(len(romanNumSplit)):
        if romanNumSplit[i] == 'X' or romanNumSplit[i] == 'x':
            flag.append(1)
    f2 = sum(flag)
    if f2 > 4:
        romanNumSplit = ['хуйня']
    else:
        flag = []

    # 3 не может быть боль трёх i подряд

    for i in range(len(romanNumSplit)):
        if romanNumSplit[i] == 'I' or romanNumSplit[i] == 'i':
            flag.append(1)
            # print (flag)
    f2 = sum(flag)
    if f2 > 3:
        romanNumSplit = ['хуйня']
    else:
        flag = []

    # 4 не может быть боль одного V подряд

    for i in range(len(romanNumSplit)):
        if romanNumSplit[i] == 'V' or romanNumSplit[i] == 'v':
            flag.append(1)
            # print (flag)
    f2 = sum(flag)
    if f2 > 1:
        romanNumSplit = ['хуйня']
    else:
        flag = []

    # 5 не может быть боль одного С подряд


    for i in range(len(romanNumSplit)):
        if romanNumSplit[i] == 'C' or romanNumSplit[i] == 'c':
            flag.append(1)
            # print (flag)
    f2 = sum(flag)
    if f2 > 1:
        romanNumSplit = ['хуйня']
    else:
        flag = []

    # 5 не может быть боль одного L подряд


    for i in range(len(romanNumSplit)):
        if romanNumSplit[i] == 'L' or romanNumSplit[i] == 'l':
            flag.append(1)
            # print (flag)
    f2 = sum(flag)
    if f2 > 1:
        romanNumSplit = ['хуйня']
    else:
        flag = []

    # 2. не может быть больше 3ёх Х подряд !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    for k in range(len(romanNumSplit) - 1):
        if romanNumSplit[k] == romanNumSplit[k - 1]:
            flag.append(1)
            #print (flag)
    f2 = sum(flag)
    if f2 > 3:
        romanNumSplit = ['хуйня']
    else:
        flag = []
    #print (romanNumSplit)
    for i in range(len(romanNumSplit)):


        if romanNumSplit[i] == 'X' or romanNumSplit[i] == 'x':
            romanNumSplit[i] = 10
        elif romanNumSplit[i] == 'V' or romanNumSplit[i] == 'v':
            romanNumSplit[i] = 5
        elif romanNumSplit[i] == 'I' or romanNumSplit[i] == 'i':
            romanNumSplit[i] = 1
        elif romanNumSplit[i] == 'L' or romanNumSplit[i] == 'l':
            romanNumSplit[i] = 50
        elif romanNumSplit[i] == 'C' or romanNumSplit[i] == 'c':
            romanNumSplit[i] = 100

    #print (romanNumSplit)
    #print(len(romanNumSplit))

    # ====================проверка чисел по возрастанию=============================
    # 8 числа должны быть по убыванию (кроме iv и ix)  если v и x на последнем месте
    #  и XL если x на 1 ом месте и
    #  XC если X на первом месте

    #  xiiv

    # for k in range(len(romanNumSplit)-1):
    #    if romanNumSplit[k] < romanNumSplit[k-1]:
    #         flag.append(1)
    #         print (sum(flag))
    # f2 = sum(flag)
    # if f2 > 1:
    #    romanNumSplit = ['хуйня']
    # elif f2 ==1 and romanNumSplit[len(romanNumSplit)-1] == 5:
    #    flag = []
    # elif f2 ==1 and romanNumSplit[len(romanNumSplit)-1] == 10:
    #    flag = []
    # elif f2 ==1 and romanNumSplit[len(romanNumSplit)-1] != 5:
    #    romanNumSplit = ['хуйня']

    #print(romanNumSplit)





    # ==========90ка и слагаемые рядом==============


    if len(romanNumSplit) > 1:
        for k in range(len(romanNumSplit) - 1):


            if romanNumSplit[k] == 10 and romanNumSplit[k + 1] == 100:  # колдовство номер 2
                romanNumSplit[k] = 90
                romanNumSplit.pop(k + 1)
    else:
        romanNumSplit = romanNumSplit

    # ==========50ка и слагаемые рядом==============


    if len(romanNumSplit) > 1:
        for k in range(len(romanNumSplit) - 1):
            if romanNumSplit[k] == 10 and romanNumSplit[k + 1] == 50:  # колдовство номер 2
                romanNumSplit[k] = 40
                romanNumSplit.pop(k + 1)
    else:
        romanNumSplit = romanNumSplit

    if len(romanNumSplit) > 1:
        for k in range(len(romanNumSplit)):
            if romanNumSplit[k - 1] == romanNumSplit[k - 2] == 1:  # ебаное колдовство
                romanNumSplit[k - 1] = 2
                romanNumSplit.pop(k - 2)
    else:
        romanNumSplit = romanNumSplit

    # print(romanNumSplit)



    if len(romanNumSplit) > 2:

        for k in range(len(romanNumSplit)):
            if romanNumSplit[k] == 2 and romanNumSplit[k - 1] == 1 or romanNumSplit[k] == 1 and romanNumSplit[
                        k - 1] == 2:
                romanNumSplit[k] = 3
                romanNumSplit.pop(k - 1)

    else:
        romanNumSplit = romanNumSplit

    # print(romanNumSplit)


    # ==========пятёрка и слагаемые рядом==============

    if len(romanNumSplit) > 1:

        for k in range(len(romanNumSplit) - 1):
            if romanNumSplit[k] == 1 and romanNumSplit[k - 1] == 5:  # колдовство номер 3
                romanNumSplit[k] = 4
                romanNumSplit.pop(k - 1)
    else:
        romanNumSplit = romanNumSplit

    #print(romanNumSplit)


    # ==========десятка и слагаемые рядом==============




    if len(romanNumSplit) > 1:
        for k in range(len(romanNumSplit) - 1):
            if romanNumSplit[k] == 1 and romanNumSplit[k - 1] == 10:  # колдовство номер 2
                romanNumSplit[k] = 9
                romanNumSplit.pop(k - 1)
    else:
        romanNumSplit = romanNumSplit

    # print(romanNumSplit)


    try:
        arabNum = sum(romanNumSplit)
        print(arabNum)
    except TypeError:
        print("Нет такого числа")
else:
    print("Memento quia pulvis es")
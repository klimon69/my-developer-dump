romanNum = input("Введите римскую цифру от 1 до 39")

romanNumSplit = list(romanNum)




for i in range(len(romanNumSplit)):
    if romanNumSplit[i] == 'X' or romanNumSplit[i] == 'x':
        romanNumSplit[i] = 10
    elif romanNumSplit[i] == 'V' or romanNumSplit[i] == 'v':
        romanNumSplit[i] = 5
    elif romanNumSplit[i] == 'I' or romanNumSplit[i] == 'i':
        romanNumSplit[i] = 1



#print(romanNumSplit)



if len(romanNumSplit)>1:
    for k in range(len(romanNumSplit)):
        if romanNumSplit[k-1] == romanNumSplit[k-2] == 1:   #ебаное колдовство
            romanNumSplit[k-1] = 2
            romanNumSplit.pop(k-2)
else:
    romanNumSplit=romanNumSplit



#print(romanNumSplit)



if len(romanNumSplit)>2:

    for k in range(len(romanNumSplit)):
        if romanNumSplit[k] == 2 and romanNumSplit[k-1] == 1 or romanNumSplit[k] == 1 and romanNumSplit[k-1] == 2:
            romanNumSplit[k] = 3
            romanNumSplit.pop(k-1)

else:
    romanNumSplit=romanNumSplit

#print(romanNumSplit)


#==========пятёрка и слагаемые рядом==============

if len(romanNumSplit)>1:

    for k in range(len(romanNumSplit)-1):
        if romanNumSplit[k] == 1 and romanNumSplit[k-1] == 5:   # колдовство номер 3
            romanNumSplit[k] = 4
            romanNumSplit.pop(k-1)
else:
    romanNumSplit=romanNumSplit

#print(romanNumSplit)


#==========десятка и слагаемые рядом==============


if len(romanNumSplit)>1:
    for k in range(len(romanNumSplit)-1):
        if romanNumSplit[k] == 1 and romanNumSplit[k-1] == 10:     # колдовство номер 2
            romanNumSplit[k] = 9
            romanNumSplit.pop(k-1)
else:
    romanNumSplit = romanNumSplit

#print(romanNumSplit)


try:
    arabNum = sum(romanNumSplit)
    print(arabNum)
except TypeError:
    print("Нет такого числа")
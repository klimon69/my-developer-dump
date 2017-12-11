import time

a = int(input("Введите сколько часов осталось до события  "))

if a == 24:
    a = 0
    b = 59

else:
    while a > 24 or a < 0:
        a = int(input("Неприемлимые значения\n Введите сколько часов осталось до события  "))

    b = int(input("Введите сколько минут осталось до события  "))

    if b == 0:
        a = a-1
        b = 59+1
    else:
        while b > 59 or b < 0:
            b = int(input("Неприемлимые значения\n Введите сколько минут осталось до события  "))

for h in range(a, 0 - 1, -1):

    for m in range(b - 1, 0 - 1, -1):
        if m == 0:
            b = 59
        for s in range(59, 0 - 1, -1):
            print("\n" * 50)
            print("До события осталось: " + str(h) + " ч : " + str(m) + " мин : " + str(s) + " сек\n\n\n\n\n")
            time.sleep(1)

print("\n" * 50)
print("-----TIME TO FAP------\n\n\n\n\n")
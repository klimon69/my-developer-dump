#with open("123.txt") as file:
 #   a = [row.strip() for row in file]
 #   a = [int(i) for i in a]
#print(a)

a = [0, 3,  0,  1,  -3]
b = []


i = 0



z        a[i] = a[i]+1
        print(a[i])

        b.append(1)
        print(a)
    elif a[i]>0:

        i = i + a[i]
        a[i] = a[i] + 1
        b.append(1)
        print('i=' + str(i))
        print("a[i] = " + str(a[i]))
        print(a)
    elif a[i]<0:

        i = i - a[i]
        a[i] = a[i] + 1
        b.append(1)
        print('i=' + str(i))
        print("a[i] = " + str(a[i]))
        print(a)

print(len(b))

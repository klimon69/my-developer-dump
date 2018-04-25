


with open("123.txt") as file:
    a = [row.strip() for row in file]
    a = [int(i) for i in a]


#a = [0, 3,  0,  1,  -3]
b = []


i = 0




while i < len(a)+1:


    if a[i] == 0:
        a[i] = a[i]+1
        print(a)
        b.append(1)

        print(a[i])




    elif a[i] > 0:
        a[i] = a[i]+1
        print(a)
        i = i+ a[i]-1
        b.append(1)

        print(a[i])




    elif a[i] < 0:
        a[i] = a[i]+1
        print(a)
        i = i+abs(a[i])+1
        b.append(1)

        #print(a[i])


print(int(len(b)+1))
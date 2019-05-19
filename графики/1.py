import matplotlib.pyplot as plt

x_d = input("Введите x координату точки: ")
y_d = input("Введите y координату точки: ")

x1, y1 = [-1, 12], [1, 4]
plt.axis([-10, 30, -10, 30])

plt.xlabel('x')
plt.ylabel('y')
plt.plot(x1, y1, marker = 'o')
plt.plot(int(x_d), int(y_d),  marker = 'o')
check = D = (int(x_d) - x1[0]) * (y1[1] - y1[0]) - (int(y_d) - y1[0]) * (x1[1] - x1[0])

if check>0:
    plt.title("Точка находиться справа от прямой")
elif check<0:
    plt.title("Точка находиться слева от прямой")
else:
    plt.title("Точка находиться на прямой")
plt.show()
# Задание 1

import numpy as np
a=np.random.random(10)*20
print(sorted(a))

# Задание 2

x=np.zeros((8,8))

x[1::2,::2]=1
x[::2,1::2]=1
print(x)

# Задание 3

a=np.ones((8,4))
b=np.ones((4,2))
print(np.dot(a,b))

# Задание 4
st=0
mas=np.array(range(10), float)
while st<10:
    ran = np.random.random()
    if ran!=0 or ran!=1:
        mas[st]=ran
        st=st+1

print(mas)


# Задание 5

def matrix(number):
    spis = list()
    for i in range(2, number):
        if number % i ==0:
            spis.append(i)
    if len(spis)==0:
        return print ("число простое")
    print(spis)
    for i in range(0,len(spis)):
        for j in range(0,len(spis)):
            mat=np.ones((spis[i],spis[j]))
            print(mat)

matrix(6)
# Задание 1

import numpy as np
# a=np.random.random(10)*20
# print(sorted(a))
#
# # Задание 2
#
# x=np.zeros((8,8))
#
# x[1::2,::2]=1
# x[::2,1::2]=1
# print(x)
#
# # Задание 3
#
# a=np.ones((8,4))
# b=np.ones((4,2))
# print(np.dot(a,b))
#
# # Задание 4
# st=0
# mas=np.array(range(10), float)
# while st<10:
#     ran = np.random.random()
#     if ran!=0 or ran!=1:
#         mas[st]=ran
#         st=st+1
#
# print(mas)
#
#
# # Задание 5
#
# def matrix(number):
#     spis = list()
#     for i in range(2, number):
#         if number % i ==0:
#             spis.append(i)
#     if len(spis)==0:
#         return print ("число простое")
#     print(spis)
#     for i in range(0,len(spis)):
#         for j in range(0,len(spis)):
#             mat=np.ones((spis[i],spis[j]))
#             print(mat)
#
# matrix(6)
#

# Задание 6

# Задание 7

def fn(A, S, last=False):
    X= len(A)
    B = np.random.randint(1, 5, (S,X), dtype=int)
    C= A * B
    D = np.array([])
    for i in C:
        el=np.sum(i)
        D = np.append(D, el)

    if last == False:
        D = np.sin(D)
    else:
        D = np.maximum(D,0)
    return D,B


A= np.array([1,3,5,7,4])
S=10
A_1, Ran_1= fn(A, S)
print (A_1,'\n',Ran_1)
print('')
A_2, Ran_2 = fn(A_1, S,False)
print (A_2,'\n',Ran_2)
print('')
S=5
A_3, Ran_3 = fn(A_2, S, True)
A_4 = A_3*100
print (A_4,'\n',Ran_3)

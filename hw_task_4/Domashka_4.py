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

st=0.00000001
en=0.99999999
ran = np.random.randint(low=st, high=en, size=10 )
print(ran)

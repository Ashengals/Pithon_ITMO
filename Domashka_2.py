# Задание_1
print('Задание_1')


a=['domashka','Python', 'data', 'php', 'go', 'les', 'C', 'mrak', 'go']
st = ['Python', 'php', 'go', 'C']
i=0
while i< len(st):
    a = list(filter(lambda x: x!=st[i], a))
    i +=1
print(a)

# Задание_2
print('Задание_2')

param=4
st=[1,3,6,5,7,9,12,17,18,21,44,24,3,1,6,7,10]
print(list(filter(lambda x: x%param == 0, st)))

# Задание_3
print('Задание_3')

def korrect(*args):
    list_arg=list(args[0])
    item = list(filter(lambda x: isinstance(x, str), list_arg))
    kor = (*item,)
    return kor

st=[1,'data', 3,6,5, 'sem', 7,9,'mega',12,17, 'vosem', 18,21,44,24,'ura', 3,1,6,'list',7,'vse',10]

print(korrect(st))

# Задание_4
print('Задание_4')

def sravn(a,b):
    c=[]
    for i in a:
        if i in b and i not in c:
            c.append(i)
    return c

a=[1,'data', 3,6,5, 'sem', 7,9,'mega',12,17, 'vosem', 18,21,44,24,'ura', 3,1,6,'list',7,'vse',10]
b=[7,'Python', 15, 'php', 'go', 'list', 8, 'mrak', 24]

print(sravn(a,b))

# Задание_5
print('Задание_5')


# Задание_6
print('Задание_6')

def proverka(fn):
    def wrapper(*args):
        try:
            b = fn(*args)
            print(f'результат:{b}')
        except Exception:
             print('Ваши значения не строковые')

    return wrapper
@proverka
def itog(a):
    sum_1=0
    for i in a:
        sum_1 = sum_1 + i
    return sum_1

@proverka
def proiz(a):
    sum_2=1
    for i in a:
        sum_2=sum_2*i
    return sum_2

a=(1,'data', 3,6,5, 'sem', 7,9,'mega',12,17, 'vosem', 18,21,44,24,'ura', 3,1,6,'list',7,'vse',10)

itog(a)
proiz(a)

a=(7, 15, 8, 42, 24)

itog(a)
proiz(a)

# Задание_7
print('Задание_7')



def proverka(fn):
    def wrapper(*args):
        try:
            b = fn(*args)
            print(f'результат:{b}')
        except Exception:
             a=list(filter(lambda x: isinstance(x, int), args[0]))
             wrapper(a)
    return wrapper
@proverka
def itog(a):
    sum_1=0
    for i in a:
        sum_1 = sum_1 + i
    return sum_1

@proverka
def proiz(a):
    sum_2=1
    for i in a:
        sum_2=sum_2*i
    return sum_2

a=(1,'data', 3,6,5, 'sem', 7,9,'mega',12,17, 'vosem', 18,21,44,24,'ura', 3,1,6,'list',7,'vse',10)

itog(a)
proiz(a)

a=(7, 15, 8, 42, 24)

itog(a)
proiz(a)

# Задание_8
print('Задание_8')

def min_max(a):
    pr=0
    while pr==0:
        b=a[0]
        c = b[1]
        pr=1
        for i in range(1,len(a)):
            b1 = a[i]
            c1 = b1[1]
            if c>c1:
                a[i]=b
                a[i-1]=b1
                pr=0
            else:
                b=b1
                c=c1
    return a

elements = [(2, 12, "Mg"), (1, 11, "Na"), (1, 3, "Li"), (2, 4, "Be")]

v=min_max(elements)
print(v)


# Задание_9
print('Задание_9')
import time

def time_f(fn):
    def wrapper(*args):
        na4alo=time.time()
        result=fn(*args)
        end_t=time.time()
        tau=end_t-na4alo
        print(f'Время выполнения программы:{tau} секунд')
        return result
    return wrapper


@time_f
def itog():
    sum_1=0
    for i in range(10000000):
        sum_1 = sum_1 + i
    return sum_1

@time_f
def proiz():
    sum_2=1
    for i in range(10000000):
        sum_2=sum_2*i
    return sum_2



itog()
proiz()







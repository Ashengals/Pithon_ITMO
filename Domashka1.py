
#Задание 1
s="" # По умолчанию строка пустая
def len_string_s(s): #объявляю функцию
    print(len(s))   #вывод на экран длины передаваемой строки
    
len_string_s("Hello Word") #вызов функции для этой строки
len_string_s('ПИШ')         #вызов функции для этой строки
len_string_s('Политех')    #вызов функции для этой строки

#Задание 2
def len_max(a,b):
    if len(a)>len(b):
        print(a)
    elif len(a)<len(b):
        print(b)
    else:
        print('списки равны')

a=[5, 10, 15, 20, 25, 30, 35,40]
b=['udav', 'piton', 'gde', '4to', 'kogda']
len_max(a,b)

a=[5, 10, 15, 20, 25, 30, 35,40]
b=['udav', 'piton', 'gde', '4to', 'kogda',1,2,3]
len_max(a,b)

a=[5, 10, 15, 20, 25]
b=['udav', 'piton', 'gde', '4to', 'kogda',1,2,3]
len_max(a,b)


#Задание 3
spisok=[1,2,3,4,5]
def spisok_new(spisok):
    i=input("Vvedite novij element v spisok:")
    spisok.append(i)
    return spisok
    
print(spisok_new(spisok))
print(spisok_new(spisok))

#Задание 4
def sto(a):
    if a>100:
        print('+')
    elif a<100:
        print('-')

sto(99)
sto(101)
sto(100)

#Задание 5
def vopros(str_2, str_1):
    if str_2 in str_1:
        print("DA")
    else:
        print("HET")


str_1="test"
str_2="test1"
print('str_2 содержит в себе str_1?')
vopros(str_2,str_1)

#Задание 6

a=[1,3,0,-1,-2]
def hi_null(a):
    s=0
    for i in a:
        if i>0:
            s=s+1
    return (s)        
print(hi_null(a))

#Задание 7


def day_numb(god, mes):
    day = god*12*29 + mes*29
    return (day)
    
print(day_numb(1,3))


#Задание 8

def abbrvalg(strok):
    try: 
        abb=strok[0]
        L=len(strok)
        i=1
        while i<L:
            if strok[i]==' ':
                abb=abb+strok[i+1]
            i=i+1
        print(abb)
    except TypeError:
        print("Введите строку")

        
abbrvalg("Что делать с ошибкой: признать, принять, извлечь урок, забыть")

#Задание 9

def fack(numb):
    count=1
    i=1
    while i <= numb:
        count=count*i
        i=i+1
    return(count)
   
numb=6
print(fack(numb))


#Задание 10

lst =[2,4,5,8,9,13]

lst[0]=lst[0]*0
lst[1]=lst[1]*1
lst[2]=lst[2]*2
lst[3]=lst[3]*3
lst[4]=lst[4]*4
lst[5]=lst[5]*5


print(lst)

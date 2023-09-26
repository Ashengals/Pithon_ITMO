#Задание 1:

class Pr9mougol:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def per_1(self):
        p=self.x*2+self.y*2
        print(f"Периметр:{p}")

    def s(self):
        s1=self.x*self.y
        print(f"Площадь:{s1}")

pasient = Pr9mougol(6,6)
pasient.per_1()
pasient.s()

#Задание 2

class Teacher:

    def __init__(self, kolvo=0):
        self.kolvo=kolvo

    def teach(self, data, *stud):
        for i in stud:
            i.take(data)
            self.kolvo = self.kolvo + 1

class Student:

    def __init__(self):
        self.knowledge = []

    def take(self, new_data):
        self.knowledge.append(new_data)

class Mater:

    def __init__(self, *data):
        self.data=list(data)


Obj_data=Mater('Python', 'Version Control Systems', 'Relational Databases', 'NoSQL databases', 'Message Brokers')
obj_teach=Teacher()
obj_stud1=Student()
obj_stud2=Student()
obj_stud3=Student()
obj_stud4=Student()

obj_teach.teach('Python',obj_stud3,obj_stud2, obj_stud1)
obj_teach.teach('Relational Databases',obj_stud3,obj_stud1)
obj_teach.teach('NoSQL databases',obj_stud4)
obj_teach.teach('Message Brokers',obj_stud2,obj_stud4)
obj_teach.teach('Version Control Systems')

print(f'Первый:{obj_stud1.knowledge}')
print(f'Второй:{obj_stud2.knowledge}')
print(f'Третий:{obj_stud3.knowledge}')
print(f'Четвертый:{obj_stud4.knowledge}')

print(f'Обучил:{obj_teach.kolvo}')



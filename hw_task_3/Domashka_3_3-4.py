#Задание 2

class Men:

    def __init__(self, fio, god, pol):
        self.fio = fio
        self.god = god
        self.pol = pol


class Teacher (Men):

    def __init__(self, fio, god, pol, kolvo=0):
        self.kolvo=kolvo
        super().__init__(fio, god, pol)

    def teach(self, data, *stud):
        for i in stud:
            i.take(data)
            self.kolvo = self.kolvo + 1

class Student (Men):

    def __init__(self, fio, god, pol):
        self.knowledge = []
        super().__init__(fio, god, pol)

    def take(self, new_data):
        self.knowledge.append(new_data)

    def __len__(self):
        return len(self.knowledge)



class Mater:

    def __init__(self, *data):
        self.data=list(data)

    def __len__(self):
        return len(self.data)


Obj_data=Mater('Python', 'Version Control Systems', 'Relational Databases', 'NoSQL databases', 'Message Brokers')
obj_teach=Teacher("Ленин Владимир Ильич", 100, 'муж')
obj_stud1=Student("Сидоров Сергей Андреевич", 25, "жен")
obj_stud2=Student("Иванов Борис Сергеевич", 13, "муж")
obj_stud3=Student("Васечкин Петр Петрович", 35, "муж")
obj_stud4=Student("Петечкин Василий Васильевич", 23, "жен")

obj_teach.teach('Python',obj_stud3,obj_stud2, obj_stud1)
obj_teach.teach('Relational Databases',obj_stud3,obj_stud1)
obj_teach.teach('NoSQL databases',obj_stud4)
obj_teach.teach('Message Brokers',obj_stud2,obj_stud4,obj_stud2)
obj_teach.teach('Version Control Systems')

print(f'Первый:{obj_stud1.knowledge}')
print(f'Второй:{obj_stud2.knowledge}')
print(f'Третий:{obj_stud3.knowledge}')
print(f'Четвертый:{obj_stud4.knowledge}')

print(f'Обучил:{obj_teach.kolvo}')

print(len(obj_stud1))
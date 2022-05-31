from ClassD import Class
from Student import Student
from Teacher import Teacher
import pickle
from log import log


def fill_info():
    student1 = Student('Михаил', "Стручкин", 13, 9)
    student1.add_mark('ОБЖ', 5, '12/01')
    student2 = Student('Елизавета', "Пупкина", 14, 9)
    student2.add_mark('ОБЖ', 3, '12/01')
    student3 = Student('Иван', "Иванов", 13, 9)
    student4 = Student('Кристина', "Мисина", 14, 9)
    student4.add_mark('Матеша', 5, '1/1')
    clas_teacher = Teacher('Людмила', 'Трусечкина', 45, '216', ['ИЗО'])
    clas_teacher.add_subj('Информатика')
    list_students = []
    list_students += student1, student2, student3, student4
    main_class = Class(7, list_students, clas_teacher)
    return main_class


def main():
    main_class = fill_info()
    with open('data.pickle', 'wb') as file:
        pickle.dump(main_class, file)

    with open('data.pickle', 'rb') as file:
        classs = pickle.load(file)
    print(classs)

    classs.__getitem__(2)
    classs.__len__()
    try:
        print("Введите индекс ученика, которого хотите удалить:")
        index = int(input())
        x = classs.__len__()
        if index < 1 or index == 0:
            raise ValueError("Индексы учеников идет от единицы!")
        if index > x:
            raise IndexError(f"Вы ввели индекс, который больше количества учеников, а именно больше: {x}\n")
        classs.__delitem__(index)
        print("Ученик по индексу[", index, "] удален!")
        print(classs)
    except ValueError as err:
        log("ERR",'', err)
        print(err, "\nПопробуйте еще раз!")
        index = int(input())
        classs.__delitem__(index )
        print("Ученик по индексу[", index, "] удален!")
        print(classs)
    except IndexError as err:
        log("ERR",'', err)
        print(err, "\nПопробуйте еще раз!")
        index = int(input())
        classs.__delitem__(index)
        print("Ученик по индексу[", index, "] удален!")
        print(classs)
if __name__=="__main__":
    main()
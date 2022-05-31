from Student import Student
from Teacher import Teacher
from log import log

class Class(Student, Teacher):
    def __init__(self, n_clas, list_students, clas_teacher):
        self.n_clas = n_clas
        self.list_students = list_students
        self.clas_teacher = clas_teacher
        self.main_clas = []
        self.main_clas.append(self.clas_teacher)
        self.main_clas += self.list_students
        log("CRE",' ', "экземпляр класса Class", "__init__")

    def __len__(self):
        log("INF","print", "количество",  "__len__")
        print("Количество студентов:", len(self.list_students))
        return len(self.list_students)

    def __getitem__(self, index):
        log("INF","print", "человек",  "__getitem__")
        print("Человек по индексу[", index, "]:", self.main_clas[index])

    def __delitem__(self, index):
        log("INF","delete", "студент", "__delitem__")
        self.main_clas.pop(index)
        return self.main_clas

    def __setitem__(self, index, person):
        log("INF", "change", "студент", "__setitem__")
        self.main_clas[index] = person


    def __sub__(self, student):
        log("INF", "delete", "студент", "__sub__")
        self.main_clas.remove(student)
        return self.main_clas

    def __add__(self, student):
        log("INF","add", "студент", "__add__")
        self.main_clas.append(student)
        return self.main_clas

    def __str__(self):
        log("INF", "print","класс", "__str__")
        s = "Class №{}\nClass teacher:{}\nStudents:\n".format(self.n_clas, self.clas_teacher)
        for j in range(1, len(self.main_clas)):
            s = s + str(j) + ' - ' + str(self.main_clas[j]) + '\n'
        return s


    def file(self, address):
        f = open(address, "w")
        f.writelines(f"Class №{self.n_clas}\nClass teacher:{self.clas_teacher}\n\nStudents:\n")
        for j in range(1, len(self.main_clas)):
            x = self.main_clas[j]
            s = str(j) + ' - ' + str(x) + '\n'
            f.writelines(s)
            f.write("Journal:\n")
            if not x.journal:
                f.writelines('Журнал оценок пуст! :С')
            else:
                for i in x.journal:
                    h = x.prr(i, x.journal)
                    f.writelines(h)
            f.writelines("\n\n")
        f.close

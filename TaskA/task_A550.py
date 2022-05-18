# Создать список (библиотека книг), состоящий из словарей (книги). Словари должны содержать как минимум 5 полей
# (например, номер, название, год издания...). В список добавить хотя бы 10 словарей.
# Конструкция вида:
# library = [{"id" : 123456, "title" : "Война и мир", "author" : "Толстой",...} , {...}, {...}, ...]
# Реализовать функции:
# – вывода информации о всех книгах;
# – вывода информации о книге по введенному с клавиатуры номеру;
# – вывода количества книг, старше введённого года;
# – обновлении всей информации о книге по введенному номеру;
# – удалении книги по номеру.
# Провести тестирование функций.

library = [
    {
        'id':1,
        'title':' Sono Bisque Doll wa Koi wo suru ',
        'Author':'Фукуда Синъити',
        'Amount of chapters':72,
        'My rating from 0 to 10':10
    },
    {
        'id':2,
        'title':'Solo Leveling',
        'Author':'Ки Сорён',
        'Amount of chapters':179,
        'My rating from 0 to 10':10
    },
    {
        'id':3,
        'title':'Koe no Katachi',
        'Author':'Ойма Ёситоки',
        'Amount of chapters':50,
        'My rating from 0 to 10': 8.5
    },
    {
        'id':4,
        'title':'Chijen In Deoteulaeb',
        'Author':'Сункки',
        'Amount of chapters':77,
        'My rating from 0 to 10':9
    },
    {
        'id':5,
        'title':'Sotsugyousei',
        'Author':'Накамура Асумико',
        'Amount of chapters':20,
        'My rating from 0 to 10':10
    },
    {
        'id':6,
        'title':'Here U Are',
        'Author':'Ди Цзюнь',
        'Amount of chapters':158,
        'My rating from 0 to 10':9.5
    },
    {
        'id':7,
        'title':'Sweet Home',
        'Author':'Ким Карнби',
        'Amount of chapters':140,
        'My rating from 0 to 10':10
    },
    {
        'id':8,
        'title':'My story!',
        'Author':'Кавахара Кадзунэ',
        'Amount of chapters':49,
        'My rating from 0 to 10':8
    },
    {
        'id':9,
        'title':'Jujutsu Kaisen',
        'Author':'Акутами Гэгэ',
        'Amount of chapters':300,
        'My rating from 0 to 10':10
    },
    {
        'id':10,
        'title':'Wotaku ni Koi wa Muzukashii',
        'Author':'Фудзита',
        'Amount of chapters':62,
        'My rating from 0 to 10':8
    }

]

def get_info(*lst):
    for i in range(10):
        print(lst[0][i],sep="\n")


def get_book_by_num():
    print("Введите номер книги, которую Вы хотите вывести на экран. 1 - 10", sep='\n')
    num = (int(input()))
    for i in range(len(library)):
        if library[i]['id'] == num:
            print(library[i])

def book_rating():
    counter = 0
    for i in range(len(library)):
        if library[i]['My rating from 0 to 10']>9:
            counter+=1
    print("Книг с рейтингом выше 9: ",counter)

def upd_inf():
    print("Введите номер книги, о которой информацию Вы хотите обновить: ")
    num = int(input())
    print("Обновляем информацию!",  sep="\n")
    for i in range(len(library)):
        if library[i]['id'] == num:
            for key, value in library[i].items():
                print(key, ":")
                if type(library[i][key]) == int:
                    library[i][key] = int(input())
                if type(library[i][key]) == str:
                     library[i][key] = input()

            print(library[i])

def delete_the_book(library):
    print("Введите номер книги, которую Вы хотите удалить: ")
    num = int(input())
    for i in range(len(library)):
        if library[i]['id'] == num:
            del library[i]
            break
    get_info(library)
def main():
    while True:
        print("Функции, доступные Вам:","1 - Вывод информации о всех книгах",
              "2 - Вывод информации о книге по введенному с клавиатуры номеру",
              "3 -  Вывод количества книг, рейтинг который выше 9",
              "4 - Обновление всей информации о книге по введенному номеру",
              "5 - Удаление книги по номеру ",
              "Введите ноль, чтобы закончить работу программы. ", sep="\n")
        menu = int(input())
        if menu == 1:
            get_info(library)
        elif menu == 2:
            get_book_by_num()
        elif menu == 3:
            book_rating()
        elif menu == 4:
            upd_inf()
        elif menu == 5:
            delete_the_book(library)
        elif menu == 0:
            break

if __name__=="__main__":
    main()
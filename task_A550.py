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

def get_info(lst):
    for i in range(len(lst)):
        print(lst[i])
        print()
def get_book_by_num(num):
    print("Введите номер книги, которую Вы хотите вывести на экран. 1 - 10")
    print()

def main():
    get_info(library)

if __name__=="__main__":
    main()
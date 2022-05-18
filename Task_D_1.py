"""
Необходимо создать текстовый файл и реализовать функцию логирования (без использования модуля
logging). Функция должна вызываться из каждого метода ранее реализованных классов и записывать в
файл строки следующего содержания: КЛЮЧ --- ДАТА И ВРЕМЯ --- КОММЕНТАРИЙ.
Ключи: CRE (создание экземпляра класса), INF (изменение), ERR (сработало исключение).
Комментарий: создано …, удален …, добавлен …, распечатан …
"""
from datetime import datetime
import pickle
from log import log
from Class import Class


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
    classs.__delitem__(index-1)
    print("Ученик по индексу[", index, "] удален!")
    print(classs)
except ValueError as err:
    log("ERR", err)
    print(err, "\nПопробуйте еще раз!")
    index = int(input())
    classs.__delitem__(index-1)
    print("Ученик по индексу[", index, "] удален!")
    print(classs)
except IndexError as err:
    log("ERR", err)
    print(err, "\nПопробуйте еще раз!")
    index = int(input())
    classs.__delitem__(index-1)
    print("Ученик по индексу[", index, "] удален!")
    print(classs)
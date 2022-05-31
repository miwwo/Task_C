"""
Создать класс Person с полями имя, фамилия, возраст. Добавить конструктор класса.
"""
from log import log
class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        log("CRE",'',"объект класса Person", "__init_")
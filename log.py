"""
Необходимо создать текстовый файл и реализовать функцию логирования (без использования модуля
logging). Функция должна вызываться из каждого метода ранее реализованных классов и записывать в
файл строки следующего содержания: КЛЮЧ --- ДАТА И ВРЕМЯ --- КОММЕНТАРИЙ.
Ключи: CRE (создание экземпляра класса), INF (изменение), ERR (сработало исключение).
Комментарий: создано …, удален …, добавлен …, распечатан …
"""
from datetime import datetime



def log(key, self = "self", inf = "inf", func="func"):
    f = open("log.txt", "a", encoding="utf-8")
    if key == "CRE":
        f.write(key + "---" + datetime.now().strftime("%d/%m/%Y %H:%M") + "---" + f"создано {self}.\n")
    elif key == "INF":
        if inf == "del":
            f.write(key + "---" + datetime.now().strftime("%d/%m/%Y %H:%M") + "---" + f"удалён {self} методом {func}.\n")
        elif inf == "add":
            f.write(key + "---" + datetime.now().strftime("%d/%m/%Y %H:%M") + "---" + f"добавлен {self} методом {func}.\n")
        elif inf == "pr":
            f.write(key + "---" + datetime.now().strftime("%d/%m/%Y %H:%M") + "---" + f"распечатан {self} методом {func}.\n")
        elif inf == "ch":
            f.write(key + "---" + datetime.now().strftime("%d/%m/%Y %H:%M") + "---" + f"изменен {self} методом {func}.\n")
    elif key == "ERR":
        f.write(key + "---" + datetime.now().strftime("%d/%m/%Y %H:%M") + "---" + f"сраболато исключение {self}.\n")
    f.close()

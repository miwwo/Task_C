# Написать функцию longest_word, которая возвращает последнее наибольшее по длине слово из заданной строки
#
# Пример:
# longest_word("red blue gold") ==> "gold"


import traceback


def longest_word(string_of_words):
    # Тело функции
    return ""


# Тесты
try:
    assert longest_word("a b c d e fgh") == "fgh"
    assert longest_word("one two three four five") == "three"
    assert longest_word("red blue grey") == "grey"
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")

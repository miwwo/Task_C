# Написать функцию palindrome, которая для заданного числа num возвращает список всех числовых палиндромов,
# содержащихся в каждом номере. Массив должен быть отсортирован в порядке возрастания,
# а любые дубликаты должны быть удалены.
#
# Пример:
# palindrome(34322122)  =>  [22, 212, 343, 22122]


import traceback

def pal(b):
    flag = 0
    length = len(b)-1
    for i in range(0, length // 2 + 1):
        if b[i] == b[length - i]:
            flag = 0
        else:
            flag = 1

            break
    return flag

def palindrome(line):
    palindromes = []
    a = str(line)
    linee=str(line)
    length = len(a)
    a = []
    for i in range(length):
        a.append(linee[i])
    flag = 0
    for j in range(0, length):
        b = []
        b.append(a[j])
        for k in range(j+1, length):
            b.append(a[k])
            if pal(b) == 0:
                c = ''
                for i in range(len(b)):
                    c = c+b[i]
                c = int(c)
                fl = 0
                for i in range(len(palindromes)):
                    if palindromes[i] == c or c == 0:
                        fl = 1
                if fl == 0:
                    palindromes.append(c)
                palindromes.sort()
    return palindromes


# Тесты
try:
    assert palindrome(1551) == [55, 1551]
    assert palindrome(221122) == [11, 22, 2112, 221122]
    assert palindrome(10015885) == [88, 1001, 5885]
    assert palindrome(13598) == []
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
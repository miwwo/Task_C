# Написать функцию max_mult(lst), которая возвращает список из двух элементов списка lst, 
# произведение которых будет максимальным. Список lst содержит целые числа.
#
# Пример:
# max_mult([1,2,3,4,5]) ==> [4,5] 
# max_mult([1,2,-3,4,-5]) ==> [-3,-5]


import traceback


def max_mult(lst):
    max_pr = temp = lst[0]*lst[1]
    ans = [0, 0]
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            temp = lst[i]*lst[j]
            print(lst[i],' ',lst[j])
            if temp >= max_pr:
                max_pr = temp
                ans[0] = lst[i]
                ans[1] = lst[j]
    return ans


# Тесты
try:
    assert max_mult([1, 2, 3, 4, 5]) == [4, 5]
    assert max_mult([1, 2, -3, 4, -5]) == [-3, -5]
    assert max_mult([4, 6, 2, -3, 0, 5, 1]) == [6, 5]
    assert max_mult([-5, -6, 3, 4, 6, 6, 1]) == [6, 6]
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")


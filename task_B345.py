# Написать функцию range_parser, которая переводит строку, задающую диапазон в соответствующий
# ему список целых чисел. Диапазон может включать в себя конструкции следующего вида
# n1-n2,n3,n4-n5:n6 (от n1 до n2 включительно, n3, от n4 до n5 включительно с шагом n6),
# конструкции могут быть разделены ',' или ', '
#
# Пример:
# range_parser("1-10,14, 20-25:2") ==> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 20, 22, 24]


import traceback

def func1(b,e,h):
    list=[]
    for i in range(b,e+1,h):
        list.append(i)
    return list

def func2(str,h):
    temp = str.split('-')
    j = 0
    temp[j] = int(temp[j])
    temp[j+1] = int(temp[j + 1])
    h=int(h)
    return func1(temp[j], temp[j + 1], h)

def range_parser(s):
    string = s
    w = string.split(', ')
    ans=[]
    for i in range(len(w)):
        str=w[i]
        temp1=str.split(',')
        for j in range(len(temp1)):
            str1=temp1[j]
            if str1.find('-')!=-1 and str1.find(':')==-1:
                ans+=func2(str1,1)
                #temp1.remove(temp1[j])
            if str1.find(':')!=-1:
                temp2=str1.split(':')
                k=0
                ans+=func2(temp2[k],temp2[k+1])
                #temp1.remove(temp1[j])
            if str1.find('-')==-1 and str1.find(':')==-1:
                temp1[j] = int(temp1[j])
                ans.append(temp1[j])


    return ans


# Тесты
try:
    assert range_parser("2") == [2]
    assert range_parser("5-10") == [5, 6, 7, 8, 9, 10]
    assert range_parser("1-10,14, 20-25:2") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 20, 22, 24]
    assert range_parser("1-3, 14-16,20-25:2, 26-30:3") == [1, 2, 3, 14, 15, 16, 20, 22, 24, 26, 29]
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")

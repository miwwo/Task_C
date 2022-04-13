# В цепочках ДНК аденин (A)	и тимин (T) являются дополнениями друг к другу,
# также как гуанин (G) и цитозин (C). Написать функцию DNA_strand, которая
# получив в виде строки одну цепочку возвращает вторую.
#
# Примеры:
# DNA_strand("ATTGC") ==> "TAACG"
# DNA_strand("GTAT") ==> "CATA"

import traceback


def DNA_strand(dna):
    string = dna
    print(string)
    news=''
    for i in range(len(string)):
        if string[i]=='A':
            news+='T'
        elif string[i]=='T':
            news +='A'
        elif string[i]=='G':
            news +='C'
        elif string[i]=='C':
            news +='G'
    return news


# Тесты
try:
    assert DNA_strand("ATTGCGCTTA") == "TAACGCGAAT"
    assert DNA_strand("AAAAAA") == "TTTTTT"
    assert DNA_strand("ATCGGGCCAATT") == "TAGCCCGGTTAA"
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")

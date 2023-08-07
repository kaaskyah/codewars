# Дезоксирибонуклеиновая кислота (ДНК) - химическое вещество, содержащееся в ядре клеток 
# и несущее в себе "инструкции" для развития и функционирования живых организмов.

# Если вы хотите узнать больше: http://en.wikipedia.org/wiki/DNA

# В строках ДНК символы "A" и "T" являются дополнением друг друга, как и "C" и "G". 
# Ваша функция получает одну сторону ДНК (строку, за исключением Haskell); вам нужно вернуть другую, 
# комплементарную ей сторону. Нить ДНК никогда не бывает пустой, либо ДНК вообще не существует 
# (опять же, за исключением Haskell).

# Другие похожие упражнения можно найти здесь: http://rosalind.info/problems/list-view/ (источник).

# Пример: (вход --> выход)

# "ATTGC" --> "TAACG"
# "GTAT" --> "CATA"

def DNA_strand(dna):
    res = ''
    for i in dna:
        if i == 'A':
            res += 'T'
        elif i == 'T':
            res += 'A'
        elif i == 'C':
            res += 'G'
        elif i == 'G':
            res += 'C'
    return res
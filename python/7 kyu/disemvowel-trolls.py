# Тролли атакуют ваш раздел комментариев!

# Обычный способ решения этой ситуации - удаление всех гласных из комментариев троллей, что нейтрализует угрозу.

# Ваша задача - написать функцию, которая принимает строку и возвращает новую строку с удаленными гласными.

# Например, строка "This website is for losers LOL!" превратится в "Ths wbst s fr lsrs LL!".

# Примечание: в этом ката y не считается гласной.

def disemvowel(string):
    res = ''
    for i in string:
        if i not in 'aeoiuAEOUI':
            res += str(i)
    return res
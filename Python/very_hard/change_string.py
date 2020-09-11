def change_string(word):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZA'
    return ''.join(alpha[alpha.index(i) + 1] if i.isupper() else i.upper() for i in word)[::-1]

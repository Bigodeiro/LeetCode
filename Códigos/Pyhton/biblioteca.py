def dec_SLS(func):
    def wrapper(input):

        input = list(input)
        val = func(input)
        return ''.join(val)

    return wrapper

def dec_tempo(func):
    def wrapper(a):

        print("inicio")
        val = func(a)
        print("fim")
        return val

    return wrapper

@dec_SLS
def testef(b):
    i = 0
    while i < len(b):                   #*chr: retorna o caractere correspondente ao numero do input
        b[i] = chr(ord(b[i]) + 1)       #*ord: retorna o numero correspondente ao caractere do input
        i += 1
    return b

@dec_tempo
def testea(a):
    print(a + 1)

testea(13)   
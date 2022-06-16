def dec_SLS(func):
    def wrapper(input):

        input = list(input)
        val = func(input)
        return ''.join(val)

    return wrapper

@dec_SLS
def testef(b):
    i = 0
    while i < len(b):
        b[i] = chr(ord(b[i]) + 1)
#chr: retorna o caractere correspondente ao numero do input
#ord: retorna o numero correspondente ao caractere do input
        i += 1
    return b


print(testef('teste'))
# Nesse arquivo vou reunir conhecimentos que aprendi ao longo do tempo sobre python que considero facil de esquecer.


#!DECORATORS
def decorator_StringListString(func):
    def wrapper(input):

        input = list(input)
        val = func(input)
        return ''.join(val)

    return wrapper

@decorator_StringListString
def testef(b):
    i = 0
    while i < len(b):                   #*chr: retorna o caractere correspondente ao numero do input
        b[i] = chr(ord(b[i]) + 1)       #*ord: retorna o numero correspondente ao caractere do input
        i += 1
    return b

#!Incialização do código
"""
Para permitr que o código seja usado como uma biblioteca mesmo, (sem ser executado quando importado) é necessário fazer essa inicialização, que checará em
qual contexto o código está sendo lido (no caso, "__main__" indica que ele está sendo lido para ser executado), para que possamos importar apenas as 
funções se quisermos.
"""
if __name__ == "__main__":

    print(f"{testef('teste')}\n") #*nota: é possivel usar as diferentes as aspas para conseguir usar o printf propriamente

    #!FOR ... ELSE 
    #? quando acaba o array o "else" é executado
    arr = [1,2,3]
    for x in arr:
        print("as vezes")
    else: print(f"sempre \n")

    #! OPERADOR TERNÁRIO
    score = 10 

        #?opção1 if condição else opção 2
    result = "passou" if score > 6 else "reprouvou"
    print(f"{result}\n")
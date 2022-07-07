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

    #!FOR ... ELSE
    def for_selse():
        #? quando acaba o array o "else" é executado
        arr = [1,2,3]
        for x in arr:
            print("as vezes")
        else: print(f"sempre \n")

    #! OPERADOR TERNÁRIO
    def operador_ternario():
        score = 10 

            #?opção1 if condição else opção 2
        result = "passou" if score > 6 else "reprouvou"
        print(f"{result}\n")

    #! ENUMERATE
    #? enumerate() é uma função que pode ser usada em um loop, ela retorna um contador de quantas vezes aconteceu o loop, e retorna a variavel/elemento de uma lista ou qualquer outra estrutura de dados que seja iterável

    def enumumerate_1():
        #*Se apenas uma variavel recebe o enumerate(), é retornado uma tupla com o numero da iteração, e o valor respectivo da varivel
        var_iteravel = ['a', 'b', 'c', 'd']

        for x in enumerate(var_iteravel):
            print(f"{x} {type(x)}")
    
    def enumumerate_2():
        #*Se duas variaveis recebem o enumerate(), é retornado um int com o numero da iteração, e o elemento respectivo 
        var_iteravel = ['a', 'b', 'c', 'd']

        for contador, valor in enumerate(var_iteravel):
            print(f"{contador} {valor}")
    
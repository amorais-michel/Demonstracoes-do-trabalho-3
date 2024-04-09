import math

numero_erro= float(input("Numero:"))

fatorial = 0
e = 0
erro = float('inf')
while erro > numero_erro:
    e = e + 1 / math.factorial(fatorial)
    erro = 1 / math.factorial(fatorial)
    fatorial +=1
    print("e = ", e)
    print("Erro de é menor do que = ", erro)




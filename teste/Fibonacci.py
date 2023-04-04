# solicita que o usuário informe um número
num = int(input("Digite um número: "))
fib1, fib2 = 0, 1

# loop que calcula a sequência de Fibonacci até encontrar um valor maior ou igual ao número informado
while fib2 < num:
    fib1, fib2 = fib2, fib1 + fib2
    
# verifica se o número informado pertence à sequência
if fib2 == num:
    print(num, "pertence à sequência de Fibonacci")
else:
    print(num, "não pertence à sequência de Fibonacci")

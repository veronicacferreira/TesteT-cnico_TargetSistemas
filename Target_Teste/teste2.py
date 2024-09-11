def n_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n
    
numero = int(input("Digite um número: "))
if n_fibonacci(numero):
    print("O número pertence à sequência de Fibonacci!")
else:
    print("O número não pertence à sequência de Fibonacci!")
def pertence_fibonacci(n):
  

    def is_perfeito_quadrado(x):
        
        import math
        raiz = int(math.sqrt(x))
        return raiz * raiz == x

   
    def eh_numero_fibonacci(x):
       
        return is_perfeito_quadrado(5 * x * x + 4) or is_perfeito_quadrado(5 * x * x - 4)

    return eh_numero_fibonacci(n)


numero = int(input("Digite um número: "))


if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")

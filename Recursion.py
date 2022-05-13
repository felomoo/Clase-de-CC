"""def factorial(n):
    #caso base
    if n == 0:
        return 1
        #caso recursivo
    else:
        #n! = n * (n-1)!
        return n * factorial(n-1)
def main():
    n = int(input("Ingrese un numero n: "))
    print("El factorial de", n, "es", factorial(n))
main()"""

"""def elevar(base, potencia):
    if potencia == 0:
        return 1
    else:
        n = base * elevar(base, potencia - 1)"""

def fibonacci(n):
    if n ==0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n -2) + fibonacci(n-1)

def main():
    n = int(input("Ingrese un numero n: "))
    print("El fibonacci de:", n, "es", fibonacci(n))
main()

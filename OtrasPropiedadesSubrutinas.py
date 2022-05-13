#OPERACIONES
"""def suma(a,b):
    return a + b

def resta(a,b):
    return a- b

def mult(a,b):
    return a * b

def miOperacion(v1, v2, op):
    return op(v1, v2)

def main():
    print("Suma:", miOperacion(10, 5, suma))
    print("Resta:", miOperacion(10, 5, resta))
    print("Multi:", miOperacion(10, 5, mult))

main()"""

"""def sumatoria(n, operacion):
    cont, acc = 1, 0
    while cont <= n:
        acc = acc + operacion(cont)
        cont+=1
    return acc

def valor(x):
    return x

def cuadrado(x):
    return x*x

def cubo(x):
    return x*x*x"""

def funcion_compuesta(f,g):
    def h(x):
        return f(g(x))

    return h
def cuadrado(x):
    return x*x
def sucesor(x):
    return x + 1

func1 = funcion_compuesta(cuadrado, sucesor)
func2 = funcion_compuesta(sucesor, cuadrado)

print("Resultrado cuadrado-sucesor", func1(10))
print("Resultado sucesor-cuadrado:", func2(10))
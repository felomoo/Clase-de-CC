#def suma(a,b):
#    return a + b

#def resta(a,b):
#    return a- b

#def mult(a,b):
#    return a * b

"""def miOperacion(v1, v2, op):
    return op(v1, v2)

def main():
    print("Suma:", miOperacion(10, 5, lambda x,y: x + y))
    print("Resta:", miOperacion(10, 5, lambda x,y: x - y))
    print("Multi:", miOperacion(10, 5, lambda x,y: x * y))

main()"""

"""def funcion_compuesta(f,g):
    return lambda x: f(g(x))
def cuadrado(x):
    return x*x
def sucesor(x):
    return x + 1

func1 = funcion_compuesta(lambda x: pow(x,2), lambda x: x+1)
func2 = funcion_compuesta(sucesor, cuadrado)

print("Resultrado cuadrado-sucesor", func1(10))
print("Resultado sucesor-cuadrado:", func2(10))"""

l1 = list(range(1,21))

l2 = list(range(1,41,2))

r = list(map(lambda x, y: x + y, l1,l2))
print(l1)
print(l2)
print(r)



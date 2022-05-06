import random
f = open("prueba.txt")

def leerLinea():
    txt = f.readline()
    print(txt)

def leerlINEAS():
    s = f.read()
    print(s)

def leerEnLista():
    l = f.readlines()
    print(l)

def leerParametro():
    x = random.randint(0,20)
    a = f.read(x)

def escribir():
    archivo = open("prueba2.txt", "w")
    archivo.write("primer linea\n")
    archivo.write("Segunda linea\n")
    archivo.write("Terncera linea\n")
    archivo.close()
def escribirSeguido():
    archivo=open("prueba2.txt", "a")
    archivo.write("Siguiente linea\n")
    archivo.close()

escribirSeguido()
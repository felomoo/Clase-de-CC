import time
import random
from threading import Thread

def generador(l):
    for cont in range(8):
        v = random.randint(1,99)
        time.sleep(1)
        l.append(v)
        print('GAenerador:', l)

def consumidor(l):
    for cont in range(5):
        time.sleep(2)
        v = l.pop(0)
        print('el consumidor saco:', v)

def main():
    lista = []
    print('La lista empieza', lista)
    th1 = Thread(target=generador, args=(lista,))
    th2 = Thread(target=consumidor, args = (lista,))

    th1.start()
    th2.start()

main()
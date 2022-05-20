from threading import Thread
import time

#Definir Subrutina

def printer(number, n, tiempo):
    for x in range(1,n):
        print('Thread #',number, ': ',x)
        time.sleep(tiempo)
    print('thread #',number,'termino')

def main():
    THR = Thread(target=printer, args=(1,20,0.25,))
    THR.start()
    thr = Thread(target=printer, args = (2,15,0.67,))
    thr.start()
    for cont in range(10):
        print('principal:', cont)
        time.sleep(0.5)

main()
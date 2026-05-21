import multiprocessing
import time


semaforo = None
sentido: int = 0

def init(s, sen):
    global semaforo
    global sentido
    semaforo=s
    sentido = sen

def cruzamento(carro):
    global semaforo
    global sentido
    with semaforo:
        sentido.value = sentido.value + 1

        if sentido.value ==1:
            sent = 'Norte'
        elif sentido.value ==2:
            sent = 'Sul'
        elif sentido.value ==3:
            sent = 'Leste'
        elif sentido.value ==4:
            sent = 'Oeste'

    
        
        print('O carro', carro, 'passou o cruzamento no sentido', sent)
        



def main():
    sem =  None
    params: int = [0] * 4
    
    sent: int = 0 

    sent = multiprocessing.Value('i', 0)

    for i in range(4):
        params[i]= (i+1)

  
    with multiprocessing.Manager() as manager:
        sem = manager.Semaphore(1)
        with multiprocessing.Pool(processes=4, initializer=init, initargs=(sem, sent)) as pool:
            pool.map(cruzamento,params)


if __name__ == '__main__':
    main()
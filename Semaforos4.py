import multiprocessing
import random
import time 


semaforo = None
def init(s):
    global semaforo
    semaforo = s

def voltas(equipe, carro):
    global semaforo
    tempo: int = 0
    voltas: int = 1 
    


    with semaforo:
        while voltas <= 3:
            tempo = random.randint(1, 3)
            time.sleep(tempo)
            print ('O', carro, 'da equipe', equipe, 'levou', tempo, 'minutos na volta', voltas )
            voltas +=1


def main():
    sem = None
    params = [(0, 0)] *14

    for i in range (14):
        equipe = (i//2) + 1
        params[i] = (equipe, 'carroA')
        if i%2 != 0:
            params[i] = (equipe, 'CarroB')
    
    print (params)

    with multiprocessing.Manager() as manager:
        sem = manager.Semaphore(5)
        with multiprocessing.Pool(processes=14, initializer=init, initargs=(sem,)) as pool:
            pool.starmap(voltas, params)

    



if __name__ == '__main__':
    main()
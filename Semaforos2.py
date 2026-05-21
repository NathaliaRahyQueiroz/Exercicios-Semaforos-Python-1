import multiprocessing
import random
import time

pos_porta: int  = 0
semaforo = None
def init(pos, s):
    global pos_porta
    global semaforo
    pos_porta = pos
    semaforo = s

def percurso(pessoa, velocidade, t):
    global semaforo 
    dis: int = 200
    total: int = 0 
    
    
    while total<dis:

        total = total + velocidade

       

        time.sleep(0.1)

        if total>=dis:

            with semaforo:
                pos_porta.value = pos_porta.value + 1
                print ('A pessoa', pessoa, 'atravessou a porta na posição', pos_porta.value)
                time.sleep(t)
        else:
             print ('A pessoa', pessoa, 'andou', total, 'metros')

def main():
    posicao: int  = 0
    posicao = multiprocessing.Value('i', 0)
    vel: int =0
    tempo: int =0
    params = [(0, 0, 0)] *4
    sem = None

    for i in range(4):
        vel = random.randint(4, 6)
        tempo = random.randint(1, 2)
        params[i] = (i+1, vel, tempo)

    print (params)

    with multiprocessing.Manager() as manager:
        sem = manager.Semaphore(1)
        with multiprocessing.Pool(processes=4, initializer=init, initargs=(posicao, sem)) as pool:
            pool.starmap(percurso, params)

if __name__ == '__main__':
    main()
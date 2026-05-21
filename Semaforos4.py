import multiprocessing
import random
import time 


semaforo = None
equipes = None

def init(s, eq):
    global semaforo
    global equipes
    semaforo = s
    equipes = eq
    


def pista(equipe, carro):
    global semaforo
    global equipes 
    voltas: int = 1
    tempo: int = 0


        
    

    with semaforo:
        while equipe in equipes:
            time.sleep(0.2)


        for i in range (5):
            if equipes[i] == 0:
                equipes[i] = equipe
                break
            

        while voltas<=3:
            tempo = random.randint(1,3)
            time.sleep(tempo)
            print ('O', carro, 'da equipe', equipe, 'levou', tempo, 'minutos na volta', voltas )
            voltas +=1

        for i in range (5):
            if equipes[i] == equipe:
                equipes[i] = 0
                break

def main():
    sem = None
    equipes: int = [0]*5
    equipes = multiprocessing.Array('i', equipes)
    params = [(0,0)] *14

    for i in range (14):
        equipe = (i//2) + 1
        params[i] = (equipe, 'Carro_A')
        if i%2 != 0:
            params[i] = (equipe, 'Carro_B')
    
    

    with multiprocessing.Manager() as manager:
        sem = manager.Semaphore(5)
        with multiprocessing.Pool(processes=14, initializer=init, initargs=(sem, equipes,)) as pool:
            pool.starmap(pista, params)

    



if __name__ == '__main__':
    main()



import multiprocessing
import time
import random

pos_chegada: int = 0 

def init(chegada):
    global pos_chegada
    pos_chegada = chegada

def processamento (sapo, distancia):
    global pos_chegada
    total: int = 0
    pulo: int = 0

    
    while total < distancia:
        
        pulo = random.randint(1, 5)
            
        total = total + pulo
        
        time.sleep(0.5)
        if total >= distancia:
            pos_chegada.value +=1
            print ('O sapo', sapo, 'chegou em',pos_chegada.value,'º lugar')
        else:
            print ('O sapo', sapo, 'deu um pulo de', pulo, 'cm e percorreu', total, 'cm')

    

def main():
    
    params = [(0, 0)] * 5
    distancia = int(input('Digite a distância total a ser percorrida:'))
    chegada:int =0
    chegada = multiprocessing.Value('i', 0)

    for i in range (5):
        
        params [i] = (i+1, distancia)
    
    with multiprocessing.Pool(processes=5, initializer=init, initargs=(chegada,)) as pool:
        pool.starmap(processamento, params)

if __name__ == '__main__':
    main()
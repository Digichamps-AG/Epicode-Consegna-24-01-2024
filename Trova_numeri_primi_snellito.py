#Elencare i numeri primi da 1 a n, chiedendo n all'utente e implementando l'algoritmo del "Crivello di Eratostene"

import numpy as np


def prime_numbers(x: int):
    '''
    inserire il numero (intero, positivo) fino a cui si vogliono conoscere i numeri primi
    '''
    #mi serve un array che mi dia i primi x numeri
    crivello = np.arange(2, x+1, 1)
    

    #ora devo creare un filtro che elimini tutti i multipli di 2
    filtroMultipli2 = crivello % 2 != 0 
 

    #ora devo creare un filtro che elimini tutti i multipli di 3, usando l'array in cui ho già tolto i multipli di 2
    filtroMultipli3 = crivello % 3 != 0
   
    #ora devo creare un filtro che elimini tutti i multipli di 5, usando l'array in cui ho già tolto i multipli di 3
    filtroMultipli5 = crivello % 5 != 0
     
    #ora devo creare un filtro che elimini tutti i multipli di 7, usando l'array in cui ho già tolto i multipli di 5
    filtroMultipli7 = crivello % 7 != 0

    #mi servono i numeri per cui ho filtrato, in forma di array
    numeri_filtrati = np.array([2,3,5,7])

    #mi serve il crivello con tutti i filtri:
    crivello_filtrato = crivello[filtroMultipli2 & filtroMultipli3 & filtroMultipli5 & filtroMultipli7]

    #mi serve un array finale con i numeri per cui ho filtrato e il crivello filtrato
    numeri_primi = np.concatenate([numeri_filtrati, crivello_filtrato])
    return(numeri_primi)

test = prime_numbers(55)
print(test)
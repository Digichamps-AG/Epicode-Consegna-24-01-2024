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
    crivello_senza_2 = crivello[filtroMultipli2]
   

    #ora devo creare un filtro che elimini tutti i multipli di 3, usando l'array in cui ho già tolto i multipli di 2
    filtroMultipli3 = crivello_senza_2 % 3 != 0
    crivello_senza_3 = crivello_senza_2[filtroMultipli3]

    #ora devo creare un filtro che elimini tutti i multipli di 5, usando l'array in cui ho già tolto i multipli di 3
    filtroMultipli5 = crivello_senza_3 % 5 != 0
    crivello_senza_5 = crivello_senza_3[filtroMultipli5]
 
    #ora devo creare un filtro che elimini tutti i multipli di 7, usando l'array in cui ho già tolto i multipli di 5
    filtroMultipli7 = crivello_senza_5 % 7 != 0
    crivello_senza_7 = crivello_senza_5[filtroMultipli7]

    #mi servono i numeri per cui ho filtrato, in forma di array
    numeri_filtrati = np.array([2,3,5,7])

    #mi serve un array finale con i numeri per cui ho filtrato e quelli filtrati
    numeri_primi = np.concatenate([numeri_filtrati, crivello_senza_7])
    return(numeri_primi)

test = prime_numbers(55)
print(test)
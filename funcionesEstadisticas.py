# Para la materia de estadistica 1 se implementan las siguientes formulas
#  a) Esperanza
#  b) Varianza

import numpy as np


def esperanza(x):
    """
        esperanza = promedio

        Parametros:

            - x: list, los datos para a calcular
    """
    return np.mean(x)

def varianza(x,exp,varSample=True,sqr=False):
    """
        La forma en la que se calcula la varianza es usando E(x**exp) - E(x)**exp

        Parametros:

            - x: list, los datos para a calcular
            - exp: int, el exponente en el cual se calculará la varianza
            - varSample: bool, si calculará la varianza muestral o no
            - sqr: bool, regresa la raizaexp de la varianza
    """
    if varSample:
        result = 0
        xTilde = esperanza(x)
        for i in x:
            result += (i - xTilde)**exp
        return result/(len(x)-1) if sqr == False else (result/(len(x)-1))**(1/exp)
    else:
        return np.mean(np.array(x)**exp) if sqr == False else np.mean(np.array(x)**exp)**(1/exp)

def momentoMedia(x,exp,mSample=False):
    result = 0
    xTilde = esperanza(x)
    for i in x:
        result += (i - xTilde)**exp
    return result/(len(x)-1) if mSample else result/len(x)



print(momentoMedia([2,3,4,5,6.1,6.3,6.5,6.5,6.5,6.5,6.5,6.7,6.9,7,8,9,10],3))
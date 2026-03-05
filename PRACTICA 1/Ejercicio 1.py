import time
import random

class Cronometro:

    def __init__(self):
        self.__inicia = int(time.time() * 1000)
        self.__finaliza = 0

    def get_inicia(self):
        return self.__inicia

    def get_finaliza(self):
        return self.__finaliza

    def inicia(self):
        self.__inicia = int(time.time() * 1000)

    def detener(self):
        self.__finaliza = int(time.time() * 1000)

    def lapsoDeTiempo(self):
        return self.__finaliza - self.__inicia


if __name__ == "__main__":

    numeros = [random.randint(0, 100000) for _ in range(100000)]

    cronometro = Cronometro()

    for i in range(len(numeros) - 1):
        minimo = i
        for j in range(i + 1, len(numeros)):
            if numeros[j] < numeros[minimo]:
                minimo = j
        numeros[i], numeros[minimo] = numeros[minimo], numeros[i]

    cronometro.detener()

    print("Tiempo de ejecucion:", cronometro.lapsoDeTiempo(), "milisegundos")
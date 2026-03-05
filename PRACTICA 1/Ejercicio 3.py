import math

class EcuacionCuadratica:

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def getDiscriminante(self):
        return self.__b**2 - 4 * self.__a * self.__c

    def getRaiz1(self):
        if self.getDiscriminante() >= 0:
            return (-self.__b + math.sqrt(self.getDiscriminante())) / (2 * self.__a)
        return 0

    def getRaiz2(self):
        if self.getDiscriminante() >= 0:
            return (-self.__b - math.sqrt(self.getDiscriminante())) / (2 * self.__a)
        return 0


if __name__ == "__main__":

    a, b, c = map(float, input("Ingrese a, b, c: ").split())

    ecuacion = EcuacionCuadratica(a, b, c)

    discriminante = ecuacion.getDiscriminante()

    if discriminante > 0:
        print("La ecuacion tiene dos raices", ecuacion.getRaiz1(), "y", ecuacion.getRaiz2())
    elif discriminante == 0:
        print("La ecuacion tiene una raiz", ecuacion.getRaiz1())
    else:
        print("La ecuacion no tiene raices reales")
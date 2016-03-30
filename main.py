# calcula la potencia de 2 ints con una base < 10 y exponente < 4, ambos positivos
from dbConnection import dbConnection

class Power:
    def __init__(self, base, exponent):
        self.base = base
        self.exponent = exponent

    def powerFunction(self):
        if self.base.__class__.__name__ != "int":
            raise Exception

        # if self.base.__class__.__name__ > 10 or self.base.__class__.__name__ < 0:
        #     raise Exception
        # if self.exponent.__class__.__name__ > 4 or self.exponent.__class__.__name__ < 0:
        #     raise Exception
        result = pow(self.base, self.exponent)
        return result

    #calcula la raiz cuadrada de la base y comprueba si es negativa
    def squareRoot(self):
        if self.base.__class__.__name__ < 0:
            raise Exception


def main():
    #Entrada a la base de datos

    dbConnection1 = dbConnection('power')
    print 'Calcular potencia de tipo entero:\n'
    print 'Introduzca la base: (0<base<10)'
    base = raw_input()
    print 'Introduzca el exponente (0<=base<4)\n'
    exponent = raw_input()
    power = Power(base, exponent)

    resultado = power.powerFunction(power.base, power.exponent)
    dic = {'resultado': resultado}
    dbConnection.collection.save(dic)



    print 'la base es:'
    print power.base
    print 'el exponente es:'
    print power.exponent


if __name__ == '__main__':
   main()




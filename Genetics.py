# coding=utf-8
"""
import random
#import pdb
#import math

class IndividuoRep:

    ##############
    #Class Vars:
    #Nbits - Numero de bits para a representacao 1 bit para parte inteira, 7 bits para a fracionaria
    #Tipo = Tipo de representacao, 'd' para decimal e 'b' para binaria
    #codific[Nbits] - Representação do individuo
    #value - valor da representacao
    #fitnessValue - valor de avaliacao
    ###############

    def __init__(self, Nbits, RangeX, RangeY, InicializacaoX=None, InicializacaoY=None, Tipo='d', orderNumber=1, Generation=1):
        self.Nbits = Nbits
        self.Tipo = Tipo
        self.codificX = range(Nbits)
        self.codificY = range(Nbits)
        self.valueX = InicializacaoX
        self.valueY = InicializacaoY
        self.number = orderNumber
        self.Generation = Generation
        try:
            if InicializacaoX is None and InicializacaoY is None:
                if Tipo == 'd':
                    self.codificX[0] = random.choice(range(RangeX[0], RangeX[1]))
                    self.codificY[0] = random.choice(range(RangeY[0], RangeY[1]))
                    for i in range(len(self.codificX)-1):
                        self.codificX[i+1] = random.choice(range(0, 9))
                        self.codificY[i+1] = random.choice(range(0, 9))
                    self.valueX = self.setToNumber()
                else:
                    for i in range(len(self.codific)-1):
                        self.codific[i+1] = random.choice(range(0, 1))
            else:
                self.codific = [int(x) for x in str(Inicializacao)]
        except TypeError:
            print("Missing Args")
        self.fitnessValue = self.fitnessFunction()

    def setToNumber(self):
        parteInteira = self.codific[0]
        strConvert = ''
        parteFrac = int(strConvert.join(str(element) for element in self.codific[1:]))
        parteFrac = parteFrac/pow(10, self.Nbits-1)
        return parteInteira+parteFrac

    def fitnessFunction(self):
        # Override this
        return 0

    def mutation(self):
        # Override this
        return 0

    def crossOver(self):
        # Override this
        return 0

    def __str__(self):
        print("Individuo {} da geracao {}".format(self.number, self.Generation))
        print("Valor: {}".format(self.value), end=' ')
        print(self.codific)
        print("Valor de Fitness: {}".format(self.fitnessValue))

    def getNbits(self):
        return self.Nbits

    def getTipo(self):
        return self.Tipo

    def getCodific(self):
        return self.codific

    def getValue(self):
        return self.value

    def getFitnessValue(self):
        return self.fitnessValue

    def getGeneration(self):
        return self.Generation

    def getOrder(self):
        return self.number
"""

from abc import ABCMeta, abstractmethod
import random
import pdb
from NotImplementedError import NotImplementedException

class IndividuoRep(metaclass=ABCMeta):


    ##############
    #Class Vars:
    #Nbits - Numero de bits para a representacao 1 bit para parte inteira, 7 bits para a fracionaria
    #Tipo = Tipo de representacao, 'd' para decimal e 'b' para binaria
    #codificX[Nbits] - Representação do individuo X
    #codificY[Nbits] - Representação do Individuo Y
    #number - Nth filho gerado
    #generation - geracao do individuo
    #valueX - valor da representacao X
    #valueY - valor da representacao Y
    #fitnessValue - valor de avaliacao
    #NPI - Quantidade de bits para a parte inteira
    #NPF - Quantidade de bits para a parte fracionaria
    ###############

    def __init__(self, Nbits, RangeX, RangeY, InicializacaoX=None, InicializacaoY=None, Tipo='d', orderNumber=1, Generation=1, PI=1):
	
        self.Nbits = Nbits
        pdb.set_trace()
        self.Tipo = Tipo
        self.codificX = []
        self.codificY = []
        self.valueX = InicializacaoX
        self.valueY = InicializacaoY
        self.number = orderNumber
        self.Generation = Generation
        self.NPI = PI
        self.NPF = Nbits - PI
        try:
            if InicializacaoX is None and InicializacaoY is None:
                if Tipo == 'd':
                    self.codificX.append(random.choice(range(RangeX[0], RangeX[1])))
                    self.codificY.append(random.choice(range(RangeY[0], RangeY[1])))
                    for i in range(self.Nbits - 1):
                        self.codificX.append(random.choice(range(0, 9)))
                        self.codificY.append(random.choice(range(0, 9)))
                    self.valueX = self.setToNumber()[0]
                    self.valueY = self.setToNumber()[1]
                else:
                    for i in range(len(self.codific) - 1):
                        self.codificX[i + 1] = random.choice(range(0, 1))
                        self.codificY[i + 1] = random.choice(range(0, 1))
                    raise NotImplementedException
            else:
                raise NotImplementedException
        except TypeError:
            print("Missing Args")
        except NotImplementedException:
            print("This feature wasn't implemented yet")
        self.fitnessValue = self.fitnessFunction()

    #TODO
    #Implementar parte inteira/fracionaria com quantidade de bits variavel

    def setToNumber(self):
        parteInteiraX = self.codificX[0]
        parteInteiraY = self.codificY[0]
        strConvertX = ''
        strConvertY = ''
        parteFracX = int(strConvertX.join(str(element) for element in self.codificX[1:]))
        parteFracY = int(strConvertY.join(str(element) for element in self.codificY[1:]))
        parteFracX = parteFracX/pow(10, self.Nbits - 1)
        parteFracY = parteFracY/pow(10, self.Nbits - 1)
        return [parteInteiraX + parteFracX, parteInteiraY + parteFracY]

    @abstractmethod
    def fitnessFunction(self):
        pass

    @abstractmethod
    def mutation(self):
        pass

    @abstractmethod
    def crossOver(self):
        pass

    def __str__(self):
        print("Individuo {} da geracao {}".format(self.number, self.Generation))
        print("ValorX: {}, ValorY: {}".format(self.valueX, self.valueY))
        print("X: {}, Y: {}".format(self.codificX, self.codificY))
        print("Valor de Fitness: {}".format(self.fitnessValue))

    def getNbits(self):
        return self.Nbits

    def getTipo(self):
        return self.Tipo

    def getCodific(self):
        return [self.codificX, self.codificY]

    def getValue(self):
        return [self.valueX, self.valueY]

    def getFitnessValue(self):
        return self.fitnessValue

    def getGeneration(self):
        return self.Generation

    def getOrder(self):
        return self.number
# coding=utf-8

__author__ = "Airton Depauli Junior"
__license__ = "GPL"


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
        #pdb.set_trace()
        self.Tipo = Tipo
        self.codificX = []
        self.codificY = []
        self.valueX = InicializacaoX
        self.valueY = InicializacaoY
        self.number = orderNumber
        self.Generation = Generation
        self.NPI = PI
        self.NPF = Nbits - PI
        self.EspacoBuscaX = RangeX
        self.EspacoBuscaY = RangeY
        self.fitnessValue = 0
        self.debug = False
        try:
            if InicializacaoX is None and InicializacaoY is None:
                if Tipo == 'd':
                    self.codificX.append(random.randint(RangeX[0], RangeX[1]))
                    self.codificY.append(random.randint(RangeY[0], RangeY[1]))
                    for i in range(self.Nbits - 1):
                        self.codificX.append(random.randint(0,9))
                        self.codificY.append(random.randint(0,9))
                    #self.valueX = self.setToNumber()[0]
                    #self.valueY = self.setToNumber()[1]
                    self.boundariesCorrection(RangeX, RangeY)
                    self.setToNumber()
                else:
                    for i in range(len(self.codificX) - 1):
                        self.codificX[i + 1] = random.randint(0,1)
                        self.codificY[i + 1] = random.randint(0,1)
                    raise NotImplementedException
            else:
                raise NotImplementedException
        except TypeError:
            print("Missing Args")
        except NotImplementedException:
            print("This feature wasn't implemented yet")
        #self.fitnessValue = self.fitnessFunction()
        self.fitnessFunction()

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
        if parteInteiraX>=0:
            self.valueX = parteInteiraX + parteFracX
        else:
            self.valueX = parteInteiraX - parteFracX
        if parteInteiraY>=0:
            self.valueY = parteInteiraY + parteFracY
        else:
            self.valueY = parteInteiraY - parteFracY
        #return [parteInteiraX + parteFracX, parteInteiraY + parteFracY]

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
        return "Individuo {} da geracao {}\nValorX: {}, ValorY: {}\nX: {}, Y: {}\nValor de Fitness: {}\n".format(self.number, self.Generation,self.valueX, self.valueY, self.codificX, self.codificY, self.fitnessValue)
        #print("Individuo {} da geracao {}".format(self.number, self.Generation))
        #print("ValorX: {}, ValorY: {}".format(self.valueX, self.valueY))
        #print("X: {}, Y: {}".format(self.codificX, self.codificY))
        #print("Valor de Fitness: {}".format(self.fitnessValue))

    def getNbits(self):
        return self.Nbits

    def getTipo(self):
        return self.Tipo

    def getCodificX(self):
        return self.codificX

    def getCodificY(self):
        return self.codificY

    def getValueX(self):
        return self.valueX

    def getValueY(self):
        return self.valueY

    def getFitnessValue(self):
        return self.fitnessValue

    def getGeneration(self):
        return self.Generation

    def getOrder(self):
        return self.number

    def setCodificX(self, nCodificX):
        self.codificX = nCodificX

    def setCodificY(self, nCodificY):
        self.codificY = nCodificY

    def update(self):
        self.boundariesCorrection2(self.EspacoBuscaX, self.EspacoBuscaY)
        self.setToNumber()
        self.fitnessFunction()

    def boundariesCorrection(self, RangeX, RangeY):
        if self.codificX[0] == RangeX[0] or self.codificX[0] == RangeX[1]:
            if random.random() <= 0.7:
                self.codificX[0] = 0
            else:
                for i in range(1, self.Nbits):
                    self.codificX[i] = 0
        if self.codificY[0] == RangeY[0] or self.codificY[0] == RangeY[1]:
            if random.random() <= 0.7:
                self.codificY[0] = 0
            else:
                for i in range(1, self.Nbits):
                    self.codificY[i] = 0

    def boundariesCorrection2(self, RangeX, RangeY):
        if self.codificX[0] == RangeX[0] or self.codificX[0] == RangeX[1]:
            for i in range(1, self.Nbits):
                self.codificX[i] = 0
        if self.codificY[0] == RangeY[0] or self.codificY[0] == RangeY[1]:
            for i in range(1, self.Nbits):
                self.codificY[i] = 0

    def correctOrderNumber(self):
        pass


    #TODO
    #Separate Functions call, just one return per function
    #Method signature must be the same for abstractmethod and overridden method
    #Corrections with OO
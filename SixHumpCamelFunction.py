from Genetics import IndividuoRep
import random
import math


class SHCamel(IndividuoRep):
    def fitnessFunction(self):
        firstTerm = (4 - 2.1 * (self.valueX * self.valueX) + (pow(self.valueX, 4) / 3)) * self.valueX * self.valueX
        secondTerm = (-4 + 4 * (self.valueY * self.valueY)) * (self.valueY * self.valueY)
        self.fitnessValue = firstTerm + self.valueX * self.valueY + secondTerm
        #return firstTerm + self.valueX * self.valueY + secondTerm

    def mutation(self, mutationProbability):
        if random.random()<mutationProbability/100:
            if self.debug:
                print("\n\nMutation\n\n")
            escolha = random.randint(1,3)
            if escolha == 1:
                posicaoMut = random.randint(0, self.Nbits-1)
                if self.debug:
                    print("Mutacao em X, posicao {}".format(posicaoMut))
                if posicaoMut == 0:
                    self.codificX[posicaoMut] = random.randint(self.EspacoBuscaX[0], self.EspacoBuscaX[1])
                else:
                    self.codificX[posicaoMut] = random.randint(0,9)
            elif escolha == 2:
                posicaoMut = random.randint(0, self.Nbits-1)
                if self.debug:
                    print("Mutation em Y, posicao {}".format(posicaoMut))
                if posicaoMut == 0:
                    self.codificY[posicaoMut] = random.randint(self.EspacoBuscaY[0], self.EspacoBuscaY[1])
                else:
                    self.codificY[posicaoMut] = random.randint(0,9)
            else:
                posicaoMutX = random.randint(1, self.Nbits-1)
                posicaoMutY = random.randint(1, self.Nbits-1)
                if self.debug:
                    print("Mutation in X, posicao {}\nMutation in Y, posicao {}".format(posicaoMutX, posicaoMutY))
                self.codificX[posicaoMutX] = random.randint(0,9)
                self.codificY[posicaoMutY] = random.randint(0,9)
        if self.debug:
            print("Old value X: {}\nOld value Y: {}". format(self.getValueX(), self.getValueY()))
        self.update()

    #TODO
    # Mutation as a sum of a random value (derivative??)
    # Replace for upper boundary

    #SINGLE POINT Crossover
    def crossOver(self, Partner):
        crossPoint = random.randint(0, self.Nbits-1)
        if self.debug:
            print(crossPoint)
            print("X1: {} Y1: {}".format(self.codificX, self.codificY))
            print("X2: {} Y2: {}".format(Partner.getCodificX(), Partner.getCodificY()))
        TempVectorX = self.codificX
        TempVectorY = self.codificY
        self.codificX = self.codificX[:crossPoint+1] + Partner.getCodificX()[crossPoint+1:]
        Partner.setCodificX(Partner.getCodificX()[:crossPoint+1]+TempVectorX[crossPoint+1:])
        self.codificY = self.codificY[:crossPoint + 1] + Partner.getCodificY()[crossPoint + 1:]
        Partner.setCodificY(Partner.getCodificY()[:crossPoint + 1] + TempVectorY[crossPoint + 1:])
        if self.debug:
            print("NewX1: {}, NewY1: {}".format(self.codificX, self.codificY))
            print("NewX2: {}, NewY2: {}".format(Partner.getCodificX(), Partner.getCodificY()))
        self.update()
        Partner.update()

    #TODO
    #Uniform Crossover
    #Two Point Crossover
    #Different Positions for X and Y axis

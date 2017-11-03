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
            print("Old value X: {}\nOld value Y: {}". format(self.getValue()[0], self.getValue()[1]))
        self.update()

    #TODO
    # Mutation as a sum of a random value (derivative??)
    # Replace for upper boundary

    #SINGLE POINT Crossover
    def crossOver(self, Partner):
        crossPoint = random.randint(0, self.Nbits-1)
        self.codificX = self.codificX[:crossPoint+1] + Partner.getCodific()[0][crossPoint+1:len(self.codificX)]
        Partner.setCodificX(Partner.getCodific()[0][crossPoint+1]+self.codificX[crossPoint+1:len(self.codificX)])
        self.codificY = self.codificY[:crossPoint + 1] + Partner.getCodific()[1][crossPoint + 1:len(self.codificY)]
        Partner.setCodificY(Partner.getCodific()[1][crossPoint + 1] + self.codificY[crossPoint + 1:len(self.codificY)])

    #TODO
    #Uniform Crossover
    #Two Point Crossover
    #Different Positions for X and Y axis

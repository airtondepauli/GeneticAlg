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
            escolha = random.randint(1,3)
            if escolha == 1:
                posicaoMut = random.randint(0, self.Nbits-1)
                if posicaoMut == 0:
                    self.codificX[posicaoMut] = random.randint(self.EspacoBuscaX[0], self.EspacoBuscaX[1])
                else:
                    self.codificX[posicaoMut] = random.randint(0,9)
            elif escolha == 2:
                posicaoMut = random.randint(0, self.Nbits-1)
                if posicaoMut == 0:
                    self.codificY[posicaoMut] = random.randint(self.EspacoBuscaY[0], self.EspacoBuscaY[1])
                else:
                    self.codificY[posicaoMut] = random.randint(0,9)
            else:
                posicaoMutX = random.randint(1, self.Nbits-1)
                posicaoMutY = random.randint(1, self.Nbits-1)
                self.codificX[posicaoMutX] = random.randint(0,9)
                self.codificY[posicaoMutY] = random.randint(0,9)



    def crossOver(self):
        return 0

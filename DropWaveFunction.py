from Genetics import IndividuoRep
import random
import copy
import math

class DropWave(IndividuoRep):
    def fitnessFunction(self):
        firstTerm = -1 + math.cos(12*math.sqrt(pow(self.valueX, 2) + pow(self.valueY, 2)))
        secondTerm = 1/2*(pow(self.valueX, 2)+ pow(self.valueY, 2)) + 2
        self.fitnessValue = firstTerm/secondTerm

    def mutation(self, mutationProbability):
        if random.random() < mutationProbability / 100:
            if self.debug:
                print("\n\nMutation\n\n")
            escolha = random.randint(1, 3)
            if escolha == 1:
                posicaoMut = random.randint(0, self.Nbits - 1)
                if self.debug:
                    print("Mutacao em X, posicao {}".format(posicaoMut))
                if posicaoMut == 0:
                    self.codificX[posicaoMut] = random.randint(self.EspacoBuscaX[0], self.EspacoBuscaX[1])
                else:
                    self.codificX[posicaoMut] = random.randint(0, 9)
            elif escolha == 2:
                posicaoMut = random.randint(0, self.Nbits - 1)
                if self.debug:
                    print("Mutation em Y, posicao {}".format(posicaoMut))
                if posicaoMut == 0:
                    self.codificY[posicaoMut] = random.randint(self.EspacoBuscaY[0], self.EspacoBuscaY[1])
                else:
                    self.codificY[posicaoMut] = random.randint(0, 9)
            else:
                posicaoMutX = random.randint(1, self.Nbits - 1)
                posicaoMutY = random.randint(1, self.Nbits - 1)
                if self.debug:
                    print("Mutation in X, posicao {}\nMutation in Y, posicao {}".format(posicaoMutX, posicaoMutY))
                self.codificX[posicaoMutX] = random.randint(0, 9)
                self.codificY[posicaoMutY] = random.randint(0, 9)
        if self.debug:
            print("Old value X: {}\nOld value Y: {}".format(self.getValueX(), self.getValueY()))
        self.update()

        # TODO
        # Mutation as a sum of a random value (derivative??)
        # Replace for upper boundary

        # SINGLE POINT Crossover

    def crossOver(self, Partner):
        SELF = copy.deepcopy(self)
        Match = copy.deepcopy(Partner)
        crossPoint = random.randint(0, self.Nbits - 1)
        if SELF.debug:
            print(crossPoint)
            print("X1: {} Y1: {}".format(SELF.codificX, SELF.codificY))
            print("X2: {} Y2: {}".format(Match.getCodificX(), Match.getCodificY()))
        TempVectorX = SELF.codificX
        TempVectorY = SELF.codificY
        SELF.codificX = SELF.codificX[:crossPoint + 1] + Match.getCodificX()[crossPoint + 1:]
        Match.setCodificX(Match.getCodificX()[:crossPoint + 1] + TempVectorX[crossPoint + 1:])
        SELF.codificY = SELF.codificY[:crossPoint + 1] + Match.getCodificY()[crossPoint + 1:]
        Match.setCodificY(Match.getCodificY()[:crossPoint + 1] + TempVectorY[crossPoint + 1:])
        if self.debug:
            print("NewX1: {}, NewY1: {}".format(SELF.codificX, SELF.codificY))
            print("NewX2: {}, NewY2: {}".format(Match.getCodificX(), Match.getCodificY()))
        SELF.update()
        Match.update()
        return [SELF, Match]

    def UniformCrossOver(self, Partner):
        SELF = copy.deepcopy(self)
        Match = copy.deepcopy(Partner)
        for i in range(SELF.Nbits):
            if random.random() <= 0.5:
                tempX = SELF.codificX[i]
                SELF.codificX[i] = Match.getCodificX()[i]
                Match.codificX[i] = tempX
            if random.random() <= 0.5:
                tempY = SELF.codificY[i]
                SELF.codificY[i] = Match.getCodificY()[i]
                Match.codificY[i] = tempY
        SELF.update()
        Match.update()
        return [SELF, Match]

        # TODO
        # Uniform Crossover
        # Two Point Crossover
        # Different Positions for X and Y axis

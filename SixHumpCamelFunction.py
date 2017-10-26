from Genetics import IndividuoRep
import math


class SHCamel(IndividuoRep):
    def fitnessFunction(self):
        firstTerm = (4 - 2.1 * (self.valueX * self.valueX) + (pow(self.valueX, 4) / 3)) * self.valueX * self.valueX
        secondTerm = (-4 + 4 * (self.valueY * self.valueY)) * (self.valueY * self.valueY)
        return firstTerm + self.valueX * self.valueY + secondTerm

    def mutation(self):
        return 0

    def crossOver(self):
        return 0

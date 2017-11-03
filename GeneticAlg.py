from ListIndiv import ListGenetic
from SixHumpCamelFunction import SHCamel
import random
import math
import pdb

class GeneticAlgorithmController:

    """
    Tamanho - Numero de individuos na populacao
    Geracoes - Numero de geracoes desejada
    Pc - Probability of CrossOver
    Pm - Probability of Mutation
    Elite - Percentage of population that will survive to next generation
    CrossPercentage - Porcentagem da nova populacao que será formada por crossover
    RandomSurvivors - Porcentagem da população que sobreviverá randomicamente
    Population - Vetor da população
    NewPopulation - Vetor para gerar nova População
    RandomRegeneration - Porcentagem de indiviudos novos gerados randomicamente
    """


    def __init__(self, Tamanho, Geracoes, Pc, Pm, Elite, CrossPercentage, RandomSurvivors, NBits, RangeX, RangeY, Tipo='d', PI=1):
        self.Size = Tamanho
        self.NGeneration = Geracoes
        self.Pc = Pc
        self.Pm = Pm
        self.EliteSurv = Elite
        self.CrossPercentage = CrossPercentage
        self.RandomSurvivors = RandomSurvivors
        self.RandomRegeneration = 1 - Elite - CrossPercentage - RandomSurvivors
        self.CurrentGeneration = 1
        self.Population = ListGenetic(self.Size, NBits, RangeX, RangeY, Tipo, self.CurrentGeneration, PI)
        self.Population.initialize()
        self.NPopulation = ListGenetic(self.Size, NBits, RangeX, RangeY, Tipo, self.CurrentGeneration+1, PI)

    def run(self):
        pass

    def createNewGeneration(self):
        pass

    def averageFitness(self):
        pass

    def getBestIndiv(self):
        pass

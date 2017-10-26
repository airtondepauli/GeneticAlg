from Genetics import IndividuoRep
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

    def __init__(self, Tamanho, Geracoes, Pc, Pm, Elite, CrossPercentage, RandomSurvivors, ):
        self.Size = Tamanho
        self.NGeneration = Geracoes
        self.Pc = Pc
        self.Pm = Pm
        self.EliteSurv = Elite
        self.CrossPercentage = CrossPercentage
        self.RandomSurvivors = RandomSurvivors
        self.Population = []
        self.NewPopulation = []
        self.RandomRegeneration = 1 - Elite - CrossPercentage - RandomSurvivors
        for i in range(self.Size):
            self.Population.append()
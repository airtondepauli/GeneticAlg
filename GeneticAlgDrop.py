from ListIndivDropWave import ListGenetic
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
        self.Pc = Pc/100
        self.Pm = Pm
        self.EliteSurv = Elite
        self.CrossPercentage = CrossPercentage
        self.RandomSurvivors = RandomSurvivors
        self.RandomRegeneration = 1 - Elite/100 - CrossPercentage/100 - RandomSurvivors/100
        self.CurrentGeneration = 1
        self.Population = ListGenetic(self.Size, NBits, RangeX, RangeY, None, None, Tipo, self.CurrentGeneration, PI)
        self.Population.initialize()
        self.NPopulation = ListGenetic(self.Size, NBits, RangeX, RangeY, None, None, Tipo, self.CurrentGeneration+1, PI)
        self.BestIndiv = []
        self.Average = []

    def run(self):
        while self.CurrentGeneration<=self.NGeneration:
            self.createNewGeneration()
            self.Population = self.NPopulation
            self.NPopulation = ListGenetic(self.Size, self.Population.Nbits, self.Population.RangeX, self.Population.RangeY, None, None, self.Population.Tipo, self.CurrentGeneration+1, self.Population.PI)
            self.CurrentGeneration+=1
            self.BestIndiv.append(self.Population.bestIndiv())
            self.Average.append(self.Population.averageFitness())
            #if self.Population.bestIndiv().getFitnessValue() < -1:
             #   print(self.Population.bestIndiv())

            #print("####################")
            #self.Population.printDebug()
            #print("####################")



    def createNewGeneration(self):
        #######Random survivors########
        #pdb.set_trace()
        RndSurv = int(self.Size * self.RandomSurvivors/100)
        ListRndSurv = self.Population.randomSelection(RndSurv)
        self.NPopulation.addBlock(ListRndSurv)

        #######Crossover##############
        CrossOverSurv = int(self.Size * self.CrossPercentage/100)
        Matches = 0
        while CrossOverSurv-Matches>0:
            MatingPool = self.Population.randomSelection(CrossOverSurv)
            for i in range(0, CrossOverSurv-1, 2):
                if random.random() < self.Pc and CrossOverSurv-Matches>0:
                    TempList = MatingPool[i].UniformCrossOver(MatingPool[i+1])
                    self.NPopulation.addElement(TempList[0])
                    self.NPopulation.addElement(TempList[1])
                    Matches += 2

        #######Elite#########
        AmountElite = int(self.Size * self.EliteSurv/100)
        if not self.Population.isSorted:
            self.Population.Ordena()
        EliteSurvivor = self.Population.pickBest(AmountElite)
        self.NPopulation.addBlock(EliteSurvivor)

        ####Random Regenarition#########
        self.NPopulation.completeRandom(self.CurrentGeneration)

        #########Mutation#########
        for item in self.NPopulation.List:
            item.mutation(self.Pm)

        self.CurrentGeneration+=1


    def averageFitness(self):
        print(self.Population.averageFitness())

    def getBestIndiv(self):
        return self.Population.bestIndiv()
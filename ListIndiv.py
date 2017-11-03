from SixHumpCamelFunction import SHCamel
import random
from PopulationFull import ListFullException
import pdb

class ListGenetic:
    def __init__(self, Tamanho, Nbits, RangeX, RangeY, InicializacaoX=None, InicializacaoY=None, Tipo='d', Generation=1, PI=1):
        self.Nbits = Nbits
        self.Tipo = Tipo
        self.Size = Tamanho
        self.GeracaoAtual = Generation
        self.RangeX = RangeX
        self.RangeY = RangeY
        self.InicializacaoX = InicializacaoX
        self.InicializacaoY = InicializacaoY
        self.OrderNumber = 1
        self.PI = PI
        self.List = []
        self.isSorted = False
        self.Livres = self.Size

    def initialize(self):
        for i in range(self.Size):
            self.List.append(SHCamel(self.Nbits, self.RangeX, self.RangeY, self.InicializacaoX, self.InicializacaoY, self.Tipo, self.OrderNumber, self.GeracaoAtual, self.PI ))
            self.OrderNumber += 1
            self.Livres -=1


    def Ordena(self):
        self.List.sort(key=SHCamel.getFitnessValue)
        self.isSorted = True

    def debugPrint(self):
        for indiv in self.List:
            print(indiv)
            print("\n")

    def averageFitness(self):
        averageFitness = 0;
        for indiv in self.List:
            averageFitness += indiv.getFitnessValue()
        return averageFitness/self.Size

    def bestIndiv(self):
        if self.isSorted is True:
            return self.List[0]
        else:
            self.Ordena()
            return self.List[0]

    def randomSelection(self, quantidade):
        listaSelecionada = random.sample(self.List, quantidade)
        return listaSelecionada

    def pickBest(self, quantidade):
        listaSelecionada = []
        if self.isSorted is False:
            self.Ordena()
        for i in range(quantidade):
            listaSelecionada.append(self.List[i])
        return  listaSelecionada

    def __str__(self):
        return "Tamanho: {}\n".format(self.Size)

    def __len__(self):
        return self.Size

    def addElement(self, NIndiv):
        if self.Livres == 0:
            raise ListFullException
        else:
            self.List.append(NIndiv)
            self.Livres-=1

    def addBlock(self, listIndiv):
        if len(listIndiv) <= self.Livres:
            self.Livres = self.Livres + listIndiv
        else:
            raise ListFullException
from SixHumpCamelFunction import SHCamel
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
        self.Population = []
        self.isSorted = False
        for i in range(Tamanho):
            self.Population.append(SHCamel(self.Nbits, self.RangeX, self.RangeY, self.InicializacaoX, self.InicializacaoY, self.Tipo, self.OrderNumber, self.GeracaoAtual, self.PI ))
            self.OrderNumber += 1


    def Ordena(self):
        self.Population.sort(key=SHCamel.getFitnessValue)
        self.isSorted = True

    def debugPrint(self):
        for indiv in self.Population:
            print(indiv)
            print("\n")

    def averageFitness(self):
        averageFitness = 0;
        for indiv in self.Population:
            averageFitness += indiv.getFitnessValue()
        return averageFitness/self.Size

    def bestIndiv(self):
        if self.isSorted is True:
            return self.Population[0]
        else:
            self.Ordena()
            return self.Population[0]


    def randomSelection(self, quantidade):
        pass

    def pickBest(self, quantidade):
        pass

    def __str__(self):
        return "Tamanho: {}\n".format(self.Size)

    def __len__(self):
        return self.Size

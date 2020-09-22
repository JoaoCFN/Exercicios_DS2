from Animal import Animal

class Cachorro(Animal):
    def __init__(self, nome, idade, genero, peso, raca, tipo_pelo):
        super().__init__(nome, idade, genero, peso)
        self._raca = raca  
        self._tipo_pelo = tipo_pelo
        self.som = "Latido"

    def obter_informacoes(self):
        return super().obter_informacoes() + "\nRaça: {} | Tipo do Pêlo: {} \n".format(self._raca, self._tipo_pelo)
        
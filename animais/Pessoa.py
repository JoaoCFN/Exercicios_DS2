from Animal import Animal

class Pessoa(Animal):
    def __init__(self,  nome, idade, genero, peso, naturalidade, ocupacao):
        super().__init__(nome, idade, genero, peso)
        self._naturalidade = naturalidade
        self.ocupacao = ocupacao
        self.som = "Fala"
    
    def obter_informacoes(self):
        return super().obter_informacoes() + "\nNaturalidade: {} | Ocupação: {} \n".format(self._naturalidade, self.ocupacao)

    @property
    def ocupacao(self):
        return self._ocupacao
    
    @ocupacao.setter
    def ocupacao(self, nova_ocupacao):
        if nova_ocupacao != "Docente":
            self._ocupacao = nova_ocupacao

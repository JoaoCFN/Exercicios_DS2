class Circulo:
    pi = 3.14

    def __init__(self, raio):
        self.raio = raio
    
    def obter_area(self):
        return Circulo.pi * (self.raio ** 2) 

    def obter_circunferencia(self):
        return 2 * Circulo.pi * self.raio

    @classmethod
    def atualizar_pi(cls, novo_valor):
        Circulo.pi = novo_valor
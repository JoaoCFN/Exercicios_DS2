class Quadrado:
    diag = 1.41

    def __init__(self, lado):
        self.lado = lado

    def obter_area(self):
        return self.lado * self.lado

    def obter_perimetro(self):
        return self.lado * 4

    def obter_diagonal(self):
        return self.lado * Quadrado.diag

    @classmethod
    def atualizar_diag(cls, novo_valor):
        Quadrado.diag = novo_valor


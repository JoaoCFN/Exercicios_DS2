from Jogo import Jogo
from random import shuffle
class JogoCartas(Jogo):
    def __init__(self, nome, clas_etaria, preco, qtd_jogadores, deck):
        super().__init__(nome, clas_etaria, 1, preco)
        self._qtd_jogadores = qtd_jogadores
        self.deck = deck
    
    def embaralhar(self):
        shuffle(self.deck)
        cartas = ""
        for carta in self.deck:
            cartas += "{}; ".format(carta)
        return cartas

    def dados_jogo(self):
        return super().dados_jogo() + "\nQuantidade de jogadores: {} \nDeck: {}".format(self._qtd_jogadores, self.embaralhar())


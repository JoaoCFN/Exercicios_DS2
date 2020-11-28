from Agencia import Agencia
from Voo import Voo
from Localidade import SSA, BER, FEN, MIA, SYD, DXB
from Reserva import Reserva

class Gerenciador:
    _instancia = None

    def __init__(self):
        self.ag = Agencia("Forma Turismo")
        self.voo1 = Voo(SSA(), BER())
        self.voo2 = Voo(SSA(), BER(), FEN())
        self.voo3 = Voo(MIA(), SYD())
        self.voo4 = Voo(MIA(), SYD(), BER(), DXB())
        
        self.voos_disponiveis = [self.voo1, self.voo2, self.voo3, self.voo4]

    @staticmethod
    def get_instance(self):
        if Gerenciador._instancia is None:
            Gerenciador._instancia = Gerenciador()

        return Gerenciador._instancia

    def reservar(self, voo, classe):
        voo_escolhido = self.voos_disponiveis[voo - 1]
        reserva = Reserva(voo_escolhido, classe)

        return self.ag.realizar_reserva(reserva)

    def obter_dados_reserva(self, num_reserva):
        return self.ag.buscar_reserva(num_reserva)
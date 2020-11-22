# from agencia import Agencia
# from voo import Voo

class Gerenciador:
    instancia = None

    def __init__(self):
        self.ag = Agencia("Forma Turismo")
        self.voo1 = Voo(SSA(), BER())
        self.voo2 = Voo(SSA(), BER(), FEN())
        self.voo3 = Voo(MIA(), SYD())
        self.voo4 = Voo(MIA(), SYD(), BER(), DXB())

        self.voos_disponiveis = [voo1, voo2, voo3, voo4]

    @staticmethod
    def get_instance(self):
        if Gerenciador.instancia is None:
            instancia = Gerenciador()

        return instancia

    def reservar(self, voo, classe):
        voo_escolhido = self.voos_disponiveis[voo - 1]

        reserva = Reserva(voo_escolhido, classe)

        return self.ag.realizar_reserva(reserva)

    def obter_dados_reserva(self, num_reserva):
        return self.ag.buscar_reserva(num_reserva)
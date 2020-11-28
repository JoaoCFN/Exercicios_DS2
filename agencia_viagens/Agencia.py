class Agencia:
    def __init__(self, nome):
        self.nome = nome
        self.reservas_realizadas = []

    def realizar_reserva(self, reserva):
        self.reservas_realizadas.append(reserva)        
        return reserva.num_reserva

    def buscar_reserva(self, numero_reserva):
        for reserva in self.reservas_realizadas:
            if numero_reserva == reserva.num_reserva:
                return reserva.get_info_reserva()

        return "Reserva não encontrada"
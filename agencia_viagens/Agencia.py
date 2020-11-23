class Agencia:
    def __init__(self, nome):
        self.nome = nome
        self.reservas_realizadas = []

    def realizar_reserva(self, reserva):
        # print(reserva.voo.origem, reserva.voo.destino. reserva.voo.escala)
        # print(reserva.get_info_reserva())
        self.reservas_realizadas.append(reserva)
        return reserva.num_reserva
        # print(len(self.reservas_realizadas))

    def buscar_reserva(self, numero_reserva):
        for reserva in self.reservas_realizadas:
            if numero_reserva == reserva.num_reserva:
                print("Objeto da disgraça: {}".format(reserva))
                return reserva.get_info_reserva()

            return "Reserva não encontrada"
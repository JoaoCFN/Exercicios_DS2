from Gerenciador import Gerenciador

def main():
    gerenciador = Gerenciador()
    acao_inicial = 0  

    while acao_inicial != 3:
        acao_inicial = int(input("Olá!\nO que deseja fazer nossa agência?\n1) Resevar vôo \n2) Ver dados da reserva \n3) Sair \n"))

        if acao_inicial >= 1 and acao_inicial <= 3:
            if acao_inicial == 1:
                voo_escolhido = int(input("Escolha o seu vôo: \n1) SSA-BER (direto) \n2) SSA-BER (escala em FEN) \n3) MIA-SYD (direto) \n4) MIA-SYD (escala em BER e DXB) \n"))  

                classe_escolhida = input("Escolha a sua classe \nX - Classe executiva \nOutra tecla - Classe econômica \n")

                numero_reserva = gerenciador.reservar(voo_escolhido, classe_escolhida)
                print("Número da sua reserva: {}".format(numero_reserva))
            elif acao_inicial == 2:
                reserva_desejada = int(input("Digite o número da reserva que você deseja ver os dados: "))  

                dados_reserva = gerenciador.obter_dados_reserva(reserva_desejada)

                print(dados_reserva)
            else:
                print("Obrigado por usar o nosso programa :)")
                break
        else:
            print("Opção inválida")

main()
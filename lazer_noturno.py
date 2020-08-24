opcao_lazer = -1
while opcao_lazer < 1 or opcao_lazer > 4:
    opcao_lazer = int(input("O que você vai fazer hoje a noite? \n1) Jogar \n2) Assistir Seriado \n3) Usar redes sociais \n4) Programar\n"))

    if opcao_lazer >= 1 and opcao_lazer <= 3:
        pass
    elif opcao_lazer == 4:
        print("É mentira!!")
        break
else:
    print("Bom lazer :)")
opiniao = -1
qtd_pizzas = 0

while opiniao < 0 or opiniao > 5:
    opiniao = int(input(
        "O que você acha de python? \n 1)Muito Barril \n 2)Barril \n 3)Mais ou Menos \n 4)De boa \n 5)Muito de boa \n"
    ))

    if opiniao == 0:
        print("Saída inesperada\nVocê ficará sem pizzas")
        break
    elif opiniao == 1 or opiniao == 2:
        qtd_pizzas += 1
    elif opiniao == 3 or opiniao == 4:
        qtd_pizzas += 2
    elif opiniao == 5:
        qtd_pizzas += 3
else:
    print("Você ganhou {} pizzas!".format(qtd_pizzas))
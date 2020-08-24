precos_viagem = [5000, 6500, 7500, 8500, 10000]

destino_desejado = int(input(
    "Informe o destino desejado:\n 0 - Miami\n 1 - Barcelona\n 2 - Florença\n 3 - Amesterdã\n 4 - Tóquio\n"
))
qtd_pessoas = int(input("Informe a quantidade de pessoas da viagem\n"))

valor_total_viagem = precos_viagem[destino_desejado] * qtd_pessoas

print("Valor total da viagem: R${}".format(valor_total_viagem))
print("O valor total da viagem ficou entre R$12000,00 e R$17000,00: {}"
      .format(valor_total_viagem >= 12000 and valor_total_viagem <= 17000)
)
print("O valor pode ser parcelado em 3x iguais: {}"
      .format(valor_total_viagem % 3 == 0)
)
print("O destino escolhido fica fora da Europa: {}"
      .format(destino_desejado == 0 or destino_desejado == 4)
)

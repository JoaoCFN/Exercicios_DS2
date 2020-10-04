from Churros import Churros
from Refresco import Refresco
from OpcaoInvalidaError import OpcaoInvalidaError
from Venda import Venda

itens = []


def main():
    opcao = -1
    while opcao != 4:
        print("=============== VENDA DO CHAVES ===============")
        try:
            opcao = int(input("O que deseja fazer?\n1) Comprar refresco\n2) Comprar churros\n3) Pagar\n4) Sair\n"))
        except ValueError:
            print("Informe apenas um número.")
        else:
            if 0 < opcao < 3:
                iniciar_compra(opcao)
            elif opcao == 3:
                pagar()
                break
            elif opcao > 4:
                print("Informe um número válido.")


def iniciar_compra(produto):
    try:
        tamanho_produto = int(input("Digite o tamanho do produto: \n0) Pequeno \n1) Médio \n2) Grande \n"))
        if tamanho_produto >= 0 and tamanho_produto <= 2:
            if produto == 1:
                sabores_obtidos = Refresco.sabores
            else:
                sabores_obtidos = Churros.sabores

            comprar_produto(sabores_obtidos, tamanho_produto)
        else:
            raise OpcaoInvalidaError()

    except OpcaoInvalidaError:
        print(OpcaoInvalidaError.mensagem_padrao)


def comprar_produto(opcoes_sabor, tamanho):
    print("Qual sabor você quer?")
    try:
        for i, opcao_sabor in enumerate(opcoes_sabor):
            print(str(i) + " - " + opcao_sabor)
        sabor = input()
        if sabor != '0' and sabor != '1' and sabor != '2':
            raise OpcaoInvalidaError()
    except OpcaoInvalidaError:
        print(OpcaoInvalidaError.mensagem_padrao)
    else:
        if opcoes_sabor[0] == Refresco.sabores[0]:
            acucar = input("Você quer açúcar? (S para Sim / Outra tecla para Não)\n")
            produto = Refresco(int(sabor), tamanho, acucar)
        else:
            cobertura = input("Você quer cobertura? (S para Sim / Outra tecla para Não)\n")
            produto = Churros(int(sabor), tamanho, cobertura)
        itens.append(produto)


def pagar():
    if len(itens) > 0:
        forma_pagamento = input("Como deseja pagar?\nC para Cartão / Outra tecla para Dinheiro\n")
        venda = Venda(itens, forma_pagamento)
        print("=============== DADOS DA VENDA ===============")
        print(venda.extrato_venda())
    else:
        print("Não há itens. Compra encerrada.")


main()

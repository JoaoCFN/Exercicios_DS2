def assembleDozens(num, number_in_full, units, dozens, others_dozens): 
    # numbers less than 19
    if num < 20:
        for key, value in dozens.items():
            if num == key:
                number_in_full += value
    # numbers greater than 19
    else:
        # dozens
        dozens = (num // 10) * 10
        for key, value in others_dozens.items():
            if dozens == key:
                number_in_full += value
        # unit
        unit = num % 10
        for key, value in units.items():
            if unit != 0 and unit == key:
                number_in_full += " e {}".format(value)

    return number_in_full

def assembleNumbers(num, number_in_full, units, dozens, others_dozens):
    lenNum = len(str(num))

    if lenNum == 1:
        # positives
        for key, value in units.items():
            if num == key:
                number_in_full += value
    elif lenNum == 2:
        # positives
        if num > 0:
            number_in_full += assembleDozens(num, number_in_full, units, dozens, others_dozens)
        # negatives
        else:
            unit = abs(num)
            for key, value in units.items():
                if unit == key:
                    number_in_full += "menos {}".format(value)
    elif lenNum == 3:
        # negatives
        number_in_full += "menos " + assembleDozens(abs(num), number_in_full, units, dozens, others_dozens)

    return number_in_full

def main():
    number_in_full = ""

    units = {0: "zero", 1: "um", 2: "dois", 3: "três", 4: "quatro", 5: "cinco", 6: "seis", 7: "sete", 8: "oito", 9: "nove"}

    dozens = {10: "dez", 11: "onze", 12: "doze", 13: "treze", 14: "quatorze", 15: "quinze", 16: "dezesseis", 17: "dezessete", 18: "dezoito", 19: "dezenove"}

    others_dozens = {20: "vinte", 30: "trinta", 40: "quarenta", 50: "cinquenta", 60: "sessenta", 70: "setenta", 80: "oitenta", 90: "noventa"}

    num = int(input("Digite um número inteiro entre -99 e 99 \n"))
    written_number = assembleNumbers(num, number_in_full, units, dozens, others_dozens)
    print(written_number)
    
main()
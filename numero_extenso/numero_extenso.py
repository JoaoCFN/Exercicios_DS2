def assembleTens(num, word, units, tens, others_tens): 
    # numbers less than 20
    if num < 20:
        for key, value in tens.items():
            if num == key:
                word += value
    # numbers greater than 19
    else:
        # tens
        tens = (num // 10) * 10
        for key, value in others_tens.items():
            if tens == key:
                word += value
        # unit
        unit = num % 10
        for key, value in units.items():
            if unit != 0 and unit == key:
                word += " e {}".format(value)

    return word

def assembleUnits(num, word, units):
    for key, value in units.items():
        if num == key:
            word += value

def assembleNumbers(num, word, units, tens, others_tens):
    lenNum = len(str(num))

    if lenNum == 1:
        # positives
        assembleUnits(num, word, units)
    elif lenNum == 2:
        # positives
        if num > 0:
            word += assembleTens(num, word, units, tens, others_tens)
        # negatives
        else:
            word += "menos " + assembleUnits(abs(num), word, units)
    elif lenNum == 3:
        # negatives
        word += "menos " + assembleTens(abs(num), word, units, tens, others_tens)

    return word

def main():
    word = ""

    units = {0: "zero", 1: "um", 2: "dois", 3: "três", 4: "quatro", 5: "cinco", 6: "seis", 7: "sete", 8: "oito", 9: "nove"}

    tens = {10: "dez", 11: "onze", 12: "doze", 13: "treze", 14: "quatorze", 15: "quinze", 16: "dezesseis", 17: "dezessete", 18: "dezoito", 19: "dezenove"}

    others_tens = {20: "vinte", 30: "trinta", 40: "quarenta", 50: "cinquenta", 60: "sessenta", 70: "setenta", 80: "oitenta", 90: "noventa"}

    num = int(input("Digite um número inteiro entre -99 e 99 \n"))
    written_number = assembleNumbers(num, word, units, tens, others_tens)
    print(written_number)
    
main()
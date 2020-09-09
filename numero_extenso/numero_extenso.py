def assemble_tens(num, word, units, tens, others_tens): 
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

def assemble_units(num, word, units):
    for key, value in units.items():
        if num == key:
            word += value

def assemble_word(num, word, units, tens, others_tens):
    len_num = len(str(num))

    if len_num == 1:
        # positives
        assemble_units(num, word, units)
    elif len_num == 2:
        # positives
        if num > 0:
            word += assemble_tens(num, word, units, tens, others_tens)
        # negatives
        else:
            word += "menos " + assemble_units(abs(num), word, units)
    elif len_num == 3:
        # negatives
        word += "menos " + assemble_tens(abs(num), word, units, tens, others_tens)

    return word

def main():
    word = ""
    num = -100

    units = {0: "zero", 1: "um", 2: "dois", 3: "três", 4: "quatro", 5: "cinco", 6: "seis", 7: "sete", 8: "oito", 9: "nove"}

    tens = {10: "dez", 11: "onze", 12: "doze", 13: "treze", 14: "quatorze", 15: "quinze", 16: "dezesseis", 17: "dezessete", 18: "dezoito", 19: "dezenove"}

    others_tens = {20: "vinte", 30: "trinta", 40: "quarenta", 50: "cinquenta", 60: "sessenta", 70: "setenta", 80: "oitenta", 90: "noventa"}

    while num < -99 or num > 99:
        try:
            num = int(input("Digite um número inteiro entre -99 e 99 \n"))
            if num >= -99 and num <= 99:
                written_number = assemble_word(num, word, units, tens, others_tens)
                print(written_number)
            else: 
                print("Informe um número válido")
        except ValueError: 
            print("Informe um valor válido")
    
main()
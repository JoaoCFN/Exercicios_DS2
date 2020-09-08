def splitNum(num):
    digitList = []
    lenNum = len(str(num))

    if lenNum == 1:
        digitList.append(num)
    elif lenNum == 2:
        if num > 0:
            digitList.append(num // 10)
            digitList.append(num % 10)
        else:
            digitList.append("-")
            digitList.append(abs(num))
    elif lenNum == 3:
        digitList.append("-")
        digitList.append(abs(num) // 10)
        digitList.append(abs(num) % 10)

    return digitList

def writeNum(num):
    unit = {0: "zero", 1: "um", 2: "dois", 3: "três", 4: "quatro", 5: "cinco", 6: "seis", 7: "sete", 8: "oito", 9: "nove"}

    dozens = {11: "onze", 12: "doze", 13: "treze", 14: "quatorze", 15: "quinze", 16: "dezesseis", 17: "dezessete", 18: "dezoito", 19: "dezenove"}

    others_dozens = {20: "vinte", 30: "trinta", 40: "quarenta", 50: "cinquenta", 60: "sessenta", 70: "setenta", 80: "oitenta", 90: "noventa"}

    for k, v in others_dozens.items():
        print(k, v)

def main():
    num = int(input("Digite um número inteiro entre -99 e 99 \n"))
    
    digitList = splitNum(num)
    print(digitList)

    writeNum(num)
    
if __name__ == "__main__":
    main()
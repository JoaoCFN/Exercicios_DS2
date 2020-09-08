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

def main():
    num = int(input("Digite um número inteiro entre -99 e 99 \n"))
    
    digitList = splitNum(num)
    print(digitList)
    
if __name__ == "__main__":
    main()
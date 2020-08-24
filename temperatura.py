temps = [33.5, 28.7, 36.1, 30.9, 35.3, 27.0]

for temp in temps:
    if temp >= 35:
        print("A temperatura é muito quente {}".format(temp))
    elif temp >= 30 and temp < 35:
        print("A temperatura é quente {}".format(temp))
    else:
        print("A temperatura é amena {}".format(temp))
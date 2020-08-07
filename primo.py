valor = True
def primo(numero):
    global valor
    if numero%2 == 0 or numero%3 == 0 or numero%5 == 0 or numero%7 == 0 or numero%11 == 0:
        valor = False
    else:
        for x in range(2, numero):
            if numero%x == 0:
                print(x)
                valor = False
    return valor

print(primo(99400303))
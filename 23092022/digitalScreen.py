def main():
    n = int(input("Ingrese el numero n: "))
    escala = int(input("Ingrese la escala: "))
    n_copy = n
    n_inv = 0
    while n > 0:
        n_inv = n_inv * 10 + (n % 10)
        n = n // 10
    n = n_copy
    cont_digitos = 1
    while n > 9:
            cont_digitos += 1
            n = n // 10
    cont_pos = 0
    cont_repeticiones = 0
    while cont_pos < 5:
        n_inv_copy = n_inv
        cont = 0
        while cont < cont_digitos:
            res = (n_inv % 10)
            n_inv = n_inv // 10
            if cont_pos == 0:
                if res == 1 or res == 4:
                    print(" ", end="")
                    cont_repeticiones_horizontales = 0
                    while cont_repeticiones_horizontales < escala:
                        print(" ", end="")
                        cont_repeticiones_horizontales += 1
                    print(" ", end="")
                else:
                    print(" ", end="")
                    cont_repeticiones_horizontales = 0
                    while cont_repeticiones_horizontales < escala:
                        print("-", end="")
                        cont_repeticiones_horizontales += 1
                    print(" ", end="")
            if cont_pos == 1:
                if res == 0 or res == 4 or res == 8 or res == 9:
                    print("|", end="")
                    cont_repeticiones_horizontales = 0
                    while cont_repeticiones_horizontales < escala:
                        print(" ", end="")
                        cont_repeticiones_horizontales += 1
                    print("|", end="")
                elif res == 5 or res == 6:
                    print("|", end="")
                    cont_repeticiones_horizontales = 0
                    while cont_repeticiones_horizontales < escala:
                        print(" ", end="")
                        cont_repeticiones_horizontales += 1
                    print(" ", end="")
                else:
                    print(" ", end="")
                    cont_repeticiones_horizontales = 0
                    while cont_repeticiones_horizontales < escala:
                        print(" ", end="")
                        cont_repeticiones_horizontales += 1
                    print("|", end="")
            if cont_pos == 2:
                if res == 0 or res == 1 or res == 7:
                    print(" ", end="")
                    cont_repeticiones_horizontales = 0
                    while cont_repeticiones_horizontales < escala:
                        print(" ", end="")
                        cont_repeticiones_horizontales += 1
                    print(" ", end="")
                else:
                    print(" ", end="")
                    cont_repeticiones_horizontales = 0
                    while cont_repeticiones_horizontales < escala:
                        print("-", end="")
                        cont_repeticiones_horizontales += 1
                    print(" ", end="")
            if cont_pos == 3:
                if res == 0 or res == 6 or res == 8:
                    print("|", end="")
                    cont_repeticiones_horizontales = 0
                    while cont_repeticiones_horizontales < escala:
                        print(" ", end="")
                        cont_repeticiones_horizontales += 1
                    print("|", end="")
                elif res == 2:
                    print("|", end="")
                    cont_repeticiones_horizontales = 0
                    while cont_repeticiones_horizontales < escala:
                        print(" ", end="")
                        cont_repeticiones_horizontales += 1
                    print(" ", end="")
                else:
                    print(" ", end="")
                    cont_repeticiones_horizontales = 0
                    while cont_repeticiones_horizontales < escala:
                        print(" ", end="")
                        cont_repeticiones_horizontales += 1
                    print("|", end="")
            if cont_pos == 4:
                if res == 1 or res == 4 or res == 7:
                    print(" ", end="")
                    cont_repeticiones_horizontales = 0
                    while cont_repeticiones_horizontales < escala:
                        print(" ", end="")
                        cont_repeticiones_horizontales += 1
                    print(" ", end="")
                else:
                    print(" ", end="")
                    cont_repeticiones_horizontales = 0
                    while cont_repeticiones_horizontales < escala:
                        print("-", end="")
                        cont_repeticiones_horizontales += 1
                    print(" ", end="")
            cont += 1
        print("")
        n_inv = n_inv_copy
        if(cont_repeticiones < escala - 1 and (cont_pos == 1 or cont_pos == 3)):
            cont_repeticiones += 1
        else:
            cont_pos += 1
            cont_repeticiones = 0
main()
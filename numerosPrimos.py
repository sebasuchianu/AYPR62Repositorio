def main():
    n = int(input("Ingrse n: "))
    while n < 1:
        n = int(input("Ingrse n: "))
    cont = 1
    while (cont <= n):
        copy_cont = cont
        cont_multiplos = 0
        while (copy_cont >= 1):
            if (cont % copy_cont == 0):
                cont_multiplos += 1
            copy_cont -= 1
        if (cont_multiplos == 2):
            print(cont)
        cont += 1

main()

    
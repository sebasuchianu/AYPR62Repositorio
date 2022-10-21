def procedimiento(pos, contador, registro, ram):
    solicitarDatos(ram)
    while ram[pos] != "100":
        centenas, decenas, unidades = dividirNumero(ram[pos])
        contador += 1
        if centenas == "2":
            funcion200(registro, decenas, unidades)
            pos += 1
        elif centenas == "3":
            funcion300(registro, decenas, unidades)
            pos += 1
        elif centenas == "4":
            funcion400(registro, decenas, unidades)
            pos += 1
        elif centenas == "5":
            funcion500(registro, decenas, unidades)
            pos += 1
        elif centenas == "6":
            funcion600(registro, decenas, unidades)
            pos += 1
        elif centenas == "7":
            funcion700(registro, decenas, unidades)
            pos += 1
        elif centenas == "8":
            funcion800(registro, ram, decenas, unidades)
            pos += 1
        elif centenas == "9":
            funcion900(registro, ram, decenas, unidades)
            pos += 1
        elif centenas == "0":
            pos = funcion000(registro, pos, decenas, unidades)
    return contador + 1

def solicitarDatos(ram):
    pos = 0
    while True:
        ram[pos] = input("")
        if ram[pos] == "100":
            break
        pos += 1

def dividirNumero(numero):
    return numero[0], numero[1], numero[2]

def funcion200(registro, d, n):
    registro[int(d)] = int(n) % 1000

def funcion300(registro, d, n):
    registro[int(d)] = (registro[int(d)] + int(n)) % 1000

def funcion400(registro, d, n):
    registro[int(d)] = (registro[int(d)] * int(n)) % 1000

def funcion500(registro, d, s):
    registro[int(d)] = registro[int(s)]

def funcion600(registro, d, s):
    registro[int(d)] = (registro[int(d)] + registro[int(s)]) % 1000

def funcion700(registro, d, s):
    registro[int(d)] = (registro[int(d)] * registro[int(s)]) % 1000

def funcion800(registro, ram, d, a):
    registro[int(d)] = int(ram[registro[int(a)]])

def funcion900(registro, ram, a, s):
    ram[registro[int(a)]] = str(registro[int(s)])

def funcion000(registro, pos, d, s):
    if registro[int(s)] != 0:
        pos = registro[int(d)]
    else:
        pos += 1
    return pos


def main():
    pos = 0
    contador = 0
    registro = [int(0) for _ in range(10)]
    ram = ["000" for _ in range(1000)]
    contador = procedimiento(pos, contador, registro, ram)
    print(contador)

main()
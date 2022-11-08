from sys import stdin
def solicitarDato():
    palabra = stdin.readline().strip()
    if palabra == "":
        return palabra
    return [str(x) for x in palabra]

def main():
    palabra = solicitarDato()
    palabra2 = solicitarDato()
    while palabra != "" or palabra2 != "":
        posicion = 0
        letras = []
        for letra in palabra:
            for letra2 in palabra2:
                if letra == letra2:
                    letras += letra
                    palabra2.remove(letra)
                    break
        letras.sort()
        print("".join(letras))
        palabra = solicitarDato()
        palabra2 = solicitarDato()
        
main()